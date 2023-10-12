import pygame
import numpy as np
import cv2
import glob
import re
import datetime

class ScreenSave:
    """Screen frame capturing class
    screen : screen to save
    images_path : path to save sequence of images
    video_path : path to save video
    
    """
    def __init__(self, screen, images_path, video_path):
        self.screen = screen
        self.frame_count = 0
        self.images_path = images_path
        self.video_write_path = video_path

    def capture_image(self, screen):
        image_name = "%s/%08d.png"%(self.images_path, self.frame_count)
        pygame.image.save(screen, image_name)
        self.frame_count += 1

    def save_video(self, fps):
        filenames = glob.glob("./%s/*.png" %self.images_path)
        filenames.sort(key=lambda x: int(re.search(r'(\d+)\.png', x).group(1)))
        now = datetime.datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        out = cv2.VideoWriter('%s/%s.avi'%(self.video_write_path, dt_string), cv2.VideoWriter_fourcc(*'DIVX'), 60, (1920, 1080))

        for filename in filenames:
            img = img = cv2.imread(filename=filename)
            out.write(img)
            print(filename)