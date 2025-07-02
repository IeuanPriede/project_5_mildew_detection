import streamlit as st
import matplotlib.pyplot as plt

def project_hypothesis_body():
    """
    Display content for Project Hypotheses Page
    """
    st.write("### Project Hypothesis")

    st.info(
        f"**Hypothesis**\n"
        f"* Cherry leaves affected by powdery mildew exhibit consistent visual patterns "
        f"that can be detected and accurately classified by a machine learning model."
    )

    st.write("### Validation Strategy")

    st.success(
        f"**Step 1: Visual Analysis**\n"
        f"* Generate average and variability images for each class (healthy vs. infected) "
        f"to confirm visible differences.\n"
        f"\n"
        f"**Step 2: Model Training**\n"
        f"* Train a Convolutional Neural Network (CNN) using the labeled cherry leaf dataset.\n"
        f"\n"
        f"**Step 3: Performance Evaluation**\n"
        f"* Evaluate the model using accuracy, confusion matrix, and class-specific metrics "
        f"to measure its predictive performance.\n"
        f"\n"
        f"**Step 4: Model Deployment**\n"
        f"* Deploy the trained model in an interactive dashboard and test it with new leaf images "
        f"to assess real-world usability.\n"
        f"\n"
        f"**Target Accuracy:** ≥ 97%"
    )
