import streamlit as st
import pandas as pd
import plotly.express as px

#page config.........
st.set_page_config(page_title='My S tramlit Website',page_icon='📊',layout='wide')

# title and description........
st.title('My Streamlit Website')
st.markdown('### A simple data visuilization app website with streamlit')

#Add a sidebar
st.sidebar.header('NAVIGATION')

#create a some sample data.....
data ={
    'year':[2019,2020,2021,2022,2023],
    'sales':[100,200,300,400,500],
    'Expenses':[50,100,150,200,250],
    'Profit':[50,100,150,200,250],
    'Revenue':[150,300,450,600,750],
    
}
df = pd.DataFrame(data)

#add intteractive elements 
selected_metric = st.sidebar.selectbox(
    'Choose a metric',
    ['Sales','Expenses','Profit','Revenue']
)

#add two columns.......
col1,col2 = st.columns(2)


with col1:
    st.subheader('Data overview')
    st.dataframe(df)

with col2:
    st.subheader(f'{selected_metric} over the years')
    fig = px.line(df,x='year',y=selected_metric)
    st.plotly_chart(fig)

#add a file uploader..........
st.header('File Uploader')
uploaded_file = st.file_uploader('Choose a csv file',type='csv')

if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write('Data from uploaded file')
    st.dataframe(df_uploaded.head())

## add a bar chart visuilization......
st.header('Bar Chart')

#user select a columns for x and y axis.........
if not df_uploaded.empty:
    x_columns =st.selectbox('Select x-axis columns',df_uploaded.columns)
    y_columns =st.selectbox('select y-axis columns',df_uploaded.columns)

#display the bar chart.........
    fig = px.bar(df_uploaded,x=x_columns,y=y_columns)
    st.plotly_chart(fig)

    


