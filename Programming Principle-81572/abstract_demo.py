from abc import ABC, abstractmethod
from interfaces import IFly, IJump, IClimb

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    def describe(self):
        return f"{self.name} makes the sound {self.make_sound()}"
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal, IJump):
    def __init__(self, name):
        super().__init__(name)
    def jump(self):
        raise NotImplementedError(
            "Dog.jump() has not been implemented yet."
        )
    def make_sound(self):
        return "Woof Woof Ow"

    class Cat(Animal, IJump, IClimb):
        def __init__(self, name):
            super().__init__(name)
        def jump(self):
            raise NotImplementedError(
                "Cat.jump() has not been implemented yet."
            )
        def climb(self):
            raise NotImplementedError(
                "Cat.climb() has not been implemented yet."
            )
        def jump(self):
            return "Boing Boing Boing"
        def make_sound(self):
            return "Meow Meow Ow"

        class Landbird(Animal, IJump):
            def __init__(self, name):
                super().__init__(name)
            def jump(self):
                return "Hop Hop Hop"
                )
            def make_sound(self):
                return "squawk squawk Ow"

            class FlyBird(Animal, IFly, IJump):
                def __init__(self, name):
                    super().__init__(name)
                def fly(self):
                    raise NotImplementedError(
                        "FlyBird.fly() has not been implemented yet."
                    )
                def jump(self):
                    return "Hop Hop Hop"
        
                def land(self):
                    raise NotImplementedError(
                        "FlyBird.land() has not been implemented yet."
                    )
                def make_sound(self):
                    return "Chirp Chirp Ow"