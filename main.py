import streamlit as st
import pandas as pd
import numpy as np

# Create some example data
data = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.randn(10)
})

# Display the data in a line chart
st.line_chart(data['y'])

# You can also customize the chart by providing a dictionary with additional options
# For example, adding a title and labels
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data, use_container_width=True)

# You can also use st.plotly_chart for more interactivity
# import plotly.express as px
# fig = px.line(chart_data, x=chart_data.index, y=['a', 'b', 'c'])
# st.plotly_chart(fig)
