import os
import time
import datetime
import click
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import text, create_engine
import dbus
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from config import QUIZ_TABLE, config, ARDUINO_USE, ARDUINO_PORT, ARDUINO_BAUD 
import serial
from faker import Faker

# if arduino cant connect try this to find ttyACM* or ttyUSB* port: ls /dev/tty*
arduino = serial.Serial(ARDUINO_PORT, ARDUINO_BAUD, timeout=1)

def count_questions_by_round(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"SELECT COUNT(*) FROM questions WHERE round = {round_id}")
    )
    for row in result:
        count = row[0]
    connection.close()
    return count

def get_questions_for_round(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    questions = []
    result = connection.execute(text(f"SELECT id, question, answer, seq FROM questions WHERE round = {round_id} ORDER BY seq ASC"))
    for row in result:
        questions.append([row.id, row.seq, row.question, row.answer])
    connection.close()
    return questions

def change_play_mode_silent(play_mode):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(
        text(f"update config set value = {play_mode} where name ='play_mode'")
    )
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

# to remove?
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

# to remove?
def set_round_four_playoff():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update play_off set player = 3, points = 0 where id =1"))
    connection.execute(text(f"update play_off set player = 7, points = 0 where id =2"))
    connection.execute(text(f"update play_off set player = 11, points = 0 where id =3"))
    connection.execute(text(f"update play_off set player = 4, points = 0 where id =4"))
    connection.execute(text(f"update play_off set player = 8, points = 0 where id =5"))
    connection.execute(text(f"update play_off set player = 12, points = 0 where id =6"))
    connection.execute(text(f"update round set round = 'Playoff' where id = 4"))
    connection.commit()
    connection.close()


def countdown():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text("SELECT value FROM config WHERE name = 'final_date'")
    )
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

    countdown.days = count // 86400
    countdown.hours = str((count - int(countdown.days) * 86400) // 3600).zfill(2)
    countdown.minutes = str(
        (count - int(countdown.days) * 86400 - int(countdown.hours) * 3600) // 60
    ).zfill(2)
    countdown.seconds = str(
        count
        - int(countdown.days) * 86400
        - int(countdown.hours) * 3600
        - int(countdown.minutes) * 60
    ).zfill(2)
    countdown.daytext = f"noch {countdown.days} Tage und"

    if countdown.days == 0:
        countdown.daytext = "HEUTE in"
    print(
        f"\tnoch {countdown.days} Tage : {countdown.hours} Stunden : {countdown.minutes} Minuten : {countdown.seconds} Sekunden..."
    )
    return countdown


def play_correct():
    pygame.mixer.music.load("sounds/correct.mp3")
    pygame.mixer.music.play()


def play_wrong():
    pygame.mixer.music.load("sounds/wrong.mp3")
    pygame.mixer.music.play()

def play_buzzer():
    pygame.mixer.music.load("sounds/buzzer.mp3")
    pygame.mixer.music.play()


def play_clock():
    pygame.mixer.music.load("sounds/clock.mp3")
    pygame.mixer.music.play()


def play_hit():
    pygame.mixer.music.load("sounds/hit.mp3")
    pygame.mixer.music.play()


def generate_fake_names():
    FakeNames = []
    for i in range(16):
        fake = Faker('de_DE')
        FakeNames.append(fake.first_name())
    print(FakeNames)
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    for i in range(16):
        connection.execute(text(f"update player set name = '{FakeNames[i]}' where id = {i+1}"))
        connection.commit()
    connection.close() 

def new_player_names(
    player1,
    player2,
    player3,
    player4,
    player5,
    player6,
    player7,
    player8,
    player9,
    player10,
    player11,
    player12,
    player13,
    player14,
    player15,
    player16,
):
    update_player_name(1, player1)
    update_player_name(2, player2)
    update_player_name(3, player3)
    update_player_name(4, player4)
    update_player_name(5, player5)
    update_player_name(6, player6)
    update_player_name(7, player7)
    update_player_name(8, player8)
    update_player_name(9, player9)
    update_player_name(10, player10)
    update_player_name(11, player11)
    update_player_name(12, player12)
    update_player_name(13, player13)
    update_player_name(14, player14)
    update_player_name(15, player15)
    update_player_name(16, player16)
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
            connection.execute(
                text(f"update player_round set player = 13 where id = 13")
            )
            connection.execute(
                text(f"update player_round set player = 14 where id = 14")
            )
            connection.execute(
                text(f"update player_round set player = 15 where id = 15")
            )
            connection.execute(
                text(f"update player_round set player = 16 where id = 16")
            )
            connection.execute(
                text(f"update player_round set player = 1 where id = 17")
            )
            connection.execute(
                text(f"update player_round set player = 5 where id = 18")
            )
            connection.execute(
                text(f"update player_round set player = 10 where id = 19")
            )
            connection.execute(
                text(f"update player_round set player = 14 where id = 20")
            )
            connection.execute(
                text(f"update player_round set player = 9 where id = 21")
            )
            connection.execute(
                text(f"update player_round set player = 13 where id = 22")
            )
            connection.execute(
                text(f"update player_round set player = 2 where id = 23")
            )
            connection.execute(
                text(f"update player_round set player = 6 where id = 24")
            )
            connection.execute(
                text(f"update player_round set player = 1 where id = 25")
            )
            connection.execute(
                text(f"update player_round set player = 9 where id = 26")
            )
            connection.execute(
                text(f"update player_round set player = 5 where id = 27")
            )
            connection.execute(
                text(f"update player_round set player = 13 where id = 28")
            )
            connection.execute(
                text(f"update player_round set player = 1 where id = 29")
            )
            connection.commit()
        if play_mode == "2" or play_mode == 2:
            connection.execute(
                text(f"update player_round set player = 3 where id = 13")
            )
            connection.execute(
                text(f"update player_round set player = 7 where id = 14")
            )
            connection.execute(
                text(f"update player_round set player = 11 where id = 15")
            )
            connection.execute(
                text(f"update player_round set player = 4 where id = 16")
            )
            connection.execute(
                text(f"update player_round set player = 1 where id = 17")
            )
            connection.execute(
                text(f"update player_round set player = 5 where id = 18")
            )
            connection.execute(
                text(f"update player_round set player = 10 where id = 19")
            )
            connection.execute(
                text(f"update player_round set player = 7 where id = 20")
            )
            connection.execute(
                text(f"update player_round set player = 9 where id = 21")
            )
            connection.execute(
                text(f"update player_round set player = 3 where id = 22")
            )
            connection.execute(
                text(f"update player_round set player = 2 where id = 23")
            )
            connection.execute(
                text(f"update player_round set player = 6 where id = 24")
            )
            connection.execute(
                text(f"update player_round set player = 1 where id = 25")
            )
            connection.execute(
                text(f"update player_round set player = 9 where id = 26")
            )
            connection.execute(
                text(f"update player_round set player = 5 where id = 27")
            )
            connection.execute(
                text(f"update player_round set player = 13 where id = 28")
            )
            connection.execute(
                text(f"update player_round set player = 1 where id = 29")
            )
            connection.commit()
        connection.commit()
        connection.execute(text(f"update questions set played = 0"))
        connection.commit()
        connection.execute(
            text(f"update last_question set question ='', answer='', comment='', image = 'standard.jpg'")
        )
        connection.commit()
        connection.execute(
            text(f"update config set value = 0 where name ='monitor_round'")
        )
        connection.commit()
        connection.execute(
            text(f"update config set value = 4 where name ='buzzer_blocked'")
        )
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
    connection.execute(text(f"update last_question set question ='', answer='', image = 'standard.jpg', comment = ''"))
    connection.commit()
    connection.execute(text(f"update config set value = 0 where name ='monitor_round'"))
    connection.commit()
    connection.execute(
        text(f"update config set value = 4 where name ='buzzer_blocked'")
    )
    connection.commit()
    connection.execute(text(f"update player_round set is_active = 1"))
    connection.commit()
    connection.close()
    print("reset player points silent")


def reset_buzzer_blocked():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(
        text(f"update config set value = 4 where name ='buzzer_blocked'")
    )
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
    points.player_1_points = str(get_player_points(1, round_id)).zfill(2)
    points.player_2_points = str(get_player_points(2, round_id)).zfill(2)
    points.player_3_points = str(get_player_points(3, round_id)).zfill(2)
    points.player_4_points = str(get_player_points(4, round_id)).zfill(2)
    points.player_1_name = get_player_name(1, round_id)
    points.player_2_name = get_player_name(2, round_id)
    points.player_3_name = get_player_name(3, round_id)
    points.player_4_name = get_player_name(4, round_id)
    points.global_player_id_1 = get_global_player_id(1, round_id)
    points.global_player_id_2 = get_global_player_id(2, round_id)
    points.global_player_id_3 = get_global_player_id(3, round_id)
    points.global_player_id_4 = get_global_player_id(4, round_id)
    points.player_1_state = get_player_state(1, round_id)
    points.player_2_state = get_player_state(2, round_id)
    points.player_3_state = get_player_state(3, round_id)
    points.player_4_state = get_player_state(4, round_id)
    points.points_to_play = get_points_to_play(round_id)

    return points


def set_buzzer_blocked(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    player_1_state = get_player_state(1, round_id)
    player_2_state = get_player_state(2, round_id)
    player_3_state = get_player_state(3, round_id)
    player_4_state = get_player_state(4, round_id)
    # print(f"player active states: player 1: {player_1_state}, player 2: {player_2_state}, player 3: {player_3_state}, player 4: {player_4_state}")
    connection.execute(
        text("update config set value = 4 where name = 'buzzer_blocked'")
    )
    connection.commit()
    if int(player_1_state) == 0:
        print("buzzer player 1 blocked")
        connection.execute(
            text("update config set value = 0 where name = 'buzzer_blocked'")
        )
        connection.commit()
    if int(player_2_state) == 0:
        print("buzzer player 2 blocked")
        connection.execute(
            text("update config set value = 1 where name = 'buzzer_blocked'")
        )
        connection.commit()
    if int(player_3_state) == 0:
        print("buzzer player 3 blocked")
        connection.execute(
            text("update config set value = 2 where name = 'buzzer_blocked'")
        )
        connection.commit()
    if int(player_4_state) == 0:
        print("buzzer player 4 blocked")
        connection.execute(
            text("update config set value = 3 where name = 'buzzer_blocked'")
        )
        connection.commit()
    connection.close()

def reset_buzzer():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(
        text("update config set value = 5 where name = 'buzzer_blocked'")
    )
    print("RESET ALL BUZZER")
    connection.commit()
    connection.execute(
        text("update config set value = 4 where name = 'buzzer_pressed'")
    )
    connection.commit()
    connection.close()
    send_buzzer_blocked()

def set_buzzer_pressed(buzzer_pressed):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(
        text(f"update config set value = {buzzer_pressed} where name = 'buzzer_pressed'")
    )
    connection.commit()
    connection.close()

def get_buzzer_pressed_from_db():
    buzzer_pressed = 4
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text("select value from config where name = 'buzzer_pressed'")
    )
    for row in result:
        buzzer_pressed = row.value
    connection.close()
    return buzzer_pressed

def send_buzzer_blocked():
    buzzer_blocked = get_buzzer_blocked()
    arduino.write(bytes(buzzer_blocked, "utf-8"))
    # print(f"sent blocked buzzer to arduino")

def get_version_number():
    version_number = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text("select value from config where name = 'version'")
    )
    for row in result:
        version_number = row.value
    connection.close()
    return version_number

