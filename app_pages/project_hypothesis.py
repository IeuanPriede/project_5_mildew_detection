import streamlit as st
import matplotlib.pyplot as plt


def project_hypothesis_body():
    """
    Display content for Project Hypotheses Page
    """
    st.write("### Project Hypotheses")

    # Hypothesis 1
    st.info(
        "**Hypothesis 1**\n"
        "* Cherry leaves affected by powdery mildew exhibit consistent "
        "visual patterns that can be detected and accurately classified "
        "by a machine learning model."
    )

    # Hypothesis 2
    st.info(
        "**Hypothesis 2**\n"
        "* Powdery mildew primarily affects specific regions of the leaf "
        "(e.g., edges or veins), creating spatial patterns that can be "
        "exploited by a convolutional neural network."
    )

    # Hypothesis 3
    st.info(
        "**Hypothesis 3**\n"
        "* Variability in colour and texture between healthy and infected "
        "leaves is sufficiently distinct to allow accurate classification "
        "without manual feature engineering."
    )

    # Hypothesis 4
    st.info(
        "**Hypothesis 4**\n"
        "* The model's classification performance is resilient to moderate "
        "variations in image quality (e.g., lighting, resolution, "
        "orientation), supporting deployment in real-world field conditions."
    )

    st.write("### Validation Strategy")

    st.success(
        "**Step 1: Visual Analysis**\n"
        "* Generate average and variability images for each class (healthy "
        "vs. infected) to confirm visible differences.\n\n"

        "**Step 2: Region Sensitivity**\n"
        "* Use saliency maps or Grad-CAM to verify whether the CNN attends "
        "to the infected areas consistently.\n\n"

        "**Step 3: Texture and Colour Evaluation**\n"
        "* Extract RGB histograms and texture descriptors. Train a simple "
        "classifier to determine whether these features alone allow "
        "separation.\n\n"

        "**Step 4: Image Robustness Testing**\n"
        "* Evaluate the model's predictions on augmented images with changes "
        "to brightness, noise, and orientation.\n\n"

        "**Step 5: Model Training**\n"
        "* Train a Convolutional Neural Network (CNN) using the labeled "
        "cherry leaf dataset.\n\n"

        "**Step 6: Performance Evaluation**\n"
        "* Assess the model using accuracy, confusion matrix, precision, "
        "recall, and F1-score.\n\n"

        "**Step 7: Model Deployment**\n"
        "* Integrate the trained model into a Streamlit dashboard to allow "
        "real-time predictions from uploaded images.\n\n"

        "**Target Accuracy:** ≥ 97%"
    )
