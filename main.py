import streamlit as st
import cv2
from PIL import Image
import numpy as np
from helper import load_model, classify_image
import settings

model = load_model(settings.CLASSIFICATION_MODEL)
class_names = ['No DR', 'Mild', 'Moderate', 'Severe', 'Proliferative DR']

def main():
    st.title("Klasifikasi Retinopati Diabetik")

    uploaded_file = st.file_uploader("Upload Citra Retina", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        st.image(image, channels="BGR", caption="Citra Retina", use_container_width=True)

        if st.button("Prediksi"):
            pred_class, confidence = classify_image(image, model, class_names)
            st.success(f"Prediksi: {pred_class} (Confidence: {confidence:.2f})")

