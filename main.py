from unicodedata import name

class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age =  age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        self.name = name
        print(name)

    def change_age(self, age):
        self.age = age
        print(age)

    def add_track(self, track):
        self.tracks.append(track)
        print(self.tracks)

    def get_score(self):
        print(self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# # Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()