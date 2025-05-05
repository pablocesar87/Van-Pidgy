import pygame
from pygame.locals import *
from typing import List

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOX_WIDTH = 200
BOX_HEIGHT = 20
FONT_SIZE = 18

def get_key() -> int:
    """Wait for a key press and return the key."""
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                return event.key

def display_box(screen: pygame.Surface, message: str) -> None:
    """Display a message in a box in the middle of the screen."""
    font = pygame.font.Font(None, FONT_SIZE)
    screen_width, screen_height = screen.get_size()
    box_rect = pygame.Rect(
        (screen_width // 2) - (BOX_WIDTH // 2),
        (screen_height // 2) - (BOX_HEIGHT // 2),
        BOX_WIDTH,
        BOX_HEIGHT
    )
    pygame.draw.rect(screen, BLACK, box_rect)
    pygame.draw.rect(screen, WHITE, box_rect.inflate(4, 4), 1)
    if message:
        text_surface = font.render(message, True, WHITE)
        screen.blit(text_surface, (box_rect.x + 5, box_rect.y + 2))
    pygame.display.flip()

def ask(screen: pygame.Surface, question: str) -> str:
    """Prompt the user with a question and return their input."""
    pygame.font.init()
    current_string: List[str] = []
    display_box(screen, f"{question}: {''.join(current_string)}")
    while True:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[:-1]
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif 32 <= inkey <= 126:  # Printable ASCII range
            current_string.append(chr(inkey))
        display_box(screen, f"{question}: {''.join(current_string)}")
    return ''.join(current_string)

def main() -> None:
    """Main function to test the input box."""
    pygame.init()
    screen = pygame.display.set_mode((320, 240))
    pygame.display.set_caption("Input Box Test")
    try:
        user_input = ask(screen, "Your name")
        print(f"{user_input} was entered")
    finally:
        pygame.quit()

if __name__ == '__main__':
    main()
