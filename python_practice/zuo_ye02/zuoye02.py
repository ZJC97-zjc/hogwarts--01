import yaml


class Animal():
    name: str = "default"
    age: int = 0
    gender: str = 'male'
    colour: str = "white"

    def __init__(self, name, age, gender, colour):
        self.name = name
        self.age = age
        self.gender = gender
        self.colour = colour
        # print("成功")

    def bark(self, barking):
        print(f"{self.name} is barking me!")

    def run(self):
        print(f"{self.name} is running!")


class Cat(Animal):
    Cat_hair: str = ""

    def __init__(self, Cat_hair, name, age, gender, colour):
        self.Cat_hair = Cat_hair
        super().__init__(name, age, gender, colour)

    def catch_mouse(self):
        print(f"{self.name} can catch mouse!")

    def bark(self, mm_bark):
        mm_bark = self.bark
        # super().bark(mm_bark)
        print(f"{self.name} is {self.age} years old and {self.name} is a {self.colour} cat!")
        print(f"{self.name} is a {self.Cat_hair} cat.")
        print(f"{self.name} is miaomiao to me!")


class Dog(Animal):
    Dog_hair: str = ""

    def __init__(self, Dog_hair, name, age, gender, colour):
        self.Dog_hair = Dog_hair
        super().__init__(name, age, gender, colour)

    def care_home(self):
        print(f"{self.name} is a good housekeeper!")

    def bark(self, ww_bark):
        ww_bark = self.bark
        # super().bark(ww_bark)
        print(f"{self.name} is wangwang to me!")
        print(f"{self.name} is a lovely {self.colour} dog!")
        print(f"{self.name} is {self.age} years old!")


if __name__ == '__main__':
    with open("zuo_ye02.yaml") as f:
        datas = yaml.safe_load(f)
        Cat_hair = datas['default']['Cat_hair']
        name = datas['default']['name']
        age = datas['default']['age']
        gender = datas['default']['gender']
        colour = datas['default']['colour']
        bark_mm_bark = datas['default']['bark_mm_bark']

        c = Cat(Cat_hair, name, age, gender, colour)
        c.bark(bark_mm_bark)

    with open("zuo_ye03.yaml") as f:
        datas = yaml.safe_load(f)
        Dog_hair = datas['default']['Dog_hair']
        name = datas['default']['name']
        gender = datas['default']['gender']
        age = datas['default']['age']
        colour = datas['default']['colour']
        bark_ww_bark = datas['default']['bark_ww_bark']

        d = Dog(Dog_hair, name, age, gender, colour)
        d.bark(bark_ww_bark)

    # catty = Cat("short_hair","catty",2,'female',"oringe")
    # print(catty.name)
    # print(catty.age)
    # print(catty.gender)
    # print(catty.colour)
    # print(catty.Cat_hair)
    # catty.catch_mouse()
    #
    # doggy = Dog("long_hair","doggy",5,'male',"black")
    # print(doggy.name)
    # print(doggy.gender)
    # print(doggy.age)
    # print(doggy.colour)
    # print(doggy.Dog_hair)
    # doggy.care_home()
