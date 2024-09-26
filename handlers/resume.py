from handlers import procs
from utils import Color, Header
def run():
    print(Header("SHOW ALL ROUNDS"))
    round_id = procs.choose_round()
    play_mode = procs.get_play_mode()
    if play_mode == "1":
        procs.play_mode1(round_id)
    elif play_mode == "2":
        procs.play_mode2(round_id)
    elif play_mode == "3":
        # procs.play_mode3(round_id)
        print(f"\n\t>>> Spielmodus {Color.RED}3{Color.BLUE} ist noch nicht implementiert! <<<")
    procs.mainmenu()
