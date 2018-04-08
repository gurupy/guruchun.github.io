class MyClass:
    name = "-"

    def __init__(self, _family):
        self.family = _family
        print ("class created --->", self.family)
        
    def __del__(self):
        print ("class destroyed ---", self.family)

    def setFamily(self, _family):
        self.family = _family
        print ("family changed...", _family)
        
    def setName(self, _name):
        self.name = _name
        print ("name changed...", _name)
        
    def say(self, _message):
        print (_message, self.name, self.family)


obj = MyClass("chun")
obj.setName("haechul")
obj.say("hi!")

obj2 = MyClass("park")
obj2.say("hi!")
obj2.setFamily("kim")
obj2.setName("steve")
obj2.say("hi!")

del obj2
del obj
