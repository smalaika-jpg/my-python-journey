       # FLOWER SHOP VISIT
print("Hey Alexa!")
greetings = input("Enter your greeting's reply: ")

def asking_question():
    offer = input("Actually today i want to go to a flower shop, would you like to join me?: (yes/no) ").lower()
    time = 2
    return time
time = asking_question()

print(f"Maybe! It can take longer than {time} hours, like {time+2} hours.")
friends_answer = input("Enter it is ok or not (Yes/No): ")

if friends_answer == "Yes":
   print("Wow!I am too excited now!")
elif friends_answer == "No":
   print("That's completely ok!Would love to go with you next time")
else:
   print("Error!Invalid answer.")

print("Do you know which flower I'm planning to buy?")
flower_guess = input("Enter the name of flower you can guess according to your friend's mood: ")

flower_character = {
     "name": "tulip",
     "color": "white",
     "condition": "fully bloom"
}
print(f"I love {flower_character['color']} {flower_character['name']}s when they are in {flower_character['condition']}.")
opinion = input("Enter your opinion related your friend's flower choice")

print("I think it's time to go!")
