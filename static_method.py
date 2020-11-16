class Student:
    def __init__(self, name, perc):
        self.name = name
        self.perc = perc

    def msg(self):
        print(self.name+" got "+self.perc+"%")
    
    @staticmethod
    def get_age(age):
        if age < 18:
            print("belongs to school")
        else:
            print("not belongs to school")


s1=Student("xxxx","99")
s1.msg()
s1.get_age(7)