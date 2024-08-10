from player import player
import highscore
import admin
from highscore import*
n= input('Select Interface:\n'
         
         '1.Administrative\n'
         '2.Player\n')
if n=='1':
    admin.Administrative()
elif n=='2':
    c=player()
    highscore(c)

else:
    print('select correct option!')
