import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Bureau Cats')

data_url = 'https://raw.githubusercontent.com/jeffmacke/IDOT_pay_items/main/IDOTpayitems.csv'

@st.cache
def load_stream_github_csv (url):
    df = pd.read_csv(url,index_col=0,dtype='str')
    df['Quantity']=pd.to_numeric(df['Quantity'],errors="coerce")
    df['AwardedUnitPrice']=pd.to_numeric(df['AwardedUnitPrice'],errors="coerce")
    df['Source']=pd.to_datetime(df['Source'])
    df['Year']=pd.DatetimeIndex(df['Source']).year
    return df
idot_data = load_stream_github_csv(data_url)

st.sidebar.header('Select Pay Item')
selected_item = st.sidebar.text_input('Item', 'A2C010G5')  
selected_low_qty = int(st.sidebar.text_input('From quantity',0))
selected_high_qty = int(st.sidebar.text_input('to quantity',50000))

st.markdown("""
This app performs simple analysis of IDOT bid tabulation data!
* **Python libraries:** seaborn, pandas, streamlit
* **Data source:** [idot.illinois.com](https://idot.illinois.gov/).
""")

st.subheader("Bid Items 2017 to 2021 based on Selection")

selection = idot_data[(idot_data['PayItemNumber']==selected_item)&(idot_data['Quantity']>selected_low_qty)&(idot_data['Quantity']<selected_high_qty)]
selection

st.subheader(selection['PayItemDescription'].iloc[0]+  "\nQuantity vs. Awarded Price Regression Line")

fig=sns.jointplot(data=selection, x=selection['Quantity'],y=selection['AwardedUnitPrice'],kind="reg")
st.pyplot(fig)

st.subheader(selection['PayItemDescription'].iloc[0]+"\nStatistics")

item_stats = selection.describe()
item_stats
