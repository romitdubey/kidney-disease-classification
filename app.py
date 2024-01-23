import streamlit as st
from PIL import Image
from cnnClassifier.pipeline.prediction import PredictionPipeline  # Import your prediction pipeline class
import subprocess
import os


# Streamlit web app
def main():
    st.title("Kidney Disease Classification App")

    # Upload image through streamlit
    uploaded_image = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_image is not None:
        col1, col2 = st.columns(2)

        # Column 1: Display the image
        col1.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)
        
        # Prediction Pipeline
        pipeline = PredictionPipeline(filename=uploaded_image)
        # Column 2: Display the prediction result
        if col2.button("Predict"):
            with st.spinner('Predicting...'):
                prediction_result = pipeline.predict()

                # Display the prediction result
                col2.success(f"Prediction: {prediction_result[0]['image']}")
                

# Run the app
if __name__ == '__main__':
    main()