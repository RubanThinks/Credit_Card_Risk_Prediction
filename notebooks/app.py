
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

def main():
  colA1, colA2 = st.beta_columns(2)
  with colA1:
    st.info("loan_status")
    person_amount = st.number_input("How many trees are planted", value=500, step=100)

