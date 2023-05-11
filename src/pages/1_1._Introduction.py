import streamlit as st
st.latex(r'''
\min_{[W,] b, \mathbf{w}} \frac{1}{2}||\mathbf{w}||^2 + C\sum_{i=1}^nl(f(\mathbf{x}_i) [,y_i]) \left[+ \frac{1}{2}\sum_{l=1}^L||\mathbf{W}_l||_{Fro}^2\right]
''')