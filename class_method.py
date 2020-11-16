class student:
    def __init__(self, name, perc):
        self.name=name
        self.perc=perc
    
    def msg(self):
        print(self.name+" got "+self.perc+"%")

    @classmethod
    def get_perc(cls, name, marks):
        return cls(name, str((int(marks)/600)*100))

s1=student.get_perc("xxxx","560")
s1.msg()
s2=student("yyyy","99.9")
s2.msg()