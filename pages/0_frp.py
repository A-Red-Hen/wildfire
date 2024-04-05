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
    st.markdown("In the Wildfire Risk map, for a chosen date, the AI model predicts the wildfire intensity based on meteorological, topographical and vegetation inputs for each census tract across the USA. Each census tract is assigned a value of “0” or “1”, based on the AI model’s Wildfire intensity predictions. A census tract is assigned a value of “0” if its predicted wildfire intensity Fire Radiative Power (FRP) is &lt; 5.0 megawatts. Each census tract is assigned a value of “1” if its predicted wildfire intensity FRP is &gt; 5.0 megawatts.")
    create_plotly_map_1(date)
    st.markdown("In the Combined Vulnerability map, for each census tract, the predicted wildfire risk from the AI model is combined with the tract’s social vulnerability index, giving a combined vulnerability score called CV.")
    st.markdown("Tracts in darker reds have high combined vulnerability, i.e., they have both high wildfire risk AND are highly socially vulnerable. Fire managers can use this map as an assistive tool to determine areas requiring urgent support with special accommodations needed for those communities, during wildfire disasters across the USA. Some examples of Special accommodations include evacuation warnings in native language for non-English speaking communities and special assistance to evacuate communities with high disabled population.")
elif date == DATE_TWO:
    create_plotly_map(date)
    st.markdown("In the Wildfire Risk map, for a chosen date, the AI model predicts the wildfire intensity based on meteorological, topographical and vegetation inputs for each census tract across the USA. Each census tract is assigned a value of “0” or “1”, based on the AI model’s Wildfire intensity predictions. A census tract is assigned a value of “0” if its predicted wildfire intensity Fire Radiative Power (FRP) is &lt; 5.0 megawatts. Each census tract is assigned a value of “1” if its predicted wildfire intensity FRP is &gt; 5.0 megawatts.")
    create_plotly_map_1(date)
    st.markdown("In the Combined Vulnerability map, for each census tract, the predicted wildfire risk from the AI model is combined with the tract’s social vulnerability index, giving a combined vulnerability score called CV.")
    st.markdown("Tracts in darker reds have high combined vulnerability, i.e., they have both high wildfire risk AND are highly socially vulnerable. Fire managers can use this map as an assistive tool to determine areas requiring urgent support with special accommodations needed for those communities, during wildfire disasters across the USA. Some examples of Special accommodations include evacuation warnings in native language for non-English speaking communities and special assistance to evacuate communities with high disabled population.")
elif date == DATE_THREE:
    create_plotly_map(date)
    st.markdown("In the Wildfire Risk map, for a chosen date, the AI model predicts the wildfire intensity based on meteorological, topographical and vegetation inputs for each census tract across the USA. Each census tract is assigned a value of “0” or “1”, based on the AI model’s Wildfire intensity predictions. A census tract is assigned a value of “0” if its predicted wildfire intensity Fire Radiative Power (FRP) is &lt; 5.0 megawatts. Each census tract is assigned a value of “1” if its predicted wildfire intensity FRP is &gt; 5.0 megawatts.")
    create_plotly_map_1(date)
    st.markdown("In the Combined Vulnerability map, for each census tract, the predicted wildfire risk from the AI model is combined with the tract’s social vulnerability index, giving a combined vulnerability score called CV.")
    st.markdown("Tracts in darker reds have high combined vulnerability, i.e., they have both high wildfire risk AND are highly socially vulnerable. Fire managers can use this map as an assistive tool to determine areas requiring urgent support with special accommodations needed for those communities, during wildfire disasters across the USA. Some examples of Special accommodations include evacuation warnings in native language for non-English speaking communities and special assistance to evacuate communities with high disabled population.")
elif date == DATE_FOUR:
    create_plotly_map(date)
    st.markdown("In the Wildfire Risk map, for a chosen date, the AI model predicts the wildfire intensity based on meteorological, topographical and vegetation inputs for each census tract across the USA. Each census tract is assigned a value of “0” or “1”, based on the AI model’s Wildfire intensity predictions. A census tract is assigned a value of “0” if its predicted wildfire intensity Fire Radiative Power (FRP) is &lt; 5.0 megawatts. Each census tract is assigned a value of “1” if its predicted wildfire intensity FRP is &gt; 5.0 megawatts.")
    create_plotly_map_1(date)
    st.markdown("In the Combined Vulnerability map, for each census tract, the predicted wildfire risk from the AI model is combined with the tract’s social vulnerability index, giving a combined vulnerability score called CV.")
    st.markdown("Tracts in darker reds have high combined vulnerability, i.e., they have both high wildfire risk AND are highly socially vulnerable. Fire managers can use this map as an assistive tool to determine areas requiring urgent support with special accommodations needed for those communities, during wildfire disasters across the USA. Some examples of Special accommodations include evacuation warnings in native language for non-English speaking communities and special assistance to evacuate communities with high disabled population.")
elif date == DATE_FIVE:
    create_plotly_map(date)
    st.markdown("In the Wildfire Risk map, for a chosen date, the AI model predicts the wildfire intensity based on meteorological, topographical and vegetation inputs for each census tract across the USA. Each census tract is assigned a value of “0” or “1”, based on the AI model’s Wildfire intensity predictions. A census tract is assigned a value of “0” if its predicted wildfire intensity Fire Radiative Power (FRP) is &lt; 5.0 megawatts. Each census tract is assigned a value of “1” if its predicted wildfire intensity FRP is &gt; 5.0 megawatts.")
    create_plotly_map_1(date)
    st.markdown("In the Combined Vulnerability map, for each census tract, the predicted wildfire risk from the AI model is combined with the tract’s social vulnerability index, giving a combined vulnerability score called CV.")
    st.markdown("Tracts in darker reds have high combined vulnerability, i.e., they have both high wildfire risk AND are highly socially vulnerable. Fire managers can use this map as an assistive tool to determine areas requiring urgent support with special accommodations needed for those communities, during wildfire disasters across the USA. Some examples of Special accommodations include evacuation warnings in native language for non-English speaking communities and special assistance to evacuate communities with high disabled population.")

st.text_area(
    "",
    "This prototype obtains predictions from the AI model, processes and displays the maps for a few sample tracts and for few sample dates only, in order to have a short run time for user. In these maps, in order to populate all the ~80,000 census tracts across the USA takes very long run times. Instantaneous visualizations across ~80,000 census tracts across the USA requires very large processing power, for which funding is required",
    )