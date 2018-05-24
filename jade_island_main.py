cwd = os.getcwd()
sys.path.append(cwd+"/./../")

import time

# room imports
import adventure_game2.rooms.room1 as r1
import adventure_game2.rooms.room2 as r2
import adventure_game2.rooms.room3 as r3
import adventure_game2.rooms.room4 as r4
import adventure_game2.rooms.room5 as r5
import adventure_game2.rooms.room6 as r6
import adventure_game2.rooms.room7 as r7
import adventure_game2.rooms.room8 as r8
import adventure_game2.rooms.room9 as r9
import adventure_game2.rooms.room10 as r10
import adventure_game2.rooms.room11 as r11
import adventure_game2.rooms.room12 as r12
import adventure_game2.rooms.room13 as r13
import adventure_game2.rooms.room14 as r14
import adventure_game2.rooms.room15 as r15

#required for coloram
from colorama import init
init()


#Room First Entrance Verifications

room1_entrance = 0


#Room First Entrace Descriptions
room1_desc = '''\t\tYou wake up in a daze. Your head is throbbing, and 
    it seems you have forgotten where you are and how you got there.
    You check your pockets... you have a knife, flashlight, and some rope.'''




# Default the player to the first room
room_number = 1

# Player Inventory
player_inventory = {
    'knife' : 1,
    'flashlight': 1,
    'key' : 0,
    'rope' : 1
}

print("\t\t\tWelcome to the maze game...\n Pay very close attention to the descriptions of each room\n Use 'help' for your commands at the start of the game.")

should_continue = True
while should_continue:
    if room_number == 1:
        room_number = r1.run_room( player_inventory )
    elif room_number == 2:
        room_number = r2.run_room( player_inventory )
    elif room_number == 3:
        room_number = r3.run_room( player_inventory )
    elif room_number == 4:
        room_number = r4.run_room( player_inventory )
    elif room_number == 5:
        room_number = r5.run_room( player_inventory )
    elif room_number == 6:
        room_number = r6.run_room( player_inventory )
    elif room_number == 7:
        room_number = r7.run_room( player_inventory )
    elif room_number == 8:
        room_number = r8.run_room( player_inventory )
    elif room_number == 9:
        room_number = r9.run_room( player_inventory )
    elif room_number == 10:
        room_number = r10.run_room( player_inventory )
    elif room_number == 11:
        room_number = r11.run_room( player_inventory )
    elif room_number == 12:
        room_number = r12.run_room( player_inventory )
    elif room_number == 13:
        room_number = r13.run_room( player_inventory )
    elif room_number == 14:
        room_number = r14.run_room( player_inventory )
    elif room_number == 15:
        room_number = r15.run_room( player_inventory )
    else:

        break
#

print("The game has ended...")
