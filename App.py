import streamlit as st
from PIL import Image

st.title("The TB Active Case Finding Data Collection")
st.subheader("A Statewise Active and Latent Tuberculosis Data Entry Form")

img = Image.open("tbimage 3.png")
st.image(img)

st.text_input("First name")

st.text_input("Last name")

st.text_input("State of Origin of Infected person")

st.number_input("Family size", step=1)

st.selectbox("Gender",["Male", "Female", "Others"])

st.radio("Age Group",["Under Thirty", "Thirty-Below Seventy", "Over Seventy"])

st.text_input("Home Address")

img = Image.open("imageb.jpg")
st.sidebar.image(img)

def bmi_calc(w,h):
    bmi = w/(h**2)
    bmi =  round(bmi,1)

    if bmi >= 35:
        return f"Your BMI is {bmi}, you are at risk of obesity class 2."
    elif 30 <= bmi < 35:
        return f"Your BMI is {bmi}, you are at risk of obesity class 1."
    elif 25 <= bmi < 30:
        return f"Your BMI is {bmi}, you are at risk of pre- obesity."
    elif 18.5 <= bmi < 25:
        return f"Your BMI is {bmi}, you are within the healthy range."
    else:
        return f"Your BMI is {bmi}, you are at risk of underweight."
    
House_number = st.number_input("Enter your house number", step=1)
     
x = st.sidebar.number_input("Enter Your Weight", step=0.1)
y = st.sidebar.number_input("Enter Your Height", step=0.1)


Temprature = st.slider("Slide to indicate your body temprature in celcius", 0, 100)
 
if st.sidebar.button("Calculate BMI"):
    z = x/(y**2)
    st.sidebar.write(f"Your BMI is {z}")

st.date_input("First Date of Noticeable Sypmtoms")

if st.checkbox("Click If Symptoms are severe"):
    st.success("Refer to Nearest TB Treatment Centre")
