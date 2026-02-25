import sys , os , configparser

# Добавление родительской директории к sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортирование модулей приложения
from Data.Scripts.cmd import CMD_AuthorLogo

CMD_AuthorLogo()