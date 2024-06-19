import random

comp = ["1", "2", "3"]  # List of choices as strings
u = 0
c = 0

print("\n0. exit \n1. Rock \n2. Paper \n3. Scissor")
userChoice = int(input("Enter your choice: "))

while userChoice:
    compChoice = int(random.choice(comp))  # Convert to integer
    print(f"Computer chose: {compChoice}")

    match userChoice:
        case 1:
            if compChoice == 1:
                print("Match tie :)")
                u += 1
                c += 1
            elif compChoice == 2:
                print("Computer wins!")
                c += 1
            elif compChoice == 3:
                print("User wins!")
                u += 1 
        case 2:
            if compChoice == 1:
                print("User wins!")
                u += 1
            elif compChoice == 2:
                print("Match tie :)")
                u += 1
                c += 1
            elif compChoice == 3:
                print("Computer wins!")
                c += 1
        case 3:
            if compChoice == 1:
                print("Computer wins!")
                c += 1
            elif compChoice == 2:
                print("User wins!")
                u += 1
            elif compChoice == 3:
                print("Match tie :)")
                u += 1
                c += 1
        case _:
            print("Invalid choice :(")
    
    print(f"User: {u} - Computer: {c}")  # Print scores

    print("\n0. exit \n1. Rock \n2. Paper \n3. Scissor")
    userChoice = int(input("Enter your choice: "))

print("Final scores - User: ", u, " Computer: ", c)
