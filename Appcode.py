import streamlit as st
from streamlit_lottie import st_lottie_spinner
import pickle
import json
from flask import request
def main():
    st.title("loan acceptance")
    
    attributes = []
    for i in range(1, 14):
        attributes.append(st.text_input(f"Enter attribute {i}: "))
    
    detection = ""
    if st.button("Detect"):
        with open("dt.pkl","rb") as file:
            model=pickle.load(file)
        msg = st.empty()
        prepared_input = [float(attr) for attr in attributes]  # Assuming the attributes are numerical
        prediction = model.predict([prepared_input])[0]
        if prediction == 1:
            msg.error("will take loan")
        elif prediction== 0:
            msg.success("Wont take Loan")
            st.balloons()

if __name__ == '__main__':
    main()
