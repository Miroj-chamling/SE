import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('./trained_model.sav', 'rb'))


def diabetic_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0] == 0:
        st.success("Non Diabetec")
    else:
        st.success("Diabetec")


def main():
    st.title('Diabetes prediction web app')
    # title is a function like a header in streamlit library
    Pregnancies = st.text_input('Number of pregnancies')
    # st.text_input function takes the data from user as input
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood pressure value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin value')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input(
        'Diabetes Pedigree function value')
    Age = st.text_input('Age of a person')

    if st.button('CHECK RESULT'):
        diabetic_prediction(
            [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])


if __name__ == '__main__':
    main()
