'''
Milestone 2
Blackjack Game
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f"{self.rank} of {self.suit}"


class Deck():

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += "\n" + card.__str__()
		return "The deck has: "+deck_comp


	def shuffle(self):
		random.shuffle(self.deck)
	
	def deal(self):
		return self.deck.pop()		

class Hand():

	def __init__(self):
		self.card = []
		self.value = 0
		self.aces = 0

	def add_card(self, card):
		self.card.append(card)
		self.value += values[card.rank]

		if card.rank == "Ace":
			self.aces += 1

	def adjust_for_ace(self):
		
		while self.value > 21 and self.aces > 0:
			self.value -= 10
			self.aces -= 1

class Chips():
	
	def __init__(self, total = 100):
		self.total = total
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet


def take_bet(chips):

	while True:

		try: 
			chips.bet = int(input("How many chips would you like to bet? "))
		except:
			print("Sorry, please provide integer")

		else:
			if chips.bet > chips.total:
				print("Sorry, you don't have enough chips. You have {} left".format(chips.total))
			else:
				break

def hit(deck, hand):

	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_ace()

def hit_or_stand(deck, hand):
	global playing

	while True:
		x = input("Hit or stand? Enter h or s: ")
		if x[0].lower() == 'h':
			hit(deck,hand)
		elif x[0].lower() == 's':
			print("Player stands, Dealer's turn")
			playing = False
		else:
			print("Sorry, i didn't not understand that! Please enter h or s only")
			continue

		break

def show_some(player, dealer):
	print("DEALER HAND:")
	print("one card hidden")
	print(dealer.card[1])
	print("\n")
	print("PLAYER HAND: ")
	for card in player.card:
		print(card)
	print("\n")


def show_all(player, dealer):
	print("DEALER HAND:")
	for card in dealer.card:
		print(card)
	print("\n")
	print("PLAYER HAND: ")
	for card in player.card:
		print(card)


def player_bust(player,dealer, chips):
	print("PLAYER BUSTS")
	chips.lose_bet()


def player_win(player,dealer, chips):
	print("PLAYER WINS!")
	chips.win_bet()

def dealer_bust(player,dealer, chips):
	print("PLAYER WINS! DEALER BUSTED")
	chips.win_bet()

def dealer_win(player,dealer, chips):
	print("PLAYER BUSTS! DEALER WINS")
	chips.lose_bet()

def push(player,dealer, chips):
	print("Dealer and player tie! PUSH")


while True:

	print("WELCOME TO BLACKJACK")

	#create nd shuffle deck, deal two cards to players
	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())


	#set up player's chips
	players_chips = Chips()

	#prompt player for bet
	take_bet(players_chips)

	#show cards (but keep dealer card half hidden)
	show_some(player_hand, dealer_hand)

	while playing:
		#prompt player to hit or stand
		hit_or_stand(deck,player_hand)

		#show cards
		show_some(player_hand, dealer_hand)

		#if player hand exceeds 21, player busts and break out of loop
		if player_hand.value > 21:
			player_bust(player_hand, dealer_hand, players_chips)
			break

	#if player didn't bust, play dealers hand until Dealer reaches 17
	if player_hand.value <= 21:

		while dealer_hand.value < 17:
			hit(deck, dealer_hand)

		#show dealer cards
		show_all(player_hand,dealer_hand)

		#run different win scenarios
		if dealer_hand.value > 21:
			dealer_bust(player_hand, dealer_hand,players_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_win(player_hand, dealer_hand,players_chips)
		elif dealer_hand.value < player_hand.value:
			player_win(player_hand, dealer_hand,players_chips)
		else:
			push(player_hand, dealer_hand,players_chips)

	#inform player of their chips total
	print("\n Player total chips: {}".format(players_chips.total))

	#ask to play again
	new_game = input("Would like to play another hand? [Y/N] ")

	if new_game[0].lower() == "y":
		playing = True
		continue

	else:
		print("Thanks for playing")
		break
