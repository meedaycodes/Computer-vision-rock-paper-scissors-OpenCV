import random
from keras.models import load_model
import numpy as np
import cv2
import time


model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class Rps:
    def __init__(self):
        self.choices = ["Rock","Paper", "Scissors", "Nothing"]
        self.computerwins = 0
        self.userwins = 0
       

    def get_computer_choice(self):
        rps_list = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(rps_list)
        computer_choice = computer_choice.lower()
        return computer_choice

    def get_user_choice(self):
        end_time = time.time() + 0.5
        while end_time > time.time(): 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            
            # Press q to close the window
            max_arr = np.argmax(prediction[0][:3])
            user_choice = self.choices[max_arr].lower()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return user_choice

        cap.release()

        cv2.destroyAllWindows()
        
        

        # After the loop release the cap objectclear
        # Destroy all the windows
        
    def get_winner(self):

        computer_choice = self.get_computer_choice()
        user_choice = self.get_user_choice()
        
        if (computer_choice == "scissors" and user_choice == "rock") or (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors"):
            print(f'You picked {user_choice}, the computer picked {computer_choice}. Congratulations!! You won the game')
            self.userwins += 1
        elif (computer_choice == "scissors" and user_choice == "paper") or (computer_choice == "rock" and user_choice == "scissors") or (computer_choice == "paper" and user_choice == "rock"):
            print(f'You picked {user_choice}, the computer picked {computer_choice}. Sorry!! You lost the game')
            self.computerwins += 1
        else:
            print(f'You picked {user_choice}, the computer picked {computer_choice}. It is a tie!! Please try again')
        self.decide_winner()

    def decide_winner(self):
        if self.userwins <= 3 and self.computerwins <= 3:
            start_time = time.time()
            print(f"The computer have won {self.computerwins} times")
            print(f"The user have won {self.userwins} times")
            self.get_winner()
        elif self.userwins > 3:
            print("Congratulations!! You won this round Great job")
        else:
            print("Sorry!! The computer won this round. Try again next time")

game = Rps()
#game.get_winner()
game.decide_winner()