def get_buzzer_blocked():
    buzzer_blocked = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select value from config where name = 'buzzer_blocked'")
    )
    for row in result:
        buzzer_blocked = row.value
    connection.close()
    return buzzer_blocked

def get_buzzer_pressed_from_serial():
    buzzer_pressed = arduino.readline().decode("utf-8").strip()
    return buzzer_pressed

def update_player_name(global_player_id, player_name):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(
        text(f"update player set name = '{player_name}' where id = {global_player_id}")
    )
    connection.commit()
    connection.close()


def get_play_round():
    round_id = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select value from config where name = 'play_round'")
    )
    for row in result:
        round_id = row.value
    connection.close()
    round_id = int(round_id)
    return round_id


def get_monitor_round():
    round_id = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select value from config where name = 'monitor_round'")
    )
    for row in result:
        round_id = row.value
    connection.close()
    round_id = int(round_id)
    return round_id

# to remove?
def get_player_color(player_id, round_id):
    player_color = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(
            f"select color from player_round where player_round_id = {player_id} and round = {round_id}"
        )
    )
    for row in result:
        player_color = row.color
    connection.close()
    return player_color


def get_player_state(player_id, round_id):
    player_state = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(
            f"select is_active from player_round where player_round_id = {player_id} and round = {round_id}"
        )
    )
    for row in result:
        player_state = row.is_active
    connection.close()
    return player_state


