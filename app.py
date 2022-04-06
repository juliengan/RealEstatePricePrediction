import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import pydeck as pdk
import plotly.express as px


	
st.markdown(
      """
	  <style>
     .main {
     color: #6495ED;

     }</style>
      
      """,
      unsafe_allow_html=True
  )

    #Header:
Image = Image.open('logo.png')
st.image(Image, width = 220)
st.text('Land valueviz is an app that permits to visualize land values data and compare them. All in pure Python..')
	
	
   #Data Loading dataset:
st.header('Lets visualize 💫!')
st.text('This website is using 2016 and 2020s data')
st.balloons()

	#Importing Datasets, i choose to work only with 2016 and 2020

@st.cache
def load_data1():
	df = pd.read_csv("full_2016.csv")
	return df
df = load_data1()


@st.cache
def load_data2():
	df2 = pd.read_csv("full_2020.csv")
	return df2
df2 = load_data2()

 
    # This cand lead you to the website from which the datasets are token for additional informations
st.text(' If you want to learn more you can visit the 🇫🇷 government website  : ')
if st.button("Take me to their website"):
	st.write("[🇫🇷 www.data.gouv.fr 🇫🇷 ]( https://www.data.gouv.fr/en/datasets/demandes-de-valeurs-foncieres/)")


    #Datasets

st.sidebar.write('Select a year to show the data:')
option_1 = st.sidebar.checkbox('👉 2016 👈')
option_2 = st.sidebar.checkbox('👉 2020 👈')
if option_1:
	st.write(df.head(1000))
	st.write(' 2016 Data here 👆  ')
	st.text(' Click on the 💬 on the right to save the chart')

if option_2:
	st.write(df2.head(1000))
	st.write(' 2020 Data here 👆  ')
	st.text(' Click on the 💬 on the right to save the chart')

   #modelTraining:

#Bar chart
st.text(' This is a bar chart showing our data according to each commune')	
df = pd.read_csv("full_2016.csv")
code_commune = df['code_commune'].value_counts().head(20)
st.bar_chart(code_commune )


df2 = pd.read_csv("full_2020.csv")
st.text(' Click on the 💬 on the right to save the chart')
code_commune = df['code_commune'].value_counts().head(10)
st.bar_chart(code_commune )
      

st.text(' Our app aim to visualize 2016 and 2020s data, by comparing mainly between these 2 years')
st.title(' ** 2016 VS 2020 **')


	#Commune according to the land value (2016)
st.text(' 2016')

fig = px.scatter(df, x="valeur_fonciere", y="code_commune")
fig.show()
st.write(fig)

    	#Commune according to the land value (2020)
st.text(' 2020')

fig = px.scatter(df, x="valeur_fonciere", y="code_commune")
fig.show()
st.write(fig)



st.header('Time to train the model !')
st.text( 'You got to choose the hyperparameters of the model and see how the perormance change')
sel_col, disp_col = st.columns(2) 
max_depth = sel_col.slider( ' Choose a departement ', min_value = 00 , max_value = 101)
    

df = pd.read_csv("full_2016.csv")
df['latitude']=pd.to_numeric(df['latitude']) 
df['longitude']=pd.to_numeric(df['longitude'])
map_data = df[["latitude", "longitude"]]

st.map(map_data)





