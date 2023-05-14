import streamlit as st

st.markdown('# Introduction')

st.write('''
Welcome to ML II. In this lecture we study about how to see the machine learning models from a statistical perspective. 
To begin with the lecture, let's see the **Unifying Equation** for the machine learning models studied in Machine Learning 1 taught by Prof. Dr. Marius Kloft.
''')

st.write('''###### Unifying Equation from ML1:''')

st.latex(r'''
\min_{[W,] b, \mathbf{w}} \frac{1}{2}||\mathbf{w}||^2 + C\sum_{i=1}^nl(f(\mathbf{x}_i) [,y_i]) \left[+ \frac{1}{2}\sum_{l=1}^L||\mathbf{W}_l||_{Fro}^2\right]
''')
        
st.write("where we have that")


st.code("#Remember this equation as it will help connect the dots later.")