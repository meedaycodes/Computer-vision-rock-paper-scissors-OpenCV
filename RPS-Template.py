import cv2
from keras.models import load_model
import numpy as np
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
rps = ["rock", "paper", "scissors", "Nothing"]
end_time = time.time() + 6.0


def get_user():
    while end_time > time.time():
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.putText(frame, "Lets Play Rock-Paper-Scissors", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        max_arr = np.argmax(prediction[0][:3])
        #print(max_arr)
        user_choice = rps[max_arr]
        print(user_choice)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()      
    # After the loop release the cap objectclear
    # Destroy all the windows
    cv2.destroyAllWindows()
    return user_choice

x = get_user()
