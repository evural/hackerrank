import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from linked_list import LinkedList

class Animal(object):
    def __init__(self, name):
        self.name = name
        self.timestamp = None

class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.timestamp = None

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.timestamp = None

class AnimalShelter:
    def __init__(self):
        self.dog_list = LinkedList()
        self.cat_list = LinkedList()
        self.timestamp = 0
    def enqueue(self, animal):
        animal.timestamp = self.timestamp
        self.timestamp += 1
        if isinstance(animal, Dog):
            self.dog_list.insert_back(animal)
        elif isinstance(animal, Cat):
            self.cat_list.insert_back(animal)
    def dequeueAny(self):
        if self.dog_list.get_size() == 0:
            return self.dequeueCat()
        if self.cat_list.get_size() == 0:
            return self.dequeueDog()
        dog = self.dog_list.get_node_at(0).data
        cat = self.cat_list.get_node_at(0).data
        if dog.timestamp < cat.timestamp:
            return self.dequeueDog()
        return self.dequeueCat()
    def dequeueDog(self):
        dog = self.dog_list.get_node_at(0).data
        self.dog_list.remove_front()
        return dog
    def dequeueCat(self):
        cat = self.cat_list.get_node_at(0).data
        self.cat_list.remove_front()
        return cat
        
        
if __name__ == "__main__":
    animal_shelter = AnimalShelter()
    cat = Cat("cat1") 
    animal_shelter.enqueue(cat)
    dog = Dog("dog1")
    animal_shelter.enqueue(dog)
    cat2 = Cat("cat2") 
    animal_shelter.enqueue(cat2)
    dog = Dog("dog2")
    animal_shelter.enqueue(dog)
    cat3 = Cat("cat3") 
    animal_shelter.enqueue(cat3)
    cat4 = Cat("cat4") 
    animal_shelter.enqueue(cat4)
    dog = Dog("dog3")
    animal_shelter.enqueue(dog)
    dog = Dog("dog4")
    animal_shelter.enqueue(dog)
    print animal_shelter.dequeueAny().name
    print animal_shelter.dequeueAny().name
    print animal_shelter.dequeueAny().name
    print animal_shelter.dequeueAny().name
    print animal_shelter.dequeueAny().name
    print animal_shelter.dequeueAny().name
    print animal_shelter.dequeueAny().name
    print animal_shelter.dequeueAny().name
