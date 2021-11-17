from distutils.core import setup
import py2app
OPTIONS = {}

Mydata_files = [('Background', [r'.\images\6-66713_pacman-ghost-wallpaper-pacman-ghost.jpg']),
('Explosion', [r'.\images\explosion.png']),
('player', [r'.\images\player.png']),
('slime', [r'.\images\pixelarthh.png']),
('walk', [r'.\images\walk.png']),
('walk', [r'.\images\pacman_sound.wav']),
('walk', [r'.\images\game_over_sound.wav'])]
   


setup(app=['main.py'],data_files = Mydata_files,options={'py2app': OPTIONS},    
            setup_requires=["py2app"],) 