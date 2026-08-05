from typing import NotRequired, TypedDict, Required
class Movie(TypedDict):
    title: Required[str]
    year: int
m1: Movie = {"title": "Black Panther", "year": 2010}
m2: Movie = {"title": "Avengers"}
m3: Movie = {"year": 2004}
print(m1)
print(m2)
print(m3)