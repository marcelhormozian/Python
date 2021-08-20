# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 23:04:25 2021

@author: Startklar
"""
import streamlit as st
import pandas as pd



@st.cache()
def f():
    return


flows = [0,0,0,0,0]
for case_nr in range(0,5):
    flows[case_nr] = st.slider('point'+str(case_nr),0,2000,400,step=10)


sum = sum(flows)
st.header('summ of values of all sliders: ')
st.write(sum)



