import tensorflow as tf
import numpy as np
from PIL import Image

def load_model_keras(model_path):
    import tensorflow as tf
    model = tf.keras.models.load_model(model_path)
    print(model.summary())  # cek input layer
    return model

def extract_features(image):
    import numpy as np
    image = image.convert('L').resize((224, 224))
    arr = np.array(image) / 255.0
    mean_val = np.mean(arr)
    std_val = np.std(arr)
    min_val = np.min(arr)
    max_val = np.max(arr)
    features = np.array([mean_val, std_val, min_val, max_val])
    return features.reshape(1, -1)



def classify_image(model, image_pil):
    img = image_pil.resize((224, 224))
    img_array = np.array(img) / 255.0
    processed = np.expand_dims(img_array, axis=0)

    preds = model.predict(processed)
    class_idx = np.argmax(preds)
    confidence = np.max(preds)
    
    labels = [
        "No DR: Tidak ada lesi",
        "Mild: Hanya mikroaneurisma",
        "Moderate: Luas area eksudat > 500",
        "Severe: Perdarahan di 4 kuadran / pelebaran pembuluh",
        "PDR: Dengan neovaskularisasi atau kondisi lanjutan"
    ]

    return labels[class_idx], confidence