def set_play_round_by_round_id(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(
        text(f"update config set value = {round_id} where name = 'play_round'")
    )
    print(f"play round set to {round_id} in database")
    connection.commit()
    connection.close()


def set_monitor_round_by_round_id(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(
        text(f"update config set value = {round_id} where name = 'monitor_round'")
    )
    connection.commit()
    connection.close()


def set_last_question(question, answer, image, comment):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update last_question set question = '{question}'"))
    connection.commit()
    connection.execute(text(f"update last_question set answer = '{answer}'"))
    connection.commit()
    connection.execute(text(f"update last_question set image = '{image}'"))
    connection.commit()
    connection.execute(text(f"update last_question set comment = '{comment}'"))
    connection.commit()
    connection.close()

# to remove?
def index_players_of_round(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(
            f"select player.name, points from player_round inner join player on player_round.player = player.id where round = {round_id}"
        )
    )
    players = []
    round_name = get_round_name(round_id)
    print(f"\n{Color.MAGENTA}{round_name}{Color.BLUE}")
    print(f"-" * 20)
    for row in result:
        name = row.name
        points = row.points
        spacer = 20 - len(name) - len(str(points)) - 6
        print(f"{name}", " " * spacer, f"[ {points} ]")
    connection.close()
    return players


def get_play_mode():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    play_mode = 1
    result = connection.execute(
        text("select value from config where name = 'play_mode'")
    )
    for row in result:
        play_mode = row.value
    connection.close()
    return play_mode

#to remove?
def get_round_info(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(text("select id, name from player order by id"))
    players = []
    for row in result:
        id = row.id
        name = row.name
        print("\t[ {:<4s} ] {:<20s}".format(f"{Color.MAGENTA}{id}{Color.BLUE}", name))
        players.append({"\tid": f"{id}", "name": f"{name}"})
    connection.close()
    return players


def get_next_question(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(
            f"select id,question, answer, comment, seq, image from questions where round = {round_id} and played = 0 order by seq asc limit 1"
        )
    )
    next_question = {}
    for row in result:
        next_question["id"] = row.id
        next_question["question"] = row.question
        next_question["answer"] = row.answer
        next_question["comment"] = row.comment
        next_question["seq"] = row.seq
        if row.image == "":
            next_question["image"] = "standard.jpg"
        else:
            next_question["image"] = row.image
    result = connection.execute(text(f"select * from questions where round = {round_id}"))
    next_question["total"] = result.rowcount
    connection.close()
    return next_question

# to remove?
def get_points_to_play(round_id):
    next_song = get_next_song(round_id)
    maximum = get_round_maximum_songs(round_id)
    get_seq = next_song.get("seq", 0)
    points_to_go = 0
    # for debugging:
    # print(f"points to go: {points_to_go}")
    # print(f"get_seq: {get_seq}")
    # print(f"maximum: {maximum}")
    if (get_seq > maximum) or (get_seq == 0):
        points_to_go = "--"
    else:
        points_to_go = (maximum - (get_seq - 1)) * 2
    return points_to_go


def get_last_question():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select question, answer, image, comment from last_question")
    )
    last_question = {}
    for row in result:
        last_question["question"] = row.question
        last_question["answer"] = row.answer
        last_question["image"] = row.image
        last_question["comment"] = row.comment
    connection.close()
    return last_question

def get_song_details(id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    songDetails = {}
    result = connection.execute(text(f"select title, artist, round, seq, played, comment, year, cover from songs where id = {id}"))
    for row in result:
        songDetails["title"] = row.title
        songDetails["artist"] = row.artist
        songDetails["round"] = row.round
        songDetails["seq"] = row.seq
        songDetails["played"] = row.played
        songDetails["comment"] = row.comment
        songDetails["year"] = row.year
        songDetails["cover"] = row.cover
    connection.close()
    return songDetails

def get_song_details_by_name(title):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    songDetails = {}
    result = connection.execute(text(f"select id, title, artist, round, seq, played, comment, year, cover from songs where title = '{title}'"))
    for row in result:
        songDetails["id"] = row.id
        songDetails["title"] = row.title
        songDetails["artist"] = row.artist
        songDetails["round"] = row.round
        songDetails["seq"] = row.seq
        songDetails["played"] = row.played
        songDetails["comment"] = row.comment
        songDetails["year"] = row.year
        songDetails["cover"] = row.cover
    connection.close()
    return songDetails

def add_question_to_database(question, answer, round, seq, played, comment, image):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(
        text(
            f"insert into questions (question, answer, round, seq, played, comment, image) values ('{question}', '{answer}', '{round}', '{seq}', '{played}', '{comment}', '{image}')"
        )
    )
    connection.commit()
    print(f"QUESTION {question} ADDED")
    connection.close()

def remove_question_from_database(id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"delete from questions where id = {id}"))
    connection.commit()
    print(f"QUESTION {id} DELETED")
    connection.close()

def change_question_details(id, question, answer, round, seq, played, comment, image):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update questions set question = '{question}' where id = {id}"))
    connection.commit()
    connection.execute(text(f"update questions set answer = '{answer}' where id = {id}"))
    connection.commit()
    connection.execute(text(f"update questions set round = '{round}' where id = {id}"))
    connection.commit()
    connection.execute(text(f"update questions set seq = '{seq}' where id = {id}"))
    connection.commit()
    connection.execute(text(f"update questions set played = '{played}' where id = {id}"))
    connection.commit()
    connection.execute(text(f"update questions set comment = '{comment}' where id = {id}"))
    connection.commit()
    connection.execute(text(f"update questions set image = '{image}' where id = {id}"))
    connection.commit()
    print(f"QUESTION {id} UPDATED")
    connection.close()

def change_question_seq(id, seq):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(text(f"update questions set seq = '{seq}' where id = {id}"))
    connection.commit()
    connection.close()

def mark_question_as_played(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(
        text(
            f"update questions set played = 1 where round = {round_id} and played = 0 order by seq asc limit 1"
        )
    )
    connection.commit()
    connection.close()


def get_round_name(round_id):
    round_name = "nothing"
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(text(f"select round from round where id = {round_id}"))
    for row in result:
        round_name = row.round
    connection.close()
    return round_name


def get_global_player_id(player_id, round_id):
    global_player_id = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(
            f"select player from player_round where player_round_id = {player_id} and round = {round_id}"
        )
    )
    for row in result:
        global_player_id = row.player
    connection.close()
    return global_player_id


def get_player_points(player_id, round_id):
    points = 0
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(
            f"select points from player_round where player_round_id = {player_id} and round = {round_id}"
        )
    )
    for row in result:
        points = row.points
    connection.close()
    return points


def get_player_name(player_id, round_id):
    name = 0
    global_player_id = get_global_player_id(player_id, round_id)
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select name from player where id = {global_player_id}")
    )
    for row in result:
        player_name = row.name
    connection.close()
    return player_name


