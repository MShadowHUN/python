from case import Gephaz
from cfan import Procihuto
from gpu import Videokartya
from power import Tap
from cpu import Proci
from ram import Ram
from mother import Alaplap
from hdd import Hdd
from ssd import Ssd

class Pc:
    def __init__(self, gpu:Videokartya, cpu:Proci, tap:Tap, ram:Ram, alaplap:Alaplap, gephaz:Gephaz, procihuto:Procihuto, ssd:Ssd, hdd:Hdd):
        super(). __init__() 

        self.gpu:Videokartya=gpu
        self.cpu:Proci=cpu
        self.tap:Tap=tap
        self.ram:Ram=ram
        self.alaplap:Alaplap=alaplap
        self.gephaz:Gephaz=gephaz
        self.procihuto:Procihuto=procihuto
        self.ssd:Ssd=ssd
        self.hdd:Hdd=hdd
    def __str__(self):
        return f"Videókártya:\n{self.gpu}\nProcesszor:\n{self.cpu}\nTápegység:\n{self.tap}\nRAM:\n{self.ram}\nAlaplap:\n{self.alaplap}\nGépház:\n{self.gephaz}\nProcesszor hűtő:\n{self.procihuto}\nSSD:\n{self.ssd}\nMerevlemez:\n{self.hdd}"