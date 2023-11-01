import PySimpleGUI as sg
import threading
import game_logic

layout = [
    [sg.Button("Почати гру")],
]

window = sg.Window("Графічний інтерфейс", layout)
game_thread = None  

def start_game():
    global game_thread
    if game_thread is None or not game_thread.is_alive():
        game_thread = threading.Thread(target=game_logic.guess_the_number)
        game_thread.start()

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Почати гру':
        start_game()

window.close()