def get_player_name_from_global_id(global_player_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select name from player where id = {global_player_id}")
    )
    for row in result:
        player_name = row.name
    connection.close()
    return player_name

def round_ranking(round_id):
    ranks = {
        get_player_name(1, round_id): get_player_points(1, round_id),
        get_player_name(2, round_id): get_player_points(2, round_id),
        get_player_name(3, round_id): get_player_points(3, round_id),
        get_player_name(4, round_id): get_player_points(4, round_id),
    }
    ranks = dict(sorted(ranks.items(), key=lambda item: item[1], reverse=True))
    # print(f"\t{Color.MAGENTA} Ranking\n{Color.BLUE}")
    # print("\t-----------------")
    # for key in ranks:
    #     print(f"\t{key} : {ranks[key]}")
    # print("\t-----------------")
    keys = list(ranks)
    return ranks


def sort_ranking(round_id):
    ranks = {
        get_global_player_id(1, round_id): get_player_points(1, round_id),
        get_global_player_id(2, round_id): get_player_points(2, round_id),
        get_global_player_id(3, round_id): get_player_points(3, round_id),
        get_global_player_id(4, round_id): get_player_points(4, round_id),
    }
    ranks = dict(sorted(ranks.items(), key=lambda item: item[1], reverse=True))
    keys = list(ranks)
    round_id = int(round_id)

    if round_id == 1:
        update_final_round(1, 5, keys[0])
        update_final_round(3, 6, keys[1])
    if round_id == 2:
        update_final_round(2, 5, keys[0])
        update_final_round(4, 6, keys[1])
    if round_id == 3:
        update_final_round(1, 6, keys[0])
        update_final_round(3, 5, keys[1])
    if round_id == 4:
        update_final_round(2, 6, keys[0])
        update_final_round(4, 5, keys[1])
    if round_id == 5:
        update_final_round(1, 7, keys[0])
        update_final_round(3, 7, keys[1])
    if round_id == 6:
        update_final_round(2, 7, keys[0])
        update_final_round(4, 7, keys[1])
    if round_id == 7:
        update_final_round(1, 8, keys[0])


