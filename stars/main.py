                                                                                                                 
import pygame                                                                                                    
import random                                                                                                    
from pygame.locals import *                                                                                      
                                                                                                                 
                                                                                                                 
def generate_star_data():                                                                                        
    star_name = f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}-{random.randint(1000, 9999)}"                    
    population = random.randint(1, 1000000) * 10**(random.randint(0, 6))                                         
    industry = random.choice(['Mining', 'Agriculture', 'Manufacturing', 'Research', 'Commerce'])                 
                                                                                                                 
    return {                                                                                                     
        'name': star_name,                                                                                       
        'population': population,                                                                                
        'industry': industry                                                                                     
    }                                                                                                            
                                                                                                                 
                                                                                                                 
pygame.init()                                                                                                    
screen = pygame.display.set_mode((1200, 1200))                                                                     
pygame.display.set_caption('Starmap')                                                                            
                                                                                                                 
star_coordinates = [(random.randint(0, 1200), random.randint(0, 1200)) for _ in range(100)]                        
                                                                                                                 
running = True                                                                                                   
clicked_star = None                                                                                              
star_data = generate_star_data()                                                                                 
                                                                                                                 
while running:                                                                                                   
    screen.fill((0, 0, 0))                                                                                       
                                                                                                                 
    for event in pygame.event.get():                                                                             
        if event.type == QUIT:                                                                                   
            running = False                                                                                      
        elif event.type == MOUSEBUTTONDOWN:                                                                      
            mouse_pos = event.pos                                                                                
            for idx, coord in enumerate(star_coordinates):                                                       
                if pygame.Rect(coord[0] - 3, coord[1] - 3, 6, 6).collidepoint(mouse_pos):                        
                    clicked_star = coord                                                                         
                    star_data = generate_star_data()                                                             
                    break                                                                                        
                                                                                                                 
    for coord in star_coordinates:                                                                               
        pygame.draw.lines(screen, (255, 255, 255), True, [(coord[0] - 2, coord[1]), (coord[0] + 2, coord[1])], 1)
        pygame.draw.lines(screen, (255, 255, 255), True, [(coord[0], coord[1] - 2), (coord[0], coord[1] + 2)], 1)
                                                                                                                 
    if clicked_star:                                                                                             
        pygame.draw.rect(screen, (128, 128, 128), (605, 10, 185, 580))                                           
        font = pygame.font.Font(None, 16)                                                                        
        text_surface = font.render(f'Star Name: {star_data["name"]}', True, (255, 255, 255))                     
        screen.blit(text_surface, (615, 60))                                                                     
                                                                                                                 
        text_surface = font.render(f'Population: {star_data["population"]}', True, (255, 255, 255))              
        screen.blit(text_surface, (615, 120))                                                                    
                                                                                                                 
        text_surface = font.render(f'Industry: {star_data["industry"]}', True, (255, 255, 255))                  
        screen.blit(text_surface, (615, 180))                                                                    
                                                                                                                 
    pygame.display.flip()                                                                                        
                                                                                                                 
pygame.quit()  