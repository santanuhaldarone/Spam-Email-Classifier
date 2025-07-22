import streamlit as st
from utils import load_model, predict_spam

vectorizer, model = load_model()

st.set_page_config(page_title="Spam Classifier", page_icon="")
st.title("Email Spam Classifier")
st.markdown("Check whether your email is **Spam** or **Not Spam** using a machine learning model.")

email_text = st.text_area("Enter email content below:", height=200)

if st.button("Classify"):
    if not email_text.strip():
        st.warning("Please enter the email content.")
    else:
        label, confidence = predict_spam(email_text, vectorizer, model)
        st.success(f"Prediction: **{label}**")
        st.info(f" Confidence: {confidence}%")


st.markdown("---")
st.caption("Made with ❤️ by Santanu")
