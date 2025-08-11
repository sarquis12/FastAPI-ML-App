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
        "grant_type": "password",
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


def send_feedback(
    token: str, feedback: str, score: float, prediction: str, image_file_name: str
) -> requests.Response:
    """
    Send user feedback to the /feedback endpoint.
    """
    # TODO: Implement the send_feedback function

    url = f"{API_BASE_URL}/feedback"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "feedback": feedback,
        "score": score,
        "predicted_class": prediction,
        "image_file_name": image_file_name
    }

    response = requests.post(url, headers=headers, json=payload)
    return response
