from distutils.core import setup 
import py2exe
import os
 


Mydata_files = [('Background', [r'.\images\Unticccctled-1.jpg']),
('Explosion', [r'.\images\explosion.png']),
('player', [r'.\images\player.png']),
('slime', [r'.\images\pixelartddddd.png']),
('walk', [r'.\images\walk.png']),
('walk', [r'.\images\pacman_sound.wav']),
('walk', [r'.\images\game_over_sound.wav'])]
   


setup(console=['main.py'],data_files = Mydata_files,
            options={"py2exe":{ "unbuffered": True,"optimize": 2,}}) 