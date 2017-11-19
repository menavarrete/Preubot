import requests
import os

bot_id = os.environ['key']
url = "https://api.telegram.org/bot"
password = os.environ['admin_key']

functions = ["/salas", "/actividades", "/ensayos", "/help", "/voluntarios", "/talleres", "/contacto", "/apoyo", "/errores"]


def send_message(user_id, message):
    method = "sendMessage"
    data = {"chat_id": user_id,
            "text": message}
    r = requests.post(url + bot_id + "/" + method, data=data)

def send_photo(user_id, photo):
    method = "sendPhoto"
    data = {"chat_id": user_id,
            "photo": photo}
    return requests.post(url + bot_id + "/" + method, data=data)


def create_content(name):
    file = open(name+'.txt', 'r').read()
    return file


def handle(user_id, body):
    body1 = body.split(" ")
    if body1[0] in functions:
        send_message(user_id, create_content(body1[0][1:]))
        return

    elif body1[0] == "/profesores":
        imagen = 'https://4.bp.blogspot.com/-y3av9_IrIbA/We_EUd-Z--I/AAAAAAAAAbc/vjw8Z0h50yojgT7GJ69gf-lfus741m53ACK4BGAYYCw/s1600/Captura%2Bde%2Bpantalla%2B2017-10-24%2Ba%2Bla%2528s%2529%2B19.52.03.png'
        send_photo(user_id, imagen)
        return


    body2 = body.split('&&')
    if body2[0].split('_')[0] == '/set' and body2[1] == password:
        file = open(body2[0].split('_')[1] + '.txt', 'w')
        file.write(body2[2])
        file.close()
        send_message(user_id, "Status: ok\nFunction changed successfully")
        return

    if body2[0] == '/create' and body2[1] == password:
        file = open(body2[2] + '.txt', 'w')
        file.close()
        functions.append('/' + body2[2])
        send_message(user_id, "Status: ok\nFunction created successfully")
        return
