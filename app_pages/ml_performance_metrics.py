import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def ml_performance_metrics():
    """
    Display text and images for
    the Performance Metrics page
    """
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    distribute_label = plt.imread(
        f"outputs/{version}/labels_distribution.png"
    )
    st.image(
        distribute_label,
        caption='Labels Distribution on Train, Validation and Test Sets'
    )

    st.info(
        "* The dataset was divided into 3 parts, "
        "a train set, a test set, and a validation set. "
        "This is the most common way to proportion data for "
        "Machine Learning.\n"
        "* The train set, being the largest, was the first "
        "data the ML model was introduced to. "
        "The larger size of this dataset ensures that the "
        "model will be exposed to a sufficient amount of data "
        "that it will be able to fully learn the difference "
        "between both kinds of images.\n"
        "* The validation set was then used to improve "
        "the model's performance.\n"
        "* Finally, the test set was used as a final check "
        "to ensure that the model can handle new data and that "
        "it had learned as intended."
    )
    st.write("---")

    st.write("### Model History")
    col1, col2 = st.columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')

    st.info(
        "* As the above graphs show, the model performed "
        "generally at a high level of accuracy.\n"
        "* Initial performance on the training set "
        "improved quickly in the first few epochs. "
        "Despite a drop in performance at epoch 7, "
        "the model regained accuracy in the next one "
        "and continued to improve.\n"
        "* The graph for loss, which indicates how well "
        "a model performs by examining how different "
        "the predictions it makes are from the truth, "
        "shows that the model performed well on both "
        "the training and validation sets. Overfitting has "
        "also been kept to a minimum."
    )

    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(
        pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy'])
    )
    st.info(
        "* The client at the outset of this project "
        "requested a ML model that could predict "
        "with 97% accuracy whether a leaf had mildew "
        "or not based on the image.\n"
        "* As the above table shows, the model predicted "
        "with 99% accuracy the status of "
        "images in the test dataset. We may therefore "
        "consider this requirement satisfied."
    )
