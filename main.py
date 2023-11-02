import PySimpleGUI as sg
import threading
import game_logic

layout = [
    [sg.Button("Почати гру")],
    [sg.Radio("Легкий", "RADIO1", default=True, size=(10, 1), key="-EASY-"), sg.Radio("Середній", "RADIO1", key="-MEDIUM-")],
]

window = sg.Window("Графічний інтерфейс", layout)
game_thread = None  

def start_game(difficulty):
    global game_thread
    if game_thread is None or not game_thread.is_alive():
        game_thread = threading.Thread(target=game_logic.guess_the_number, args=(difficulty,))
        game_thread.start()

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Почати гру':
        difficulty = "easy" if values["-EASY-"] else "medium"
        start_game(difficulty)

window.close()
 
