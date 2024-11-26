import streamlit as st

st.title("Streamlit Class")
st.write("This is a practice deployment")


st.text_input("Enter your name", placeholder="eg Olufemi Olagbaju")
st.text_input("Enter password", type='password')
st.text_area("Tell me about yourself", placeholder="eg I am a .....")
st.slider("pick a range", 1,16)
st.number_input("Enter you weight")

st.checkbox("I am a Male")
st.radio("Select a gender", options=["Male","Female"])
st.selectbox("Select a gender", options=["Male","Female"])
st.multiselect("Select a gender", options=["Male","Female"])


st.header("Olufemi")
st.subheader("My surname is Olagbaju")
st.write("I love python")
st.divider()
st.text("This is a very nice app")
st.success("What a success!!")
st.warning("Stop there")
st.info("Plum weapons!!")
st.error("Try Again!!")
st.exception(ZeroDivisionError("Trying to divide by zero"))
st.image("https://i.redd.it/k9xpmm86sjub1.jpg")