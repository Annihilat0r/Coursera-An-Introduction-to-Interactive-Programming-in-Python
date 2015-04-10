# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = [36, 48]
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    
cent = simplegui.load_image('http://s1.sendimage.me/PnFaQnFR.png')
blackjack = simplegui.load_image('http://s1.sendimage.me/srhlAnGv.png')
bender = simplegui.load_image('http://s1.sendimage.me/EAbAHnGu.jpeg')
# initialize some useful global variables
in_play = False
money = 330
bet = 30
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos, rot):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE, rot)
        
# define hand class
class Hand:
    def __init__(self):
        self.cardsinhand = []

    def __str__(self):
        ans = ("Cards in hand: ")
        for i in range(len(self.cardsinhand)):
            ans += (self.cardsinhand[i]).suit + (self.cardsinhand[i]).rank + '; '
        return ans

    def add_card(self, card):
        self.cardsinhand.append(card)

    def get_value(self):
        val = 0
        sa = False #Is there A?
        for i in range(len(self.cardsinhand)):
            rank = VALUES[(self.cardsinhand[i]).rank]
            if rank == 1 and not sa : #if it is A, is before any A?
                val += 10
                sa = True #Now we have A and we newer come here
            val += rank
        if val > 21 and sa: #We have A and val > 21.
            val -= 10
        return val
            
   
    def draw(self, canvas, pos):
        for i in range(len(self.cardsinhand)):
            if in_play and i == 0 and self == comp:
                i = 1
            (self.cardsinhand[i]).draw(canvas, [pos[0] +10*i, pos[1]], 0.15*i)
        if self == player or not in_play:
            canvas.draw_text(str(self.get_value()), (pos[0], pos[1]+120), 22, 'White')
        
# define deck class 
class Deck:
    def __init__(self):
        self.deckcards = []
        for x in SUITS:
            for y in RANKS:
                self.deckcards.append(Card(x,y))

    def shuffle(self):
        random.shuffle(self.deckcards)

    def deal_card(self):
        return self.deckcards.pop()
    
    def __str__(self):
        ans = ("Cards in Desk: ")
        for i in range(len(self.deckcards)):
            ans += (self.deckcards[i]).suit + (self.deckcards[i]).rank + '; '
        return ans

#define event handlers for buttons
def deal():
    global outcome, in_play, player, comp, deck, debug, busted, game, money, bet, bank
    busted = False
    if money == 0:
        game = "GAME OVER"
        in_play = False
    else:
        game = "HIT or STAND?"
    if inp.get_text() == '':
                inp.set_text('0')    
    if int(inp.get_text())> money:
        bet = money
    else:
        bet = int(inp.get_text())
    deck = Deck()
    deck.shuffle()
    comp = Hand()
    comp.add_card(deck.deal_card())
    player = Hand()
    player.add_card(deck.deal_card())
    comp.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    player.draw
    money -= bet
    bank = bet*2
    in_play = True

def hit():
    global in_play, game
    if not game == "GAME OVER":
        if in_play:
            global busted
            player.add_card(deck.deal_card())
            if player.get_value() > 21 :
                busted = True
                in_play = False
                stand()
            
def stand():
    global in_play, busted, game, money, bet, bank
    if not game == "GAME OVER":
        if in_play:
            in_play = False
            if comp.get_value() <= 16 and not busted:
                while comp.get_value() <= 17:
                    comp.add_card(deck.deal_card())
            if player.get_value() <= comp.get_value() <= 21:
                game = 'DEALER WIN!'
            else:
                game = 'YOU WIN!'
                money += bank
        else:
            game = 'You have busted'
    
    
def bet_input(text):
    pass

def color():
    global CARD_BACK_CENTER
    if CARD_BACK_CENTER[0] < CARD_BACK_SIZE[0]:
        CARD_BACK_CENTER[0] += CARD_BACK_SIZE[0]
    else:
        CARD_BACK_CENTER[0] -= CARD_BACK_SIZE[0]
    
# draw handler    
def draw(canvas):
    global in_play, game, money, bank, bet
    canvas.draw_image(blackjack, (165,66), (330,132), (282,70), (330, 132)) 
    canvas.draw_image(bender, (75,100), (150,200), (523,70), (150, 200))   
    
    if (not game == "GAME OVER") and money <1000:
        
        if in_play:
            canvas.draw_text("BANK: "+str(bank), (200,350), 30, "Yellow")
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [200 + 36, 150 + CARD_BACK_CENTER[1]], CARD_SIZE)    
        else:
            if int(inp.get_text()) == 0:
                bet = 0
            if int(inp.get_text())> money:
                canvas.draw_text("You don't have "+str(inp.get_text())+'! Only '+ str(money), (200,350), 30, "Yellow")
                bet = money
            else:
                bet = int(inp.get_text())
                canvas.draw_text("New deal with bet: "+str(bet)+'?', (200,350), 30, "Yellow")
        
        player.draw(canvas,(200,400))
        comp.draw(canvas,(200,150))
        
        for i in range(len(deck.deckcards)):
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [30 + 36, 500 + CARD_BACK_CENTER[1] - 10*i], CARD_SIZE, 1.6 + 0.02*i )    
        
        canvas.draw_text(game, (200,300), 30, "White")
        canvas.draw_text('$'+ str(money), (515,590), 30, "Yellow")
        
        i = 0
        while i < money/10:
            i += 1
            canvas.draw_image(cent, (80,80), (160,160), [550, 550 - 4*i], (60, 60))  
        
    elif money >= 1000:
        i = 0
        x = 0
        while i < 238:
            i += 1
            if x > 160:
                x -= 155
            else:
                x += 2
            #print x
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50 + 3*x, 90 + CARD_BACK_CENTER[1] + 1.7*i], CARD_SIZE, 0.05*i)    
        canvas.draw_text("YOU WIN!", (60,300), 100, "Black")
        
    else:
          
        canvas.draw_text("GAME OVER", (220,300), 30, "White")
  
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
inp = frame.add_input("Bet:", bet_input, 50)
inp.set_text('30')
frame.set_draw_handler(draw)
frame.add_button("Change deck color", color, 200)
frame.add_label("", 200)
frame.add_label("Try to earn $1000 and you will see magic :)", 200)

# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
