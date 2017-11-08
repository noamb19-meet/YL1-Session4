class Animal(object):
    def __init__(self, sound, name, age, favorite_color):
        self.sound=sound
        self.name=name
        self.age=age
        self.favorite_color=favorite_color

    def eat(self, food):
        print("test")

    def description(self):
        print(self.name+" is "+str(self.age)+" years old and loves the color "+self.favorite_color)
i=Animal("bark","shosha",2,"blue")
i.eat("cake")
i.description()
    
