# implementation of card game - Memory

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random


# helper function to initialize globals
def new_game():
    global cardlist, exposed, game_state, counter
    cardlist = range(8)+range(8)
    random.shuffle(cardlist)
    exposed = [True]*16
    game_state = 0  
    counter = 0
    label.set_text("Turns = " + str(counter))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global cardlist, exposed, game_state, picked_card1, picked_card2, counter
    picked_card = pos[0]/100
    if exposed[picked_card]:

#open card logic
        if game_state == 0:
            game_state = 1
            picked_card1 = picked_card
        elif game_state == 1:
            game_state = 2
            picked_card2 = picked_card
            counter += 1
            if cardlist[picked_card1] == cardlist[picked_card2]:
                picked_card1 =  16
        else:
            game_state = 1
            if picked_card1<16:
                exposed[picked_card1] = True
                exposed[picked_card2] = True
            picked_card1 = picked_card
        exposed[picked_card] = False
        label.set_text("Turns = " + str(counter))
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    #canvas.draw_image(image, (50, 75), (100, 150), (50, 75), (100, 150))
    i = 0
    for card in cardlist:
        canvas.draw_image(image, ((50+100*card), 75), (100, 150), ((50+i), 75), (100, 150))
        canvas.draw_line((100+i,0),(100+i,150), 1,'white')
        i += 100
    i = 0
    for back in exposed:
        if back:
            canvas.draw_image(image_back, (354/2, 540/2), (354, 540), ((50+i), 75), (100, 150))
            
#if you don't like my design - uncomment next line
           #canvas.draw_line((50+i, 0), (50+i,150), 100, 'Green')
            canvas.draw_line((100+i,0),(100+i,150), 1,'black')
        i += 100
        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 1600, 150)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
image = simplegui.load_image('http://s24.postimg.org/gkpjo5745/image.jpg')
image_back = simplegui.load_image('http://www.ukrcards.com.ua/catalog/1330218527.jpg')
# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
