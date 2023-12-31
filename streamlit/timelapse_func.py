import geemap
import time

# Sentinel-1 timelapse function
def create_sentinel1_timelapse(roi, start_date, end_date, frequency, output_gif):
    geemap.sentinel1_timelapse(
    roi=roi,
    out_gif=output_gif,
    start_year=int(start_date[:4]),
    end_year=int(end_date[:4]),
    start_date=f"{start_date[4:6]}-{start_date[6:]}",  
    end_date=f"{end_date[4:6]}-{end_date[6:]}",
    frequency=frequency,
    date_format=None,
    palette='Greys',
    vis_params=None,
    dimensions=(1024, 768),
    frames_per_second=3,
    crs='EPSG:3857',
    overlay_data=None,
    overlay_color='black',
    overlay_width=1,
    overlay_opacity=1.0,
    title=None,
    title_xy=('2%', '90%'),
    add_text=True,
    text_xy=('2%', '2%'),
    text_sequence=None,
    font_type='arial.ttf',
    font_size=20,
    font_color='white',
    add_progress_bar=True,
    progress_bar_color='blue',
    progress_bar_height=5,
    add_colorbar=False,
    colorbar_width=6.0,
    colorbar_height=0.4,
    colorbar_label=None,
    colorbar_label_size=12,
    colorbar_label_weight='normal',
    colorbar_tick_size=10,
    colorbar_bg_color=None,
    colorbar_orientation='horizontal',
    colorbar_dpi='figure',
    colorbar_xy=None,
    colorbar_size=(300, 300),
    loop=0, mp4=False,
    fading=False,
    orbitProperties_pass='ASCENDING'
    )
    return


# Sentinel-2 timelapse function
def create_sentinel2_timelapse(roi, start_date, end_date, frequency, output_gif):
    geemap.sentinel2_timelapse(
    roi=roi,
    out_gif=output_gif,
    start_year=int(start_date[:4]),
    end_year=int(end_date[:4]),
    start_date=f"{start_date[4:6]}-{start_date[6:]}",  
    end_date=f"{end_date[4:6]}-{end_date[6:]}",
    frequency=frequency,
    date_format=None,
    bands=['Red', 'Green', 'Blue'],
    vis_params=None,
    dimensions=(1024, 768),
    frames_per_second=1,
    crs='EPSG:3857',
    overlay_data=None,
    overlay_color='black',
    overlay_width=1,
    overlay_opacity=1.0,
    title=None,
    title_xy=('2%', '90%'),
    add_text=True,
    text_xy=('2%', '2%'),
    text_sequence=None,
    font_type='arial.ttf',
    font_size=20,
    font_color='white',
    add_progress_bar=True,
    progress_bar_color='blue',
    progress_bar_height=5,
    loop=0, mp4=False,  
    fading=False,
    )
    return

def long_running_task():
    # Wait 5 seconds and return the phrase 'Work Done'
    time.sleep(5)
    return "작업 완료!"
