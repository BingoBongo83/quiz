from tkinter import *
import tkinter
from tkinter import ttk
from handlers import procs
from handlers import new, resume
import pygame
import os
import time


title = "Quiz"
my_round_id = 0
player_1_name = "---"
player_2_name = "---"
player_3_name = "---"
player_4_name = "---"
player_1_points = 0
player_2_points = 0
player_3_points = 0
player_4_points = 0
maximum = 0
next_question = {}
next_question = procs.get_next_question(my_round_id)
global_player_id_1 = 0
global_player_id_2 = 0
global_player_id_3 = 0
global_player_id_4 = 0
round_name = "-"

pygame.mixer.init()


def main():
    root = tkinter.Tk()
    root.title("Quiz")
    root.minsize(1600, 900)
    root.configure(bg="black")
    style = ttk.Style()
    style.configure("False.TButton", background="red3", foreground="black")
    style.map("False.TButton", background=[("active", "red2")])
    style = ttk.Style()
    style.configure("Correct.TButton", background="green3", foreground="black")
    style.map("Correct.TButton", background=[("active", "green2")])
    style = ttk.Style()
    style.configure("Skip.TButton", background="yellow3", foreground="black")
    style.map("Skip.TButton", background=[("active", "yellow2")])
    style = ttk.Style()
    style.configure("Skip.TLabel", background="black", foreground="yellow3")
    style = ttk.Style()
    style.configure("Spotify.TLabel", background="black", foreground="green3", font=("Verdana", 15))
    style = ttk.Style()
    style.configure("TButton", background="grey20", foreground="green4")
    style.map("TButton", background=[("active", "black")])
    style = ttk.Style()
    style.configure("TLabel", background="black", foreground="green4")
    style = ttk.Style()
    style.configure("Title.TLabel", background="black", foreground="green4", font=("Verdana", 35), anchor="center")
    style = ttk.Style()
    style.configure("SubTitle.TLabel", background="black", foreground="green4", font=("Verdana", 25), anchor="center")
    style = ttk.Style()
    style.configure("TournamentTitle.TLabel", background="black", foreground="green4", font=("Verdana", 30))
    style = ttk.Style()
    style.configure("TournamentPlayer1.TLabel", background="black", foreground="green3", font=("Verdana", 15))
    style = ttk.Style()
    style.configure("TournamentPlayer2.TLabel", background="black", foreground="gray60", font=("Verdana", 15))
    style = ttk.Style()
    style.configure("Tournament.TSeparator", background="green4")
    style = ttk.Style()
    style.configure("QuestionNumber.TLabel", background="black", foreground="yellow3", font=("Verdana", 16))
    style = ttk.Style()
    style.configure("Question.TLabel", background="black", foreground="dodgerblue2", font=("Verdana", 20))
    style = ttk.Style()
    style.configure("QuestionAnswer.TLabel", background="black", foreground="dodgerblue2", font=("Verdana", 20))
    style = ttk.Style()
    style.configure("green.Horizontal.TProgressbar", troughcolor="black", bordercolor="yellow3", background="yellow3")
    style.map("green.Horizontal.TProgressbar" , background=[("active", "yellow3")], troughcolor=[("active", "black")], bordercolor=[("active", "yellow3")])
    play_mode = procs.get_play_mode()

    main_label = ttk.Label(root, text="Musikquiz", style="Title.TLabel")
    if play_mode == "1":
        playmode_label = ttk.Label(root, text=f"Spielmodus: {play_mode} (16 Spieler)", style="SubTitle.TLabel")
    elif play_mode == "2":
        playmode_label = ttk.Label(root, text=f"Spielmodus: {play_mode} (12 Spieler & PlayOff)", style="SubTitle.TLabel")

    main_label.pack()
    playmode_label.pack()

    button_play = ttk.Button(root, text="Spielen", command=playmode, width=15)
    monitor_button = ttk.Button(root, text="Monitor", width=15)
    show_tournament_button = ttk.Button(root, text="Turnierbaum", command=lambda: tournament_window(), width=15)
    button_settings = ttk.Button(root, text="Einstellungen", command=settings_window, width=15)
    exit_button = ttk.Button(root, text="Beenden", command=root.destroy, width=15)

    button_play.pack()
    monitor_button.pack()
    show_tournament_button.pack()
    button_settings.pack()
    exit_button.pack()

    root.mainloop()

def play_correct():
    pygame.mixer.music.load("sounds/correct.mp3")
    pygame.mixer.music.play()

def play_wrong():
    pygame.mixer.music.load("sounds/false.mp3")
    pygame.mixer.music.play()

def play_clock():
    pygame.mixer.music.load("sounds/clock.mp3")
    pygame.mixer.music.play()

def play_hit():
    pygame.mixer.music.load("sounds/hit.mp3")
    pygame.mixer.music.play()

