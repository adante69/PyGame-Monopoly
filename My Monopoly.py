import pygame, sys, random, math
from input_pole import InputField
from PIL import Image

class Program:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1000),pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = 228, 39, 39
        self.GREEN = (51, 255, 51)
        self.input_field = InputField(self.screen, self.font)
        self.player_count = 0
        self.player_names = []
        self.kocky = [1, 1]
        self.chance_text = 'chance'
        self.predaj_text = 'company'
        self.pole_is_active = ''
        self.whose_turn = 1
        self.polya_coord = {0: (730, 100)}
        self.monopolies = {1:['Bata', 'Notino'], 2:['Komenskeho', 'STU', 'Paneuropska', 'EUBA'],
                           3:['Studentska', 'Haiserky', 'Lentilky'], 4:['Slovakia', 'Opavia', 'Figaro'],
                           5:['Becherovka', 'TatraTea'],
                           6:['Kofola', 'Vinea', 'Zlaty Bazant'], 7:['Aupark', 'Avion', 'Eurovea'],
                           8:['VZP', 'Dovera', 'Union'],
                           9:['Slovenska Sporitelna', 'Tatra Banka', 'Vub Banka'],
                           10:['Slovnaft', 'Slovenske Elektrarne']}
        self.whose_monopoly = {1:0, 2:0,
                           3:0, 4:0,
                           5:0,
                           6:0, 7:0,
                           8:0,
                           9:0,
                           10:0}

        self.company = {1:'Bata', 3:'Notino', 5:'Komenskeho', 15:'STU', 25:'Paneuropska', 35:'EUBA',
                           6:'Studentska', 7:'Haiserky', 9:'Lentilky', 11:'Slovakia', 13:'Opavia', 14:'Figaro',
                           12:'Becherovka', 28:'TatraTea',
                           16:'Kofola', 18:'Vinea', 19:'Zlaty Bazant', 21:'Aupark', 23:'Avion', 24:'Eurovea',
                           26:'VZP', 27:'Dovera', 29:'Union',
                           31:'Slovenska Sporitelna', 32: 'Tatra Banka', 34: 'Vub Banka',
                         37: 'Slovnaft', 39: 'Slovenske Elektrarne'}
        self.company_const = {1: 'Bata', 3: 'Notino', 5: 'Komenskeho', 15: 'STU', 25: 'Paneuropska', 35: 'EUBA',
                        6: 'Studentska', 7: 'Haiserky', 9: 'Lentilky', 11: 'Slovakia', 13: 'Opavia', 14: 'Figaro',
                        12: 'Becherovka', 28: 'TatraTea',
                        16: 'Kofola', 18: 'Vinea', 19: 'Zlaty Bazant', 21: 'Aupark', 23: 'Avion', 24: 'Eurovea',
                        26: 'VZP', 27: 'Dovera', 29: 'Union',
                        31: 'Slovenska Sporitelna', 32: 'Tatra Banka', 34: 'Vub Banka',
                        37: 'Slovnaft', 39: 'Slovenske Elektrarne'}
        self.companies_buttons = {}
        self.companies_filials = {0: 0,
            1: 1, 2: 2, 3: 0, 4: 3, 5: 0, 6: 0, 7: 0,
            8: 0, 9: 0, 10: 0,11: 0, 12: 0, 13: 0, 14: 0,
            15: 0, 16: 0, 17: 0, 18: 0, 19: 3, 20: 0, 21: 0,
            22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0,
                                  31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0}
        self.kruh = 0
        self.win = 1
        self.polya_colors = { 0: self.BLACK,
            1: self.BLACK, 2: self.BLACK, 3: self.BLACK, 4: self.BLACK, 5: self.BLACK, 6: self.BLACK, 7: self.BLACK,
            8: self.BLACK,9: self.BLACK,10: self.BLACK,11: self.BLACK ,12: self.BLACK,13: self.BLACK,14: self.BLACK,
            15: self.BLACK,16: self.BLACK,17: self.BLACK,18: self.BLACK,19: self.BLACK,20: self.BLACK,21: self.BLACK,
            22: self.BLACK,23: self.BLACK,24: self.BLACK,25: self.BLACK ,26: self.BLACK,27: self.BLACK,28: self.BLACK,
            29: self.BLACK,30: self.BLACK,31: self.BLACK,32: self.BLACK,33: self.BLACK,34: self.BLACK,35: self.BLACK,
            36: self.BLACK,37: self.BLACK,38: self.BLACK,39: self.BLACK
        }
        self.ceny_polej = {1: 600, 3: 600, 5: 2000, 6: 1000, 7: 1000, 9: 1200, 11: 1400, 12: 1500, 13: 1400, 14: 1600,
                           15: 2000, 16: 1800, 18: 1800, 19: 2000, 21: 2200, 23: 2200, 24: 2400, 25: 2000, 26: 2600,
                           27: 2600, 28: 1500, 29: 2800, 31: 3000, 32: 3000, 34: 3200, 35: 2000, 37: 3500, 39: 4000}
        self.sell_ceny_polej = {1: 500, 3: 500, 5: 1500, 6: 800, 7: 800, 9: 1000, 11: 1200, 12: 1300, 13: 1200,
                           14: 1400,
                           15: 1800, 16: 1500, 18: 1500, 19: 1600, 21: 1800, 23: 1800, 24: 1900, 25: 1800, 26: 2200,
                           27: 2100, 28: 1200, 29: 2000, 31: 2400, 32: 2400, 34: 2500, 35: 1800, 37: 2900, 39: 3000}
        self.chance = ['participating in teleportation testing', 'accidentally dropped the dice. The search will take all the time',
                    'hits a yard sale and spends 1,000 there', 'arrested for money laundering and sent to jail',
                       'wins first place in a beauty contest and gets 1,500 for it', 'wins 2,000 in the lottery']
        self.vyber_fak_k = 0
        self.vyber_fak_s = 5
        self.vyber_fak_e = 8
        self.is_aktiv_k = {0: self.RED, 1: self.BLACK, 2: self.BLACK, 3: self.BLACK, 4: self.BLACK}
        self.is_aktiv_s = {5: self.RED, 6: self.BLACK, 7: self.BLACK}
        self.is_aktiv_e = {8: self.RED, 9: self.BLACK}

        self.main_menu()

    def draw_text(self, text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_obj, text_rect)

    def main_menu(self):
        while True:
            self.screen.fill(self.WHITE)
            image = pygame.image.load('obrazky/logo.png')
            image = pygame.transform.scale(image, (1300, 900))
            self.screen.blit(image, (320, 10))

            image = pygame.image.load('obrazky/sesterenka.png')
            image = pygame.transform.scale(image, (90, 90))

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(820, 800, 300, 70)
            button_2 = pygame.Rect(820, 930, 300, 70)
            button_3 = pygame.Rect(1800, 950, 100, 100)
            button_4 = pygame.Rect(50,970,300,70)



            pygame.draw.rect(self.screen, self.RED, button_1, border_radius=15)
            pygame.draw.rect(self.screen, self.RED, button_2, border_radius=15)
            pygame.draw.rect(self.screen, self.RED, button_3, border_radius=15)
            pygame.draw.rect(self.screen, self.RED, button_4, border_radius=15)
            self.screen.blit(image, (1805, 955))

            self.draw_text('Play', self.font, self.WHITE, self.screen, 935, 820)
            self.draw_text('Exit', self.font, self.WHITE, self.screen, 910, 950)
            self.draw_text('Rules', self.font, self.BLACK, self.screen, 130, 990)

            click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            if button_1.collidepoint((mx, my)):
                if click:
                    self.get_players()
            if button_2.collidepoint((mx, my)):
                if click:
                    pygame.quit()
                    sys.exit()
            if button_3.collidepoint((mx, my)):
                if click:
                    self.nastavenia()
            if button_4.collidepoint((mx,my)):
                if click:
                    self.pravidla()


            pygame.display.update()
            self.clock.tick(60)

    def pravidla(self):
        with open('rules.txt') as f:
            lines = f.readlines()
        while True:
            while True:
                self.screen.fill(self.WHITE)
                back_button = pygame.Rect(50, 960, 140, 70)

                mx, my = pygame.mouse.get_pos()

                pygame.draw.rect(self.screen, self.RED, back_button, border_radius=15)
                self.draw_text('Back', self.font, self.BLACK, self.screen, 80, 980)
                self.draw_text('Rules', pygame.font.Font(None, 100), self.BLACK, self.screen,
                               840, 45)

                for i in range(len(lines)):
                    self.draw_text(lines[i][0:-1], pygame.font.Font(None, 24), self.BLACK, self.screen,
                                   700, 200 + (i * 15))

                click = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True

                if back_button.collidepoint((mx, my)):
                    if click:
                        return

                pygame.display.update()
                self.clock.tick(60)

    def get_players(self):
        click = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                player_count = self.input_field.handle_event(event)
                self.player_count = player_count
                if player_count is not None and (player_count > 1 and player_count < 7):
                    self.get_player_names()

            self.input_field.update()

            self.screen.fill(self.WHITE)
            self.draw_text('Number of players', pygame.font.Font(None, 60), self.BLACK, self.screen,
                           800, 520)
            self.draw_text('(min 2, max 6)', pygame.font.Font(None, 60), self.BLACK, self.screen,
                           820, 690)

            back_button = pygame.Rect(50, 960, 140, 70)

            mx, my = pygame.mouse.get_pos()

            if back_button.collidepoint((mx, my)):
                if click:
                    return

            pygame.draw.rect(self.screen, self.RED, back_button, border_radius=15)
            self.draw_text('Back', self.font, self.WHITE, self.screen, 80, 980)

            self.input_field.draw()
            pygame.display.update()
            self.clock.tick(60)

            click = False

    def get_player_names(self):
        text = ''
        click = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if text:
                            self.player_names.append(text)
                            text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

            self.screen.fill(self.WHITE)

            self.draw_text('Enter Player Names', self.font, self.BLACK, self.screen, 780, 400)

            pygame.draw.rect(self.screen, self.RED, (850, 470, 200, 50), 2)
            self.draw_text(text, self.font, self.RED, self.screen, 855, 480)

            pygame.draw.rect(self.screen, self.RED, (825, 550, 250, 50), border_radius=15)
            self.draw_text('Start Game', self.font, self.WHITE, self.screen, 860, 560)

            mx, my = pygame.mouse.get_pos()
            start_game_button = pygame.Rect(825, 550, 250, 50)

            if start_game_button.collidepoint((mx, my)):
                pygame.draw.rect(self.screen, (127, 3, 3), start_game_button, border_radius=15)
                self.draw_text('Start Game', self.font, self.WHITE, self.screen, 860, 560)
                if click:
                    if text and len(self.player_names) == self.player_count - 1:
                        self.player_names.append(text)
                        self.game()
                    elif text == "" and len(self.player_names) == self.player_count:
                        self.game()

            back_button = pygame.Rect(50, 960, 140, 70)

            mx, my = pygame.mouse.get_pos()

            if back_button.collidepoint((mx, my)):
                if click:
                    return

            pygame.draw.rect(self.screen, self.RED, back_button, border_radius=15)
            self.draw_text('Back', self.font, self.WHITE, self.screen, 80, 980)
            click = False
            pygame.display.update()
            self.clock.tick(60)

    def find_key_by_value(self,dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                return key
        return None
    def winning(self,winner_name):
        while True:
            self.screen.fill(self.WHITE)
            gif_path = 'obrazky/win-game.gif'
            text = f'{winner_name} víťaz'
            gif = Image.open(gif_path)
            frames = []
            try:
                while True:
                    frame = gif.convert('RGBA')
                    frame = pygame.image.fromstring(frame.tobytes(), frame.size, 'RGBA')
                    frames.append(frame)
                    gif.seek(gif.tell() + 1)
            except EOFError:
                pass

            frame_index = 0
            play_animation = True
            while True:
                self.screen.fill(self.WHITE)

                ok_button = pygame.Rect(900, 800, 110, 50)

                mx, my = pygame.mouse.get_pos()

                pygame.draw.rect(self.screen, self.RED, ok_button, border_radius=15)
                self.draw_text('OK', self.font, self.WHITE, self.screen, 932, 810)
                click = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True

                if ok_button.collidepoint((mx, my)):
                    if click:
                        self.main_menu()

                if play_animation:
                    self.screen.blit(frames[frame_index], (650, 200))
                    x_name = 940 - (5 * len(text))
                    self.draw_text(text, self.font, self.BLACK, self.screen, x_name, 720)
                    frame_index = (frame_index + 1) % len(frames)

                pygame.display.flip()

                self.clock.tick(30)


    def game(self):
        players = Players()
        star_size = (15,15)
        y = 5
        for i in range(self.player_count):
            players._player_name[i + 1] = self.player_names[i]
            x = random.randint(0, y)
            y -= 1
            players._player_color[i + 1] = players.players_colors_available[x]
            players.players_colors_available.pop(x)
            if self.player_count < 4:
               players._player_wallet[i + 1] = 10000
            elif self.player_count > 3:
                players._player_wallet[i + 1] = 7000
            elif self.player_count == 6:
                players._player_wallet[i + 1] = 5000
            players.player_pole[i + 1] = 0
            players.current_pole[i + 1] = 0
            players.time_in_jail[i + 1] = 0
            players.players_active[i+1] = 1
            players._player_companies[i + 1] = []
            if i == 0:
                players.player_pos[i + 1] = [715, 100]
                players.target_x[i + 1] = 715
                players.target_y[i + 1] = 100
            elif i == 1:
                players.player_pos[i + 1] = [745, 100]
                players.target_x[i + 1] = 745
                players.target_y[i + 1] = 100
            elif i == 2:
                players.player_pos[i + 1] = [715, 130]
                players.target_x[i + 1] = 715
                players.target_y[i + 1] = 130
            elif i == 3:
                players.player_pos[i + 1] = [745, 130]
                players.target_x[i + 1] = 745
                players.target_y[i + 1] = 130
            elif i == 4:
                players.player_pos[i + 1] = [715, 70]
                players.target_x[i + 1] = 715
                players.target_y[i + 1] = 70
            elif i == 5:
                players.player_pos[i + 1] = [745, 70]
                players.target_x[i + 1] = 745
                players.target_y[i + 1] = 70

        while True:
            self.screen.fill(self.WHITE)

            back_button = pygame.Rect(50, 960, 140, 70)

            mx, my = pygame.mouse.get_pos()



            pygame.draw.rect(self.screen, self.RED, back_button, border_radius=15)
            self.draw_text('Back', self.font, self.WHITE, self.screen, 80, 980)

            gap = 4
            start_x = 680
            big_rect = 100
            small_rect = 80
            start_y = 50 + gap + big_rect
            for i in range(11):
                if i == 10:
                    pygame.draw.rect(self.screen, self.polya_colors.get(i), pygame.Rect(start_x, 50, big_rect,
                                                                                        big_rect))
                    image = pygame.image.load('obrazky/head/10.png')
                    image = pygame.transform.scale(image, (big_rect, big_rect))
                    self.screen.blit(image, (start_x, 50))
                    self.polya_coord[i] = (start_x + 50, 100)
                elif i == 0:
                    pygame.draw.rect(self.screen, self.polya_colors.get(i), pygame.Rect(start_x, 50, big_rect,
                                                                                        big_rect))
                    image = pygame.image.load('obrazky/head/0.png')
                    image = pygame.transform.scale(image, (big_rect, big_rect))
                    self.screen.blit(image, (start_x, 50))
                    start_x += big_rect + gap
                else:
                    pygame.draw.rect(self.screen, self.polya_colors.get(i), pygame.Rect(start_x, 50, small_rect,
                                                                                        big_rect))
                    if i != 2 or i != 4 or i != 8:
                              self.companies_buttons[i] = pygame.Rect(start_x, 50, small_rect, big_rect)
                    if i < 4 and i != 2:
                        pygame.draw.rect(self.screen, (242, 21, 190), pygame.Rect(start_x, 25, small_rect, 25))
                        x_cena = start_x + 35 - (3 * len(str(self.ceny_polej.get(i))))
                        self.draw_text(str(self.ceny_polej.get(i)),pygame.font.Font(None, 25),self.WHITE,
                                       self.screen, x_cena,30)
                    elif i == 5:
                        pygame.draw.rect(self.screen, self.RED, pygame.Rect(start_x, 25, small_rect, 25))
                        x_cena = start_x + 35 - (3 * len(str(self.ceny_polej.get(i))))
                        self.draw_text(str(self.ceny_polej.get(i)), pygame.font.Font(None, 25), self.WHITE,
                                       self.screen, x_cena, 30)
                    elif i > 5 and i != 8:
                        pygame.draw.rect(self.screen, (228, 206, 13), pygame.Rect(start_x, 25, small_rect, 25))
                        x_cena = start_x + 35 - (3 * len(str(self.ceny_polej.get(i))))
                        self.draw_text(str(self.ceny_polej.get(i)), pygame.font.Font(None, 25), self.WHITE,
                                       self.screen, x_cena, 30)
                    if i != 5:
                       image = pygame.image.load(f'obrazky/head/{i}.png')
                    else:
                        image = pygame.image.load(f'obrazky/vyber fak/{self.vyber_fak_k}.png')
                    image = pygame.transform.scale(image, (small_rect - (2 * gap), big_rect - (2 * gap)))
                    self.screen.blit(image, (start_x + 4, 54))
                    if self.companies_filials.get(i) != 0:
                       kolvo = self.companies_filials.get(i) - 1
                       for i in range(self.companies_filials.get(i)):
                           image = pygame.image.load('obrazky/star.png')
                           image = pygame.transform.scale(image, star_size)
                           star_x = start_x + 34 - (7.5 * kolvo) + (i*8)
                           kolvo -= 1
                           star_y = 137
                           self.screen.blit(image, (star_x,star_y))
                    self.polya_coord[i] = (start_x + 40, 100)
                    start_x += small_rect + gap
            for i in range(10):
                if i == 9:
                    pygame.draw.rect(self.screen, self.polya_colors.get(i + 11), pygame.Rect(start_x, start_y,
                                                                                             big_rect, big_rect))
                    image = pygame.image.load('obrazky/right/9.png')
                    image = pygame.transform.scale(image, (big_rect, big_rect))
                    self.screen.blit(image, (start_x, start_y))
                    self.polya_coord[i + 11] = (start_x + 50, start_y + 50)
                else:
                    pygame.draw.rect(self.screen, self.polya_colors.get(i + 11), pygame.Rect(start_x, start_y, big_rect,
                                                                                        small_rect))
                    if i + 11 != 17:
                         self.companies_buttons[i+11] = pygame.Rect(start_x, start_y, big_rect,small_rect)
                    if i >= 0 and i != 1 and i < 4:
                        pygame.draw.rect(self.screen, (11, 229, 135),
                                         pygame.Rect(start_x + big_rect, start_y, 25, small_rect))
                        font = pygame.font.Font(None, 25)
                        text_content = str(self.ceny_polej.get(i + 11))
                        text_surface = font.render(text_content, True, self.WHITE)
                        rotated_text_surface = pygame.transform.rotate(text_surface, 270)
                        rotated_text_rect = rotated_text_surface.get_rect(topleft=(start_x + big_rect, start_y + 15))
                        self.screen.blit(rotated_text_surface,rotated_text_rect)
                    elif i == 1:
                        pygame.draw.rect(self.screen, (116, 11, 53),
                                         pygame.Rect(start_x + big_rect, start_y, 25, small_rect))
                        font = pygame.font.Font(None, 25)
                        text_content = str(self.ceny_polej.get(i + 11))
                        text_surface = font.render(text_content, True, self.WHITE)
                        rotated_text_surface = pygame.transform.rotate(text_surface, 270)
                        rotated_text_rect = rotated_text_surface.get_rect(topleft=(start_x + big_rect, start_y + 15))
                        self.screen.blit(rotated_text_surface, rotated_text_rect)
                    elif i == 4:
                        pygame.draw.rect(self.screen, self.RED,
                                         pygame.Rect(start_x + big_rect, start_y, 25, small_rect))
                        font = pygame.font.Font(None, 25)
                        text_content = str(self.ceny_polej.get(i + 11))
                        text_surface = font.render(text_content, True, self.WHITE)
                        rotated_text_surface = pygame.transform.rotate(text_surface, 270)
                        rotated_text_rect = rotated_text_surface.get_rect(topleft=(start_x + big_rect, start_y + 15))
                        self.screen.blit(rotated_text_surface, rotated_text_rect)
                    elif i > 4 and i != 6:
                        pygame.draw.rect(self.screen, (0, 99, 247),
                                         pygame.Rect(start_x + big_rect, start_y, 25, small_rect))
                        font = pygame.font.Font(None, 25)
                        text_content = str(self.ceny_polej.get(i + 11))
                        text_surface = font.render(text_content, True, self.WHITE)
                        rotated_text_surface = pygame.transform.rotate(text_surface, 270)
                        rotated_text_rect = rotated_text_surface.get_rect(topleft=(start_x + big_rect, start_y + 15))
                        self.screen.blit(rotated_text_surface, rotated_text_rect)
                    if i != 4:
                       image = pygame.image.load(f'obrazky/right/{i}.png')
                    else:
                       image = pygame.image.load(f'obrazky/vyber fak/{self.vyber_fak_s}.png')
                    image = pygame.transform.scale(image, (big_rect - (2 * gap), small_rect - (2 * gap)))
                    self.screen.blit(image, (start_x + 4, start_y + 4))
                    if self.companies_filials.get(i+11) != 0:
                       kolvo = self.companies_filials.get(i+11) - 1
                       for i in range(self.companies_filials.get(i+11)):
                           image = pygame.image.load('obrazky/star.png')
                           image = pygame.transform.scale(image, star_size)
                           kolvo -= 1
                           star_y = start_y + 25 - (7.5 * kolvo) + (i*8)
                           self.screen.blit(image, (start_x,star_y))
                    self.polya_coord[i + 11] = (start_x + 50, start_y + 40)
                    start_y += small_rect + gap
            start_x -= gap + small_rect
            for i in range(10):
                if i == 9:
                    start_x -= 20
                    pygame.draw.rect(self.screen, self.BLACK, pygame.Rect(start_x, start_y, big_rect, big_rect))
                    image = pygame.image.load('obrazky/bottom/9.png')
                    image = pygame.transform.scale(image, (big_rect, big_rect))
                    self.screen.blit(image, (start_x, start_y))
                    self.polya_coord[i + 21] = (start_x + 50, start_y + 50)
                else:
                    pygame.draw.rect(self.screen, self.polya_colors.get(i + 21), pygame.Rect(start_x, start_y,
                                                                                             small_rect, big_rect))
                    if i + 21 != 22:
                        self.companies_buttons[i+21] = pygame.Rect(start_x, start_y,small_rect, big_rect)
                    if i >= 0 and i != 1 and i < 4:
                        pygame.draw.rect(self.screen, (0, 247, 33), pygame.Rect(start_x, start_y - 25,
                                                                                small_rect, 25))
                        x_cena = start_x + 35 - (3 * len(str(self.ceny_polej.get(i))))
                        self.draw_text(str(self.ceny_polej.get(i + 21)), pygame.font.Font(None, 25),
                                       self.WHITE, self.screen, x_cena, start_y - 20)
                    elif i == 4:
                        pygame.draw.rect(self.screen, self.RED, pygame.Rect(start_x, start_y - 25, small_rect, 25))
                        x_cena = start_x + 35 - (3 * len(str(self.ceny_polej.get(i))))
                        self.draw_text(str(self.ceny_polej.get(i + 21)), pygame.font.Font(None, 25),
                                       self.WHITE, self.screen, x_cena, start_y - 20)
                    elif i >= 5 and i != 7:
                        pygame.draw.rect(self.screen, (0, 153, 153), pygame.Rect(start_x, start_y - 25,
                                                                                 small_rect, 25))
                        x_cena = start_x + 35 - (3 * len(str(self.ceny_polej.get(i))))
                        self.draw_text(str(self.ceny_polej.get(i + 21)), pygame.font.Font(None, 25),
                                       self.WHITE, self.screen, x_cena, start_y - 20)
                    elif i == 7:
                        pygame.draw.rect(self.screen, (116, 11, 53),
                                         pygame.Rect(start_x, start_y - 25, small_rect, 25))
                        x_cena = start_x + 35 - (3 * len(str(self.ceny_polej.get(i))))
                        self.draw_text(str(self.ceny_polej.get(i + 21)), pygame.font.Font(None, 25),
                                       self.WHITE, self.screen, x_cena, start_y - 20)

                    image = pygame.image.load(f'obrazky/bottom/{i}.png')
                    image = pygame.transform.scale(image, (small_rect - (2 * gap), big_rect - (2 * gap)))
                    self.screen.blit(image, (start_x + 4, start_y + 4))
                    if self.companies_filials.get(i+21) != 0:
                       kolvo = self.companies_filials.get(i+21) - 1
                       for i in range(self.companies_filials.get(i+21)):
                           image = pygame.image.load('obrazky/star.png')
                           image = pygame.transform.scale(image, star_size)
                           star_x = start_x + 34 - (7.5 * kolvo) + (i*8)
                           kolvo -= 1
                           star_y = start_y + 90
                           self.screen.blit(image, (star_x,star_y))
                    self.polya_coord[i + 21] = (start_x + 40, start_y + 50)
                    start_x -= (small_rect + gap)
            start_y -= gap + small_rect
            for i in range(9):
                pygame.draw.rect(self.screen, self.polya_colors.get(i + 31), pygame.Rect(start_x, start_y, big_rect,
                                                                                         small_rect))
                if i + 31 != 33 or i + 31 != 36 or i + 31 != 38:
                    self.companies_buttons[i+31] = pygame.Rect(start_x, start_y, big_rect, small_rect)
                if i >= 0 and i != 2 and i < 4:
                    pygame.draw.rect(self.screen, (127, 0, 255), pygame.Rect(start_x - 25, start_y, 25,
                                                                             small_rect))
                    font = pygame.font.Font(None, 25)
                    text_content = str(self.ceny_polej.get(i + 31))
                    text_surface = font.render(text_content, True, self.WHITE)
                    rotated_text_surface = pygame.transform.rotate(text_surface, 90)
                    rotated_text_rect = rotated_text_surface.get_rect(topleft=(start_x - 18, start_y + 19))
                    self.screen.blit(rotated_text_surface, rotated_text_rect)
                elif i == 4:
                    pygame.draw.rect(self.screen, self.RED, pygame.Rect(start_x - 25, start_y, 25, small_rect))
                    font = pygame.font.Font(None, 25)
                    text_content = str(self.ceny_polej.get(i + 31))
                    text_surface = font.render(text_content, True, self.WHITE)
                    rotated_text_surface = pygame.transform.rotate(text_surface, 90)
                    rotated_text_rect = rotated_text_surface.get_rect(topleft=(start_x - 18, start_y + 19))
                    self.screen.blit(rotated_text_surface, rotated_text_rect)
                elif i == 6 or i == 8:
                    pygame.draw.rect(self.screen, (128, 128, 128), pygame.Rect(start_x - 25, start_y, 25,
                                                                               small_rect))
                    font = pygame.font.Font(None, 25)
                    text_content = str(self.ceny_polej.get(i + 31))
                    text_surface = font.render(text_content, True, self.WHITE)
                    rotated_text_surface = pygame.transform.rotate(text_surface, 90)
                    rotated_text_rect = rotated_text_surface.get_rect(topleft=(start_x - 18, start_y + 19))
                    self.screen.blit(rotated_text_surface, rotated_text_rect)
                if i != 4:
                    image = pygame.image.load(f'obrazky/left/{i}.png')
                else:
                    image = pygame.image.load(f'obrazky/vyber fak/{self.vyber_fak_e}.png')
                image = pygame.transform.scale(image, (big_rect - (2 * gap), small_rect - (2 * gap)))
                self.screen.blit(image, (start_x + 4, start_y + 4))
                if self.companies_filials.get(i + 31) != 0:
                    kolvo = self.companies_filials.get(i + 31) - 1
                    for i in range(self.companies_filials.get(i + 31)):
                        image = pygame.image.load('obrazky/star.png')
                        image = pygame.transform.scale(image, star_size)
                        kolvo -= 1
                        star_y = start_y + 25 - (7.5 * kolvo) + (i * 8)
                        self.screen.blit(image, (start_x+85, star_y))
                self.polya_coord[i + 31] = (start_x + 50, start_y + 40)
                start_y -= small_rect + gap

            for i in range(self.player_count):
              if players.players_active[i+1] != 0:
                pygame.draw.rect(self.screen, (240, 238, 238), pygame.Rect(330, 50 + (i * 160), 250, 150))
                self.draw_text(self.player_names[i], pygame.font.Font(None, 44), self.BLACK, self.screen,
                               340, 110 + (i * 160))
                self.draw_text(str(players._player_wallet.get(i + 1)), pygame.font.Font(None, 42),
                               self.BLACK, self.screen, 340, 155 + (i * 160))
                pygame.draw.circle(self.screen, players._player_color.get(i + 1)[1], (560, 130 + (i * 160)),
                                   10 + 5)
                pygame.draw.circle(self.screen, players._player_color.get(i + 1)[0], (560, 130 + (i * 160)),
                                   10)
                pygame.draw.circle(self.screen, players._player_color.get(i + 1)[1], players.player_pos.get(i + 1),
                                   10 + 5)
                pygame.draw.circle(self.screen, players._player_color.get(i + 1)[0], players.player_pos.get(i + 1),
                                   10)

            for i in range(2):
                pygame.draw.rect(self.screen, self.BLACK, pygame.Rect(1050 + (i * 150), 450, 100, 100))
                image = pygame.image.load(f'obrazky/kocky/{self.kocky[i]}.png')
                image = pygame.transform.scale(image, (100, 100))
                self.screen.blit(image, (1049 + (i * 150), 449))

            pygame.draw.rect(self.screen, (240, 238, 238), pygame.Rect(800, 160, 720, 200), border_radius=15)
            chod_button = pygame.Rect(830, 280, 630, 60)
            pygame.draw.rect(self.screen, self.GREEN, chod_button, border_radius=15)
            self.draw_text('roll the dice', self.font, self.WHITE, self.screen, 1040, 295)
            x = 1175 - (13 * len(players._player_name.get(self.whose_turn)))
            chance_x = 1170 - (6 * len(self.chance_text))
            self.draw_text(f'{players._player_name.get(self.whose_turn)}', self.font, self.BLACK, self.screen, x,
                           200)
            self.draw_text(f'{self.chance_text}', pygame.font.Font(None, 35), self.BLACK, self.screen,
                           chance_x, 580)

            pygame.draw.rect(self.screen, (240, 238, 238), pygame.Rect(800, 620, 720,
                                                                       250), border_radius=15)
            pygame.draw.rect(self.screen, self.RED, pygame.Rect(1160, 800, 310,
                                                                       50), border_radius=15)
            predat_button = pygame.Rect(1160, 800, 310, 50)
            pygame.draw.rect(self.screen, self.GREEN, pygame.Rect(840, 800, 310,
                                                                       50), border_radius=15)
            pobocka_button = pygame.Rect(840, 800, 310, 50)
            self.draw_text('branch office', pygame.font.Font(None, 39), self.WHITE,
                           self.screen, 850, 810)
            self.draw_text('sell ', pygame.font.Font(None, 39), self.WHITE,
                           self.screen, 1260, 810)
            predaj_x = 1130 - (3 * len(self.predaj_text))
            self.draw_text(self.predaj_text, pygame.font.Font(None, 39), self.BLACK,
                           self.screen, predaj_x, 670)

            for i in range(self.player_count):
                current_x, current_y = players.player_pos.get(i + 1)
                target_x, target_y = players.target_x.get(i + 1), players.target_y.get(i + 1)

                if (players.current_pole.get(i + 1) >= 0 and players.current_pole.get(i + 1) < 11) or (
                        players.current_pole.get(i + 1) >= 20 and players.current_pole.get(i + 1) < 31):
                    if current_x != target_x:
                        dx = target_x - current_x
                        distancex = math.sqrt(dx ** 2)
                        speed = 15
                        if distancex > speed:
                            players.player_pos[i + 1][0] = current_x + int(speed * dx / distancex)
                        else:
                            players.player_pos[i + 1][0] = target_x
                    elif current_y != target_y:
                        dy = target_y - current_y
                        distancey = math.sqrt(dy ** 2)
                        speed = 15
                        if distancey > speed:
                            players.player_pos[i + 1][1] = current_y + int(speed * dy / distancey)
                        else:
                            players.player_pos[i + 1][1] = target_y
                else:
                    if current_y != target_y:
                        dy = target_y - current_y
                        distancey = math.sqrt(dy ** 2)
                        speed = 15
                        if distancey > speed:
                            players.player_pos[i + 1][1] = current_y + int(speed * dy / distancey)
                        else:
                            players.player_pos[i + 1][1] = target_y
                    elif current_x != target_x:
                        dx = target_x - current_x
                        distancex = math.sqrt(dx ** 2)
                        speed = 15
                        if distancex > speed:
                            players.player_pos[i + 1][0] = current_x + int(speed * dx / distancex)
                        else:
                            players.player_pos[i + 1][0] = target_x

            click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            if back_button.collidepoint((mx, my)):
                if click:
                    self.main_menu()
            if chod_button.collidepoint((mx, my)):
                pygame.draw.rect(self.screen, (0, 255, 0), chod_button, border_radius=15)
                self.draw_text('roll the dice', self.font, self.WHITE, self.screen, 1040, 295)
                if click:
                 if players.players_active[self.whose_turn] != 0:
                   if players.time_in_jail[self.whose_turn] > 0:
                            players.time_in_jail[self.whose_turn] = players.time_in_jail.get(self.whose_turn) - 1
                   else:
                        for i in range(2):
                            self.kocky[i] = random.randint(1, 6)
                        sucet_koc = (self.kocky[0] + self.kocky[1])
                        players.current_pole[self.whose_turn] = players.player_pole.get(self.whose_turn)
                        pred_kruh = self.kruh
                        self.kruh += (players.player_pole.get(self.whose_turn) + sucet_koc) // 40
                        players.player_pole[self.whose_turn] = (players.player_pole.get(self.whose_turn) +
                                                                sucet_koc) % 40
                        if self.kruh > pred_kruh and self.kruh < (13 * self.player_count):
                           players._player_wallet[self.whose_turn] = players._player_wallet.get(self.whose_turn) + 2000
                        pole = players.player_pole.get(self.whose_turn)
                        players.target_x[self.whose_turn] = self.polya_coord.get(pole)[0]
                        players.target_y[self.whose_turn] = self.polya_coord.get(pole)[1]
                        if pole == 0:
                           players._player_wallet[self.whose_turn] = players._player_wallet.get(self.whose_turn) + 1000
                        elif pole == 36:
                            players._player_wallet[self.whose_turn] = players._player_wallet.get(self.whose_turn) - 1000
                        elif pole == 4:
                            players._player_wallet[self.whose_turn] = players._player_wallet.get(self.whose_turn) - 2000
                        elif pole == 2 or pole == 8 or pole == 17 or pole == 22 or pole == 33 or pole == 38:
                               self.chance_text = self.chance[random.randint(0,5)]
                               if self.chance_text == 'participating in teleportation testing':
                                  players.player_pole[self.whose_turn] = random.randint(0,39)
                                  players.current_pole[self.whose_turn] = random.randint(0,39)
                                  players.target_x[self.whose_turn] = self.polya_coord.get(random.randint(0,
                                                                                                          39))[0]
                                  players.target_y[self.whose_turn] = self.polya_coord.get(random.randint(0,
                                                                                                          39))[1]
                               elif self.chance_text == 'The dice accidentally fell. The search takes 1 move':
                                  players.time_in_jail[self.whose_turn] = 1
                               elif self.chance_text == 'hits a sale and spends 1 000':
                                  players._player_wallet[self.whose_turn] = players._player_wallet.get(
                                       self.whose_turn) - 1000
                               elif self.chance_text == 'arrested for money laundering and sent to prison':
                                   players.player_pole[self.whose_turn] = 10
                                   players.current_pole[self.whose_turn] = 10
                                   players.target_x[self.whose_turn] = self.polya_coord.get(10)[0]
                                   players.target_y[self.whose_turn] = self.polya_coord.get(10)[1]
                                   players.time_in_jail[self.whose_turn] = 3
                               elif self.chance_text == 'won 1st place in the beauty contest and received 1 500':
                                   players._player_wallet[self.whose_turn] = players._player_wallet.get(
                                       self.whose_turn) + 1500
                               elif self.chance_text == 'won 2 000 in the lottery.':
                                   players._player_wallet[self.whose_turn] = players._player_wallet.get(
                                      self.whose_turn) + 2000
                        elif pole == 20:
                            self.win = random.randint(0, 1)
                            print(self.win)
                            if self.win == 1:
                                players._player_wallet[self.whose_turn] = players._player_wallet.get(
                                    self.whose_turn) + 3000
                            else:
                                players._player_wallet[self.whose_turn] = players._player_wallet.get(
                                    self.whose_turn) - 1000

                            self.casino()
                        elif pole == 30:
                            self.chance_text = 'the player is sent to jail.'
                            players.player_pole[self.whose_turn] = 10
                            players.current_pole[self.whose_turn] = 10
                            players.target_x[self.whose_turn] = self.polya_coord.get(10)[0]
                            players.target_y[self.whose_turn] = self.polya_coord.get(10)[1]
                            players.time_in_jail[self.whose_turn] = 3
                        else:
                            if players._player_color.get(self.whose_turn)[0] != self.polya_colors.get(pole):
                               if self.ceny_polej.get(pole):
                                   if pole != 12 and pole != 28:
                                        players._player_wallet[self.whose_turn] = players._player_wallet.get(
                                               self.whose_turn) - self.ceny_polej.get(pole)
                                        for i in range(self.player_count):
                                            if i + 1 != self.whose_turn:
                                               if self.company_const.get(pole) in players._player_companies[i+1]:
                                                   players._player_wallet[i+1] = (players._player_wallet.get(i+1) +
                                                                                  self.ceny_polej.get(pole))
                                   else:
                                       if self.whose_monopoly[5] == 0:
                                           players._player_wallet[self.whose_turn] = players._player_wallet.get(
                                           self.whose_turn) - (sucet_koc * 150)
                                           for i in range(self.player_count):
                                               if i + 1 != self.whose_turn:
                                                   if self.company_const.get(pole) in players._player_companies[i + 1]:
                                                       players._player_wallet[i + 1] = (
                                                                   players._player_wallet.get(i + 1) +
                                                                   (sucet_koc * 150))
                                       else:
                                           players._player_wallet[self.whose_turn] = players._player_wallet.get(
                                            self.whose_turn) - (sucet_koc * 250)
                                           for i in range(self.player_count):
                                               if i + 1 != self.whose_turn:
                                                   if self.company_const.get(pole) in players._player_companies[i + 1]:
                                                       players._player_wallet[i + 1] = (
                                                                   players._player_wallet.get(i + 1) +
                                                                   (sucet_koc * 250))
                            if pole in self.company:
                                collection = players._player_companies.get(self.whose_turn)
                                collection.append(self.company.pop(pole))
                                players._player_companies[self.whose_turn] = collection
                                if pole == 1 or pole == 3:
                                    if set(self.monopolies.get(1)).issubset(
                                        set(collection)):
                                        self.whose_monopoly[1] = self.whose_turn
                                if pole == 5 or pole == 15 or pole == 25 or pole == 35:
                                    if set(self.monopolies.get(2)).issubset(
                                        set(collection)):
                                        self.whose_monopoly[2] = self.whose_turn
                                if pole == 6 or pole == 7 or pole == 9:
                                    if set(self.monopolies.get(3)).issubset(
                                        set(collection)):
                                        self.whose_monopoly[3] = self.whose_turn
                                if pole == 11 or pole == 13 or pole == 14:
                                    if set(self.monopolies.get(4)).issubset(
                                        set(collection)):
                                        self.whose_monopoly[4] = self.whose_turn
                                if pole == 12 or pole == 28:
                                    if set(self.monopolies.get(5)).issubset(
                                        set(collection)):
                                        self.whose_monopoly[5] = self.whose_turn
                                if pole == 16 or pole == 18 or pole == 19:
                                    if set(self.monopolies.get(6)).issubset(
                                        set(collection)):
                                        self.whose_monopoly[6] = self.whose_turn
                                if pole == 21 or pole == 23 or pole == 24:
                                    if set(self.monopolies.get(7)).issubset(
                                        set(collection)):
                                        self.whose_monopoly[7] = self.whose_turn
                                if pole == 26 or pole == 27 or pole == 29:
                                    if set(self.monopolies.get(8)).issubset(
                                        set(collection)):
                                        self.whose_monopoly[8] = self.whose_turn
                                if pole == 31 or pole == 32 or pole == 34:
                                    if set(self.monopolies.get(9)).issubset(
                                        set(collection)):
                                        self.whose_monopoly[9] = self.whose_turn
                                if pole == 27 or pole == 39:
                                    if set(self.monopolies.get(10)).issubset(set(collection)):
                                        self.whose_monopoly[10] = self.whose_turn
                                self.polya_colors[pole] = players._player_color[self.whose_turn][0]
                                if pole != 12 and pole != 28:
                                   self.ceny_polej[pole] = self.ceny_polej.get(pole) // 10
                                else:
                                    if self.whose_monopoly[5] == 0:
                                       self.ceny_polej[pole] = '150x'
                                    else:
                                        self.ceny_polej[pole] = '250x'

                   if self.whose_turn != self.player_count:
                            self.whose_turn += 1
                   else:
                            self.whose_turn = 1

                   if players._player_wallet[self.whose_turn] < 0:
                       players.players_active[self.whose_turn] = 0

                   count_active_players = 0
                   for i in range(self.player_count):
                       if players.players_active[i+1] != 0:
                           count_active_players += 1
                   if count_active_players == 1:
                       winner_name = self.find_key_by_value(players.players_active,1)
                       with open('Result.txt', 'a') as f:
                           f.write('Game\n')
                           for i in range(self.player_count):
                             f.write(f'{players._player_name[i+1]}:'
                                     f' {players._player_wallet[i+1]}$\n')
                             f.write(f'{players._player_companies[i+1]}')
                             f.write('\n')
                       self.winning(winner_name)
                 else:
                     if self.whose_turn != self.player_count:
                         self.whose_turn += 1
                     else:
                         self.whose_turn = 1


            if self.companies_buttons.get(1).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[1]:
                        self.predaj_text = 'Baťa'
                        self.pole_is_active = 'Bata'

            if self.companies_buttons.get(3).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[3]:
                        self.predaj_text = 'Notino'
                        self.pole_is_active = 'Notino'
            if self.companies_buttons.get(5).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[5]:
                        if self.vyber_fak_k != 1:
                            self.predaj_text = 'Univerzita Komenskeho'
                        else:
                            self.predaj_text = 'Matfyz'
                        self.pole_is_active = 'Komenskeho'
            if self.companies_buttons.get(6).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[6]:
                        self.predaj_text = 'Studentska'
                        self.pole_is_active = 'Studentska'
            if self.companies_buttons.get(7).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[7]:
                        self.predaj_text = 'Haiserky'
                        self.pole_is_active = 'Haiserky'
            if self.companies_buttons.get(9).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[9]:
                        self.predaj_text = 'Lentilky'
                        self.pole_is_active = 'Lentilky'
            if self.companies_buttons.get(11).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[11]:
                        self.predaj_text = 'Slovakia'
                        self.pole_is_active = 'Slovakia'
            if self.companies_buttons.get(12).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[12]:
                        self.predaj_text = 'Becherovka'
                        self.pole_is_active = 'Becherovka'
            if self.companies_buttons.get(13).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[13]:
                        self.predaj_text = 'Opavia'
                        self.pole_is_active = 'Opavia'
            if self.companies_buttons.get(14).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[14]:
                        self.predaj_text = 'Figaro'
                        self.pole_is_active = 'Figaro'
            if self.companies_buttons.get(15).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[15]:
                        self.predaj_text = 'STU'
                        self.pole_is_active = 'STU'
            if self.companies_buttons.get(16).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[16]:
                        self.predaj_text = 'Kofola'
                        self.pole_is_active = 'Kofola'
            if self.companies_buttons.get(18).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[18]:
                        self.predaj_text = 'Vinea'
                        self.pole_is_active = 'Vinea'
            if self.companies_buttons.get(19).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[19]:
                        self.predaj_text = 'Zlaty Bazant'
                        self.pole_is_active = 'Zlaty Bazant'
            if self.companies_buttons.get(21).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[21]:
                        self.predaj_text = 'Aupark'
                        self.pole_is_active = 'Aupark'
            if self.companies_buttons.get(23).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[23]:
                        self.predaj_text = 'Avion'
                        self.pole_is_active = 'Avion'
            if self.companies_buttons.get(24).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[24]:
                        self.predaj_text = 'Eurovea'
                        self.pole_is_active = 'Eurovea'
            if self.companies_buttons.get(25).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[25]:
                        self.predaj_text = 'Paneuropska vysoka skola'
                        self.pole_is_active = 'Paneuropska'
            if self.companies_buttons.get(26).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[26]:
                        self.predaj_text = 'VZP'
                        self.pole_is_active = 'VZP'
            if self.companies_buttons.get(27).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[27]:
                        self.predaj_text = 'Dovera'
                        self.pole_is_active = 'Dovera'
            if self.companies_buttons.get(28).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[28]:
                        self.predaj_text = 'TATRATEA'
                        self.pole_is_active = 'TatraTea'
            if self.companies_buttons.get(29).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[29]:
                        self.predaj_text = 'Union'
                        self.pole_is_active = 'Union'
            if self.companies_buttons.get(31).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[31]:
                        self.predaj_text = 'Slovenska Sporitelna'
                        self.pole_is_active = 'Slovenska Sporitelna'
            if self.companies_buttons.get(32).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[32]:
                        self.predaj_text = 'Tatra Banka'
                        self.pole_is_active = 'Tatra Banka'
            if self.companies_buttons.get(34).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[34]:
                        self.predaj_text = 'VUB Banka'
                        self.pole_is_active = 'Vub Banka'
            if self.companies_buttons.get(35).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[35]:
                        self.predaj_text = 'EUBA'
                        self.pole_is_active = 'EUBA'
            if self.companies_buttons.get(37).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[37]:
                        self.predaj_text = 'Slovnaft'
                        self.pole_is_active = 'Slovnaf'
            if self.companies_buttons.get(29).collidepoint((mx, my)):
                if click:
                    if players._player_color[self.whose_turn][0] == self.polya_colors[39]:
                        self.predaj_text = 'Slovenske Elektrarne'
                        self.pole_is_active = 'Slovenske Elektrarne'
            if predat_button.collidepoint((mx,my)):
                if click:
                    if self.pole_is_active != '':
                           pole = self.find_key_by_value(self.company_const,self.pole_is_active)
                           if pole  not in self.company:
                               if self.pole_is_active in players._player_companies.get(self.whose_turn):
                                      players._player_companies[self.whose_turn].remove(self.pole_is_active)
                                      self.company[pole] = self.company_const[pole]
                                      self.polya_colors[pole] = self.BLACK
                                      if pole != 12 and pole != 28:
                                               self.ceny_polej[pole] = self.ceny_polej.get(pole) * 10
                                      else:
                                               self.ceny_polej[pole] = 1500
                                      players._player_wallet[self.whose_turn] =\
                                          players._player_wallet.get(self.whose_turn) + self.sell_ceny_polej[pole]

            if pobocka_button.collidepoint((mx,my)):
                if click:
                    if self.pole_is_active != '':
                        pole = self.find_key_by_value(self.company_const, self.pole_is_active)
                        if pole != 12 and pole != 28:
                            if self.pole_is_active in players._player_companies.get(self.whose_turn):

                                    if self.whose_monopoly[1] == self.whose_turn:
                                        self.companies_filials[pole] = self.companies_filials.get(pole) + 1
                                        players._player_wallet[self.whose_turn] = \
                                        players._player_wallet.get(self.whose_turn) - (self.sell_ceny_polej[pole] //
                                                                               2)
                                        self.ceny_polej[pole] = (self.ceny_polej.get(pole) +
                                                                 (self.sell_ceny_polej.get(pole)//2 - 100))

                                    if self.whose_monopoly[2] == self.whose_turn:
                                        self.companies_filials[pole] = self.companies_filials.get(pole) + 1
                                        players._player_wallet[self.whose_turn] = \
                                            players._player_wallet.get(self.whose_turn) - (self.sell_ceny_polej[pole] //
                                                                                           2)
                                        self.ceny_polej[pole] = (self.ceny_polej.get(pole) +
                                                                 (self.sell_ceny_polej.get(pole) // 2 - 100))

                                    if self.whose_monopoly[3] == self.whose_turn:
                                        self.companies_filials[pole] = self.companies_filials.get(pole) + 1
                                        players._player_wallet[self.whose_turn] = \
                                            players._player_wallet.get(self.whose_turn) - (self.sell_ceny_polej[pole] //
                                                                                           2)
                                        self.ceny_polej[pole] = (self.ceny_polej.get(pole) +
                                                                 (self.sell_ceny_polej.get(pole) // 2 - 100))

                                    if self.whose_monopoly[4] == self.whose_turn:
                                        self.companies_filials[pole] = self.companies_filials.get(pole) + 1
                                        players._player_wallet[self.whose_turn] = \
                                            players._player_wallet.get(self.whose_turn) - (self.sell_ceny_polej[pole] //
                                                                                           2)
                                        self.ceny_polej[pole] = (self.ceny_polej.get(pole) +
                                                                 (self.sell_ceny_polej.get(pole) // 2 - 100))

                                    if self.whose_monopoly[5] == self.whose_turn:
                                        self.companies_filials[pole] = self.companies_filials.get(pole) + 1
                                        players._player_wallet[self.whose_turn] = \
                                            players._player_wallet.get(self.whose_turn) - (self.sell_ceny_polej[pole] //
                                                                                           2)
                                        self.ceny_polej[pole] = (self.ceny_polej.get(pole) +
                                                                 (self.sell_ceny_polej.get(pole) // 2 - 100))

                                    if self.whose_monopoly[6] == self.whose_turn:
                                        self.companies_filials[pole] = self.companies_filials.get(pole) + 1
                                        players._player_wallet[self.whose_turn] = \
                                            players._player_wallet.get(self.whose_turn) - (self.sell_ceny_polej[pole] //
                                                                                           2)
                                        self.ceny_polej[pole] = (self.ceny_polej.get(pole) +
                                                                 (self.sell_ceny_polej.get(pole) // 2 - 100))

                                    if self.whose_monopoly[7] == self.whose_turn:
                                        self.companies_filials[pole] = self.companies_filials.get(pole) + 1
                                        players._player_wallet[self.whose_turn] = \
                                            players._player_wallet.get(self.whose_turn) - (self.sell_ceny_polej[pole] //
                                                                                           2)
                                        self.ceny_polej[pole] = (self.ceny_polej.get(pole) +
                                                                 (self.sell_ceny_polej.get(pole) // 2 - 100))

                                    if self.whose_monopoly[8] == self.whose_turn:
                                        self.companies_filials[pole] = self.companies_filials.get(pole) + 1
                                        players._player_wallet[self.whose_turn] = \
                                            players._player_wallet.get(self.whose_turn) - (self.sell_ceny_polej[pole] //
                                                                                           2)
                                        self.ceny_polej[pole] = (self.ceny_polej.get(pole) +
                                                                 (self.sell_ceny_polej.get(pole) // 2 - 100))

                                    if self.whose_monopoly[9] == self.whose_turn:
                                        self.companies_filials[pole] = self.companies_filials.get(pole) + 1
                                        players._player_wallet[self.whose_turn] = \
                                            players._player_wallet.get(self.whose_turn) - (self.sell_ceny_polej[pole] //
                                                                                           2)
                                        self.ceny_polej[pole] = (self.ceny_polej.get(pole) +
                                                                 (self.sell_ceny_polej.get(pole) // 2 - 100))

                                    if self.whose_monopoly[10] == self.whose_turn:
                                        self.companies_filials[pole] = self.companies_filials.get(pole) + 1
                                        players._player_wallet[self.whose_turn] = \
                                            players._player_wallet.get(self.whose_turn) - (self.sell_ceny_polej[pole] //
                                                                                           2)
                                        self.ceny_polej[pole] = (self.ceny_polej.get(pole) +
                                                                 (self.sell_ceny_polej.get(pole) // 2 - 100))

            pygame.display.update()
            self.clock.tick(60)

    def casino(self):
        self.screen.fill(self.WHITE)
        gif_path = 'obrazky/casino/add-plz.gif'
        gif = Image.open(gif_path)
        frames = []

        try:
            while True:
                frame = gif.convert('RGBA')
                frame = pygame.image.fromstring(frame.tobytes(), frame.size, 'RGBA')
                frames.append(frame)
                gif.seek(gif.tell() + 1)
        except EOFError:
            pass

        frame_index = 0
        play_animation = True
        while True:
            self.draw_text('Casino Monopoly', pygame.font.Font(None, 100), self.BLACK, self.screen,
                           680, 100)

            roll_button = pygame.Rect(900, 800, 130, 50)

            hrat_button = pygame.Rect(887,900,160,50)

            mx, my = pygame.mouse.get_pos()

            pygame.draw.rect(self.screen, self.RED, roll_button, border_radius=15)
            self.draw_text('Result', self.font, self.WHITE, self.screen, 908, 810)
            pygame.draw.rect(self.screen, self.RED, hrat_button, border_radius=15)
            self.draw_text('Play', self.font, self.WHITE, self.screen, 927, 910)
            click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            if roll_button.collidepoint((mx, my)):
                if click:
                    self.casino_end()
            if hrat_button.collidepoint((mx, my)):
                if click:
                    return

            if play_animation:
                self.screen.blit(frames[frame_index], (870, 400))
                frame_index = (frame_index + 1) % len(frames)

            pygame.display.flip()

            self.clock.tick(30)
    def casino_end(self):
        self.screen.fill(self.WHITE)
        if self.win == 1:
              gif_path = 'obrazky/casino/win/1.gif'
              text = 'You win'

        else:
              gif_path = f'obrazky/casino/lost/{random.randint(0,1)}.gif'
              text = 'You lost'
        gif = Image.open(gif_path)
        frames = []

        try:
            while True:
                frame = gif.convert('RGBA')
                frame = pygame.image.fromstring(frame.tobytes(), frame.size, 'RGBA')
                frames.append(frame)
                gif.seek(gif.tell() + 1)
        except EOFError:
            pass

        frame_index = 0
        play_animation = True
        while True:
            self.screen.fill(self.WHITE)

            ok_button = pygame.Rect(900, 800, 110, 50)

            mx, my = pygame.mouse.get_pos()

            pygame.draw.rect(self.screen, self.RED, ok_button, border_radius=15)
            self.draw_text('OK', self.font, self.WHITE, self.screen, 932, 810)
            click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            if ok_button.collidepoint((mx, my)):
                if click:
                    return

            if play_animation:
                if gif_path == 'obrazky/casino/win/1.gif':
                      self.screen.blit(frames[frame_index], (780, 400))
                elif gif_path == f'obrazky/casino/lost/0.gif':
                    self.screen.blit(frames[frame_index], (730, 330))
                elif gif_path == f'obrazky/casino/lost/1.gif':
                    self.screen.blit(frames[frame_index], (730, 100))
                self.draw_text(text,self.font, self.BLACK,self.screen, 890, 860)

                frame_index = (frame_index + 1) % len(frames)

            pygame.display.flip()

            self.clock.tick(30)

    def nastavenia(self):
        while True:
            self.screen.fill(self.WHITE)
            self.draw_text('Settings', pygame.font.Font(None, 100), self.BLACK, self.screen,
                           800, 45)

            back_button = pygame.Rect(50, 50, 110, 50)


            mx, my = pygame.mouse.get_pos()

            pygame.draw.rect(self.screen, self.RED, back_button, border_radius=15)
            self.draw_text('Back', self.font, self.BLACK, self.screen, 60, 60)
            for i in range(5):
                pygame.draw.rect(self.screen, self.is_aktiv_k.get(i), pygame.Rect(640 + (i * 140), 200, 120, 150))
                if i == 0:
                    button_0 = pygame.Rect(640 + (i * 140), 200, 120, 150)
                elif i == 1:
                    button_1 = pygame.Rect(640 + (i * 140), 200, 120, 150)
                elif i == 2:
                    button_2 = pygame.Rect(640 + (i * 140), 200, 120, 150)
                elif i == 3:
                    button_3 = pygame.Rect(640 + (i * 140), 200, 120, 150)
                elif i == 4:
                    button_4 = pygame.Rect(640 + (i * 140), 200, 120, 150)
                image = pygame.image.load(f'obrazky/vyber fak/{i}.png')
                image = pygame.transform.scale(image, (116, 146))
                self.screen.blit(image, (640 + (i * 140) + 2, 200 + 2))
            for i in range(3):
                pygame.draw.rect(self.screen, self.is_aktiv_s.get(i+5), pygame.Rect(780 + (i * 140), 370, 120, 150))
                if i == 0:
                    button_5 = pygame.Rect(780 + (i * 140), 370, 120, 150)
                elif i == 1:
                    button_6 = pygame.Rect(780 + (i * 140), 370, 120, 150)
                elif i == 2:
                    button_7 = pygame.Rect(780 + (i * 140), 370, 120, 150)
                image = pygame.image.load(f'obrazky/vyber fak/{i+5}.png')
                image = pygame.transform.scale(image, (116, 146))
                self.screen.blit(image, (780 + (i * 140) + 2, 370 + 2))
            for i in range(2):
                pygame.draw.rect(self.screen, self.is_aktiv_e.get(i + 8), pygame.Rect(850 + (i * 140), 540, 120, 150))
                if i == 0:
                    button_8 = pygame.Rect(850 + (i * 140), 540, 120, 150)
                elif i == 1:
                    button_9 = pygame.Rect(850 + (i * 140), 540, 120, 150)
                image = pygame.image.load(f'obrazky/vyber fak/{i+8}.png')
                image = pygame.transform.scale(image, (116, 146))
                self.screen.blit(image, (850 + (i * 140) + 2, 540 + 2))

            click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            if back_button.collidepoint((mx, my)):
                if click:
                    return
            if button_0.collidepoint((mx, my)):
                if click:
                    self.vyber_fak_k = 0
                    for i in range(5):
                        if i != 0:
                           self.is_aktiv_k[i] = self.BLACK
                        else:
                           self.is_aktiv_k[i] = self.RED
            if button_1.collidepoint((mx, my)):
                if click:
                    self.vyber_fak_k = 1
                    for i in range(5):
                        if i != 1:
                            self.is_aktiv_k[i] = self.BLACK
                        else:
                            self.is_aktiv_k[i] = self.RED
            if button_2.collidepoint((mx, my)):
                if click:
                    self.vyber_fak_k = 2
                    for i in range(5):
                        if i != 2:
                            self.is_aktiv_k[i] = self.BLACK
                        else:
                            self.is_aktiv_k[i] = self.RED
            if button_3.collidepoint((mx, my)):
                if click:
                    self.vyber_fak_k = 3
                    for i in range(5):
                        if i != 3:
                            self.is_aktiv_k[i] = self.BLACK
                        else:
                            self.is_aktiv_k[i] = self.RED
            if button_4.collidepoint((mx, my)):
                if click:
                    self.vyber_fak_k = 4
                    for i in range(5):
                        if i != 4:
                            self.is_aktiv_k[i] = self.BLACK
                        else:
                            self.is_aktiv_k[i] = self.RED
            if button_5.collidepoint((mx, my)):
                if click:
                    self.vyber_fak_s = 5
                    for i in range(3):
                        if i + 5 != 5:
                            self.is_aktiv_s[i+5] = self.BLACK
                        else:
                            self.is_aktiv_s[i+5] = self.RED
            if button_6.collidepoint((mx, my)):
                if click:
                    self.vyber_fak_s = 6
                    for i in range(3):
                        if i + 5 != 6:
                            self.is_aktiv_s[i+5] = self.BLACK
                        else:
                            self.is_aktiv_s[i+5] = self.RED
            if button_7.collidepoint((mx, my)):
                if click:
                    self.vyber_fak_s = 7
                    for i in range(3):
                        if i + 5 != 7:
                            self.is_aktiv_s[i+5] = self.BLACK
                        else:
                            self.is_aktiv_s[i+5] = self.RED
            if button_8.collidepoint((mx, my)):
                if click:
                    self.vyber_fak_e = 8
                    for i in range(2):
                        if i + 8 != 8:
                            self.is_aktiv_e[i+8] = self.BLACK
                        else:
                            self.is_aktiv_e[i+8] = self.RED
            if button_9.collidepoint((mx, my)):
                if click:
                    self.vyber_fak_e = 9
                    for i in range(2):
                        if i + 8 != 9:
                            self.is_aktiv_e[i+8] = self.BLACK
                        else:
                            self.is_aktiv_e[i+8] = self.RED

            pygame.display.update()
            self.clock.tick(60)

class Players:
    def __init__(self):
        self._player_name = {}
        self._player_color = {}
        self._player_wallet = {}
        self._player_companies = {}
        self.player_pos = {}
        self.player_pole = {}
        self.current_pole = {}
        self.time_in_jail = {}
        self.target_x = {}
        self.players_active = {}
        self.target_y = {}
        self.players_colors_available = [[(2, 255, 12), (6, 126, 25)], [(174, 2, 255), (59, 6, 126)],
                                         [(255, 245, 2), (126, 121, 6)],
                                         [(255, 2, 199), (126, 6, 121)], [(255, 2, 2), (126, 6, 6)],
                                         [(2, 149, 255), (6, 75, 126)]]


if __name__ == '__main__':
    Program()
