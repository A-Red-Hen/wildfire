import streamlit as st

image_address = "homepic.jpg"
st.title('WildfireWatch')
st.subheader("Merging AI-driven wildfire predictions with social vulnerability assessments, determining areas requiring urgent support during wildfire disasters across the USA")
st.image(image_address, caption="Photo credits: Thomas Ehling on Unsplash")

st.markdown("Climate change has worsened wildfire activity in recent years. Did you know there have been around 70,000 fire incidents and 7 million acres burned every year in the USA? Also wildfires unfairly affect disadvantaged communities, like those with high poverty levels or a high percentage of disabled population. So it is critical not only to model wildfire spread accurately, but also to identify socially vulnerable areas that have a high risk for wildfire for creating equitable communities. WildfireWatch does exactly that.")