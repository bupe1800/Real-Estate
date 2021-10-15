# -*- coding: utf-8 -*-
"""app2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RfG_KsmPUe2LqJ6lcESc-29RNu762aNU
"""

import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False)
model = pickle.load(open('final_model.pkl','rb'))


def main():
  st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>House Price Predictor</h1>", unsafe_allow_html=True)
  #st.markdown("<h3 style='text-align: center; color: Black;'>Drop in The required Inputs and we will do  the rest.</h3>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: center; color: White;background-color:#0000FF'>A Machine Learning web App to predict the price of a house</h4>", unsafe_allow_html=True)
  #st.sidebar.header("What is this Project about?")
  #st.sidebar.text("It a Web app that would help the user in determining the price of a house .")
  #st.sidebar.header("What tools where used to make this?")
  #st.sidebar.text("The Model was made using a dataset from Kaggle along with using Kaggle notebooks to train the model. We made use of Sci-Kit learn in order to make our Linear Regression Model.")
  st.markdown("<h4 style='text-align: center; color: White;background-color:#800080'>Use slide bars to enter the geographic location</h4>", unsafe_allow_html=True)


  Area_Income = st.slider("Avg. Income of residents of the city",17796.63,107701.74)
  house_age = st.slider("Age of the House",2.6,9.5)
  Number_of_Rooms = st.slider("Number of Rooms",3,10)
  Number_of_Bedrooms = st.slider("Number of Bedrooms",2,6)
  Area_Population = st.slider("Area Population",24.9,25.1)

  inputs = [[Area_Income,house_age,Number_of_Rooms,Number_of_Bedrooms,Area_Population]]

  if st.button('Predict'):
    result = model.predict(inputs)
    st.success('The Estimated price of the house is {}'.format(result))


if __name__ =='__main__':
  main()