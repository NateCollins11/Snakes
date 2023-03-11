
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
GRAY = (100, 100, 100)

DIMENSIONS = [800, 800]

GRID_SIZE = 12

unit = DIMENSIONS[0] / GRID_SIZE  #px
body_part_size = unit - 2

# TODO LIST

# MAKE RANDOMLY POSITIONED FRUIT THAT DISAPPEARS WHEN YOU REACH IT
# KEEP TRACK OF PREVIOUS POSITIONS, AND DRAW THEM AS WELL
# MAKE IT SO YOU CANT GO OFF THE SIDE








def draw_grid(screen):
    for ix in range(DIMENSIONS[0]):
        for iy in range(DIMENSIONS[1]):
            pygame.draw.rect(screen, GRAY, (ix * unit , iy * unit , unit - 1, unit - 1))


def main():
    """ Main Program """

    # Call this function so the Pygame library can initialize itself
    pygame.init()
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 800])

    # Set the title of the window
    pygame.display.set_caption('Game')



    clock = pygame.time.Clock()

    done = False

    positions = [[5, 5]]

    direction = [1, 0]

    snake_length = 6

    while not done:
        # print(xpos, ypos)

        # --- Event Processing ---

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if direction != [-1, 0]:
                        direction = [1, 0]
                if event.key == pygame.K_LEFT:
                    if direction != [1, 0]:
                        direction = [-1, 0]
                if event.key == pygame.K_DOWN:
                    if direction != [0, -1]:
                        direction = [0, 1]
                if event.key == pygame.K_UP:
                    if direction != [0, 1]:
                        direction = [0, -1]
            if event.type == pygame.KEYUP:
                pass

        # --- Logic ---

        # MOVE FUNCTION

        # Check if X is between 0, 12
        if positions[0][0] >= 12 or positions[0][0] < 0:

            print('OUT OF BOUNDS' + str(positions[0][0]))
            pygame.quit()

        # Check if Y is between 0, 12
        if positions[0][1] >= 12 or positions[0][1] < 0:
            print('OUT OF BOUNDS' + str(positions[0][1]))

            pygame.quit()


        positions.insert(0, [positions[0][0] + direction[0], positions[0][1] + direction[1]])
        if len(positions) > snake_length:
            positions.pop()

        # --- Drawing ---
        screen.fill(BLACK)
        # draw_grid((screen))

        # THIS IS WHERE THE CHARACTER IS DRAWN

        for coords in positions:
            pygame.draw.rect(screen, GREEN, (coords[0] * unit, coords[1] * unit, body_part_size, body_part_size))




        pygame.display.flip()



        clock.tick(4)

    pygame.quit()


if __name__ == "__main__":
    main()