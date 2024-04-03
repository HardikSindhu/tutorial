#Abstract Class
import abc
from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def sapId(self):
     pass
    @abstractmethod
    def email(self)
     pass
    def name(self,name):
        print("my name")
    def show(self)

class professor(Employee):
    def __init__(self,name,sapId,email):
        self.n=name
        self.s=sapId
        self.e=email
        print("I am in professor class")
