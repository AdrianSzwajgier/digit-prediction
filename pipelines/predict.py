import numpy as np
from keras.src.saving import load_model

from UI.main import UI

ui = UI()
ui.main()
X_test = ui.get_feature_vector()

try:
    model = load_model('digit_recognition_model.h5')
    predictions = model.predict(X_test)
    predicted_labels = np.argmax(predictions, axis=1)
    print(predicted_labels)
except FileNotFoundError as e:
    raise FileNotFoundError("Model not found") from e
