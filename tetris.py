import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 30
GRID_X_OFFSET = 50
GRID_Y_OFFSET = 50

WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE + 2 * GRID_X_OFFSET + 200
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE + 2 * GRID_Y_OFFSET

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
GRAY = (128, 128, 128)

# Tetromino shapes
TETROMINOES = {
    'I': [
        ['.....',
         '..#..',
         '..#..',
         '..#..',
         '..#..'],
        ['.....',
         '.....',
         '####.',
         '.....',
         '.....']
    ],
    'O': [
        ['.....',
         '.....',
         '.##..',
         '.##..',
         '.....']
    ],
    'T': [
        ['.....',
         '.....',
         '.#...',
         '###..',
         '.....'],
        ['.....',
         '.....',
         '.#...',
         '.##..',
         '.#...'],
        ['.....',
         '.....',
         '.....',
         '###..',
         '.#...'],
        ['.....',
         '.....',
         '.#...',
         '##...',
         '.#...']
    ],
    'S': [
        ['.....',
         '.....',
         '.##..',
         '##...',
         '.....'],
        ['.....',
         '.#...',
         '.##..',
         '..#..',
         '.....']
    ],
    'Z': [
        ['.....',
         '.....',
         '##...',
         '.##..',
         '.....'],
        ['.....',
         '..#..',
         '.##..',
         '.#...',
         '.....']
    ],
    'J': [
        ['.....',
         '.#...',
         '.#...',
         '##...',
         '.....'],
        ['.....',
         '.....',
         '#....',
         '###..',
         '.....'],
        ['.....',
         '.##..',
         '.#...',
         '.#...',
         '.....'],
        ['.....',
         '.....',
         '###..',
         '..#..',
         '.....']
    ],
    'L': [
        ['.....',
         '..#..',
         '..#..',
         '.##..',
         '.....'],
        ['.....',
         '.....',
         '###..',
         '#....',
         '.....'],
        ['.....',
         '##...',
         '.#...',
         '.#...',
         '.....'],
        ['.....',
         '.....',
         '..#..',
         '###..',
         '.....']
    ]
}

TETROMINO_COLORS = {
    'I': CYAN,
    'O': YELLOW,
    'T': PURPLE,
    'S': GREEN,
    'Z': RED,
    'J': BLUE,
    'L': ORANGE
}

class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = GRID_WIDTH // 2 - 2
        self.y = 0
        self.rotation = 0
        
    def get_rotated_shape(self):
        return TETROMINOES[self.shape][self.rotation % len(TETROMINOES[self.shape])]
    
    def get_cells(self):
        cells = []
        shape = self.get_rotated_shape()
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell == '#':
                    cells.append((self.x + j, self.y + i))
        return cells

class TetrisGame:
    def __init__(self):
        self.grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.get_new_piece()
        self.next_piece = self.get_new_piece()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.fall_time = 0
        self.fall_speed = 500  # milliseconds
        self.game_over = False
        
    def get_new_piece(self):
        shape = random.choice(list(TETROMINOES.keys()))
        return Tetromino(shape, TETROMINO_COLORS[shape])
    
    def is_valid_position(self, piece, dx=0, dy=0, rotation=None):
        if rotation is None:
            rotation = piece.rotation
            
        # Temporarily change piece position and rotation
        old_x, old_y, old_rotation = piece.x, piece.y, piece.rotation
        piece.x += dx
        piece.y += dy
        piece.rotation = rotation
        
        # Check if position is valid
        cells = piece.get_cells()
        valid = True
        
        for x, y in cells:
            if x < 0 or x >= GRID_WIDTH or y >= GRID_HEIGHT:
                valid = False
                break
            if y >= 0 and self.grid[y][x] != BLACK:
                valid = False
                break
                
        # Restore original position and rotation
        piece.x, piece.y, piece.rotation = old_x, old_y, old_rotation
        return valid
    
    def place_piece(self, piece):
        cells = piece.get_cells()
        for x, y in cells:
            if y >= 0:
                self.grid[y][x] = piece.color
    
    def clear_lines(self):
        lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(cell != BLACK for cell in self.grid[y]):
                lines_to_clear.append(y)
        
        for y in lines_to_clear:
            del self.grid[y]
            self.grid.insert(0, [BLACK for _ in range(GRID_WIDTH)])
        
        lines_cleared = len(lines_to_clear)
        if lines_cleared > 0:
            self.lines_cleared += lines_cleared
            self.score += lines_cleared * 100 * self.level
            self.level = self.lines_cleared // 10 + 1
            self.fall_speed = max(50, 500 - (self.level - 1) * 50)
    
    def update(self, dt):
        if self.game_over:
            return
            
        self.fall_time += dt
        if self.fall_time >= self.fall_speed:
            self.fall_time = 0
            if self.is_valid_position(self.current_piece, dy=1):
                self.current_piece.y += 1
            else:
                self.place_piece(self.current_piece)
                self.clear_lines()
                self.current_piece = self.next_piece
                self.next_piece = self.get_new_piece()
                
                if not self.is_valid_position(self.current_piece):
                    self.game_over = True
    
    def move_piece(self, dx):
        if self.is_valid_position(self.current_piece, dx=dx):
            self.current_piece.x += dx
    
    def rotate_piece(self):
        new_rotation = (self.current_piece.rotation + 1) % len(TETROMINOES[self.current_piece.shape])
        if self.is_valid_position(self.current_piece, rotation=new_rotation):
            self.current_piece.rotation = new_rotation
    
    def drop_piece(self):
        while self.is_valid_position(self.current_piece, dy=1):
            self.current_piece.y += 1
        self.score += 2

