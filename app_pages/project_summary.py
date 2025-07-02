import streamlit as st
import matplotlib.pyplot as plt


def project_summary_body():
    """
    Display content for the Project Summary
    page
    """
    st.write("### Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects many plant species. "
        f"Caused by various ascomycete fungi, it appears as distinctive white spots "
        f"on the leaves and stems of infected plants.\n"
        f"* This disease thrives in environments with moderate temperatures and high humidity, "
        f"and is a common issue in horticultural crops, where it can significantly reduce yields.\n"
        f"* The client is currently facing an outbreak across several cherry tree plantations. "
        f"Manual inspection of the trees has proven inefficient, prompting the need for a more scalable solution. "
        f"The client has requested the development of a Machine Learning (ML) model capable of analyzing uploaded photos "
        f"to determine whether a leaf shows signs of infection."
    )


    st.info(
        f"**Dataset Information**\n"
        f"* The dataset provided by the client contains 4,208 images "
        f"of leaves taken from their cherry trees (2,104 each for both "
        f"healthy and infected leaves).\n"
        f"* It is available to download from "
        f"[Kaggle]"
        f"(https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)"
    )

    st.write(
        f"* For more information, please see the "
        f"[Project README file]"
        f"(https://github.com/IeuanPriede/project_5_mildew_detection/blob/main/README.md).")
    
    st.success(
        f"**Business Requirements**\n"
        f"* Farmy & Foods is facing a major challenge with powdery mildew affecting their cherry plantations. "
        f"Currently, detection is done manually: an employee inspects each tree for signs of the disease by visually examining leaf samples—"
        f"a process that takes around 30 minutes per tree. If mildew is found, a compound is applied in a separate step taking just 1 minute.\n"
        f"* With thousands of trees spread across multiple farms nationwide, this manual inspection approach is not scalable due to the time and labor involved.\n"
        f"* To improve efficiency, the company's IT team has proposed a Machine Learning (ML) system capable of instantly detecting powdery mildew from images of cherry leaves. "
        f"Farmy & Foods has provided a dataset of such images taken from their own plantations.\n"
        f"* If successful, this solution could be extended to other crops where similar manual pest detection processes are used.\n\n"
        f"**Requirement 1** - Conduct a study to determine whether healthy and infected cherry leaves can be visually distinguished using photographs.\n"
        f"* This is a critical first step in validating the feasibility of an automated visual detection system.\n\n"
        f"**Requirement 2** - Develop an ML model to predict whether a cherry leaf is healthy or infected with powdery mildew based on an uploaded image.\n"
        f"* Once visual differentiation is confirmed, we will train and evaluate a predictive model to automate the detection process."
    )