def sort_ranking_playoff(round_id):
    print(f"sorting playoffs for round {round_id}")
    ranks = {
        get_global_player_id(1, round_id): get_player_points(1, round_id),
        get_global_player_id(2, round_id): get_player_points(2, round_id),
        get_global_player_id(3, round_id): get_player_points(3, round_id),
        get_global_player_id(4, round_id): get_player_points(4, round_id),
    }
    ranks = dict(sorted(ranks.items(), key=lambda item: item[1], reverse=True))
    keys = list(ranks)
    round_id = int(round_id)

    if round_id == 1:
        play_off_round_id = 4
        final_player_id_first = 1
        final_player_id_second = 2
        update_playoff_round(1, keys[2], ranks[keys[2]])
        update_playoff_round(4, keys[3], ranks[keys[3]])
    if round_id == 2:
        play_off_round_id = 4
        final_player_id_first = 3
        final_player_id_second = 4
        update_playoff_round(2, keys[2], ranks[keys[2]])
        update_playoff_round(5, keys[3], ranks[keys[3]])
    if round_id == 3:
        play_off_round_id = 4
        final_player_id_first = 5
        final_player_id_second = 6
        update_playoff_round(3, keys[2], ranks[keys[2]])
        update_playoff_round(6, keys[3], ranks[keys[3]])
    if round_id == 5:
        update_final_round(1, 7, keys[0])
        update_final_round(3, 7, keys[1])
    if round_id == 6:
        update_final_round(2, 7, keys[0])
        update_final_round(4, 7, keys[1])
    if round_id == 7:
        final_round_id = 8
        final_player_id_first = 1
        update_final_round(final_player_id_first, final_round_id, keys[0])


