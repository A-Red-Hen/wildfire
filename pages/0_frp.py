import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

# constants
DATE_ONE = "2014-05-14"
DATE_TWO = "2014-07-18"
DATE_THREE = "2016-06-02"
DATE_FOUR = "2016-08-31"
DATE_FIVE = "2016-11-26"

# functions
def create_plotly_map(date: str) -> None:
    file_name = date + "_geodata.gpkg"
    # csv_filename = date + "_final_merged.csv"
    # csv = pd.read_csv(csv_filename)
    merged_geo_data = gpd.read_file(file_name)
    merged_geo_data["COUNTY"] = merged_geo_data["COUNTY"].str.strip()
    merged_geo_data.drop_duplicates(subset=['Polygon_ID'], inplace = True)
    merged_geo_data.drop_duplicates(subset=['geometry'], inplace = True)
    fig = px.choropleth(merged_geo_data, geojson=merged_geo_data.geometry, locations= merged_geo_data.index, color=merged_geo_data.frp,
                           color_continuous_scale="Viridis",
                           range_color=(0, 1),
                           scope="usa",
                           labels={'frp':'FirePower'},
                           hover_data={'COUNTY': True, 'FIPS': True}
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) 
    # set the plot
    # heading
    st.subheader(f"Firepower on {date} across USA")
    st.plotly_chart(fig)
def create_plotly_map_1(date: str) -> None:
    file_name = date + "_geodata.gpkg"
    # csv_filename = date + "_final_merged.csv"
    # csv = pd.read_csv(csv_filename)
    merged_geo_data = gpd.read_file(file_name)
    fig = px.choropleth(merged_geo_data, geojson=merged_geo_data.geometry, locations= merged_geo_data.index, color=merged_geo_data.sum_frprpl,
                           color_continuous_scale="Viridis",
                           range_color=(0, 2),
                           scope="usa",
                           labels={'frp':'FirePower'},
                           hover_data={'COUNTY': True, 'FIPS': True}
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) 
    # set the plot
    # heading
    st.subheader(f"Combined vulnerability on {date} across USA")
    st.plotly_chart(fig)

st.title("Map Visualizations")
# set a dropdown
date = st.selectbox(
    "Please choose a date you would like...",
    (DATE_ONE, DATE_TWO, DATE_THREE, DATE_FOUR, DATE_FIVE),
    placeholder = "Please select a date"
)

if date == DATE_ONE:
    create_plotly_map(date)
    create_plotly_map_1(date)
elif date == DATE_TWO:
    create_plotly_map(date)
    create_plotly_map_1(date)
elif date == DATE_THREE:
    create_plotly_map(date)
    create_plotly_map_1(date)
elif date == DATE_FOUR:
    create_plotly_map(date)
    create_plotly_map_1(date)
elif date == DATE_FIVE:
    create_plotly_map(date)
    create_plotly_map_1(date)