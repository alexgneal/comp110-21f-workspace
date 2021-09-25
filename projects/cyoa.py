"""Create your own adventure experience."""

__author__ = "730332729"

from random import randint
player: str = ""
points: int = 0
procedure: str = ""
endgame: str = ""
EMOJI = "\U0001F9F9"


def main() -> None:
    """Where the survey happens."""
    greet()
    answer: str = input("Yes or No? ")
    if answer == "Yes":
        print(f"Great! First, tell me where you want to go, {player}: ")
        procedure: str = input("Hogsmeade or Hogwarts? ")
        if procedure == "Hogsmeade":
            print(f"Great! Hop on your broomstick {EMOJI} and follow me to Hogsmeade, where you'll answer a few questions to see which House you belong in!")
            print(f"Whew...sorry about all that wind, {player}! Let's head into The Three Broomsticks and we'll get started! ")
            questions()
            score(points)
        else: 
            print(f"Straight to Hogwarts? Okay, {player}! We'll go to the Great Hall where the Sorting Hat can guess your results!")
            house()
    else:
        print(f"No?! You must be a Muggle...well, see ya later, {player}!")


def greet() -> None:
    """Greet the player and explain what is going on."""
    global player
    player = input("Hello! This is a quiz to find out which Hogwarts house you belong in! What is your name? ")
    print(f"Nice to meet you, {player}! Are you ready to begin? ")
    return None


def score(x: int) -> int:
    """Calculate the score and assign a house."""
    global points
    if points <= 5:
        print(f"{player}, you are in Ravenclaw! You are studious, smart, and probably spend most of your time studying. You'll always be the smartest in the room!")
    else:
        if points <= 10:
            print(f"{player}, you are in Hufflepuff! You have a kind heart and are willing to do anything for the people you love! ")
        else: 
            if points <= 15:
                print(f"{player}, you are in Gryffindor! You brave beyond measure and willing to sacrifice everything for your friends, family, and the greater good. ")
            else: 
                print(f"{player}, you are in Slytherin! There is really nothing good to say about this house and you are probably evil :) ")
    return points


def questions() -> None: 
    """Ask the questions."""
    global points
    while points < 5:
        print("Okay! Question 1: During your end-of-year exams, you notice that one of your classmates is cheating with an enchanted quill! What will you do? Here are your options: A. Nothing; you're already at the top of the class. B. Encourage the student to admit to cheating to the professor. C. Tell the professor immediately; cheating is wrong! D. Get an enchanted quill for yourself and thank them for the great idea. ")
        answer_1: str = input(f"So, {player}, what will your choice be? ")
        ans(answer_1)
        keep_going: str = input("Do you want to keep going? ")
        if keep_going == "Yes":
            print(f"Okay, next question {player}: You would be most hurt if someone called you: A. Dumb. B. Unkind. C. Coward. D. Weak. ")
            answer_2: str = input(f"So, {player}, what will your choice be? ")
            ans(answer_2)
            keep_going2: str = input("Do you want to keep going? ")
            if keep_going2 == "Yes":
                print("Okay, third question: You're dueling with another wizard; what is the first spell you cast? A. Protego. B. Expelliarmus. C. Stupefy. D. Crucio ")
                answer_3: str = input(f"So, {player}, what will your choice be? ")
                ans(answer_3)
                keep_going3: str = input("Do you want to keep going? ")
                if keep_going3 == "Yes":
                    print("Fourth question: Which skill of yours are you most proud of? A. How smart you are. B. How kind you are to others. C. How you are always up for a new adventure. D. How you can always get what you want. ")
                    answer_4: str = input(f"So, {player}, what will your choice be? ")
                    ans(answer_4)
                    keep_going4: str = input("Do you want to keep going? ")
                    if keep_going4 == "Yes":
                        print(f"Okay {player}, we're almost done! Just one more question. What would you see in the Mirror of Erised? A. Yourself, knowledge above all. B. Yourself, surrounded by family and friends. C. Yourself, experiencing an amazing adventure. D. Yourself, surrounded by all your riches. ")
                        answer_5: str = input(f"So, {player}, what will your choice be? ")
                        ans(answer_5)
                        endgame: str = input("Looks like you're all set to head up to the Great Hall in Hogwarts to see where the Sorting Hat wants to put you! Ready to go? ")
                        if endgame == "No": 
                            print("You want to answer the questions again? Okay!")
                            points = 0
    else:
        print("Looks like you're tired of playing...we'll just head over to the Great Hall then so the Sorting Hat can guess your results! ")
        house()


def ans(answer: str) -> None:
    """Answers and their point values."""
    global points
    if answer == "A":
        points = points + 1
    else: 
        if answer == "B": 
            points = points + 2
        else:
            if answer == "C":
                points = points + 3
            else:
                if answer == "D":
                    points = points + 4
    print(f"Interesting...that makes your point total {points}, {player}! ")


def house() -> None:
    """Randomly assing your house if you don't want to answer the questions."""
    house = randint(1, 4) 
    if house == 1:
        print(f"{player}, you are in Ravenclaw! You are studious, smart, and probably spend most of your time studying. You'll always be the smartest in the room!")
    else:
        if house == 2:
            print(f"{player}, you are in Hufflepuff! You have a kind heart and are willing to do anything for the people you love! ")
        else:
            if house == 3: 
                print(f"{player}, you are in Gryffindor! You brave beyond measure and willing to sacrifice everything for your friends, family, and the greater good. ")
            else: 
                if house == 4:
                    print(f"{player}, you are in Slytherin! There is really nothing good to say about this house and you are probably evil :) ")


if __name__ == "__main__":
    main()