def draw_grid(screen, game):
    # Draw grid background
    grid_rect = pygame.Rect(GRID_X_OFFSET, GRID_Y_OFFSET, 
                           GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE)
    pygame.draw.rect(screen, WHITE, grid_rect)
    pygame.draw.rect(screen, GRAY, grid_rect, 2)
    
    # Draw placed pieces
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if game.grid[y][x] != BLACK:
                rect = pygame.Rect(GRID_X_OFFSET + x * CELL_SIZE + 1,
                                 GRID_Y_OFFSET + y * CELL_SIZE + 1,
                                 CELL_SIZE - 2, CELL_SIZE - 2)
                pygame.draw.rect(screen, game.grid[y][x], rect)
    
    # Draw current piece
    if not game.game_over:
        cells = game.current_piece.get_cells()
        for x, y in cells:
            if 0 <= x < GRID_WIDTH and y >= 0:
                rect = pygame.Rect(GRID_X_OFFSET + x * CELL_SIZE + 1,
                                 GRID_Y_OFFSET + y * CELL_SIZE + 1,
                                 CELL_SIZE - 2, CELL_SIZE - 2)
                pygame.draw.rect(screen, game.current_piece.color, rect)

def draw_next_piece(screen, piece):
    # Draw next piece preview
    next_x = GRID_X_OFFSET + GRID_WIDTH * CELL_SIZE + 20
    next_y = GRID_Y_OFFSET + 50
    
    font = pygame.font.Font(None, 36)
    text = font.render("Next:", True, WHITE)
    screen.blit(text, (next_x, next_y - 30))
    
    shape = piece.get_rotated_shape()
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell == '#':
                rect = pygame.Rect(next_x + j * 20, next_y + i * 20, 18, 18)
                pygame.draw.rect(screen, piece.color, rect)

def draw_info(screen, game):
    info_x = GRID_X_OFFSET + GRID_WIDTH * CELL_SIZE + 20
    info_y = GRID_Y_OFFSET + 150
    
    font = pygame.font.Font(None, 36)
    
    score_text = font.render(f"Score: {game.score}", True, WHITE)
    level_text = font.render(f"Level: {game.level}", True, WHITE)
    lines_text = font.render(f"Lines: {game.lines_cleared}", True, WHITE)
    
    screen.blit(score_text, (info_x, info_y))
    screen.blit(level_text, (info_x, info_y + 40))
    screen.blit(lines_text, (info_x, info_y + 80))
    
    if game.game_over:
        game_over_text = font.render("GAME OVER", True, RED)
        restart_text = font.render("Press R to restart", True, WHITE)
        screen.blit(game_over_text, (info_x, info_y + 120))
        screen.blit(restart_text, (info_x, info_y + 160))

def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    
    game = TetrisGame()
    
    while True:
        dt = clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if game.game_over:
                    if event.key == pygame.K_r:
                        game = TetrisGame()
                else:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        game.move_piece(-1)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        game.move_piece(1)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        game.fall_time = game.fall_speed  # Force immediate drop
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        game.rotate_piece()
                    elif event.key == pygame.K_SPACE:
                        game.drop_piece()
        
        game.update(dt)
        
        screen.fill(BLACK)
        draw_grid(screen, game)
        
        if not game.game_over:
            draw_next_piece(screen, game.next_piece)
        
        draw_info(screen, game)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()