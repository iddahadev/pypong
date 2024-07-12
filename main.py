import pygame

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540

RACKET_WIDTH = 30
RACKET_HEIGHT = 100
RACKET_COLOR = (255, 255, 255)

PLAYER_ONE_INITIAL_X = 0
PLAYER_ONE_INITIAL_Y = (WINDOW_HEIGHT - RACKET_HEIGHT) / 2

PLAYER_TWO_INITIAL_X = WINDOW_WIDTH - RACKET_WIDTH
PLAYER_TWO_INITIAL_Y = (WINDOW_HEIGHT - RACKET_HEIGHT) / 2


BALL_RADIUS = 10
BALL_COLOR = (255, 255, 255)

BALL_INITIAL_X = WINDOW_WIDTH / 2
BALL_INITIAL_Y = WINDOW_HEIGHT / 2

FPS = 60

class Unit:
    def __init__(self, pos_x, pos_y, width, height):
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._width = width
        self._height = height
    
    def draw(self, surface):
        pass

class Racket(Unit):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, RACKET_WIDTH, RACKET_HEIGHT)
    
    def draw(self, surface):
        rect = pygame.Rect((self._pos_x, self._pos_y), (self._width, self._height))
        pygame.draw.rect(surface, RACKET_COLOR, rect)

class Ball(Unit):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, BALL_RADIUS, BALL_RADIUS)
    
    def draw(self, surface):
        coordinates = (self._pos_x, self._pos_y)
        pygame.draw.circle(surface, BALL_COLOR, coordinates, BALL_RADIUS)


class Game:
    def __init__(self):
        self.__screen = None
        self.__is_running = False
        self.__clock = None
        self.__player_one = Racket(PLAYER_ONE_INITIAL_X, PLAYER_ONE_INITIAL_Y)
        self.__player_two = Racket(PLAYER_TWO_INITIAL_X, PLAYER_TWO_INITIAL_Y)
        self.__ball = Ball(BALL_INITIAL_X, BALL_INITIAL_Y)

    def init(self):
        pygame.init()
        pygame.display.set_caption('Pypong')
        self.__screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        self.__clock = pygame.time.Clock()
    
    def play(self):
        self.__is_running = True
        while self.__is_running:
            self.__handle_events()
            self.__update()
            self.__render()
            self.__clock.tick(FPS)
        pygame.quit()
    
    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__is_running = False

    def __update(self):
        pass
            
    def __render(self):
        self.__screen.fill((0, 0, 0))
        
        self.__player_one.draw(self.__screen)
        self.__player_two.draw(self.__screen)
        self.__ball.draw(self.__screen)
        
        pygame.display.flip()

def main():
    game = Game()
    game.init()
    game.play()

main()