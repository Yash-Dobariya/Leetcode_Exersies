class Movie:
    """This class developed by me"""

    def __init__(self, title, hero, heroin) -> None:

        self.tital = title
        self.hero = hero
        self.heroin = heroin

    def info(self):
        print("Movie name", self.tital)
        print("Hero name", self.hero)
        print("Hero name", self.heroin)


list_of_movie = []
while True:
    title = input("Enter movie name : ")
    hero = input("Enter hero name : ")
    heroin = input("Enter heroin name : ")
    m = Movie(title, hero, heroin)
    list_of_movie.append(m)
    print("Movie added successfully ")
    option = input("Do you want to add movie [Yes | No] : ")

    if option.lower() == "no":
        break

print("All movie information ")

for movie in list_of_movie:
    movie.info()
    print()
