#!/usr/bin/python3
from flask import Flask, request, render_template
from handlers import procs
import os

app = Flask(__name__)

cwd = os.getcwd()
print(cwd)

@app.route('/')
def index():
    round_id = procs.get_monitor_round()
    last_song = procs.get_last_song()
    buzzer_blocked = procs.get_buzzer_blocked()
    countdown = procs.countdown()
    if round_id == 0:
        return render_template('start.html', countdown=countdown)
    if round_id == 9:
        return render_template('pause.html', last_song=last_song)
    if round_id == 8:
        player_name = procs.get_player_name(1,8)
        return render_template('end.html', player_name=player_name)
    else:
        points = procs.show_points(round_id)
        return render_template(f"index{buzzer_blocked}.html", points=points, last_song=last_song)

if __name__ == "__main__":
    app.run()
