# A decision-making game
print("Welcome to the Adventure Game!")
print("You find yourself at a fork in the road. Where will you go?")
print("1. Left - towards the dark forest.")
print("2. Right - towards the sunny beach.")
print("3. Straight - into the unknown cave.")

# Take the user's decision
choice = input("Enter 1, 2, or 3: ")

# Decision-making process
if choice == "1":
    print("You venture into the dark forest. It's spooky, but you find a treasure chest!")
    print("Congratulations, you've found gold!")
elif choice == "2":
    print("You head towards the sunny beach. It's warm and relaxing. A perfect day!")
    print("You decide to rest and enjoy the view.")
elif choice == "3":
    print("You boldly step into the unknown cave. A dragon appears!")
    print("Do you fight or run?")
    action = input("Enter 'fight' or 'run': ").lower()
    if action == "fight":
        print("You defeat the dragon and find a hidden treasure. You're a hero!")
    elif action == "run":
        print("You escape safely, but the mystery of the cave remains unsolved.")
    else:
        print("Indecision leads to trouble! The dragon chases you out.")
else:
    print("You stand still, unsure of what to do. Maybe next time you'll make a choice.")

print("Thanks for playing!")
