import math
import matplotlib.pyplot as plt

MAX_DECKSIZE = 1000
decksize = []
shuffles = []



def split(deck):
    # print("splitting deck")
    length = len(deck)
    first_half = []
    second_half = []
    for i in range(0, math.floor(length/2)):
        first_half.append(deck[i])
    for i in range(math.ceil(length/2), length):
        second_half.append(deck[i])
    return first_half, second_half

def update_deck(deck):
    deck = first_half + second_half
    return reck

def shuffle(deck):
    # print("Now shuffling deck.")
    first_half, second_half = split(deck)
    number_cards = len(deck)
    half_length = int(number_cards / 2)
    # print("Number of cards: ", number_cards)
    deck = []
    for i in range(0, int(half_length)):
        deck.append(first_half[i])
        deck.append(second_half[i])
    # print("deck shuffled")
    return deck

def find_no_of_shuffles(deck_size):
    performed_shuffles = 0
    deck = []
    for i in range(1, deck_size + 1):
        deck.append(i)
    original_deck = deck
    # print(deck)
    while True:
        deck = shuffle(deck)
        #print(i+1, ". shuffle done. ", "new deck: ",deck)
        performed_shuffles += 1
        if (deck == original_deck): break
    print("performed shuffles to restore order of deck with ", deck_size, "cards :", performed_shuffles)
    return performed_shuffles

for i in range(2, MAX_DECKSIZE):
    if i%2 == 0:
        recent_shuffles = find_no_of_shuffles(i)
        decksize.append(i)
        shuffles.append(recent_shuffles)


fig, ax = plt.subplots(1,1)
ax.plot(decksize, shuffles, label="shuffles")
ax.set_title("number of shuffles to restore order per decksize")
ax.set_xlabel("decksize")
ax.set_ylabel("number of necessary shuffles")
plt.show()