import tkinter
import random


def load_images(card_images):
    """Import cards to create a deck."""
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]

    # Next logic handle images' compatibility on different versions.
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # For each suit, retrieve the image for the card.
    for suit in suits:
        # First the number cards 1 to 10.
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            # Be sure you know where the image folder is stored.
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # Next the face cards.
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def _deal_card(frame):
    """Pop the next card from the top of the deck.

    Attention! trying to pop an item from an empty list rise an error.
    """
    next_card = deck.pop(0)
    # Add the next _card at the bottom of the deck to not run out of cards.
    deck.append(next_card)
    # Add the image to a label and display the label.
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    # Now return the card's face value.
    return next_card


def score_hand(hand):
    """Calculate the total score of all cards in the list.

    Only one ace can have the value 11, and this will be reduced
    to 1 if the hand bust.
    """
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value

        # If bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


# Create function to pass the deal_card() function to
# the command parameter in the dealer/player button.
def deal_dealer():
    global player_games
    global dealer_games
    global games_draw

    dealer_score = score_hand(dealer_hand)
    player_score = score_hand(player_hand)
    while 22 > player_score > dealer_score:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
        if dealer_score > 22:
            break
    if player_score > 21:
        result_text.set("Dealer wins!")
    elif dealer_score > 21:
        player_games += 1
        player_wins.set("Player {}".format(player_games))
        result_text.set("Player wins!")
    elif 22 > dealer_score > player_score:
        dealer_games += 1
        dealer_wins.set("Dealer {}".format(dealer_games))
        result_text.set("Dealer wins!")
    elif 22 > player_score > dealer_score:
        player_games += 1
        player_wins.set("Player {}".format(player_games))
        result_text.set("Player wins!")
    else:
        games_draw += 1
        draw.set("Draw {}".format(games_draw))
        result_text.set("Draw!")


def deal_player():
    global dealer_games
    player_score = score_hand(player_hand)
    dealer_score = score_hand(dealer_hand)
    if player_score < 21 and dealer_score < 12:
        player_hand.append(_deal_card(player_card_frame))
        player_score = score_hand(player_hand)
        player_score_label.set(player_score)
    if player_score > 21:
        dealer_games += 1
        dealer_wins.set("Dealer {}".format(dealer_games))
        result_text.set("Dealer wins!")


def initial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    # Embedded frame to hold the dealer's card images.
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, bg="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    # Embedded frame to hold the player's card images.
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, bg="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    result_text.set("")
    dealer_hand = []
    player_hand = []
    initial_deal()


def shuffle():
    random.shuffle(deck)


def play():
    initial_deal()
    mainWindow.mainloop()


def exit_game():
    mainWindow.destroy()


mainWindow = tkinter.Tk()

# Set up the screen and frame for the dealer and player.
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(bg="green")
mainWindow['padx'] = 8

# Create a frame for winner and scores.
score_frame = tkinter.Frame(mainWindow, relief="ridge", width=1, bg="green")
score_frame.grid(row=0, columnspan=3)

result_text = tkinter.StringVar()
result = tkinter.Label(score_frame, textvariable=result_text, bg="green",
                       fg="white")
result.grid(row=0, columnspan=3)

# Create label for dealer's points.
dealer_wins = tkinter.StringVar()
dealer_wins_label = tkinter.Label(score_frame, textvariable=dealer_wins,
                                  bg="green", fg="white")
dealer_wins_label.grid(row=1, column=0)

# Create label for player's points.
player_wins = tkinter.StringVar()
player_wins_label = tkinter.Label(score_frame, textvariable=player_wins,
                                  bg="green", fg="white")
player_wins_label.grid(row=1, column=1)

# Create label for tally display, games won and draw.
draw = tkinter.StringVar()
draw_label = tkinter.Label(score_frame, textvariable=draw, bg="green",
                           fg="white")
draw_label.grid(row=1, column=2)

# Create a frame for played cards and scores.
card_frame = tkinter.Frame(mainWindow, relief="sunken", width=1, bg="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

# Dealer's score.
dealer_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Dealer", bg="green", fg="white")\
    .grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, bg="green",
              fg="white").grid(row=1, column=0)

# Embedded frame to hold the dealer's card images.
dealer_card_frame = tkinter.Frame(card_frame, bg="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# Player's score
player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", bg="green", fg="white") \
    .grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, bg="green",
              fg="white").grid(row=3, column=0)

# Embedded frame to hold the player's card images.
player_card_frame = tkinter.Frame(card_frame, bg="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

# Frame to hold dealer - player - shuffle and new_game buttons.
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=4, column=0, columnspan=3, sticky="w")

# Create dealer - player - shuffle and new_game buttons.
dealer_button = tkinter.Button(button_frame, text="Dealer",
                               command=deal_dealer)
dealer_button.grid(row=0, column=0, sticky="w")

player_button = tkinter.Button(button_frame, text="Player",
                               command=deal_player)
player_button.grid(row=0, column=1, sticky="w")

new_game_button = tkinter.Button(button_frame, text="New Game",
                                 command=new_game)
new_game_button.grid(row=0, column=2, sticky="w")

shuffle_button = tkinter.Button(button_frame, text="Shuffle",
                                command=shuffle)
shuffle_button.grid(row=0, column=3, sticky="w")

# Last but not least, the exit button.
exit_button = tkinter.Button(button_frame, text="Exit game", command=exit_game)
exit_button.grid(row=0, column=4, sticky="w")

# Load cards.
cards = []
load_images(cards)

# Create a new deck of cards and shuffle them.
deck = list(cards)
shuffle()

# Create the list to store the dealer's and player's hands.
dealer_hand = []
player_hand = []

# Variables to store games won/draw.
player_games = 0
dealer_games = 0
games_draw = 0

# The next line will allow us to import the game without run it
# automatically.
if __name__ == "__main__":
    play()
