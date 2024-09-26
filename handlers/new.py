from sqlalchemy import literal
from sqlalchemy.dialects.postgresql.base import IDX_USING
from sqlalchemy.util import deprecated_cls
from utils import Color, Header
from handlers import procs
import config
import secrets

def run():
    print(Header("NEW QUIZ"))
    procs.new_player_names()
    procs.mainmenu()
