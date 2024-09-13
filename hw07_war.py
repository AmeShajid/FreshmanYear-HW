"""
Ame Shajid
Date:March 5 2024
In this homework, we will take all the hard work out of a game of War. 
The players will type their decks into the program. It will then play the game for them and tell them who won.
"""
#Function we are allowed to use
def war(deck1, deck2):
    # Check if decks have the same number of cards
    if len(deck1) != len(deck2):
        return "Cannot play if decks have different numbers of cards."

    # This shows the decks of both players
    print(f"Player 1 Deck: {deck1}")
    print(f"Player 2 Deck: {deck2}")

    while deck1 and deck2:
        # Draw the top cards from each player's deck
        card1, deck1 = deck1[0], deck1[1:]
        card2, deck2 = deck2[0], deck2[1:]

        # this part displays the cards played in the first battle
        print(f"Battle: Player 1 played {card1}")
        print(f"Battle: Player 2 played {card2}")

        # Compare the cards and then it check to find the winner of the battle
        if card1 > card2:
            deck1 = deck1 + [card1, card2]
            print(f"Player 1 won this battle.")
            print(f"After Battle: Player 1 Deck contains {deck1}")
            print(f"Player 2 Deck contains {deck2}")
        elif card2 > card1:
            deck2 = deck2 + [card2, card1]
            print(f"Player 2 won this battle.")
            print(f"After Battle: Player 1 Deck contains {deck1}")
            print(f"Player 2 Deck contains {deck2}")
        else:
            # if players tie, it will start a war by drawing additional cards
            print("Players tie on this battle. War is declared.")
            war_deck1 = deck1[:1] + deck1[1:5]
            war_deck2 = deck2[:1] + deck2[1:5]

            # Check if there are not enough cards for a war
            if len(war_deck1) < 5:
                deck2 += war_deck2
                return 2, deck2
            elif len(war_deck2) < 5:
                deck1 += war_deck1
                return 1, deck1

            # right her it will recall the battle
            redo = war(war_deck1, war_deck2)
            
            # Update decks based on the previous war outcome
            if redo == 1:
                deck1 = deck1 + [card1, card2] + war_deck1 + war_deck2
                print(f"Player 1 won this war.")
                print(f"After Battle: Player 1 Deck contains {deck1}")
                print(f"Player 2 Deck contains {deck2}")
            else:
                deck2 = deck2 + [card2, card1] + war_deck2 + war_deck1
                print(f"Player 2 won this war.")
                print(f"After Battle: Player 1 Deck contains {deck1}")
                print(f"Player 2 Deck contains {deck2}")

            # Update war decks for the next round
            war_deck1 = deck1[:4] + war_deck1[4:]
            war_deck2 = deck2[:4] + war_deck2[4:]

    # Determine the winner and remaining cards
    if not deck1:
        return 2, deck2
    else:
        return 1, deck1

# this is what pops up first the main part
print("Prepare for War (The Card Game).")
deck1 = [int(card) for card in input("Enter your cards from top to bottom. Put spaces between values.\n").split()]
deck2 = [int(card) for card in input("Enter your cards from top to bottom. Put spaces between values.\n").split()]

# Play the game and display the result
result = war(deck1, deck2)
if isinstance(result, str):
    print(result)
else:
    winner, remaining_cards = result
    print(f"Player {winner} is victorious!")

#Soemthing is wrong with my code, this one I waited very last minute to do because I had exams and I dont know why i keep getting different outomces 

