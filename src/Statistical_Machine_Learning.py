import streamlit as st

st.set_page_config(layout="wide")


# Using object notation
col1, col2 = st.columns(2)


#st.image("Logo.png")
st.title("Statistical Machine Learning")

st.write("This is a digital version of the notes I kept for statistical machine learning (ML II) taught by [Prof. Dr. Marius Kloft](https://ml.cs.uni-kl.de) and \
            [Prof. Dr. Sebastian Vollmer](https://sebastian.vollmer.ms) at Rheinland-Pfälzische Technische Universität in Kaiserslautern, RP, Deutschland. The lecture series is written from \
            a storytelling perspective. The number of topics here do not correspond to the ones delivered by the professors to maintain a more thorough understanding. Hopefully, there will be good enough segues in these notes from one topic to another. The segues will help create a solid understanding of why a \
            particular topics needs to be in the lecture. I have not covered the exam irrelevant stuff as it was in Winter Semester 2022/23.")

st.write("If you want to contribute to the notes, please open an issue on the repository: [Probabilistic-ml](https://github.com/rssr25/probabilistic-ml)")

st.write("***")

st.header("Table of contents")

#TODO: Open them in the same page

col1, col2, col3 = st.columns(3)

with col1:
    st.write("[1. Introduction and recap of Machine Learning 1](1._Introduction)")
    st.write("[2. Bayes classifier and LDA](2._Bayes_Classfier_and_LDA)")
    st.write("[3. Bayesian Linear Regression ](3._Bayesian_Linear_Regression)")
    st.write("[4. Bayesian Kernel Regression ](4._Bayesian_Kernel_Regression)")
    st.write("[5. Laplace Approximation ](5._Laplace_Approximation)")

with col2:
    st.write("[6. Bayesian DNN Regression ](6._Bayesian_DNN_Regression)")
    st.write("[7. Unifying View of Bayesian Regression ](7._Unifying_View_of_Bayesian_Regression)")
    st.write("[8. Bayesian Classification ](8._Bayesian_Classification)")
    st.write("[9. EM Algorithm ](9._EM_Algorithm)")
    st.write("[10. Understanding EM ](10._Understanding_EM)")

with col3:
    st.write("[11. Variational Inference ](11._Variational_Inference)")
    st.write("[12. Introduction to Graphical Models ](12._Introduction_to_Graphical_Models)")
    st.write("[13. Sampling ](13._Sampling)")
    st.write("[14. Hidden Markov Model ](14._Hidden_Markov_Model)")
    st.write("[15. Kalman Filter ](15._Kalman_Filter)")

st.write("***")

st.header("Notations")
st.write("""
            - Throughout the notes thoughts are written in :blue[blue]
            - The segues are written in :green[green]
            - The underlined text represents links
            - Matrices are bold and capitalized 
            - Vectors are bold and not capitalized
        """)






