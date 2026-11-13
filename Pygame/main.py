import pygame
pygame.init()

screen1 = pygame.display.set_mode((800, 400))
sprite_sheet_image = pygame.image.load('111.png').convert_alpha()


class SpriteSheet():
      def __init__(self, image):
            self.sheet = image

      def get_image(self, frame, width, height, scale):
           
            #create a simple blank surface for a specific frame on the sprite sheet
            individual_img = pygame.Surface((width, height)).convert_alpha()
            #inserting the image of that frame onto the created surface
            individual_img.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
            #self.sheet is the source of the image
            #(0, 0) is on which location of the individual_img you wish to put the image

            # ((frame * width), 0, width, height) this is the (x, y, width, height) of the self.sheet
            # This basically specifies how you want to cut the self.sheet


            individual_img = pygame.transform.scale(individual_img, (width * scale, height * scale))
           
            return individual_img

Animation_object = SpriteSheet(sprite_sheet_image)
Frames = [Animation_object.get_image(i, 24, 24, 5) for i in range(24)]

i = 0
game_active = True
while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
    
    screen1.blit(Frames[i], (200,200))

    if i < 23:
          i+=1
    else:
          i = 0

    pygame.display.update()
    pygame.time.Clock().tick(60)