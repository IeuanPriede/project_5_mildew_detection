import streamlit as st
import matplotlib.pyplot as plt


def project_summary_body():
    """
    Display content for the Project Summary page
    """
    st.write("### Project Summary")

    st.info(
        "**General Information**\n"
        "* Powdery mildew is a fungal disease that affects many plant "
        "species. Caused by various ascomycete fungi, it appears as "
        "distinctive white spots on the leaves and stems of infected "
        "plants.\n"
        "* This disease thrives in environments with moderate temperatures "
        "and high humidity, and is a common issue in horticultural crops, "
        "where it can significantly reduce yields.\n"
        "* The client is currently facing an outbreak across several cherry "
        "tree plantations. Manual inspection of the trees has proven "
        "inefficient, prompting the need for a more scalable solution. The "
        "client has requested the development of a Machine Learning (ML) "
        "model capable of analyzing uploaded photos to determine whether a "
        "leaf shows signs of infection."
    )

    st.info(
        "**Dataset Information**\n"
        "* The dataset provided by the client contains 4,208 images of "
        "leaves taken from their cherry trees (2,104 each for both healthy "
        "and infected leaves).\n"
        "* It is available to download from [Kaggle]\n"
        "(https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)."
    )

    st.write(
        "* For more information, please see the [Project README file]\n"
        "(https://shorturl.at/7O7XV)."
    )

    st.success(
        "**Business Requirements**\n"
        "* Farmy & Foods is facing a major challenge with powdery mildew "
        "affecting their cherry plantations. Currently, detection is done "
        "manually: an employee inspects each tree for signs of the disease "
        "by visually examining leaf samples—a process that takes around 30 "
        "minutes per tree. If mildew is found, a compound is applied in a "
        "separate step taking just 1 minute.\n"
        "* With thousands of trees spread across multiple farms nationwide, "
        "this manual inspection approach is not scalable due to the time "
        "and labor involved.\n"
        "* To improve efficiency, the company's IT team has proposed a "
        "Machine Learning (ML) system capable of instantly detecting "
        "powdery mildew from images of cherry leaves. Farmy & Foods has "
        "provided a dataset of such images taken from their own plantations.\n"
        "* If successful, this solution could be extended to other crops "
        "where similar manual pest detection processes are used.\n\n"
        "**Requirement 1** - Conduct a study to determine whether healthy "
        "and infected cherry leaves can be visually distinguished using "
        "photographs.\n"
        "* This is a critical first step in validating the feasibility of "
        "an automated visual detection system.\n\n"
        "**Requirement 2** - Develop an ML model to predict whether a "
        "cherry leaf is healthy or infected with powdery mildew based on "
        "an uploaded image.\n"
        "* Once visual differentiation is confirmed, we will train and "
        "evaluate a predictive model to automate the detection process."
    )
