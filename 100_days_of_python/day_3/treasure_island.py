
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".').lower()

if choice1 == "left":
    input('You\'ve come to a lake. There is an island in the middle of the lake. '
          'Type "wait" to wait for a boat. '
          'Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input('You\'ve come to a lake. '
                        'There is an island')