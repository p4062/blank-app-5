import streamlit as st
from joblib import dump, load

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

model = load('linear_regression_model.joblib')
user_input = int(input ("Enter house size:"))
input_array = np.array([user_input]).reshape(-1, 1)
predicted_price = model.predict(input_array)
print(f"Predicted Value: {predicted_price[0]:.2f}")