def playmode():
    game_window = tkinter.Toplevel()
    game_window.title("Spielen")
    game_window.minsize(800, 600)
    game_window.configure(bg="black")

    play_mode = procs.get_play_mode()
    print(f"playmode {play_mode}")

    round_name_1 = procs.get_round_name(1)
    round_name_2 = procs.get_round_name(2)
    round_name_3 = procs.get_round_name(3)
    round_name_4 = procs.get_round_name(4)
    round_name_5 = procs.get_round_name(5)
    round_name_6 = procs.get_round_name(6)
    round_name_7 = procs.get_round_name(7)

    title_label = ttk.Label(game_window, text=title, style="Title.TLabel")

    button_set_round_id_1 = ttk.Button(game_window, text=f"{round_name_1}", width=15, command=lambda:[set_round_id(1)])
    button_set_round_id_2 = ttk.Button(game_window, text=f"{round_name_2}", width=15, command=lambda:[set_round_id(2)])
    button_set_round_id_3 = ttk.Button(game_window, text=f"{round_name_3}", width=15, command=lambda:[set_round_id(3)])
    button_set_round_id_4 = ttk.Button(game_window, text=f"{round_name_4}", width=15, command=lambda:[set_round_id(4)])
    button_set_round_id_5 = ttk.Button(game_window, text=f"{round_name_5}", width=15, command=lambda:[set_round_id(5)])
    button_set_round_id_6 = ttk.Button(game_window, text=f"{round_name_6}", width=15, command=lambda:[set_round_id(6)])
    button_set_round_id_7 = ttk.Button(game_window, text=f"{round_name_7}", width=15, command=lambda:[set_round_id(7)])
    button_player_1_correct = ttk.Button(game_window, text="P1 Richtig", width=16, style="Correct.TButton", command=lambda:[answer(1,my_round_id,"correct"),play_correct()])
    button_player_2_correct = ttk.Button(game_window, text="P2 Richtig", width=16, style="Correct.TButton", command=lambda:[answer(2,my_round_id,"correct"),play_correct()])
    button_player_3_correct = ttk.Button(game_window, text="P3 Richtig", width=16, style="Correct.TButton",command=lambda:[answer(3,my_round_id,"correct"),play_correct()])
    button_player_4_correct = ttk.Button(game_window, text="P4 Richtig", width=16, style="Correct.TButton",command=lambda:[answer(4,my_round_id,"correct"),play_correct()])
    button_player_1_wrong = ttk.Button(game_window, text="P1  Falsch", width=16, style="False.TButton", command=lambda:[answer(1,my_round_id,"false"),play_wrong()])
    button_player_2_wrong = ttk.Button(game_window, text="P2  Falsch", width=16, style="False.TButton",command=lambda:[answer(2,my_round_id,"false"),play_wrong()])
    button_player_3_wrong = ttk.Button(game_window, text="P3  Falsch", width=16, style="False.TButton",command=lambda:[answer(3,my_round_id,"false"),play_wrong()])
    button_player_4_wrong = ttk.Button(game_window, text="P4  Falsch", width=16, style="False.TButton",command=lambda:[answer(4,my_round_id,"false"),play_wrong()])
    button_clock = ttk.Button(game_window, text="TikTak", style="Skip.TButton", width=16, command=lambda: play_clock())
    button_skip_question = ttk.Button(game_window, text="Frage überspringen", style="Skip.TButton", width=16, command=lambda:[answer(1,my_round_id,"skip"),play_hit()])
    exit_button = ttk.Button(game_window, text="EXIT", command=lambda:[game_window.destroy(),procs.set_monitor_to_pause()], width=15)

    player_1_name_label = Label(game_window, text=f"{player_1_name}", width=12, anchor="center", fg="green3", bg="black", font=("Verdana", 30))
    player_2_name_label = Label(game_window, text=f"{player_2_name}", width=12, anchor="center", fg="green3", bg="black", font=("Verdana", 30))
    player_3_name_label = Label(game_window, text=f"{player_3_name}", width=12, anchor="center", fg="green3", bg="black", font=("Verdana", 30))
    player_4_name_label = Label(game_window, text=f"{player_4_name}", width=12, anchor="center", fg="green3", bg="black", font=("Verdana", 30))
    player_1_points_label = Label(game_window, text=f"{player_1_points}", width=12, anchor="center", fg="green3", bg="black", font=("Verdana", 35))
    player_2_points_label = Label(game_window, text=f"{player_2_points}", width=12, anchor="center", fg="green3", bg="black", font=("Verdana", 35))
    player_3_points_label = Label(game_window, text=f"{player_3_points}", width=12, anchor="center", fg="green3", bg="black", font=("Verdana", 35))
    player_4_points_label = Label(game_window, text=f"{player_4_points}", width=12, anchor="center", fg="green3", bg="black", font=("Verdana", 35))
    question_counter_label = ttk.Label(game_window, text=f"FRAGE# {next_question.get("seq",0)} / {maximum} ({next_question['total']}):", style="QuestionNumber.TLabel")
    next_question_label = ttk.Label(game_window, text=f"FRAGE:  {next_question.get("question","")}", style="Question.TLabel")
    next_question_answer_label = ttk.Label(game_window, text=f"ANTWORT:   {next_question.get("answer","")}", style="QuestionAnswer.TLabel")
    # calculate progress bar
    progress = DoubleVar()
    progressbar = ttk.Progressbar(game_window, variable=progress, maximum=100, length=800, style="green.Horizontal.TProgressbar")

    title_label.grid(row = 0, column = 1, columnspan=2)
    player_1_name_label.grid(row = 2, column = 0)
    player_2_name_label.grid(row = 2, column = 1)
    player_3_name_label.grid(row = 2, column = 2)
    player_4_name_label.grid(row = 2, column = 3)
    player_1_points_label.grid(row = 3, column = 0)
    player_2_points_label.grid(row = 3, column = 1)
    player_3_points_label.grid(row = 3, column = 2)
    player_4_points_label.grid(row = 3, column = 3)
    button_player_1_correct.grid(row = 4, column = 0)
    button_player_2_correct.grid(row = 4, column = 1)
    button_player_3_correct.grid(row = 4, column = 2)
    button_player_4_correct.grid(row = 4, column = 3)
    button_player_1_wrong.grid(row = 5, column = 0)
    button_player_2_wrong.grid(row = 5, column = 1)
    button_player_3_wrong.grid(row = 5, column = 2)
    button_player_4_wrong.grid(row = 5, column = 3)
    progressbar.grid(row = 11, column = 1, columnspan=3)
    button_skip_question.grid(row = 8, column = 2)
    button_clock.grid(row = 9, column = 2)
    button_set_round_id_1.grid(row = 4, column = 8)
    button_set_round_id_2.grid(row = 5, column = 8)
    button_set_round_id_3.grid(row = 6, column = 8)
    button_set_round_id_4.grid(row  = 7, column = 8)
    button_set_round_id_5.grid(row = 8, column = 8)
    button_set_round_id_6.grid(row = 9, column = 8)
    button_set_round_id_7.grid(row = 10, column = 8)
    question_counter_label.grid(row = 11, column = 0)
    next_question_label.grid(row = 14, column = 0, columnspan=4)
    next_question_answer_label.grid(row = 15, column = 0, columnspan=4)
    exit_button.grid(row = 16, column = 8)

    def answer(player_id, my_round_id, answer):
        print(f"max questionss: {maximum}, round_id: {my_round_id}, round_name: {round_name}")
        print(f"global player ids: {global_player_id_1}, {global_player_id_2}, {global_player_id_3}, {global_player_id_4}")
        global_player = 0
        if player_id == 1:
            global_player = global_player_id_1
        elif player_id == 2:
            global_player = global_player_id_2
        elif player_id == 3:
            global_player = global_player_id_3
        elif player_id == 4:
            global_player = global_player_id_4
        if answer == "false":
            if player_id == 1:
                player_1_name_label.config(fg="red3")
                player_1_points_label.config(fg="red3")
                player_2_name_label.config(fg="green3")
                player_2_points_label.config(fg="green3")
                player_3_name_label.config(fg="green3")
                player_3_points_label.config(fg="green3")
                player_4_name_label.config(fg="green3")
                player_4_points_label.config(fg="green3")
            elif player_id == 2:
                player_1_name_label.config(fg="green3")
                player_1_points_label.config(fg="green3")
                player_2_name_label.config(fg="red3")
                player_2_points_label.config(fg="red3")
                player_3_name_label.config(fg="green3")
                player_3_points_label.config(fg="green3")
                player_4_name_label.config(fg="green3")
                player_4_points_label.config(fg="green3")
            elif player_id == 3:
                player_1_name_label.config(fg="green3")
                player_1_points_label.config(fg="green3")
                player_2_name_label.config(fg="green3")
                player_2_points_label.config(fg="green3")
                player_3_name_label.config(fg="red3")
                player_3_points_label.config(fg="red3")
                player_4_name_label.config(fg="green3")
                player_4_points_label.config(fg="green3")
            elif player_id == 4:
                player_1_name_label.config(fg="green3")
                player_1_points_label.config(fg="green3")
                player_2_name_label.config(fg="green3")
                player_2_points_label.config(fg="green3")
                player_3_name_label.config(fg="green3")
                player_3_points_label.config(fg="green3")
                player_4_name_label.config(fg="red3")
                player_4_points_label.config(fg="red3")
        elif answer == "correct":
            player_1_name_label.config(fg="green3")
            player_1_points_label.config(fg="green3")
            player_2_name_label.config(fg="green3")
            player_2_points_label.config(fg="green3")
            player_3_name_label.config(fg="green3")
            player_3_points_label.config(fg="green3")
            player_4_name_label.config(fg="green3")
            player_4_points_label.config(fg="green3")
        elif answer == "skip":
            player_1_name_label.config(fg="green3")
            player_1_points_label.config(fg="green3")
            player_2_name_label.config(fg="green3")
            player_2_points_label.config(fg="green3")
            player_3_name_label.config(fg="green3")
            player_3_points_label.config(fg="green3")
            player_4_name_label.config(fg="green3")
            player_4_points_label.config(fg="green3")
        procs.update_player(global_player,my_round_id,answer)
        procs.sort_ranking(my_round_id)
        procs.mark_question_as_played(my_round_id)
        procs.set_last_question(next_question['question'],next_question['answer'])
        procs.set_buzzer_blocked(my_round_id)
        if play_mode == "2" or play_mode == 2:
            if my_round_id != 4:
                print("sorting playoffs")
                procs.sort_ranking_playoff(my_round_id)
            procs.get_play_off_players_to_round()

        set_round_id(my_round_id)
        update_progressbar()

    def set_round_id(round_id):
        global my_round_id
        my_round_id = round_id
        global round_name
        round_name = procs.get_round_name(round_id)
        global title
        title = f"{round_name}"
        global maximum
        maximum = procs.get_round_maximum_questions(round_id)
        global player_1_name
        player_1_name = procs.get_player_name(1,round_id)
        global player_2_name
        player_2_name = procs.get_player_name(2,round_id)
        global player_3_name
        player_3_name = procs.get_player_name(3,round_id)
        global player_4_name
        player_4_name = procs.get_player_name(4,round_id)
        global player_1_points
        player_1_points = procs.get_player_points(1,round_id)
        global player_2_points
        player_2_points = procs.get_player_points(2,round_id)
        global player_3_points
        player_3_points = procs.get_player_points(3,round_id)
        global player_4_points
        player_4_points = procs.get_player_points(4,round_id)
        global global_player_id_1
        global_player_id_1 = procs.get_global_player_id(1,round_id)
        global global_player_id_2
        global_player_id_2 = procs.get_global_player_id(2,round_id)
        global global_player_id_3
        global_player_id_3 = procs.get_global_player_id(3,round_id)
        global global_player_id_4
        global_player_id_4 = procs.get_global_player_id(4,round_id)
        procs.set_monitor_round_by_round_id(round_id)
        global next_question
        next_question = {}
        next_question = procs.get_next_question(round_id)
        title_label.config(text=f"{round_name}")
        player_1_name_label.config(text=f"{player_1_name}")
        player_2_name_label.config(text=f"{player_2_name}")
        player_3_name_label.config(text=f"{player_3_name}")
        player_4_name_label.config(text=f"{player_4_name}")
        player_1_points_label.config(text=f"{player_1_points}")
        player_2_points_label.config(text=f"{player_2_points}")
        player_3_points_label.config(text=f"{player_3_points}")
        player_4_points_label.config(text=f"{player_4_points}")
        question_counter_label.config(text=f"FRAGE# {next_question.get('seq',0)} / {maximum} ({next_question['total']}): ")
        next_question_label.config(text=f"FRAGE:  {next_question.get("question","")}")
        next_question_answer_label.config(text=f"ANTWORT:   {next_question.get("answer","")}")
        print(f"set round to {my_round_id} ({round_name})")
        return round_id, global_player_id_1, global_player_id_2, global_player_id_3, global_player_id_4
        update_progressbar()

    def update_progressbar():
        if maximum == 0:
            progress = 0
        else:
            progress = int((next_question.get("seq",0) / maximum) * 100)
        # print(f"Progress: {progress}")
        new_value = progress
        progressbar["value"] = new_value
        game_window.after(1000, update_progressbar)
    update_progressbar()


