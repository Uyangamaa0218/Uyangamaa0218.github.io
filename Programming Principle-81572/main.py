from app_data import Appdata
from abstract_demo import Animal, Dog, Cat, Landbird, FlyBird
from heroes import Humanhero, Batman

print(Appdata.APP_VERSION)

dog = Dog("Buddy")
cat = Cat("Whiskers")
dog1 = Dog("Max")

brian = Landbird("Brian")
fly_bird = FlyBird("Sky")

print(f"dog {dog.describe()}")
print(f"cat {cat.describe()}")
print(f"bird {brian.describe()}")
print(f"Brain Jumps{brian.jump()}")
print(f"Sky Jumps{fly_bird.jump()}")
print(f"cat Jumps{cat.jump()}")

human_hero = Humanhero()
batman = Batman()

batman.fly()
batman.land()
