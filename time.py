class Time:
    def _init_(self,hour,minute,seconds):
        self.hour=hour
        self.minute=minute
        self.seconds=seconds
    def _add_(self, other):
        return self.hour+other.hour,self.minute+other.minute,self.seconds+other.seconds
o1=Time(2,10,5)
o2=Time(4,5,10)
print(o1+o2)