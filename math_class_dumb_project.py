# MATH CLASS DUMB
print("Hi students!")
greetings = input("Enter your greeting's reply: ")

# Fixed the mismatched quotes at the end of this line
print("So today we are going to learn BODMAS") 
your_remarks = input("Enter are you excited (yes/no): ")

print("We have six letters indicating six mathematical terms.")
BODMAS = ["Brackets" ,"Of" ,"Division" ,"Multiply" ,"Addition" ,"Subtraction"]
print("These are the main terms which tell how to solve any equation.")
print("We have to follow the exact pattern to get the correct answer.However,When we just have the last two terms like in an equation we have subtraction and addition terms so we apply basic rule that indicates we have start from left and then go right telling rather addition or subtraction which has the left side that operation must be done first.")

# Added a default value for left_side and fixed the space in the variable name
left_side = "Addition sign" 

# Indented the print statements below the if/elif
if left_side == "Addition sign":
    print("Addition opeartion must be done first then.")
elif left_side == "Subtraction sign":
    print("In such case,subtraction operation must be done first.")

# Fixed the indentation and the function logic here
def math_problem():
    result = 6 + 2 - 1
    return result

# Called the function using math_problem() inside the f-string
print(f"This {math_problem()} has 7 solution.")

print("That's it for today!")