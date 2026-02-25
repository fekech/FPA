import sys , os

# Добавление родительской директории к sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортирование модулей приложения
from FPA.Data.Scripts.cmd import CMD_AuthorLogo

CMD_AuthorLogo()

