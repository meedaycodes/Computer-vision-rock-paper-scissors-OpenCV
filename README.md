# Computer Vision RPS

## Training the model
- The model for the Rock-Paper-Scissors was trained on the website https://teachablemachine.withgoogle.com/
- An image project model with four classes (Rock, Paper, Scissors, Nothing)
- After Training the model, the model files Keras_model.h5 and labels.txt was downloaded and saved on my local machine

## Creating the conda Environment
- The second task was to create a conda environment and install the required python packages for this program
- The following code was used to create the environment and install the packages
```
conda create -n <envname>
conda install pip
pip install tensorflow opencv-python ipykernel

```
## Creating Manual RPS Python File
- This python file contains four functions that are required to play the Rock-Paper-Scissors (RPS) game
- The first function uses the random module to get a random string from the list provided as the computer's choice
```
def get_computer_choice():
    rps_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(rps_list)
    computer_choice = computer_choice.lower()
    return computer_choice
```
- The second function gets the user input 
```
def get_user_choice():
    user_choice = input("Enter your input here: ")
    user_choice = user_choice.lower()
    return user_choice
```
- The third function gets both input from user and computer as arguments and determines who wins based on the rules of the game
```
def get_winner(computer_choice, user_choice):
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
```
- The last method is called to play the game.  First it checks how many times both the computer and user have won, if it return an integer less than or equals to 3 the frame is kept on until one of the players wins 3 times
```
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
```
- Lastly an instance of the Rps is created and the decide_winner method is called to play the game