def tournament_window():
    play_mode = procs.get_play_mode()
    tournament_window = tkinter.Toplevel()
    tournament_window.title("Turnierbaum")
    tournament_window.minsize(900, 600)
    tournament_window.config(bg="black")
    if play_mode == "2":
        procs.get_play_off_players_to_round()
    round_name_1 = procs.get_round_name(1)
    round_name_2 = procs.get_round_name(2)
    round_name_3 = procs.get_round_name(3)
    round_name_4 = procs.get_round_name(4)
    round_name_5 = procs.get_round_name(5)
    round_name_6 = procs.get_round_name(6)
    round_name_7 = procs.get_round_name(7)
    ranks1 = procs.round_ranking(1)
    keys1 = list(ranks1.keys())
    ranks2 = procs.round_ranking(2)
    keys2 = list(ranks2.keys())
    ranks3 = procs.round_ranking(3)
    keys3 = list(ranks3.keys())
    ranks4 = procs.round_ranking(4)
    keys4 = list(ranks4.keys())
    ranks5 = procs.round_ranking(5)
    keys5 = list(ranks5.keys())
    ranks6 = procs.round_ranking(6)
    keys6 = list(ranks6.keys())
    ranks7 = procs.round_ranking(7)
    keys7 = list(ranks7.keys())
    tournament_label = ttk.Label(tournament_window, text="Turnierbaum", style="TournamentTitle.TLabel")
    runde_1_label = ttk.Label(tournament_window, text=f"{round_name_1}", style="TournamentTitle.TLabel", width=14)
    runde_2_label = ttk.Label(tournament_window, text=f"{round_name_2}", style="TournamentTitle.TLabel", width=14)
    runde_3_label = ttk.Label(tournament_window, text=f"{round_name_3}", style="TournamentTitle.TLabel", width=14)
    runde_4_label = ttk.Label(tournament_window, text=f"{round_name_4}", style="TournamentTitle.TLabel", width=14)
    runde_5_label = ttk.Label(tournament_window, text=f"{round_name_5}", style="TournamentTitle.TLabel", width=14)
    runde_6_label = ttk.Label(tournament_window, text=f"{round_name_6}", style="TournamentTitle.TLabel", width=14)
    runde_7_label = ttk.Label(tournament_window, text=f"{round_name_7}", style="TournamentTitle.TLabel", width=14)
    winner_label = ttk.Label(tournament_window, text="Gewinner", style="TournamentTitle.TLabel")
    runde1_name1 = ttk.Label(tournament_window, text=f"{keys1[0]}",width=12, style="TournamentPlayer1.TLabel")
    runde1_name2 = ttk.Label(tournament_window, text=f"{keys1[1]}",width=12, style="TournamentPlayer1.TLabel")
    runde1_name3 = ttk.Label(tournament_window, text=f"{keys1[2]}",width=12, style="TournamentPlayer2.TLabel")
    runde1_name4 = ttk.Label(tournament_window, text=f"{keys1[3]}",width=12, style="TournamentPlayer2.TLabel")
    runde1_points1 = ttk.Label(tournament_window, text=f"{ranks1[keys1[0]]}",width=2, style="TournamentPlayer1.TLabel")
    runde1_points2 = ttk.Label(tournament_window, text=f"{ranks1[keys1[1]]}",width=2, style="TournamentPlayer1.TLabel")
    runde1_points3 = ttk.Label(tournament_window, text=f"{ranks1[keys1[2]]}",width=2, style="TournamentPlayer2.TLabel")
    runde1_points4 = ttk.Label(tournament_window, text=f"{ranks1[keys1[3]]}",width=2, style="TournamentPlayer2.TLabel")
    runde2_name1 = ttk.Label(tournament_window, text=f"{keys2[0]}",width=12, style="TournamentPlayer1.TLabel")
    runde2_name2 = ttk.Label(tournament_window, text=f"{keys2[1]}",width=12, style="TournamentPlayer1.TLabel")
    runde2_name3 = ttk.Label(tournament_window, text=f"{keys2[2]}",width=12, style="TournamentPlayer2.TLabel")
    runde2_name4 = ttk.Label(tournament_window, text=f"{keys2[3]}",width=12, style="TournamentPlayer2.TLabel")
    runde2_points1 = ttk.Label(tournament_window, text=f"{ranks2[keys2[0]]}",width=2, style="TournamentPlayer1.TLabel")
    runde2_points2 = ttk.Label(tournament_window, text=f"{ranks2[keys2[1]]}",width=2, style="TournamentPlayer1.TLabel")
    runde2_points3 = ttk.Label(tournament_window, text=f"{ranks2[keys2[2]]}",width=2, style="TournamentPlayer2.TLabel")
    runde2_points4 = ttk.Label(tournament_window, text=f"{ranks2[keys2[3]]}",width=2, style="TournamentPlayer2.TLabel")
    runde3_name1 = ttk.Label(tournament_window, text=f"{keys3[0]}",width=12, style="TournamentPlayer1.TLabel")
    runde3_name2 = ttk.Label(tournament_window, text=f"{keys3[1]}",width=12, style="TournamentPlayer1.TLabel")
    runde3_name3 = ttk.Label(tournament_window, text=f"{keys3[2]}",width=12, style="TournamentPlayer2.TLabel")
    runde3_name4 = ttk.Label(tournament_window, text=f"{keys3[3]}",width=12, style="TournamentPlayer2.TLabel")
    runde3_points1 = ttk.Label(tournament_window, text=f"{ranks3[keys3[0]]}",width=2, style="TournamentPlayer1.TLabel")
    runde3_points2 = ttk.Label(tournament_window, text=f"{ranks3[keys3[1]]}",width=2, style="TournamentPlayer1.TLabel")
    runde3_points3 = ttk.Label(tournament_window, text=f"{ranks3[keys3[2]]}",width=2, style="TournamentPlayer2.TLabel")
    runde3_points4 = ttk.Label(tournament_window, text=f"{ranks3[keys3[3]]}",width=2, style="TournamentPlayer2.TLabel")
    runde4_name1 = ttk.Label(tournament_window, text=f"{keys4[0]}",width=12, style="TournamentPlayer1.TLabel")
    runde4_name2 = ttk.Label(tournament_window, text=f"{keys4[1]}",width=12, style="TournamentPlayer1.TLabel")
    runde4_name3 = ttk.Label(tournament_window, text=f"{keys4[2]}",width=12, style="TournamentPlayer2.TLabel")
    runde4_name4 = ttk.Label(tournament_window, text=f"{keys4[3]}",width=12, style="TournamentPlayer2.TLabel")
    runde4_points1 = ttk.Label(tournament_window, text=f"{ranks4[keys4[0]]}",width=2, style="TournamentPlayer1.TLabel")
    runde4_points2 = ttk.Label(tournament_window, text=f"{ranks4[keys4[1]]}",width=2, style="TournamentPlayer1.TLabel")
    runde4_points3 = ttk.Label(tournament_window, text=f"{ranks4[keys4[2]]}",width=2, style="TournamentPlayer2.TLabel")
    runde4_points4 = ttk.Label(tournament_window, text=f"{ranks4[keys4[3]]}",width=2, style="TournamentPlayer2.TLabel")
    runde5_name1 =ttk.Label(tournament_window, text=f"{keys5[0]}",width=12, style="TournamentPlayer1.TLabel")
    runde5_name2 =ttk.Label(tournament_window, text=f"{keys5[1]}",width=12, style="TournamentPlayer1.TLabel")
    runde5_name3 =ttk.Label(tournament_window, text=f"{keys5[2]}",width=12, style="TournamentPlayer2.TLabel")
    runde5_name4 =ttk.Label(tournament_window, text=f"{keys5[3]}",width=12, style="TournamentPlayer2.TLabel")
    runde5_points1 =ttk.Label(tournament_window, text=f"{ranks5[keys5[0]]}",width=2, style="TournamentPlayer1.TLabel")
    runde5_points2 =ttk.Label(tournament_window, text=f"{ranks5[keys5[1]]}",width=2, style="TournamentPlayer1.TLabel")
    runde5_points3 =ttk.Label(tournament_window, text=f"{ranks5[keys5[2]]}",width=2, style="TournamentPlayer2.TLabel")
    runde5_points4 =ttk.Label(tournament_window, text=f"{ranks5[keys5[3]]}",width=2, style="TournamentPlayer2.TLabel")
    runde6_name1 =ttk.Label(tournament_window, text=f"{keys6[0]}",width=12, style="TournamentPlayer1.TLabel")
    runde6_name2 =ttk.Label(tournament_window, text=f"{keys6[1]}",width=12, style="TournamentPlayer1.TLabel")
    runde6_name3 =ttk.Label(tournament_window, text=f"{keys6[2]}",width=12, style="TournamentPlayer2.TLabel")
    runde6_name4 =ttk.Label(tournament_window, text=f"{keys6[3]}",width=12, style="TournamentPlayer2.TLabel")
    runde6_points1 =ttk.Label(tournament_window, text=f"{ranks6[keys6[0]]}",width=2, style="TournamentPlayer1.TLabel")
    runde6_points2 =ttk.Label(tournament_window, text=f"{ranks6[keys6[1]]}",width=2, style="TournamentPlayer1.TLabel")
    runde6_points3 =ttk.Label(tournament_window, text=f"{ranks6[keys6[2]]}",width=2, style="TournamentPlayer2.TLabel")
    runde6_points4 =ttk.Label(tournament_window, text=f"{ranks6[keys6[3]]}",width=2, style="TournamentPlayer2.TLabel")
    runde7_name1 =ttk.Label(tournament_window, text=f"{keys7[0]}",width=12, style="TournamentPlayer1.TLabel")
    runde7_name2 =ttk.Label(tournament_window, text=f"{keys7[1]}",width=12, style="TournamentPlayer2.TLabel")
    runde7_name3 =ttk.Label(tournament_window, text=f"{keys7[2]}",width=12, style="TournamentPlayer2.TLabel")
    runde7_name4 =ttk.Label(tournament_window, text=f"{keys7[3]}",width=12, style="TournamentPlayer2.TLabel")
    runde7_points1 =ttk.Label(tournament_window, text=f"{ranks7[keys7[0]]}",width=2, style="TournamentPlayer1.TLabel")
    runde7_points2 =ttk.Label(tournament_window, text=f"{ranks7[keys7[1]]}",width=2, style="TournamentPlayer2.TLabel")
    runde7_points3 =ttk.Label(tournament_window, text=f"{ranks7[keys7[2]]}",width=2, style="TournamentPlayer2.TLabel")
    runde7_points4 =ttk.Label(tournament_window, text=f"{ranks7[keys7[3]]}",width=2, style="TournamentPlayer2.TLabel")
    exit_button = ttk.Button(tournament_window, text="Turnierbaum verlassen", command=lambda: tournament_window.destroy(), width=20)
    linie1 = ttk.Separator(tournament_window, orient=HORIZONTAL, style="Tournament.TSeparator")
    linie2 = ttk.Separator(tournament_window, orient=HORIZONTAL, style="Tournament.TSeparator")
    linie3 = ttk.Separator(tournament_window, orient=HORIZONTAL, style="Tournament.TSeparator")
    linie4 = ttk.Separator(tournament_window, orient=HORIZONTAL, style="Tournament.TSeparator")
    tournament_label.grid(row = 0, column = 2, columnspan = 4)
    runde_1_label.grid(row = 1, column = 0, columnspan = 2, sticky="w")
    runde_2_label.grid(row = 1, column = 2, columnspan = 2, sticky="w")
    runde_3_label.grid(row = 1, column = 4, columnspan = 2, sticky="w")
    runde_4_label.grid(row = 1, column = 6, columnspan = 2, sticky="w")
    linie1.grid(row = 2, column = 0, columnspan = 2, padx=4, sticky="ew")
    linie2.grid(row = 2, column = 2, columnspan = 2, padx=4, sticky="ew")
    linie3.grid(row = 2, column = 4, columnspan = 2, padx=4, sticky="ew")
    linie4.grid(row = 2, column = 6, columnspan = 2, padx=4, sticky="ew")
    runde1_name1.grid(row = 3, column = 0, sticky="w")
    runde1_name2.grid(row = 4, column = 0, sticky="w")
    runde1_name3.grid(row = 5, column = 0, sticky="w")
    runde1_name4.grid(row = 6, column = 0, sticky="w")
    runde1_points1.grid(row = 3, column = 1, sticky="w")
    runde1_points2.grid(row = 4, column = 1, sticky="w")
    runde1_points3.grid(row = 5, column = 1, sticky="w")
    runde1_points4.grid(row = 6, column = 1, sticky="w")
    runde2_name1.grid(row = 3, column = 2)
    runde2_name2.grid(row = 4, column = 2)
    runde2_name3.grid(row = 5, column = 2)
    runde2_name4.grid(row = 6, column = 2)
    runde2_points1.grid(row = 3, column = 3)
    runde2_points2.grid(row = 4, column = 3)
    runde2_points3.grid(row = 5, column = 3)
    runde2_points4.grid(row = 6, column = 3)
    runde3_name1.grid(row = 3, column = 4)
    runde3_name2.grid(row = 4, column = 4)
    runde3_name3.grid(row = 5, column = 4)
    runde3_name4.grid(row = 6, column = 4)
    runde3_points1.grid(row = 3, column = 5)
    runde3_points2.grid(row = 4, column = 5)
    runde3_points3.grid(row = 5, column = 5)
    runde3_points4.grid(row = 6, column = 5)
    runde4_name1.grid(row = 3, column = 6)
    runde4_name2.grid(row = 4, column = 6)
    runde4_name3.grid(row = 5, column = 6)
    runde4_name4.grid(row = 6, column = 6)
    runde4_points1.grid(row = 3, column = 7)
    runde4_points2.grid(row = 4, column = 7)
    runde4_points3.grid(row = 5, column = 7)
    runde4_points4.grid(row = 6, column = 7)
    runde5_name1.grid(row = 8, column = 2)
    runde5_name2.grid(row = 9, column = 2)
    runde5_name3.grid(row = 10, column = 2)
    runde5_name4.grid(row = 11, column = 2)
    runde5_points1.grid(row = 8, column = 3)
    runde5_points2.grid(row = 9, column = 3)
    runde5_points3.grid(row = 10, column = 3)
    runde5_points4.grid(row = 11, column = 3)
    runde6_name1.grid(row = 8, column = 4)
    runde6_name2.grid(row = 9, column = 4)
    runde6_name3.grid(row = 10, column = 4)
    runde6_name4.grid(row = 11, column = 4)
    runde6_points1.grid(row = 8, column = 5)
    runde6_points2.grid(row = 9, column = 5)
    runde6_points3.grid(row = 10, column = 5)
    runde6_points4.grid(row = 11, column = 5)
    runde7_name1.grid(row = 13, column = 3)
    runde7_name2.grid(row = 14, column = 3)
    runde7_name3.grid(row = 15, column = 3)
    runde7_name4.grid(row = 16, column = 3)
    runde7_points1.grid(row = 13, column = 4)
    runde7_points2.grid(row = 14, column = 4)
    runde7_points3.grid(row = 15, column = 4)
    runde7_points4.grid(row = 16, column = 4)
    runde_5_label.grid(row = 7, column = 2, columnspan = 2)
    runde_6_label.grid(row = 7, column = 4, columnspan = 2)
    runde_7_label.grid(row = 12, column = 2, columnspan = 4)
    exit_button.grid(row=18, column=2, columnspan=4)

