import threading

from network import NT_ReadData, NT_SendData

class DT_ReadNT(threading.Thread):
    def __init__(self,address):
        self.address = address
    def run(self):
       while True:
           NT_ReadData(self.address)

DT_ReadNTtheard = DT_ReadNT(address=("26.69.212.179",5000))
DT_ReadNTtheard.run()