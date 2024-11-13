#!/usr/bin/python3
from tkinter import Image
from flask import Flask, request, render_template
from handlers import procs
import os

app = Flask(__name__)

cwd = os.getcwd()
print(cwd)


@app.route('/')
def index():
    round_id = procs.get_play_round()
    monitor_round = procs.get_monitor_round()
    last_song = procs.get_last_song()
    buzzer_blocked = procs.get_buzzer_blocked()
    if int(buzzer_blocked) == 5:
        buzzer_blocked = 4
    countdown = procs.countdown()
    if monitor_round == 0:
        return render_template('start.html', countdown=countdown)
    if monitor_round == 9:
        return render_template('pause.html', last_song=last_song)
    if monitor_round == 8:
        player_name = procs.get_player_name(1,8)
        return render_template('end.html', player_name=player_name)
    if monitor_round == 11:
        return render_template('cover.html', last_song=last_song, cover=last_song['cover'], round=round_id)
        print("cover")
    else:
        points = procs.show_points(round_id)
        return render_template(f"index{buzzer_blocked}.html", points=points, last_song=last_song)
    procs.set_monitor_round_by_round_id(round_id)
    # print(f"set monitor to round {round_id}")

@app.route('/cover_last_song')
def cover_last_song():
    last_song = procs.get_last_song()
    return render_template('cover_last_song.html', last_song=last_song, cover=last_song['cover'])

if __name__ == "__main__":
    app.run()