def enter_player_names():
    enter_player_window = tkinter.Toplevel()
    enter_player_window.title("Spielernamen eingeben")
    enter_player_window.minsize(400, 300)
    enter_player_window.configure(bg="black")

    player1_label = ttk.Label(enter_player_window, text="Spieler 1:")
    player2_label = ttk.Label(enter_player_window, text="Spieler 2:")
    player3_label = ttk.Label(enter_player_window, text="Spieler 3:")
    player4_label = ttk.Label(enter_player_window, text="Spieler 4:")
    player5_label = ttk.Label(enter_player_window, text="Spieler 5:")
    player6_label = ttk.Label(enter_player_window, text="Spieler 6:")
    player7_label = ttk.Label(enter_player_window, text="Spieler 7:")
    player8_label = ttk.Label(enter_player_window, text="Spieler 8:")
    player9_label = ttk.Label(enter_player_window, text="Spieler 9:")
    player10_label = ttk.Label(enter_player_window, text="Spieler 10:")
    player11_label = ttk.Label(enter_player_window, text="Spieler 11:")
    player12_label = ttk.Label(enter_player_window, text="Spieler 12:")
    player13_label = ttk.Label(enter_player_window, text="Spieler 13:")
    player14_label = ttk.Label(enter_player_window, text="Spieler 14:")
    player15_label = ttk.Label(enter_player_window, text="Spieler 15:")
    player16_label = ttk.Label(enter_player_window, text="Spieler 16:")
    player1_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player2_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player3_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player4_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player5_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player6_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player7_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player8_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player9_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player10_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player11_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player12_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player13_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player14_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player15_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")
    player16_entry = ttk.Entry(enter_player_window, width=20, style="Dark.TEntry")

    cancel_button = ttk.Button(enter_player_window, text="Abbrechen", command=enter_player_window.destroy, width=20)
    confirm_button = ttk.Button(enter_player_window, text="Bestätigen", command=lambda:[procs.new_player_names_silent(player1_entry.get(), player2_entry.get(), player3_entry.get(), player4_entry.get(), player5_entry.get(), player6_entry.get(), player7_entry.get(), player8_entry.get(), player9_entry.get(), player10_entry.get(), player11_entry.get(), player12_entry.get(), player13_entry.get(), player14_entry.get(), player15_entry.get(), player16_entry.get()), enter_player_window.destroy()], width=20)
    player1_label.grid(row=1, column=1)
    player2_label.grid(row=2, column=1)
    player3_label.grid(row=3, column=1)
    player4_label.grid(row=4, column=1)
    player5_label.grid(row=5, column=1)
    player6_label.grid(row=6, column=1)
    player7_label.grid(row=7, column=1)
    player8_label.grid(row=8, column=1)
    player9_label.grid(row=9, column=1)
    player10_label.grid(row=10, column=1)
    player11_label.grid(row=11, column=1)
    player12_label.grid(row=12, column=1)
    player13_label.grid(row=13, column=1)
    player14_label.grid(row=14, column=1)
    player15_label.grid(row=15, column=1)
    player16_label.grid(row=16, column=1)
    player1_entry.grid(row=1, column=2)
    player2_entry.grid(row=2, column=2)
    player3_entry.grid(row=3, column=2)
    player4_entry.grid(row=4, column=2)
    player5_entry.grid(row=5, column=2)
    player6_entry.grid(row=6, column=2)
    player7_entry.grid(row=7, column=2)
    player8_entry.grid(row=8, column=2)
    player9_entry.grid(row=9, column=2)
    player10_entry.grid(row=10, column=2)
    player11_entry.grid(row=11, column=2)
    player12_entry.grid(row=12, column=2)
    player13_entry.grid(row=13, column=2)
    player14_entry.grid(row=14, column=2)
    player15_entry.grid(row=15, column=2)
    player16_entry.grid(row=16, column=2)
    cancel_button.grid(row=17, column=1)
    confirm_button.grid(row=17, column=2)

