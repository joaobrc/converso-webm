from moviepy.editor import VideoFileClip
import os
from pathlib import Path





def converso(caminho_video_web:str, caminho_video_saida:str):
    """
    >>> converso(r'C:\Users\joao.costa\Documents\screen-capture (8).webm', r'C:\Users\joao.costa\Documents\lace.mp4")
    'C:\Users\joao.costa\Documents\lace.mp4
    """
    
    
    video_converter = VideoFileClip(caminho_video_web)
    video_converter.write_videofile(caminho_video_saida)
    
    return print(caminho_video_saida)
    



