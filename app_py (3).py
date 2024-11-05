# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wg3FA_F1hELdPX46U8UDgaqE3pxGURF3
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import pickle
# import pandas as pd
# import streamlit as st
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.preprocessing import StandardScaler
# 
# 
# 
#

st.sidebar.header("Masukkan Data Anak")
def user_input_features():
    Umur_bulan = st.sidebar.slider("Umur (bulan)", 0, 60)
    Jenis_Kelamin = st.sidebar.selectbox("Jenis Kelamin", (1,2))
    Tinggi_Badan_cm = st.sidebar.slider("Tinggi Badan (cm)", 0, 100)
    Status_Gizi = st.sidebar.selectbox("Status Gizi", (0,1,2,3,))