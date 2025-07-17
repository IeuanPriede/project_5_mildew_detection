import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def image_visualizer_body():
    st.write("### Image Visualizer")
    st.info(
        "* This page will examine Business Requirement 1.\n"
        "* The client is interested in conducting a study to visually "
        "differentiate a healthy leaf from one with powdery mildew."
    )

    version = 'v1'
    if st.checkbox("Difference between average and variability image"):

        avg_healthy = plt.imread(
            f"outputs/{version}/avg_var_healthy.png"
        )
        avg_mildew = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png"
        )

        st.image(
            avg_healthy,
            caption='Healthy Leaf - Average and Variability'
        )
        st.image(
            avg_mildew,
            caption='Infected Leaf - Average and Variability'
        )

        st.warning(
            "* The images—especially the variability images—clearly help "
            "distinguish between healthy and diseased leaves. The mildew "
            "creates white spots that form a visible pattern on the diseased "
            "leaves in the variability images.\n"
            "* The average images also highlight a color difference: "
            "infected leaves appear as a lighter shade of green compared to "
            "healthy ones."
        )

        st.write("---")

    if st.checkbox("Differences between average healthy and infected leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.warning(
            "* The study revealed subtle pattern differences that enabled us "
            "to distinguish between healthy and infected leaves."
        )
        st.image(
            diff_between_avgs,
            caption='Difference between average images'
        )
        st.write("---")

    if st.checkbox("Image Montage"):
        st.write(
            "* To refresh the montage, click on the 'Create Montage' button"
        )
        my_data_dir = 'inputs/cherry_leaves_dataset'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(
            label="Select label", options=labels, index=0
        )

        if st.button("Create Montage"):
            image_montage(
                dir_path=my_data_dir + '/validation',
                label_to_display=label_to_display,
                nrows=8,
                ncols=3,
                figsize=(10, 25)
            )
            st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    if label_to_display in labels:
        images_list = os.listdir(f"{dir_path}/{label_to_display}")
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage.\n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces."
            )
            return

        list_rows = range(nrows)
        list_cols = range(ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        fig, axes = plt.subplots(
            nrows=nrows,
            ncols=ncols,
            figsize=figsize
        )
        for x in range(nrows * ncols):
            img = imread(
                f"{dir_path}/{label_to_display}/{img_idx[x]}"
            )
            img_shape = img.shape
            ax = axes[plot_idx[x][0], plot_idx[x][1]]
            ax.imshow(img)
            ax.set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px"
            )
            ax.set_xticks([])
            ax.set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")
