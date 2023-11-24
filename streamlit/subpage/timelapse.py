import streamlit as st
import geemap
import ee
from timelapse_func import create_sentinel1_timelapse, create_sentinel2_timelapse
import json
from ts_trend_analysis_func import create_ee_polygon_from_geojson
import datetime
import time_func
# Google Earth Engine 초기화
ee.Initialize()

def app():
    # 페이지 레이아웃 설정
    empty1, col0, empty2 = st.columns([0.1,1.0, 0.1])
    with col0:
        st.title('👀 타임랩스 생성기') # 페이지 제목
        st.write("---"*20) # 구분선
        if st.toggle("사용설명서"):
            st.write("""
Sentinel-1(레이더)과 Sentinel-2(광학) 위성 데이터를 활용하여 타임랩스를 생성하는 Streamlit 웹 애플리케이션입니다.

1. 데이터셋 및 관심 지역 선택
2. 분석 기간 및 주기 설정
3. 타임랩스 생성 버튼 클릭
4. 결과 확인

주의사항
인터넷 연결 상태에 따라 타임랩스 생성 시간이 달라질 수 있습니다.
                     """)

    # 'aoi.geojson' 파일 로드
    with open('aoi.geojson', 'r', encoding="utf-8") as f:
        geojson_data = json.load(f)

    # 관심 지역 목록
    area_names = [feature['properties']['name'] for feature in geojson_data['features']]
    area_names.append("새로운 관심영역 넣기")  # 드롭다운 목록에 새 옵션 추가

    # 섹션 나누기
    empty1, col1, col2, empty2 = st.columns([0.1,0.5, 0.3, 0.1])

    # 왼쪽 섹션: 설명 문구
    with col1:
        st.write(" 오른쪽의 옵션을 선택하고 '타임랩스 생성' 버튼을 누르면 타임랩스가 나와요. 👉🏻")

    # 오른쪽 섹션: 입력 선택
    with col2:
        with st.form("조건 폼"):
            # User's Input
            dataset = st.selectbox('위성영상 선택 :', ['Sentinel-1(레이더)', 'Sentinel-2(광학)'])
            selected_name = st.selectbox("관심지역 선택 :", area_names)

            # 날짜 선택
            start_date = st.date_input('시작날짜 (2015.05 ~) :',time_func.one_year_ago_f()) 
            end_date = st.date_input('끝날짜 (~ 오늘) :') # 디폴트: 오늘 날짜
                    
            # 주기 선택 및 매핑
            frequency_options = {'일': 'day', '월': 'month', '분기': 'quarter', '연': 'year'}
            frequency_label = st.selectbox('빈도 선택 : ', options=list(frequency_options.keys()))
            frequency = frequency_options[frequency_label]

            # '새로운 관심영역 넣기'가 선택되면 파일 업로드 기능 활성화
            if selected_name == "새로운 관심영역 넣기":
                uploaded_file = st.file_uploader("GeoJSON 파일을 업로드하세요", type=['geojson'])
                if uploaded_file is not None:
                    # 파일 읽기
                    aoi = json.load(uploaded_file)
            else:
                # 기존 관심 지역 선택
                aoi = next((feature for feature in geojson_data['features'] if feature['properties']['name'] == selected_name), None)
                
                aoi = create_ee_polygon_from_geojson(aoi)

            # 날짜를 geemap 함수와 호환되는 'YYYYMMDD' 형식으로 변환하기 위해 strftime을 사용
            formatted_start_date = start_date.strftime('%Y%m%d') # Correctly formatted as 'YYYYMMDD'
            formatted_end_date = end_date.strftime('%Y%m%d') # Correctly formatted as 'YYYYMMDD'

            # 분석 실행 버튼
            st.write("")
            proceed_button = st.form_submit_button("☑️ 타임랩스 생성")


# -------------------------결과 --------------------------
    with col1:
        if proceed_button:
            # 스피너를 통해 타임랩스 생성 중임을 사용자에게 알림
            with st.spinner('타임랩스를 생성하는 중입니다...'):
                output_gif = './timelapse.gif'  # 생성된 타임랩스를 저장할 경로와 파일명
                
                # Sentinel-1을 선택한 경우
                if dataset == 'Sentinel-1':
                    # create_sentinel1_timelapse 함수에 포맷된 날짜와 다른 필요한 매개변수 전달
                    create_sentinel1_timelapse(aoi, formatted_start_date, formatted_end_date, frequency, output_gif)    
                    st.image(output_gif, caption=f'{dataset} 타임랩스', use_column_width=True)
                
                # Sentinel-2를 선택한 경우
                elif dataset == 'Sentinel-2':
                    # create_sentinel2_timelapse 함수에 포맷된 날짜와 다른 필요한 매개변수 전달
                    create_sentinel2_timelapse(aoi, formatted_start_date, formatted_end_date, frequency, output_gif)
                    st.image(output_gif, caption=f'{dataset} 타임랩스', use_column_width=True ) 

# launch
if __name__  == "__main__" :
    app()