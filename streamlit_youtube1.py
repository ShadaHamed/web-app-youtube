# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Impors
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 1. Title and Subheader
st.title("Data Analysis")
st.subheader("Data Analysis using python & streamlit")

# 2. Upload Dataset 
upload = st.file_uploader("Upload your dataset (in CSV format)")
if upload is not None:
    data = pd.read_csv(upload)

# 3. Show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if (st.button("head")):
            st.write(data.head())
        if (st.button("tail")):
            st.write(data.tail())

# 4. Check Datatype of each column (not work)
# But first we need to Change the data type because of error: "It’s a bug that came with streamlit 0.85.0. pyarrow has an issue with numpy.dtype values (which df.dtypes returns)."
#new_data = data.astype(str)

if upload is not None:
    if st.checkbox("Datatype of each column"):
        st.text("DataTypes")
        #st.write(new_data.dtypes)
      
        
# 5. Find shape of our Dataset(number of rows and number of columns)
if upload is not None:
   data_shape = st.radio("What Dimention do you want to check? ", ('Rows', 'Columns')) 
   if data_shape == 'Rows':
       st.text("Nember of Rows")
       st.write(data.shape[0])
   if data_shape == 'Columns':
        st.text("Nember of Columns")
        st.write(data.shape[1])

# 6. Find Null values in the dataset   (not work)
if upload is not None:
    test = data.isnull().values.any()
    if test == True:
        if st.checkbox("Null values in the dataset"): 
            sns.heatmap(data.isnull())
            fig = plt.figure(figsize=(15,5))
            st.pyplot()
    else:
        st.success("congratulation, No missing value")
    
    

# 7. Find duplicate value in the dataset
if upload is not None:
    test = data.duplicated().values.any()
    if test ==True:
        st.warning("This Dataset contains some duplicate value" )
        dup = st.selectbox("Do you want to remove duplicate values", \
                            ("select One", "Yes", "No"))
        if dup == "Yes":
            data = data.drop_duplicates()
            st.text("Duplicated values are removed")
                
        if dup == "No":
            st.text("Ok, No problem")
            
# 8. Get overall statistics {describe(include='all) not work}
if upload is not None:
    if st.checkbox("Summary of the dataset"):
        st.write(data.describe())

# 9. About section 

if st.button('About App'):
    st.text("Buillt with streamlit")
    st.text("Thanks to streamlit")

# 10. By

if st.checkbox("By"):
    st.success('Shada Hamed Al-Safi')