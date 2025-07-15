# write app to sandbox

import streamlit as st
import numpy as np

# define your app content
def main():

  colA1, colA2 = st.beta_columns(2)
  with colA1:
    st.info("Number of trees")
    trees_amount = st.number_input("How many trees are planted", value=500, step=100)

  with colA2:
    st.info("Money invested")
    investment_amount = st.number_input("currency is USD", value=50000, step=10000)

  input = np.array([[trees_amount, investment_amount]]).astype(np.float64)


# execute the main function
if __name__ == '__main__':
	main()
