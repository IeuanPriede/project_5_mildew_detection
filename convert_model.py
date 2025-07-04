from tensorflow.keras.models import load_model

# Load the old .h5 model
model = load_model("outputs/v1/powdery_mildew_detector_model.h5")

# Save it in the new .keras format
model.save("outputs/v1/powdery_mildew_model.keras", save_format="keras")
