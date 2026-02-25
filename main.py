import sys , os , configparser, platform

# Добавление родительской директории к sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортирование модулей приложения
from Data.Scripts.cmd import CMD_AuthorLogo

CMD_AuthorLogo()

if __name__ == "__main__":
    FPAName = platform.node()+chr(92)+"$ "
    while True:
        UserCommand = input(FPAName)
        print('Полученна команда --> ' + UserCommand)