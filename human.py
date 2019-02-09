class Human:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def greet(self):
        print('Hi, My name is {} and I am {} years old'.format(self.name, self.age))

    def talk_about_yourself(self):
        if self.gender == 'male':
            print('I am {name} and I am too strong!'.format(name=self.name))
        else:
            print('I am {} and I am stunning!'.format(self.name))


h = Human(name='Jack', gender='male', age=23)
h2 = Human(name='Mary', gender='female', age=21)

h.greet()
h.talk_about_yourself()
print('=' * 30)
h2.greet()
h2.talk_about_yourself()


