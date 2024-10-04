from os import W_OK
from config import QUIZ_TABLE, config
from utils import Color, Header
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import text, create_engine
import random
import secrets
import paramiko
from hashlib import sha256
from itertools import chain
from handlers import new,resume
import time
import datetime
import click

def mainmenu():
    play_mode = get_play_mode()
    reset_buzzer_blocked()
    actions = {
        "n": ("Neues Quiz", new.run),
        "l": ("Liste alle Spieler auf", index_players_by_id),
        "c": ("Runde fortsetzen", resume.run),
        "z": ("Aktuelles Quiz zurücksetzen", reset_player_points),
        "i": ("Ranking anzeigeng", ranking),
        "t": ("Turnier anzeigen", index_players_of_all_rounds),
        "m": ("Monitoranzeige ändern", set_monitor_round),
        "h": ("Hilfe / Tastenbelegung", help),
        "p": ("Spielmodus ändern", change_play_mode),
        "x": ("Exit", lambda: exit()),
    }
    print(Header("MAIN MENU"))
    print(f"\n\tAktueller Spielmodus: {Color.GREEN}{play_mode}{Color.BLUE}\n\t[ 1 = 16 Spieler / 2 = 12 Spieler / 3 = 8 Spieler(Duelle) ]\n")

    for key, action in actions.items():
        description, _ = action
        print(f"\t[ {Color.MAGENTA}{key}{Color.BLUE} ] {description}")

    print("\nWähle eine Option: ")
    key = click.getchar()
    if key in actions:
        _, handler = actions[key]
        handler.__call__()

    mainmenu()

def help():
    print("\tsome help with controls and keyboard shortcuts...")
    print(f"\tkeyboard shortcuts:\n")
    print("\tin game mode press for correct answer player 1,2,3,4:")
    print(f"\t({Color.GREEN} 1 2 3 4 {Color.BLUE})")
    print("\n\tpress for wrong answer for player 1,2,3,4:")
    print(f"\t({Color.RED} q w e r {Color.BLUE})")
    print(f"\n\tpress {Color.WHITE}s{Color.BLUE} for skip question.")
    print(f"\tpress {Color.WHITE}l{Color.BLUE} for leave round, points will be saved\n")
    print("\tyou can zero all points without changing names.")
    print("\tby changing ALL NAMES all points will be zeroed and questions will be marked unplayed!")

def change_play_mode():
    print("\tWelchen Spielmodus setzen?\n\t[ 1 = 16 Spieler / 2 = 12 Spieler / 3 = 8 Spieler(Duelle) ]: \n\t ALLE SPIELSTÄNDE WERDEN GENULLT!")
    play_mode = click.getchar()
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update config set value = {play_mode} where name ='play_mode'"))
    connection.commit()
    connection.close()
    if play_mode == "1":
        set_round_four_normal()
    if play_mode == "2":
        set_round_four_playoff()
        get_play_off_players_to_round()
    reset_player_points()

def change_play_mode_silent(play_mode):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update config set value = {play_mode} where name ='play_mode'"))
    connection.commit()
    connection.close()
    if play_mode == 1:
        print("set round 4 normal")
        set_round_four_normal()
    if play_mode == 2:
        print("set round 4 playoff")
        set_round_four_playoff()
        print("get play off players to round")
        get_play_off_players_to_round()
    reset_player_points_silent()

def reset_player_points():
    print("\tDas aktuelle Quiz zurücksetzen? (y/n): ")
    action = click.getchar()
    if action == "y":
        engine = connect(QUIZ_TABLE)
        connection = engine.connect()
        connection.execute(text(f"update player_round set points = 0"))
        connection.commit()
        play_mode = get_play_mode()
        if play_mode == "1" or play_mode == 1:
            connection.execute(text(f"update player_round set player = 13 where id = 13"))
            connection.execute(text(f"update player_round set player = 14 where id = 14"))
            connection.execute(text(f"update player_round set player = 15 where id = 15"))
            connection.execute(text(f"update player_round set player = 16 where id = 16"))
            connection.execute(text(f"update player_round set player = 1 where id = 17"))
            connection.execute(text(f"update player_round set player = 5 where id = 18"))
            connection.execute(text(f"update player_round set player = 10 where id = 19"))
            connection.execute(text(f"update player_round set player = 14 where id = 20"))
            connection.execute(text(f"update player_round set player = 9 where id = 21"))
            connection.execute(text(f"update player_round set player = 13 where id = 22"))
            connection.execute(text(f"update player_round set player = 2 where id = 23"))
            connection.execute(text(f"update player_round set player = 6 where id = 24"))
            connection.execute(text(f"update player_round set player = 1 where id = 25"))
            connection.execute(text(f"update player_round set player = 9 where id = 26"))
            connection.execute(text(f"update player_round set player = 5 where id = 27"))
            connection.execute(text(f"update player_round set player = 13 where id = 28"))
            connection.execute(text(f"update player_round set player = 1 where id = 29"))
            connection.commit()
        if play_mode == "2" or play_mode == 2:
            connection.execute(text(f"update player_round set player = 3 where id = 13"))
            connection.execute(text(f"update player_round set player = 7 where id = 14"))
            connection.execute(text(f"update player_round set player = 11 where id = 15"))
            connection.execute(text(f"update player_round set player = 4 where id = 16"))
            connection.execute(text(f"update player_round set player = 1 where id = 17"))
            connection.execute(text(f"update player_round set player = 5 where id = 18"))
            connection.execute(text(f"update player_round set player = 10 where id = 19"))
            connection.execute(text(f"update player_round set player = 7 where id = 20"))
            connection.execute(text(f"update player_round set player = 9 where id = 21"))
            connection.execute(text(f"update player_round set player = 3 where id = 22"))
            connection.execute(text(f"update player_round set player = 2 where id = 23"))
            connection.execute(text(f"update player_round set player = 6 where id = 24"))
            connection.execute(text(f"update player_round set player = 1 where id = 25"))
            connection.execute(text(f"update player_round set player = 9 where id = 26"))
            connection.execute(text(f"update player_round set player = 5 where id = 27"))
            connection.execute(text(f"update player_round set player = 13 where id = 28"))
            connection.execute(text(f"update player_round set player = 1 where id = 29"))
            connection.commit()
        connection.commit()
        connection.execute(text(f"update questions set played = 0"))
        connection.commit()
        connection.execute(text(f"update last_question set question ='', artist='', year = ''"))
        connection.commit()
        connection.execute(text(f"update config set value = 0 where name ='monitor_round'"))
        connection.commit()
        connection.execute(text(f"update config set value = 0 where name ='buzzer_blocked'"))
        connection.commit()
        connection.execute(text(f"update player_round set is_active = 1"))
        connection.commit()
        connection.close()

