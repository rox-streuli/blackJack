import blackjack

# why blackjack is highlighted red???? oops... you need to run
# it from the same directory i had the complete udemy projects open :/
#
# for x in globals():
#     print(x)

# outputs...
# RuntimeError: dictionary changed size during iteration

# one way to access the globals is to make a quick copy of
# the global dictionary then iterate over
# a quick way to copy is to use the sorted function, then
# the actual code has the added advantage od producing an sorted
# list.

# g = sorted(globals())  # unpacking the dictionary
# for x in g:
#     print(x)
# outputs...
# __annotations__
# __builtins__
# __cached__
# __doc__
# __file__
# __loader__
# __name__
# __package__
# __spec__
# blackjack

# blackjack is the only object
# but if we change the import to...
#
# from blackjack import *
# g = sorted(globals())  # unpacking the dictionary
# for x in g:
#     print(x)

# will output...
# __annotations__
# __builtins__
# __cached__
# __doc__
# __file__
# __loader__
# __name__
# __package__
# __spec__
# button_frame
# card_frame
# cards
# deal_dealer
# deal_player
# dealer_button
# dealer_card_frame
# dealer_games
# dealer_hand
# dealer_score_label
# dealer_wins
# dealer_wins_label
# deck
# draw
# draw_label
# games_draw
# initial_deal
# load_images
# mainWindow
# new_game
# new_game_button
# play
# player_button
# player_card_frame
# player_games
# player_hand
# player_score_label
# player_wins
# player_wins_label
# random
# result
# result_text
# score_frame
# score_hand
# shuffle
# shuffle_button
# tkinter

# BE CAREFUL
# This way we import every object from blackjack
# inside in our module namespace, so if we created an object called
# cards, for example, then the blackjack module card would no longer
# be available.

# OH NOT ALL THE OBJECTS ARE IMPORTED!
# the newly rename _deal_card() is not in the list!!! ;D
# and if we try to use it we would get an error!

# _deal_card(dealer_card_frame)
# will output if we run it...
# NameError: name '_deal_card' is not defined

# and python will highlight the snippet with...
# Unresolved reference '_deal_card'
# Python import mechanism does actually take note of the underscore
# convention and it would not import any objects that start with an
# underscore when you import *

# using double underscores at the start of a name invokes
# Python's name mangling rules, so this convention really exist
# to prevent name clashes when subclassing objects.

# The final name convention in python is names that the start and end
# with two underscores, they can be useful but you should
# never change them!!
#
# import blackjack
#
# blackjack._deal_card(blackjack.dealer_card_frame)
# blackjack.play()

# now we will brake things changing the value of __name__ in
# blackjack.py
# we add __name__ = "__main__" in our blackjack program
# and we try to run more_imports again, the game start but the
# dealer has only one card, the line :
# blackjack._deal_card(blackjack.dealer_card_frame)
# was not executed
# That is because we set __name__ to __main__ and the test that restrict
# code execution, we are running
# the program directly from blackjack

## it will raise an error...
#  blackjack._deal_card(blackjack.dealer_card_frame)
#_tkinter.TclError: can't invoke "label" command:
# application has been destroyed

# One more use for the underscore
# a variable named '_' or '__' with nothing else, indicates a throwaway
# value, so underscore by itself is a valid variable name. Instead
# of thinking of a named for something that is not going to be used the
# convention is to call it either _ or __ for things that you might have
# access but are not going to use include tuples, we want to use some
# of the values of a tuple but not all of them, you need to unpack
# the information and the correct number of variables need to be
# assigned

# example
personal_details = ("Tim", 24, "Australia")
name, _, country = personal_details
print(name, country)
print(_)

# outputs...
# Tim Australia
# 24
