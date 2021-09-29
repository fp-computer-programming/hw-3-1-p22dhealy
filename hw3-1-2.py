# author: DMH 9/28/21

card1 = input("What is the value of your first card")
card2 = input("what is the vlaue of your second card")

points = int(card1) + int(card2)

if points > 21:
    print("You have gone bust!")
else:
    print("You are safe!")
    