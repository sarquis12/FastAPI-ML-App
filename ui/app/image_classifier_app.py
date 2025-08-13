from typing import Optional

import requests
import streamlit as st
from app.settings import API_BASE_URL
from PIL import Image


def login(username: str, password: str) -> Optional[str]:
    """
    Authenticate the user and return a JWT token if successful.
    """
    # TODO: Implement the login function

    url = f"{API_BASE_URL}/login"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "",
        "username": username,
        "password": password,
        "scope": "",
        "client_id": "",
        "client_secret": ""
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json().get("access_token")
    return None


def predict(token: str, uploaded_file: Image) -> requests.Response:
    """
    Send the uploaded image to the /model/predict endpoint.
    """
    # TODO: Implement the predict function

    url = f"{API_BASE_URL}/model/predict"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    files = {
        "file": (uploaded_file.name, uploaded_file.getvalue())
    }

    response = requests.post(url, headers=headers, files=files)
    return response


# Configure page and layout
st.set_page_config(page_title="Dogs Classifier App", page_icon="🐶")

# Title of the application
st.title("🎯 Dogs Classifier App")

# Login section in sidebar
st.sidebar.header("🔐 Login")
username = st.sidebar.text_input("User")
password = st.sidebar.text_input("Password", type="password")

if "token" not in st.session_state:
    st.session_state.token = None

if st.sidebar.button("Start Session"):
    token = login(username, password)
    if token:
        st.session_state.token = token
        st.sidebar.success("Authentication approved ✅")
    else:
        st.sidebar.error("Authentication failed ❌")

# Image upload and prediction
st.header("📤 Upload File")
uploaded_file = st.file_uploader("Choose an image (png/jpg/jpeg)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    if st.session_state.token:
        response = predict(st.session_state.token, uploaded_file)
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                st.success(f"Prediction: {data.get('prediction')} | Score: {data.get('score')}")
            else:
                st.warning("Prediction failed.")
        else:
            st.error(f"Service error: {response.status_code}")
    else:
        st.info("Please start session to classify the image.")



def send_feedback(
    token: str, feedback: str, score: float, prediction: str, image_file_name: str
) -> requests.Response:
    """
    Send user feedback to the /feedback endpoint.
    """
    # TODO: Implement the send_feedback function

    url = f"{API_BASE_URL}/feedback"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "feedback": feedback,
        "score": score,
        "predicted_class": prediction,
        "image_file_name": image_file_name
    }

    response = requests.post(url, headers=headers, json=payload)
    return response