def get_play_off_players_to_round():
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(text("select player, points from play_off"))
    play_off_ranking = {}
    for row in result:
        play_off_ranking[row.player] = row.points
    connection.close()
    rank = dict(
        sorted(play_off_ranking.items(), key=lambda item: item[1], reverse=True)
    )
    keys = list(rank)

    update_final_round(1, 4, keys[0])
    update_final_round(2, 4, keys[1])
    update_final_round(3, 4, keys[2])
    update_final_round(4, 4, keys[3])

    return play_off_ranking


def update_final_round(player_id, round_id, global_player_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(
        text(
            f"update player_round set player = '{global_player_id}' where player_round_id = {player_id} and round = {round_id}"
        )
    )
    connection.commit()
    connection.close()


def update_playoff_round(player_id, global_player_id, points):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    connection.execute(
        text(
            f"update play_off set player = '{global_player_id}', points = '{points}' where id = {player_id}"
        )
    )
    connection.commit()
    connection.close()


def get_round_maximum_questions(round_id):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    result = connection.execute(
        text(f"select maximum from max_questions where round = '{round_id}'")
    )
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


def update_player_on_answer(player_id, round_id, action):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    if action == "correct":
        connection.execute(
            text(
                f"update player_round set points = points + 2 WHERE player_round_id = '{player_id}' AND round = '{round_id}'"
            )
        )
        connection.execute(
            text(f"update player_round set is_active = 1 WHERE round = '{round_id}'")
        )
        connection.execute(
            text(f"update config set value = 4 WHERE name = 'buzzer_blocked'")
        )
        connection.commit()
        player_name = get_player_name_from_global_id(player_id)
        print(f"RICHTIGE ANTWORT VON {player_name} IN RUNDE {round_id}")
    if action == "wrong":
        connection.execute(
            text(
                f"update player_round set points = points + 2 WHERE player_round_id != '{player_id}' AND round = '{round_id}'"
            )
        )
        connection.execute(
            text(
                f"update player_round set is_active = 0 WHERE player_round_id = '{player_id}' AND round = '{round_id}'"
            )
        )
        connection.execute(
            text(
                f"update player_round set is_active = 1 WHERE player_round_id != '{player_id}' AND round = '{round_id}'"
            )
        )
        connection.commit()
        player_name = get_player_name_from_global_id(player_id)
        print(f"FALSCHE ANTWORT VON {player_name} IN RUNDE {round_id}")
    if action == "skip":
        connection.execute(
            text(f"update player_round set is_active = 1 WHERE round = '{round_id}'")
        )
        connection.execute(
            text(f"update config set value = 4 WHERE name = 'buzzer_blocked'")
        )
        connection.commit()
        print("FRAGE ÜBERSPRUNGEN")
    connection.close()

def update_player(player_id, round_id, action):
    engine = connect(QUIZ_TABLE)
    connection = engine.connect()
    if action == "correct":
        connection.execute(
            text(
                f"update player_round set points = points + 2 WHERE player = '{player_id}' AND round = '{round_id}'"
            )
        )
        connection.execute(
            text(f"update player_round set is_active = 1 WHERE round = '{round_id}'")
        )
        connection.execute(
            text(f"update config set value = 4 WHERE name = 'buzzer_blocked'")
        )
        connection.commit()
        player_name = get_player_name_from_global_id(player_id)
        print(f"\tRichtige Antwort von {player_name} in Runde {round_id}")
    if action == "wrong":
        connection.execute(
            text(
                f"update player_round set points = points + 2 WHERE player != '{player_id}' AND round = '{round_id}'"
            )
        )
        connection.execute(
            text(
                f"update player_round set is_active = 0 WHERE player = '{player_id}' AND round = '{round_id}'"
            )
        )
        connection.execute(
            text(
                f"update player_round set is_active = 1 WHERE player != '{player_id}' AND round = '{round_id}'"
            )
        )
        connection.commit()
        player_name = get_player_name_from_global_id(player_id)
        print(f"\tFalsche Antwort von {player_name} in Runde {round_id}")
    if action == "skip":
        connection.execute(
            text(f"update player_round set is_active = 1 WHERE round = '{round_id}'")
        )
        connection.execute(
            text(f"update config set value = 4 WHERE name = 'buzzer_blocked'")
        )
        connection.commit()
        print("\tskipped song")
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
