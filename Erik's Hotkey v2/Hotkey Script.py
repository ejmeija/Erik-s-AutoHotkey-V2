#Libraries
import pyautogui
import time
import colorama
import random
#Hotkeys. Customizable stuff is a bit down there.
def Minecraft_Hotkey():
    pyautogui.press("/", 1)
    print("Minecraft hotkey was Selected.")
    Random = random.choice(Words)
    pyautogui.typewrite(Random)
    print("Word", [Random],"Has been typed.")
    pyautogui.press("enter", 1)
    time.sleep(typingCooldown)
    Minecraft_Hotkey()

def Hotkey():
    pyautogui.press(ChatButton, 1)
    print("Regular Hotkey was Selected.")
    Random = random.choice(Words)
    pyautogui.typewrite(Random)
    print("Word", [Random],"Has been typed.")
    pyautogui.press("enter", 1)
    time.sleep(typingCooldown)
    Hotkey()   

#Thanks for downloading this. Unfortuantely, this does not work in roblox, since they have decided chatbots are annoying.
#Good luck!
#Words. Just do a , if you want to do more words. Its completely random which they choose.
Words = [
    "test1",
    "test2",
    "test3"
]

typingCooldown = 5


#If you are playing minecraft, I made a specific script.

Minecraft = False
#It works the same, just a little different. If you Set this to false use:

ChatButton = "/"

#REMEMBER TO SET THIS! It will press whatever character as a button that should open up the chat. Set it to blank if you don't want 
#anything to happen.








if Minecraft == True: 
       print("Picked minecraft...")
       Minecraft_Hotkey()
else:
       print("Didnt pick minecraft...")
       Hotkey()









       







