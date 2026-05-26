

# 1

class Dog:
    def __init__(self, name):
        self.name=name

    def bark(self):
        return f"{self.name} says woof"

# 2

class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height

# 3

class Counter:
    def __init__(self, value = 0):
        self._value=value

    def increment(self):
        self._value+=1

    def value(self):
        return self._value

# 4

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"({self.x}, {self.y})"

# 5

class BankAccount:
    def __init__(self, balance = 0):
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        return None

    def withdraw(self, amount):
        if self.balance-amount >=0:
            self.balance-=amount
        return None

# 6

class Temperature:
    def __init__(self ,celsius):
        self.celsius=celsius

    def to_fahrenheit(self):
        return self.celsius * 1.8 + 32

# 7

class Student:
    school = "Kodcode"
    def __init__(self, name):
        self.name=name

# 8

class Player:
    counter=0
    def __init__(self):
        Player.counter+=1

# 9

class Money:
    def __init__(self, amount):
        self.amount=amount

    def is_more_than(self, other: Money):
        return other.amount < self.amount

    def __gt__(self, other):
        return other.amount < self.amount

# 10

class Playlist:
    def __init__(self, list_of_song: list):
        self.list_of_song=list_of_song

    def add(self, title):
        self.list_of_song.append(title)

    def remove(self, title):
        self.list_of_song.remove(title)

    def count(self):
        return len(self.list_of_song)

    def __str__(self):
        return f"{",".join(self.list_of_song)}"
