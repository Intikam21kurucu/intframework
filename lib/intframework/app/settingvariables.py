import os
import importlib
from colorama import *
init(autoreset=True)

intframework = os.environ.get('INTFRAMEWORK_PATH')

console = __import__(intframework + "/intconsoleV4")

def load_variables(file):
    variables = {}
    try:
        # config.py dosyasındaki değişkenleri oku
        with open(config_file, "r") as f:
            exec(f.read(), {}, variables)
    except Exception as e:
        print(f"Error: {e}")
    return variables

def load_database(file):
    variables = {}
    try:
        # config.py dosyasındaki değişkenleri oku
        with open(config_file, "r") as f:
            exec(f.read(), {}, database)
    except Exception as e:
        print(f"Database Error: {e}")
    return database
   
def load2(file):
    variables = {}
    try:
        # config.py dosyasındaki değişkenleri oku
        with open(config_file, "r") as f:
            exec(f.read(), {}, data)
    except Exception as e:
        print(f"Error: {e}")
    return data