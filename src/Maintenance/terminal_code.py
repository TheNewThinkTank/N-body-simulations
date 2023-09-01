
from pathlib import Path
import os


def exec_terminal_cmd(path):
    os.system("cd " + str(Path.cwd()) + "\"" + path + "\"")


if __name__ == '__main__':
     print(os.getcwd())
     print(Path.cwd())
     path = '/Desktop/GperturbNew/StableStructures/pythonScripts'
     exec_terminal_cmd(path)