def reset_player_points_silent():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update player_round set points = 0"))
    connection.commit()
    play_mode = get_play_mode()
    if play_mode == "1" or play_mode == 1:
        connection.execute(text(f"update player_round set player = 13 where id = 13"))
        connection.execute(text(f"update player_round set player = 14 where id = 14"))
        connection.execute(text(f"update player_round set player = 15 where id = 15"))
        connection.execute(text(f"update player_round set player = 16 where id = 16"))
        connection.execute(text(f"update player_round set player = 1 where id = 17"))
        connection.execute(text(f"update player_round set player = 5 where id = 18"))
        connection.execute(text(f"update player_round set player = 10 where id = 19"))
        connection.execute(text(f"update player_round set player = 14 where id = 20"))
        connection.execute(text(f"update player_round set player = 9 where id = 21"))
        connection.execute(text(f"update player_round set player = 13 where id = 22"))
        connection.execute(text(f"update player_round set player = 2 where id = 23"))
        connection.execute(text(f"update player_round set player = 6 where id = 24"))
        connection.execute(text(f"update player_round set player = 1 where id = 25"))
        connection.execute(text(f"update player_round set player = 9 where id = 26"))
        connection.execute(text(f"update player_round set player = 5 where id = 27"))
        connection.execute(text(f"update player_round set player = 13 where id = 28"))
        connection.execute(text(f"update player_round set player = 1 where id = 29"))
        connection.commit()
    if play_mode == "2" or play_mode == 2:
        # get_play_off_players_to_round()
        connection.execute(text(f"update player_round set player = 3 where id = 13"))
        connection.execute(text(f"update player_round set player = 7 where id = 14"))
        connection.execute(text(f"update player_round set player = 11 where id = 15"))
        connection.execute(text(f"update player_round set player = 4 where id = 16"))
        connection.execute(text(f"update player_round set player = 1 where id = 17"))
        connection.execute(text(f"update player_round set player = 5 where id = 18"))
        connection.execute(text(f"update player_round set player = 10 where id = 19"))
        connection.execute(text(f"update player_round set player = 7 where id = 20"))
        connection.execute(text(f"update player_round set player = 9 where id = 21"))
        connection.execute(text(f"update player_round set player = 3 where id = 22"))
        connection.execute(text(f"update player_round set player = 2 where id = 23"))
        connection.execute(text(f"update player_round set player = 6 where id = 24"))
        connection.execute(text(f"update player_round set player = 1 where id = 25"))
        connection.execute(text(f"update player_round set player = 9 where id = 26"))
        connection.execute(text(f"update player_round set player = 5 where id = 27"))
        connection.execute(text(f"update player_round set player = 13 where id = 28"))
        connection.execute(text(f"update player_round set player = 1 where id = 29"))
        connection.commit()
    connection.commit()
    connection.execute(text(f"update questions set played = 0"))
    connection.commit()
    connection.execute(text(f"update last_question set question ='', answer=''"))
    connection.commit()
    connection.execute(text(f"update config set value = 0 where name ='monitor_round'"))
    connection.commit()
    connection.execute(text(f"update config set value = 0 where name ='buzzer_blocked'"))
    connection.commit()
    connection.execute(text(f"update player_round set is_active = 1"))
    connection.commit()
    connection.close()
    print("reset player points silent")


def set_round_four_normal():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update player_round set player = 13 where id = 13"))
    connection.execute(text(f"update player_round set player = 14 where id = 14"))
    connection.execute(text(f"update player_round set player = 15 where id = 15"))
    connection.execute(text(f"update player_round set player = 16 where id = 16"))
    connection.execute(text(f"update round set round = 'Vorrunde 4' where id = 4"))
    connection.commit()
    connection.close()

def set_round_four_playoff():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update play_off set player = 3, points = 0 where id =1"))
    connection.execute(text(f"update play_off set player = 4, points = 0 where id =2"))
    connection.execute(text(f"update play_off set player = 7, points = 0 where id =3"))
    connection.execute(text(f"update play_off set player = 8, points = 0 where id =4"))
    connection.execute(text(f"update play_off set player = 11, points = 0 where id =5"))
    connection.execute(text(f"update play_off set player = 12, points = 0 where id =6"))
    connection.execute(text(f"update round set round = 'Playoff' where id = 4"))
    connection.commit()
    connection.close()

