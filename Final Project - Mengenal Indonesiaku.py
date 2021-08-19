import pygame, math, random

# Set up pygame
pygame.init()

# Set up for project screen
WIDTH, HEIGHT   = 800, 500
SCREEN          = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mengenal Indonesiaku")

# Set up color
WHITE           = (255,255,255)
GREY            = (30, 30, 30)


####################################### TITLE SCREEN  : SET UP PART #######################################

# Set up background images
bghome          = pygame.image.load("titlescreen/BgHome.png").convert_alpha()

# load button
B_Makanan       = pygame.image.load("titlescreen/Button0.png").convert_alpha()
B_Permainan     = pygame.image.load("titlescreen/Button1.png").convert_alpha()
B_Pahlawan      = pygame.image.load("titlescreen/Button2.png").convert_alpha()
B_Ibukota       = pygame.image.load("titlescreen/Button3.png").convert_alpha()
C_Makanan       = pygame.image.load("titlescreen/BClick0.png").convert_alpha()
C_Permainan     = pygame.image.load("titlescreen/BClick1.png").convert_alpha()
C_Pahlawan      = pygame.image.load("titlescreen/BClick2.png").convert_alpha()
C_Ibukota       = pygame.image.load("titlescreen/BClick3.png").convert_alpha()

# Set up background music
pygame.mixer.music.load("titlescreen/SimpleJoy.mp3")
pygame.mixer.music.set_volume(0.5)


####################################### GAME SCREEN   : SET UP PART #######################################

# Set up keyboard buttons
RADIUS      = 20
GAP         = 8
letters     = []
startx      = round((WIDTH - (RADIUS * 2 + GAP) *10) / 8)
starty      = 350
A           = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 10))
    y = starty + ((i // 10) * (GAP + RADIUS *2))
    letters.append([x,y, chr(A + i), True])

# Set up fonts
LETTER_FONT         = pygame.font.Font("gamescreen/BalooTammudu2-Medium.ttf", 27)
WORD_FONT           = pygame.font.Font("gamescreen/BalooTammudu2-Medium.ttf", 45)
TITLE_FONT          = pygame.font.Font("gamescreen/BalooTammudu2-Bold.ttf", 22)

# Set up Panjat Pinang (Hangman) images
images = [] 
for i in range(5):
    image = pygame.image.load("gamescreen/panjatpinang" + str(i) + ".png")
    images.append(image)

# Set up Panjat Pinang (Hangman) category lists
panjatpinang_status = 0
words_makanan       = ["CENIL", "GUDEG", "KERUPUK", "OPOR", "PEMPEK", "RENDANG", "SEBLAK", "SOTO", "TEMPE", "TEKWAN"]
word_makanan        = random.choice(words_makanan)
words_permainan     = ["BENTENG", "CONGKLAK", "DOMIKADO", "EGRANG", "ENGKLEK", "GASING", "GUNDU", "JAMURAN", "KARAMBOL", "LAYANGAN"]
word_permainan      = random.choice(words_permainan)
words_pahlawan      = ["ANTASARI", "DIPONEGORO", "FATMAWATI", "HATTA", "KARTINI", "MALAHAYATI", "SOEKARNO", "SUDIRMAN", "SUTOMO", "WAHIDIN"]
word_pahlawan       = random.choice(words_pahlawan)
words_ibukota       = ["AMBON", "BANDUNG", "DENPASAR", "GORONTALO", "JAKARTA", "KUPANG", "MEDAN", "PALU", "SEMARANG", "YOGYAKARTA"]
word_ibukota        = random.choice(words_ibukota)
guessed = []

# Set up win or lose backgrounds
bgwin               = pygame.image.load("endscreen/berhasil.png").convert()
bglose              = pygame.image.load("endscreen/kalah.png").convert()

# Set up win or lose sound effects
win_sound = pygame.mixer.Sound("endscreen/mixkit-video-game-win-2016.wav")
lose_sound = pygame.mixer.Sound("endscreen/mixkit-musical-game-over-959.wav")


####################################### GAME SCREEN   : RUN THE CODE #######################################

# Load background and category buttons
def draw_mainmenu():
    SCREEN.fill((WHITE))
    SCREEN.blit(bghome, (0,0))
    SCREEN.blit(B_Makanan, (95,332))
    SCREEN.blit(B_Permainan, (276,332))
    SCREEN.blit(B_Pahlawan, (95,400))
    SCREEN.blit(B_Ibukota, (276,400))
    mouse = pygame.mouse.get_pos()
    if 95+136 > mouse[0] > 95 and 332+40 > mouse[1] > 332:
        SCREEN.blit(C_Makanan, (95,332))
    if 276+136 > mouse[0] > 276 and 332+40 > mouse[1] > 332:
        SCREEN.blit(C_Permainan, (276,332))
    if 95+136 > mouse[0] > 95 and 400+40 > mouse[1] > 400:
        SCREEN.blit(C_Pahlawan, (95,400))
    if 276+136 > mouse[0] > 276 and 400+40 > mouse[1] > 400:
        SCREEN.blit(C_Ibukota, (276,400))      
    
    pygame.display.update()


################ Category A: MAKANAN ################
# Load word guess
def draw_game_a():
    SCREEN.fill((WHITE))
    SCREEN.blit(images[panjatpinang_status],(0,0))
    #draw word
    display_word = ""
    for letter in word_makanan:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, GREY)
    SCREEN.blit(text, (100, 220))
    
    # Load category title
    text = TITLE_FONT.render("Kategori:  Makanan", 1, GREY)
    SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 50))

    # Load keyboard button
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(SCREEN, (240,173,73), (x, y), RADIUS, 20)
            pygame.draw.circle(SCREEN, WHITE, (x, y), RADIUS, 2)
            text = LETTER_FONT.render(ltr, 1, GREY)
            SCREEN.blit(text, (x - text.get_width()/2, y - text.get_height()/2.5))


