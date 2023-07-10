#Connect the required modules
import pygame
from random import randint
pygame.init()
 
#create a game window
clock = pygame.time.Clock()
back = (50, 50, 50) #background color
mw = pygame.display.set_mode((500, 500)) #main window
mw.fill(back)
 
#colors
BLACK = (0, 0, 0)
LIGHT_BLUE = (200, 200, 255)
 
class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        """ area: a rectangle in the right place and the right color """
        #memorize the rectangle:
        self.rect = pygame.Rect(x, y, width, height)
        #fill color - either the passed parameter or the overall background color
        self.fill_color = color
    
    #place text
    def set_text(self, text, fsize=12, text_color=BLACK):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)
        
    #draw a rectangle with text
    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))   
 
#create cards
quest_card = TextArea(120, 100, 290, 70, LIGHT_BLUE)
quest_card.set_text("Question", 75)
 
ans_card = TextArea(120, 240, 290, 70, LIGHT_BLUE)
ans_card.set_text("Answer", 75)
 
 
quest_card.draw(10,10)
ans_card.draw(10,10)
print("Hi")
run = True
while run:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
    
            if event.key == pygame.K_q:
                num = randint(1,3)
                if num == 1:
                    quest_card.set_text('What do you study at Algorithmics?', 25)
                if num == 2:
                    quest_card.set_text('What language is spoken in France?', 25)
                if num == 3:
                    quest_card.set_text('What grows on an apple tree?', 35)      
    
                quest_card.draw(10,25)
    
            if event.key == pygame.K_a:
                num = randint(1,3)
                if num == 1:
                    ans_card.set_text('Python', 35)
                if num == 2:
                    ans_card.set_text('French', 35)
                if num == 3:
                    ans_card.set_text('Apples', 35)      
    
                ans_card.draw(10, 25)
    clock.tick(40)           
 
