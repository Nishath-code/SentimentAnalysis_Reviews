import streamlit as st
import pickle

# Load model
model = pickle.load(open("modelst.pkl", "rb"))

st.set_page_config(page_title="Review Sentiment Classifier")

st.title("🍽️ Review Sentiment Classifier")
st.write("Enter a review and predict sentiment")

review = st.text_area("Enter your review:")

if st.button("Predict"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        prediction = model.predict([review])[0]

        if prediction == 1:
            st.success("✅ Positive Review")
        else:
            st.error("❌ Negative Review")
