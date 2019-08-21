import requests
from bs4 import BeautifulSoup


class Scrap():
    def __init__(self):
        self.html = requests.get("http://most.gizycko.pl/").text
        self.soup = BeautifulSoup(self.html, "lxml")

    def get_bridge_state(self):     # Returns true if bridge is open
        strings = []
        for string in self.soup.main.h1.stripped_strings:
            strings.append(string)

        return strings[1] == "OTWARTY"

    def get_time_left(self):
        time_strings = self.soup.find("div", {"id": "jeszcze_przez"}).string.split()
        hours = int(time_strings[2])
        minutes = int(time_strings[5])

        return {"hours": hours, "minutes": minutes}


if __name__ == "__main__":
    s = Scrap()
    print(s.get_bridge_state())
    print(s.get_time_left())