################ Category B: PERMAINAN ################
# Load word guess
def draw_game_b():
    SCREEN.fill((WHITE))
    SCREEN.blit(images[panjatpinang_status],(0,0))
    #draw word
    display_word = ""
    for letter in word_permainan:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, GREY)
    SCREEN.blit(text, (100, 220))
    
    # Load category title
    text = TITLE_FONT.render("Kategori:  Permainan", 1, GREY)
    SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 50))

    # Load keyboard button
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(SCREEN, (240,173,73), (x, y), RADIUS, 20)
            pygame.draw.circle(SCREEN, WHITE, (x, y), RADIUS, 2)
            text = LETTER_FONT.render(ltr, 1, GREY)
            SCREEN.blit(text, (x - text.get_width()/2, y - text.get_height()/2.5))


################ Category C: PAHLAWAN ################
# Load word guess
def draw_game_c():
    SCREEN.fill((WHITE))
    SCREEN.blit(images[panjatpinang_status],(0,0))
    #draw word
    display_word = ""
    for letter in word_pahlawan:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, GREY)
    SCREEN.blit(text, (100, 220))
    
    # Load category title
    text = TITLE_FONT.render("Kategori:  Pahlawan", 1, GREY)
    SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 50))

    # Load keyboard button
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(SCREEN, (240,173,73), (x, y), RADIUS, 20)
            pygame.draw.circle(SCREEN, WHITE, (x, y), RADIUS, 2)
            text = LETTER_FONT.render(ltr, 1, GREY)
            SCREEN.blit(text, (x - text.get_width()/2, y - text.get_height()/2.5))


################ Category D: IBU KOTA ################
# Load word guess
def draw_game_d():
    SCREEN.fill((WHITE))
    SCREEN.blit(images[panjatpinang_status],(0,0))
    #draw word
    display_word = ""
    for letter in word_ibukota:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, GREY)
    SCREEN.blit(text, (100, 220))
    
    # Load category title
    text = TITLE_FONT.render("Kategori:  Ibu Kota", 1, GREY)
    SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 50))

    # Load keyboard button
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(SCREEN, (240,173,73), (x, y), RADIUS, 20)
            pygame.draw.circle(SCREEN, WHITE, (x, y), RADIUS, 2)
            text = LETTER_FONT.render(ltr, 1, GREY)
            SCREEN.blit(text, (x - text.get_width()/2, y - text.get_height()/2.5))


