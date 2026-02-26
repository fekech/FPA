import sys , os , configparser, platform , configparser

# Добавление родительской директории к sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортирование модулей приложения
from Data.Scripts.cmd import CMD_AuthorLogo
from Data.Scripts.network import NT_KeepConnection, NT_SendData, NT_ReadData

address = ("26.69.212.179",5000)
silent_mode = False

CMD_AuthorLogo()

if NT_KeepConnection(address) == True:
    silent_mode = True
    print("Успешное подключение к серверу!")
else:
    silent_mode = False
    print("! Режим автономной работы !")

if __name__ == "__main__":
    FPAName = platform.node()+chr(92)+"$ "
    while True:
        UserCommand = input(FPAName)
        if silent_mode == False:
            print(UserCommand)
        else:
            NT_SendData(address,UserCommand)