# settings window
def settings_window():
    settings_window = tkinter.Toplevel()
    settings_window.title("Einstellungen")
    settings_window.minsize(800, 600)
    settings_window.configure(bg="black")

    settings_label = ttk.Label(settings_window, text="Einstellungen", style="SubTitle.TLabel")
    play_mode_1_button = ttk.Button(settings_window, text="Spielmodus 1", command=lambda: procs.change_play_mode_silent(1), width=18)
    play_mode_2_button = ttk.Button(settings_window, text="Spielmodus 2", command=lambda: procs.change_play_mode_silent(2), width=18)
    change_monitor_pause_button = ttk.Button(settings_window, text="Monitor PAUSE", command=procs.set_monitor_to_pause, width=18)
    change_monitor_winner_button = ttk.Button(settings_window, text="Monitor WINNER", command=procs.set_monitor_to_winner, width=18)
    set_player_names_button = ttk.Button(settings_window, text="Spielernamen setzen", width=18)
    reset_button = ttk.Button(settings_window, text="RESET!", command=lambda: procs.reset_player_points_silent(), width=18)
    exit_button = ttk.Button(settings_window, text="Einstellungen verlassen", command=lambda: settings_window.destroy(), width=18)
    settings_label.pack()
    play_mode_1_button.pack()
    play_mode_2_button.pack()
    change_monitor_pause_button.pack()
    change_monitor_winner_button.pack()
    set_player_names_button.pack()
    reset_button.pack()
    exit_button.pack()

if __name__ == "__main__":
    main()
