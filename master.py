import keyboard
from fonctions.functions_master import *


# MASTER IS THE COMPUTER WHERE THE KEYBORD IS CLICKING
finir = False


while finir != True:
    recorded = keyboard.read_key()
    if recorded == 'esc':
        finir = True
    asyncio.get_event_loop().run_until_complete(send_key(recorded))
