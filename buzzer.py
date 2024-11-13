from handlers import procs
import pygame
pygame.mixer.init()

while True:
    buzzer_pressed = procs.get_buzzer_pressed_from_serial()
    if buzzer_pressed == "0":
        print("BUZZER PLAYER 1 PRESSED")
        procs.media_pause()
        procs.play_buzzer()
        procs.set_buzzer_pressed("0")
    elif buzzer_pressed == "1":
        print("BUZZER PLAYER 2 PRESSED")
        procs.media_pause()
        procs.play_buzzer()
        procs.set_buzzer_pressed("1")
    elif buzzer_pressed == "2":
        print("BUZZER PLAYER 3 PRESSED")
        procs.media_pause()
        procs.play_buzzer()
        procs.set_buzzer_pressed("2")
    elif buzzer_pressed == "3":
        print("BUZZER PLAYER 4 PRESSED")
        procs.media_pause()
        procs.play_buzzer()
        procs.set_buzzer_pressed("3")