################ Load The Game - Category A: MAKANAN ################
def game_a():
    global panjatpinang_status
    FPS = 60
    clock = pygame.time.Clock() 
    run = True
    while run:
        clock.tick(FPS)
        draw_game_a()
        pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word_makanan:
                                panjatpinang_status += 1

        won = True
        for letter in word_makanan:
            if letter not in guessed:
                won = False
        
        if won:
            SCREEN.blit(bgwin,(0,0))
            pygame.time.delay(3000)
            win_sound.play()
            pygame.display.update()

        if panjatpinang_status == 4:
            SCREEN.blit(bglose,(0,0))
            pygame.time.delay(3000)
            lose_sound.play()
            pygame.display.update()

        pygame.display.update()


################ Load The Game - Category B: PERMAINAN ################
def game_b():
    global panjatpinang_status
    FPS = 60
    clock = pygame.time.Clock() 
    run = True
    while run:
        clock.tick(FPS)
        draw_game_b()
        pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word_permainan:
                                panjatpinang_status += 1
        won = True
        for letter in word_permainan:
            if letter not in guessed:
                won = False
                
        if won:
            SCREEN.blit(bgwin,(0,0))
            pygame.time.delay(3000)
            win_sound.play()
            pygame.display.update()

        if panjatpinang_status == 4:
            SCREEN.blit(bglose,(0,0))
            pygame.time.delay(3000)
            lose_sound.play()
            pygame.display.update()

        pygame.display.update() 


################ Load The Game - Category C: PAHLAWAN ################
def game_c():
    global panjatpinang_status
    FPS = 60
    clock = pygame.time.Clock() 
    run = True
    while run:
        clock.tick(FPS)
        draw_game_c()
        pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word_pahlawan:
                                panjatpinang_status += 1
        won = True
        for letter in word_pahlawan:
            if letter not in guessed:
                won = False
                
        if won:
            SCREEN.blit(bgwin,(0,0))
            pygame.time.delay(3000)
            win_sound.play()
            pygame.display.update()

        if panjatpinang_status == 4:
            SCREEN.blit(bglose,(0,0))
            pygame.time.delay(3000)
            lose_sound.play()
            pygame.display.update()

        pygame.display.update() 


################ Load The Game - Category D: IBU KOTA ################
def game_d():
    global panjatpinang_status
    FPS = 60
    clock = pygame.time.Clock() 
    run = True
    while run:
        clock.tick(FPS)
        draw_game_d()
        pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word_ibukota:
                                panjatpinang_status += 1
        won = True
        for letter in word_ibukota:
            if letter not in guessed:
                won = False
                
        if won:
            SCREEN.blit(bgwin,(0,0))
            pygame.time.delay(3000)
            win_sound.play()
            pygame.display.update()

        if panjatpinang_status == 4:
            SCREEN.blit(bglose,(0,0))
            pygame.time.delay(3000)
            lose_sound.play()
            pygame.display.update()
            
        pygame.display.update() 


####################################### TITLE SCREEN  : RUN THE CODE #######################################

def main_menu():
    FPS = 60
    clock = pygame.time.Clock() 
    run = True
    pygame.mixer.music.play(-1)

    while run:
        clock.tick(FPS)
        draw_mainmenu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 95+136 > mx > 95 and 332+40 > my > 332:
                    game_a()
                    pygame.display.update()
                if 276+136 > mx > 276 and 332+40 > my > 332:
                    game_b()
                    pygame.display.update()
                if 95+136 > mx > 95 and 400+40 > my > 400:
                    game_c()
                    pygame.display.update()
                if 276+136 > mx > 276 and 400+40 > my > 400:
                    game_d()
                    pygame.display.update()

main_menu()
pygame.quit()
