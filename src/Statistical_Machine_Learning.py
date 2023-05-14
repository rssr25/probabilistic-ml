import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

# Using object notation
col1, col2 = st.columns(2)


st.image("Logo.png")
st.title("Statistical Machine Learning")

st.markdown("This is a digital version of the notes I kept for statistical machine learning (ML II) taught by [Prof. Dr. Marius Kloft](https://ml.cs.uni-kl.de) and \
            [Prof. Dr. Sebastian Vollmer](https://sebastian.vollmer.ms) at Rheinland-Pfälzische Technische Universität in Kaiserslautern, RP, Deutschland. The lecture series is written from \
            a storytelling perspective. The number of topics here do not correspond to the ones delivered by the professors to maintain a more thorough understanding. Hopefully, there will be good enough segues in these notes from one topic to another. The segues will help create a solid understanding of why a \
            particular topics needs to be in the lecture. I have not covered the exam irrelevant stuff as it was in Winter Semester 2022/23.")

st.markdown("If you want to contribute to the notes, please open an issue on the repository: [Probabilistic-ml](https://github.com/rssr25/probabilistic-ml)")

st.markdown("***")

st.header("Table of contents")

#TODO: Open them in the same page
st.markdown("[1. Introduction and recap of Machine Learning 1](1._Introduction)")
st.markdown("[2. Bayes classifier and LDA](2_2._Bayes_Classfier_and_LDA)")
st.markdown("[3. Bayesian Linear Regression ](3_3._Bayesian_Linear_Regression)")
st.markdown("[4. Bayesian Kernel Regression ](4_4._Bayesian_Kernel_Regression)")
st.markdown("[5. Laplace Approximation ](5_5._Laplace_Approximation)")
st.markdown("[6. Bayesian DNN Regression ](6_6._Bayesian_DNN_Regression)")
st.markdown("[7. Unifying View of Bayesian Regression ](7_7._Unifying_View_of_Bayesian_Regression)")
st.markdown("[8. Bayesian Classification ](8_8._Bayesian_Classification)")
st.markdown("[9. EM Algorithm ](9_9._EM_Algorithm)")
st.markdown("[10. Understanding EM ](10_10._Understanding_EM)")
st.markdown("[11. Variational Inference ](11_11._Variational_Inference)")
st.markdown("[12. Introduction to Graphical Models ](12_12._Introduction_to_Graphical_Models)")
st.markdown("[13. Sampling ](13_13._Sampling)")
st.markdown("[14. Hidden Markov Model ](14_14._Hidden_Markov_Model)")
st.markdown("[15. Kalman Filter ](15_15._Kalman_Filter)")






