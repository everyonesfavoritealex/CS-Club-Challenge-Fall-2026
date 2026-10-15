"""
Author: Alex
Date: 10-15-2026
Description: Gives information on mouse status with rectangles
"""
import pygame
def hovering(mousepos,rect):
    """
    Description: Detects if mouse is within area of rect, use along with pygame.MOUSEBUTTONUP in game loop to detect if a click happened
    Parameters: (tuple) mousepos, (pygame.Rect) rect
    Return: True if mouse is within the area of rect, false othewise
    """
    if rect.x<=mousepos[0]<=(rect.x+rect.width) and rect.y<=mousepos[1]<=(rect.x+rect.height):
        return True
    return False