import blackjack

# __name__ attribute is set to be the name of the module, so that
# is the file name without a path or extension
# print(__name__)  # his example run the code automatically, not mine

# from the command line
# python -m blackjack or python3 -m blackjack

# When we run print(__name__) inside the script, it will return __main__
# instead here, it will output...
# blackjack
# (without any extensions)

# if we insert print(__main__) inside blackjack and run it here again
# will first output..
# blackjack
# and then...
# __main__
# when the game is closed

# we can make some changes to blackjack with...
# if __name__ == "__main__":
# Now the game will not run automatically and the only output
# we have with print(__name__) is __main__
# but now we have the problem the we can not initialize our game

print(__name__)

# Python does not have private objects!
# That means that we can do silly thin gs once we imported the
# module
# next line will deal an extra card to the dealer once we run play()
# with the underscore python will warn us about it use...
# Access to a protected member _deal_card of a class
# blackjack._deal_card(blackjack.dealer_card_frame)
# but we can still use it and run it
blackjack.play()  # if commented out it will not run the program

print(blackjack.cards)
# our code will output in order...
# __main__
# then play the game, and when we close it, will output the list of
# cards
# This allow us to use the same pack of card for many different types of
# games
