import streamlit as st
from PIL import Image
import helper
import settings

def main():
    st.title("Retina Disease Classification 👁️")

    uploaded_file = st.file_uploader("📤 Upload Retina Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        model = helper.load_model_keras(str(settings.DETECTION_MODEL))

        if st.button(" 🔍 Classify"):
            pred_class, confidence = helper.classify_image(model, image)
            st.success(f"Predicted Class: {pred_class} with confidence {confidence:.2f}")

            # Save to history in session state
            if "history" not in st.session_state:
                st.session_state.history = []
            st.session_state.history.append({
                "image": image,
                "pred_class": pred_class,
                "confidence": confidence
            })

def show_history():
    st.header("Prediction History")
    if "history" in st.session_state and st.session_state.history:
        for idx, record in enumerate(st.session_state.history):
            st.image(record["image"], caption=f"Prediction {idx + 1}: Class {record['pred_class']} Confidence: {record['confidence']:.2f}", use_container_width=True)
    else:
        st.write("No history yet.")