def countdown():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(text("SELECT value FROM config WHERE name = 'final_date'"))
    for row in result:
        final_date = row.value
    connection.close()
    final_date = datetime.datetime.strptime(final_date, "%b %d %Y %H:%M:%S")

    nowdate = datetime.datetime.now()
    count = int((final_date - nowdate).total_seconds())
    class Countdown:
        days: int
        hours: str
        minutes: str
        seconds: str
        daytext: str

    countdown = Countdown()

    countdown.days = count//86400
    countdown.hours = str((count-int(countdown.days)*86400)//3600).zfill(2)
    countdown.minutes = str((count-int(countdown.days)*86400-int(countdown.hours)*3600)//60).zfill(2)
    countdown.seconds = str(count-int(countdown.days)*86400-int(countdown.hours)*3600-int(countdown.minutes)*60).zfill(2)
    countdown.daytext = f"noch {countdown.days} Tage und"


    if countdown.days == 0:
       countdown.daytext = "HEUTE in"
    print(f"\tnoch {countdown.days} Tage : {countdown.hours} Stunden : {countdown.minutes} Minuten : {countdown.seconds} Sekunden...")
    return countdown

def new_player_names():
    print("\tSpieler in welchem Modus eingeben? ( 1 / 2 )\n\t(1= Gruppe 1   →   Gruppe 2   →   Gruppe 3   →   Gruppe 4\n\t    Spieler 1  →   Spieler 1  →   Spieler 1  →   Spieler 1\n\t    Spieler 2  →   Spieler 2  →   Spieler 2  →   Spieler 2)")
    print("\t(2= Gruppe 1  ↓\n\t    Spieler 1 ↓\n\t    Spieler 2 ↓\n\t    Spieler 3 ↓\n\t    Spieler 4 ↓\n\t    Gruppe 2  ↓\n\t    Spieler 1 ↓\n\t    Spieler 2 ↓)")
    action = click.getchar()
    if action == "1":
        print("player names maximum 13 characters! \n")
        play_mode = get_play_mode()
        player_1_name = input("\t1. Vorrunde Spieler 1\n\t")
        update_player_name(1,player_1_name)
        player_2_name = input("\t2. Vorrunde Spieler 1\n\t")
        update_player_name(5,player_2_name)
        player_3_name = input("\t3. Vorrunde Spieler 1\n\t")
        update_player_name(9,player_3_name)
        if play_mode == "1":
            player_4_name = input("\t4. Vorrunde Spieler 1\n\t")
            update_player_name(13,player_4_name)
        player_5_name = input("\n\t1. Vorrunde Spieler 2\n\t")
        update_player_name(2,player_5_name)
        player_6_name = input("\t2. Vorrunde Spieler 2\n\t")
        update_player_name(6,player_6_name)
        player_7_name = input("\t3. Vorrunde Spieler 2\n\t")
        update_player_name(10,player_7_name)
        if play_mode == "1":
            player_8_name = input("\t4. Vorrunde Spieler 2\n\t")
            update_player_name(14,player_8_name)
        player_9_name = input("\n\t1. Vorrunde Spieler 3\n\t")
        update_player_name(3,player_9_name)
        player_10_name = input("\t2. Vorrunde Spieler 3\n\t")
        update_player_name(7,player_10_name)
        player_11_name = input("\t3. Vorrunde Spieler 3\n\t")
        update_player_name(11,player_11_name)
        if play_mode == "1":
            player_12_name = input("\t4. Vorrunde Spieler 3\n\t")
            update_player_name(15,player_12_name)
        player_13_name = input("\n\t1. Vorrunde Spieler 4\n\t")
        update_player_name(4,player_13_name)
        player_14_name = input("\t2. Vorrunde Spieler 4\n\t")
        update_player_name(8,player_14_name)
        player_15_name = input("\t3. Vorrunde Spieler 4\n\t")
        update_player_name(12,player_15_name)
        if play_mode == "1":
            player_16_name = input("\t4. Vorrunde Spieler 4\n\t")
            update_player_name(16,player_16_name)
    if action == "2":
        print("player names maximum 13 characters! \n")
        play_mode = get_play_mode()
        player_1_name = input("\t1. Vorrunde Spieler 1\n\t")
        update_player_name(1,player_1_name)
        player_2_name = input("\t1. Vorrunde Spieler 2\n\t")
        update_player_name(2,player_2_name)
        player_3_name = input("\t1. Vorrunde Spieler 3\n\t")
        update_player_name(3,player_3_name)
        if play_mode == "1":
            player_4_name = input("\t1. Vorrunde Spieler 4\n\t")
            update_player_name(4,player_4_name)
        player_5_name = input("\n\t2. Vorrunde Spieler 1\n\t")
        update_player_name(5,player_5_name)
        player_6_name = input("\t2. Vorrunde Spieler 2\n\t")
        update_player_name(6,player_6_name)
        player_7_name = input("\t2. Vorrunde Spieler 3\n\t")
        update_player_name(7,player_7_name)
        if play_mode == "1":
            player_8_name = input("\t2. Vorrunde Spieler 4\n\t")
            update_player_name(8,player_8_name)
        player_9_name = input("\n\t3. Vorrunde Spieler 1\n\t")
        update_player_name(9,player_9_name)
        player_10_name = input("\t3. Vorrunde Spieler 2\n\t")
        update_player_name(10,player_10_name)
        player_11_name = input("\t3. Vorrunde Spieler 3\n\t")
        update_player_name(11,player_11_name)
        if play_mode == "1":
            player_12_name = input("\t3. Vorrunde Spieler 4\n\t")
            update_player_name(12,player_12_name)
        player_13_name = input("\n\t4. Vorrunde Spieler 1\n\t")
        update_player_name(13,player_13_name)
        player_14_name = input("\t4. Vorrunde Spieler 2)\n\t")
        update_player_name(14,player_14_name)
        player_15_name = input("\t4. Vorrunde Spieler 3\n\t")
        update_player_name(15,player_15_name)
        if play_mode == "1":
            player_16_name = input("\t4. Vorrunde Spieler 4\n\t")
            update_player_name(16,player_16_name)

    reset_player_points()

def reset_buzzer_blocked():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update config set value = 0 where name ='buzzer_blocked'"))
    connection.commit()
    connection.close()


def show_points(round_id):
    class Points:

        round_id: int
        round_name: str
        player_1_points: str
        player_2_points: str
        player_3_points: str
        player_4_points: str
        player_1_name: str
        player_2_name: str
        player_3_name: str
        player_4_name: str
        global_player_id_1: int
        global_player_id_2: int
        global_player_id_3: int
        global_player_id_4: int
        player_1_state: int
        player_2_state: int
        player_3_state: int
        player_4_state: int
        points_to_play: int

    points = Points()

    points.round_name = get_round_name(round_id)
    points.player_1_points = str(get_player_points(1,round_id)).zfill(2)
    points.player_2_points = str(get_player_points(2,round_id)).zfill(2)
    points.player_3_points = str(get_player_points(3,round_id)).zfill(2)
    points.player_4_points = str(get_player_points(4,round_id)).zfill(2)
    points.player_1_name = get_player_name(1,round_id)
    points.player_2_name = get_player_name(2,round_id)
    points.player_3_name = get_player_name(3,round_id)
    points.player_4_name = get_player_name(4,round_id)
    points.global_player_id_1 = get_global_player_id(1,round_id)
    points.global_player_id_2 = get_global_player_id(2,round_id)
    points.global_player_id_3 = get_global_player_id(3,round_id)
    points.global_player_id_4 = get_global_player_id(4,round_id)
    points.player_1_state = get_player_state(1,round_id)
    points.player_2_state = get_player_state(2,round_id)
    points.player_3_state = get_player_state(3,round_id)
    points.player_4_state = get_player_state(4,round_id)
    points.points_to_play = get_points_to_play(round_id)

    return points

def set_buzzer_blocked(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    player_1_state = get_player_state(1,round_id)
    player_2_state = get_player_state(2,round_id)
    player_3_state = get_player_state(3,round_id)
    player_4_state = get_player_state(4,round_id)
    # print(player_1_state,player_2_state,player_3_state,player_4_state)
    if int(player_1_state) == 0:
        # print("player 1 blocked")
        connection.execute(text(f"update config set value = 1 where name = 'buzzer_blocked'"))
        connection.commit()
    if int(player_2_state) == 0:
        # print("player 2 blocked")
        connection.execute(text(f"update config set value = 2 where name = 'buzzer_blocked'"))
        connection.commit()
    if int(player_3_state) == 0:
        # print("player 3 blocked")
        connection.execute(text(f"update config set value = 3 where name = 'buzzer_blocked'"))
        connection.commit()
    if int(player_4_state) == 0:
        # print("player 4 blocked")
        connection.execute(text(f"update config set value = 4 where name = 'buzzer_blocked'"))
        connection.commit()
    connection.close()

def get_buzzer_blocked():
    buzzer_blocked = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(text(f"select value from config where name = 'buzzer_blocked'"))
    for row in result:
        buzzer_blocked = row.value
    connection.close()
    return buzzer_blocked

def update_player_name(global_player_id,player_name):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(
        text(f"update player set name = '{player_name}' where id = {global_player_id}"))
    connection.commit()
    connection.close()

def get_monitor_round():
    round_id = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(text(f"select value from config where name = 'monitor_round'"))
    for row in result:
        round_id = row.value
    connection.close()
    round_id = int(round_id)
    return round_id

def get_player_color(player_id,round_id):
    player_color = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(text(f"select color from player_round where player_round_id = {player_id} and round = {round_id}"))
    for row in result:
        player_color = row.color
    connection.close()
    return player_color

def get_player_state(player_id,round_id):
    player_state = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(text(f"select is_active from player_round where player_round_id = {player_id} and round = {round_id}"))
    for row in result:
        player_state = row.is_active
    connection.close()
    return player_state

def set_monitor_round():
    round_id = choose_round()
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update config set value = {round_id} where name = 'monitor_round'"))
    connection.commit()
    connection.close()

def set_monitor_round_by_round_id(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update config set value = {round_id} where name = 'monitor_round'"))
    connection.commit()
    connection.close()

def set_last_question(question,answer):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update last_question set question = '{question}'"))
    connection.commit()
    connection.execute(text(f"update last_question set answer = '{answer}'"))
    connection.commit()
    connection.close()


def index_players_of_round(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select player.name, points from player_round inner join player on player_round.player = player.id where round = {round_id}"))
    players = []
    round_name = get_round_name(round_id)
    print(f"\n{Color.MAGENTA}{round_name}{Color.BLUE}")
    print(f"-"*20)
    for row in result:
        name = row.name
        points = row.points
        spacer=20-len(name)-len(str(points))-6
        print(f"{name}"," "*spacer,f"[ {points} ]")
    connection.close()
    return players

def get_play_mode():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    play_mode = 1
    result = connection.execute(text("select value from config where name = 'play_mode'"))
    for row in result:
        play_mode = row.value
    connection.close()
    return play_mode


def get_round_info(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text("select id, name from player order by id"))
    players = []
    for row in result:
        id = row.id
        name = row.name
        print(
            "\t[ {:<4s} ] {:<20s}".format(f"{Color.MAGENTA}{id}{Color.BLUE}", name))
        players.append({"\tid": f"{id}", "name": f"{name}"})
    connection.close()
    return players

def get_next_question(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select id,question, answer, seq from questions where round = {round_id} and played = 0 order by seq asc limit 1"))
    next_question = {}
    for row in result:
        next_question["id"] = row.id
        next_question["question"] = row.question
        next_question["answer"] = row.answer
        next_question["seq"] = row.seq
    result = connection.execute(text(f"select * from questions where round = {round_id}"))
    next_question["total"] = result.rowcount
    connection.close()
    return next_question

def get_points_to_play(round_id):
    next_question = get_next_question(round_id)
    maximum = get_round_maximum_questions(round_id)
    get_seq = next_question.get("seq",0)
    points_to_go = 0
    # for debugging:
    # print(f"points to go: {points_to_go}")
    # print(f"get_seq: {get_seq}")
    # print(f"maximum: {maximum}")
    if (get_seq > maximum) or (get_seq == 0):
        points_to_go = "--"
    else:
        points_to_go = (maximum - (get_seq-1))*2
    return points_to_go

def get_last_question():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select question, answer from last_question"))
    last_question = {}
    for row in result:
        last_question["question"] = row.question
        last_question["answer"] = row.answer
    connection.close()
    return last_question


def mark_question_as_played(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(
        text(f"update questions set played = 1 where round = {round_id} and played = 0 order by seq asc limit 1"))
    connection.commit()
    connection.close()


def choose_round():
    index_rounds()
    print("\tEnter the round id: ")
    round_id = click.getchar()
    print(f"round id is {round_id}")
    return round_id

def get_round_name(round_id):
    round_name = "nothing"
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select round from round where id = {round_id}"))
    for row in result:
        round_name = row.round
    connection.close()
    return round_name

def get_global_player_id(player_id,round_id):
    global_player_id = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select player from player_round where player_round_id = {player_id} and round = {round_id}"))
    for row in result:
        global_player_id = row.player
    connection.close()
    return global_player_id


def get_player_points(player_id,round_id):
    points = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select points from player_round where player_round_id = {player_id} and round = {round_id}"))
    for row in result:
        points = row.points
    connection.close()
    return points

def get_player_name(player_id,round_id):
    name = 0
    global_player_id = get_global_player_id(player_id,round_id)
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select name from player where id = {global_player_id}"))
    for row in result:
        player_name = row.name
    connection.close()
    return player_name

def get_player_name_from_global_id(global_player_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select name from player where id = {global_player_id}"))
    for row in result:
        player_name = row.name
    connection.close()
    return player_name

def index_players():
    actions = {
        "z": ("Spieler nach Eintragung anzeigen",index_players_by_id),
        "h": ("Alle Spieler aller Runden anzeigen",index_players_of_all_rounds),
        "x": ("Hauptmenu", mainmenu)
    }
    for key, action in actions.items():
        description, _ = action
        print(f"\t[ {Color.MAGENTA}{key}{Color.BLUE} ] {description}")

    print("\n\tWähle eine Option: ")
    key = click.getchar()
    if key in actions:
        _, handler = actions[key]
        handler.__call__()

def index_players_of_all_rounds():
    rounds = [1,2,3,4,5,6,7]
    play_mode = get_play_mode()
    if play_mode == "2":
        get_play_off_players_to_round()
    for round in rounds:
        index_players_of_round(round)
    mainmenu()

def show_tournament_results():
    round_1 = get_round_name(1)
    round_2 = get_round_name(2)
    round_3 = get_round_name(3)
    round_4 = get_round_name(4)
    round_5 = get_round_name(5)
    round_6 = get_round_name(6)
    round_7 = get_round_name(7)
    spacer="          "
    char_count = len(round_1)+len(round_5)+len(round_5)+len(spacer)+len(spacer)
    char_count = char_count
    print(f"\n{round_1}{spacer}{round_5}{spacer}{round_7}")
    print(f"-"*char_count)
    print(f"{round_2}{spacer}{round_6}")
    print(f"-"*char_count)
    print(f"{round_3}")
    print(f"-"*char_count)
    print(f"{round_4}")

def index_players_by_id():
    play_mode = get_play_mode()
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    if play_mode == "1":
        result = connection.execute(
            text(f"select id, name from player order by id"))
    if play_mode == "2":
        result = connection.execute(
            text(f"select id, name from player where id < 13 order by id"))
    if play_mode == "3":
        result = connection.execute(
            text(f"select id, name from player where id < 9 order by id"))
    players = []
    for row in result:
        id = row.id
        name = row.name
        print(f"\t[{id}] {name}")
    connection.close()
    return players

def index_rounds():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text("select id, round from round order by id"))
    rounds = []
    for row in result:
        id = row.id
        round = row.round
        print(
            "\t[ {:<4s} ] {:<20s}".format(f"{Color.MAGENTA}{id}{Color.BLUE}", round))
        rounds.append({"\tid": f"{id}", "name": f"{round}"})
    connection.close()
    return rounds

def ranking():
    print("Bitte Runden ID angeben: ")
    round_id = click.getchar()
    round_ranking(round_id)
    sort_ranking(round_id)
    sort_ranking_playoff(round_id)

def round_ranking(round_id):
    ranks = {
        get_player_name(1,round_id):get_player_points(1,round_id),
        get_player_name(2,round_id):get_player_points(2,round_id),
        get_player_name(3,round_id):get_player_points(3,round_id),
        get_player_name(4,round_id):get_player_points(4,round_id)
    }
    ranks = dict(sorted(ranks.items(), key=lambda item: item[1], reverse=True))
    print(f"\t{Color.MAGENTA} Ranking\n{Color.BLUE}")
    print("\t-----------------")
    for key in ranks:
        print(f"\t{key} : {ranks[key]}")
    print("\t-----------------")
    keys = list(ranks)
    return ranks

def sort_ranking(round_id):
    ranks = {
    get_global_player_id(1,round_id):get_player_points(1,round_id),
    get_global_player_id(2,round_id):get_player_points(2,round_id),
    get_global_player_id(3,round_id):get_player_points(3,round_id),
    get_global_player_id(4,round_id):get_player_points(4,round_id)
    }
    ranks = dict(sorted(ranks.items(), key=lambda item: item[1], reverse=True))
    keys = list(ranks)
    round_id = int(round_id)

    if round_id == 1:
        update_final_round(1,5,keys[0])
        update_final_round(3,6,keys[1])
    if round_id == 2:
        update_final_round(2,5,keys[0])
        update_final_round(4,6,keys[1])
    if round_id == 3:
        update_final_round(1,6,keys[0])
        update_final_round(3,5,keys[1])
    if round_id == 4:
        update_final_round(2,6,keys[0])
        update_final_round(4,5,keys[1])
    if round_id == 5:
        update_final_round(1,7,keys[0])
        update_final_round(3,7,keys[1])
    if round_id == 6:
        update_final_round(2,7,keys[0])
        update_final_round(4,7,keys[1])
    if round_id == 7:
        update_final_round(1,8,keys[0])

def sort_ranking_playoff(round_id):
    print(f"sorting playoffs for round {round_id}")
    ranks = {
    get_global_player_id(1,round_id):get_player_points(1,round_id),
    get_global_player_id(2,round_id):get_player_points(2,round_id),
    get_global_player_id(3,round_id):get_player_points(3,round_id),
    get_global_player_id(4,round_id):get_player_points(4,round_id)
    }
    ranks = dict(sorted(ranks.items(), key=lambda item: item[1], reverse=True))
    keys = list(ranks)
    round_id = int(round_id)

    if round_id == 1:
        play_off_round_id = 4
        final_player_id_first = 1
        final_player_id_second = 2
        update_playoff_round(1,keys[2],ranks[keys[2]])
        update_playoff_round(4,keys[3],ranks[keys[3]])
    if round_id == 2:
        play_off_round_id = 4
        final_player_id_first = 3
        final_player_id_second = 4
        update_playoff_round(2,keys[2],ranks[keys[2]])
        update_playoff_round(5,keys[3],ranks[keys[3]])
    if round_id == 3:
        play_off_round_id = 4
        final_player_id_first = 5
        final_player_id_second = 6
        update_playoff_round(3,keys[2],ranks[keys[2]])
        update_playoff_round(6,keys[3],ranks[keys[3]])
    if round_id == 5:
        update_final_round(1,7,keys[0])
        update_final_round(3,7,keys[1])
    if round_id == 6:
        update_final_round(2,7,keys[0])
        update_final_round(4,7,keys[1])
    if round_id == 7:
        final_round_id = 8
        final_player_id_first = 1
        update_final_round(final_player_id_first,final_round_id,keys[0])

def get_play_off_players_to_round():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(text("select player, points from play_off"))
    play_off_ranking = {}
    for row in result:
        play_off_ranking[row.player] = row.points
    connection.close()
    rank = dict(sorted(play_off_ranking.items(), key=lambda item: item[1], reverse=True))
    keys = list(rank)

    update_final_round(1,4,keys[0])
    update_final_round(2,4,keys[1])
    update_final_round(3,4,keys[2])
    update_final_round(4,4,keys[3])

    return play_off_ranking

def update_final_round(player_id,round_id,global_player_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update player_round set player = '{global_player_id}' where player_round_id = {player_id} and round = {round_id}"))
    connection.commit()
    connection.close()

def update_playoff_round(player_id,global_player_id,points):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update play_off set player = '{global_player_id}', points = '{points}' where id = {player_id}"))
    connection.commit()
    connection.close()

def show_scoreboard(buzzer_blocked,player_1_name,player_2_name,player_3_name,player_4_name,player_1_points,player_2_points,player_3_points,player_4_points):
    if buzzer_blocked == 0:
        print(f"\t[ {player_1_name} : {Color.MAGENTA}{player_1_points}{Color.BLUE} ]",
            f"\t[ {player_2_name} : {Color.MAGENTA}{player_2_points}{Color.BLUE} ]"
            f"\t[ {player_3_name} : {Color.MAGENTA}{player_3_points}{Color.BLUE} ]"
            f"\t[ {player_4_name} : {Color.MAGENTA}{player_4_points}{Color.BLUE} ]",
        )
    if buzzer_blocked == 1:
        print(f"\t{Color.RED}[ {player_1_name} : {player_1_points} ]{Color.BLUE}",
            f"\t[ {player_2_name} : {Color.MAGENTA}{player_2_points}{Color.BLUE} ]",
            f"\t[ {player_3_name} : {Color.MAGENTA}{player_3_points}{Color.BLUE} ]",
            f"\t[ {player_4_name} : {Color.MAGENTA}{player_4_points}{Color.BLUE} ]",
        )
    if buzzer_blocked == 2:
        print(f"\t[ {player_1_name} : {Color.MAGENTA}{player_1_points}{Color.BLUE} ]",
            f"\t{Color.RED}[ {player_2_name} : {player_2_points} ]{Color.BLUE}",
            f"\t[ {player_3_name} : {Color.MAGENTA}{player_3_points}{Color.BLUE} ]",
            f"\t[ {player_4_name} : {Color.MAGENTA}{player_4_points}{Color.BLUE} ]",
        )
    if buzzer_blocked == 3:
        print(f"\t[ {player_1_name} : {Color.MAGENTA}{player_1_points}{Color.BLUE} ]",
            f"\t[ {player_2_name} : {Color.MAGENTA}{player_2_points}{Color.BLUE} ]",
            f"\t{Color.RED}[ {player_3_name} : {player_3_points} ]{Color.BLUE}",
            f"\t[ {player_4_name} : {Color.MAGENTA}{player_4_points}{Color.BLUE} ]",
        )
    if buzzer_blocked == 4:
        print(f"\t[ {player_1_name} : {Color.MAGENTA}{player_1_points}{Color.BLUE} ]",
            f"\t[ {player_2_name} : {Color.MAGENTA}{player_2_points}{Color.BLUE} ]",
            f"\t[ {player_3_name} : {Color.MAGENTA}{player_3_points}{Color.BLUE} ]",
            f"\t{Color.RED}[ {player_4_name} : {player_4_points} ]{Color.BLUE}",
        )

def play_mode1(round_id):
    actions = {
        "q": ("player 1 correct", update_player),
        "w": ("player 2 correct", update_player),
        "e": ("player 3 correct", update_player),
        "r": ("player 4 correct", update_player),
        "a": ("player 1 fault", update_player),
        "s": ("player 2 fault", update_player),
        "d": ("player 3 fault", update_player),
        "f": ("player 4 fault", update_player),
        "k": ("skip question", update_player),
        "l": ("leave game" , mainmenu),
    }
    round_name = get_round_name(round_id)
    print(f"\n\t{Color.MAGENTA}{round_name}\n{Color.BLUE}")
    maximum = get_round_maximum_questions(round_id)
    set_monitor_round_by_round_id(round_id)

    next_question = {}
    next_question = get_next_question(round_id)
    points_to_play = get_points_to_play(round_id)

    player_1_points = get_player_points(1,round_id)
    player_2_points = get_player_points(2,round_id)
    player_3_points = get_player_points(3,round_id)
    player_4_points = get_player_points(4,round_id)
    player_1_name = get_player_name(1,round_id)
    player_2_name = get_player_name(2,round_id)
    player_3_name = get_player_name(3,round_id)
    player_4_name = get_player_name(4,round_id)
    global_player_id_1 = get_global_player_id(1,round_id)
    global_player_id_2 = get_global_player_id(2,round_id)
    global_player_id_3 = get_global_player_id(3,round_id)
    global_player_id_4 = get_global_player_id(4,round_id)

    set_buzzer_blocked(round_id)
    buzzer_blocked = get_buzzer_blocked()
    buzzer_blocked = int(buzzer_blocked)
    show_scoreboard(buzzer_blocked,player_1_name,player_2_name,player_3_name,player_4_name,player_1_points,player_2_points,player_3_points,player_4_points)
    print(f"\n\t{Color.YELLOW}[ Frage# {next_question.get("seq",0)} / {maximum} ({next_question['total']}) ]{Color.MAGENTA}\n\n\tFRAGE: {next_question.get("question","")}\n\tANTWORT:{next_question.get("answer","")}{Color.BLUE}")
    print(f"\n\t{Color.YELLOW}Points to play: {points_to_play}{Color.BLUE}\n")
    # key = input(print("\taction: "))
    key = click.getchar()
    if key in actions:
        _, handler = actions[key]
        if key == "q":
            handler.__call__(global_player_id_1,round_id,"correct")
        if key == "w":
            handler.__call__(global_player_id_2,round_id,"correct")
        if key == "e":
            handler.__call__(global_player_id_3,round_id,"correct")
        if key == "r":
            handler.__call__(global_player_id_4,round_id,"correct")
        if key == "a":
            handler.__call__(global_player_id_1,round_id,"false")
        if key == "s":
            handler.__call__(global_player_id_2,round_id,"false")
        if key == "d":
            handler.__call__(global_player_id_3,round_id,"false")
        if key == "f":
            handler.__call__(global_player_id_4,round_id,"false")
        if key == "k":
            handler.__call__(global_player_id_1,round_id,"skip")
        if key == "l":
            handler.__call__()
    sort_ranking(round_id)
    mark_question_as_played(round_id)
    set_last_question(next_question['question'],next_question['answer'])
    set_buzzer_blocked(round_id)

    if (next_question.get("seq",0) < maximum) and (next_question.get("seq",0) != 0):
        play_mode1(round_id)
    else:
        player_1_points = get_player_points(1,round_id)
        player_2_points = get_player_points(2,round_id)
        player_3_points = get_player_points(3,round_id)
        player_4_points = get_player_points(4,round_id)
        print()
        show_scoreboard(buzzer_blocked,player_1_name,player_2_name,player_3_name,player_4_name,player_1_points,player_2_points,player_3_points,player_4_points)
        print("\n\tMit Play-Off (Stechen) weitermachen? (y/n)")
        key = click.getchar()
        if next_question.get("seq",0) < next_question['total']:
            if key == "n":
                if round_id == "7":
                    set_monitor_to_winner()
                    mainmenu()
                else:
                    set_monitor_to_pause()
                    mainmenu()
            else:
                play_mode1(round_id)
        else:
            if round_id == "7":
                set_monitor_to_winner()
                mainmenu()
            else:
                set_monitor_to_pause()
                mainmenu()

def play_mode2(round_id):
    actions = {
        "q": ("player 1 correct", update_player),
        "w": ("player 2 correct", update_player),
        "e": ("player 3 correct", update_player),
        "r": ("player 4 correct", update_player),
        "a": ("player 1 fault", update_player),
        "s": ("player 2 fault", update_player),
        "d": ("player 3 fault", update_player),
        "f": ("player 4 fault", update_player),
        "k": ("skip song", update_player),
        "l": ("leave game" , mainmenu),
    }
    round_name = get_round_name(round_id)
    print(f"\n\t{Color.MAGENTA}{round_name}\n{Color.BLUE}")
    maximum = get_round_maximum_questions(round_id)
    set_monitor_round_by_round_id(round_id)

    next_question = {}
    next_question = get_next_question(round_id)
    points_to_play = get_points_to_play(round_id)

    player_1_points = get_player_points(1,round_id)
    player_2_points = get_player_points(2,round_id)
    player_3_points = get_player_points(3,round_id)
    player_4_points = get_player_points(4,round_id)
    player_1_name = get_player_name(1,round_id)
    player_2_name = get_player_name(2,round_id)
    player_3_name = get_player_name(3,round_id)
    player_4_name = get_player_name(4,round_id)
    global_player_id_1 = get_global_player_id(1,round_id)
    global_player_id_2 = get_global_player_id(2,round_id)
    global_player_id_3 = get_global_player_id(3,round_id)
    global_player_id_4 = get_global_player_id(4,round_id)

    set_buzzer_blocked(round_id)
    buzzer_blocked = get_buzzer_blocked()
    buzzer_blocked = int(buzzer_blocked)
    show_scoreboard(buzzer_blocked,player_1_name,player_2_name,player_3_name,player_4_name,player_1_points,player_2_points,player_3_points,player_4_points)
    print(f"\n\t{Color.YELLOW}[ Frage# {next_question.get("seq",0)} / {maximum} ({next_question['total']}) ]{Color.MAGENTA}\n\n\tFRAGE: {next_question.get("question","")}\n\tANTWORT:{next_question.get("answer","")}{Color.BLUE}")
    print(f"\n\t{Color.YELLOW}Points to play: {points_to_play}{Color.BLUE}\n")
    print("\taction: ")
    key = click.getchar()
    if key in actions:
        _, handler = actions[key]
        if key == "q":
            handler.__call__(global_player_id_1,round_id,"correct")
        if key == "w":
            handler.__call__(global_player_id_2,round_id,"correct")
        if key == "e":
            handler.__call__(global_player_id_3,round_id,"correct")
        if key == "r":
            handler.__call__(global_player_id_4,round_id,"correct")
        if key == "a":
            handler.__call__(global_player_id_1,round_id,"false")
        if key == "s":
            handler.__call__(global_player_id_2,round_id,"false")
        if key == "d":
            handler.__call__(global_player_id_3,round_id,"false")
        if key == "f":
            handler.__call__(global_player_id_4,round_id,"false")
        if key == "k":
            handler.__call__(global_player_id_1,round_id,"skip")
        if key == "l":
            handler.__call__()
    sort_ranking(round_id)
    if round_id != "4":
        sort_ranking_playoff(round_id)

    mark_question_as_played(round_id)
    set_last_question(next_question.get("question",""),next_question.get("answer",""))
    set_buzzer_blocked(round_id)
    get_play_off_players_to_round()

    if (next_question.get("seq",0) < maximum) and (next_question.get("seq",0) != 0):
        play_mode2(round_id)
    else:
        player_1_points = get_player_points(1,round_id)
        player_2_points = get_player_points(2,round_id)
        player_3_points = get_player_points(3,round_id)
        player_4_points = get_player_points(4,round_id)
        print()
        show_scoreboard(buzzer_blocked,player_1_name,player_2_name,player_3_name,player_4_name,player_1_points,player_2_points,player_3_points,player_4_points)
        print("\n\tMit Play-Off (Stechen) weitermachen? (y/n)")
        key = click.getchar()
        if next_question.get("seq",0) < next_question['total']:
            if key == "n":
                if round_id == "7":
                    set_monitor_to_winner()
                    mainmenu()
                else:
                    set_monitor_to_pause()
                    mainmenu()
            else:
                play_mode2(round_id)
        else:
            if round_id == "7":
                set_monitor_to_winner()
                mainmenu()
            else:
                set_monitor_to_pause()
                mainmenu()

def get_round_maximum_questions(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(text(f"select maximum from max_questions where round = '{round_id}'"))
    for row in result:
        maximum = row.maximum
    connection.close()
    return maximum

def set_monitor_to_pause():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text("update config set value = 9 where name ='monitor_round'"))
    connection.commit()
    connection.close()

def set_monitor_to_winner():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text("update config set value = 8 where name ='monitor_round'"))
    connection.commit()
    connection.close()

def update_player(player_id,round_id,action):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    if action == "correct":
        connection.execute(text(f"update player_round set points = points + 2 WHERE player = '{player_id}' AND round = '{round_id}'"))
        connection.execute(text(f"update player_round set is_active = 1 WHERE round = '{round_id}'"))
        connection.execute(text(f"update config set value = 0 WHERE name = 'buzzer_blocked'"))
        connection.commit()
        player_name = get_player_name_from_global_id(player_id)
        print(f"\tRichtige Antwort von {player_name}")
    if action == "false":
        connection.execute(text(f"update player_round set points = points + 2 WHERE player != '{player_id}' AND round = '{round_id}'"))
        connection.execute(text(f"update player_round set is_active = 0 WHERE player = '{player_id}' AND round = '{round_id}'"))
        connection.execute(text(f"update player_round set is_active = 1 WHERE player != '{player_id}' AND round = '{round_id}'"))
        connection.commit()
        player_name = get_player_name_from_global_id(player_id)
        print(f"\tFalsche Antwort von {player_name}")
    if action == "skip":
        connection.execute(text(f"update player_round set is_active = 1 WHERE round = '{round_id}'"))
        connection.execute(text(f"update config set value = 0 WHERE name = 'buzzer_blocked'"))
        connection.commit()
        print("\tskipped question")
    connection.close()

def connect(database):
    try:
        params = config()
        conn_string = f"{params['driver']}://{params['username']}:{params['password']}@{params['hostname']}:{params['port']}/{database}"
        engine = create_engine(conn_string)
        if not database_exists(engine.url):
            create_database(engine.url)
        return engine
    except:
        return print(f"Connection to {database} failed.")
