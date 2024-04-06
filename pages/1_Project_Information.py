import streamlit as st

st.title('Information')

st.header('Wildfire intensity modeling')
st.markdown('Wildfiire intensity prediction modeling was done using machine learning classification methods for Fire Radiative Power(FRP) Threshold of 5.0 megawatts, using a very large input dataset (WildfireDB) containing meterological, topographical and vegetation data across the USA.')
st.markdown('The AI model predicts the wildfire intensity based on meteorological, topographical and vegetation inputs for each census tract across the USA. Each census tract is assigned a value of “0” or “1”, based on the AI model’s wildfire intensity predictions. A census tract is assigned a value of “0” if its predicted wildfire intensity Fire Radiative Power (FRP) is &lt; 5.0 megawatts. Each census tract is assigned a value of “1” if its predicted wildfire intensity FRP is &gt; 5.0 megawatts.')

st.header('Social Vulnerability')
st.markdown('**Social Vulnerability** shows the extent to which a community has social conditions, e.g. high poverty, high percentage of disabled population or low transportation access. These conditions may affect the community’s ability to prevent human suffering (mortality, not being able to recover from financial loss, losing their homes, getting displaced from the community) during disaster events.')
st.markdown('The social vulnerability data for &lt;project name&gt; was obtained from the Centers for Disease Control and Prevention’s CDC SVI Database, which ranks all the ~80,000 census tracts across the USA based on their social vulnerability index (SVI). SVI is calculated for each census tract based on the 15 factors shown in below picture. The SVI value for each tract will be a real number in the range of 0.0 to 1.0, with the least socially vulnerable tracts having a value of 0.0 and the most socially vulnerable tracts having a value of 1.0.')
img1 = "img1.png"
st.image(img1, caption="Themes and Factors for Social Vulnerability (taken from the CDC SVI Database)")

st.header('Combined Vulnerability')
st.markdown('Combined Vulnerability is defined in the context of a community’s exposure to wildfire hazard along with its ability to withstand the impact of the wildfire at the census tract level.')

img2 = "img2.png"
st.image(img2)

st.markdown('CV tract will range from 0.0 to 2.0, where tracts that have the highest combined vulnerability have values closer to 2.0.')
st.markdown('Fire managers can use this score as an assistive metric to determine areas requiring urgent support with special accommodations needed for those communities, during wildfire disasters across the USA.')

img3 = "img3.png"
st.image(img3)