from requests import get


class WibuAPI():
    def __init__(self):
        self.base_url = "https://wibu-api.eu.org/api"
        self.deprecated_url = "https://api.wibu-api.eu.org/api"

    def lendrive(self, link):
        try:
            url = f"{self.base_url}/anime/lendrive?link={link}"
            response = get(url, timeout=5)
            return response.json()
        except  Exception as e:
            return "An error occured report on @YBotsSupport\n\n{}".format(e)

    def anichin(self, link):
        try:
            url = f"{self.base_url}/anime/anichin?link={link}"
            response = get(url, timeout=5)
            return response.json()
        except  Exception as e:
            return "An error occured report on @YBotsSupport\n\n{}".format(e)

    def kusonime(self, link):
        try:
            url = f"{self.base_url}/anime/kusonime?link={link}"
            response = get(url, timeout=5)
            return response.json()
        except  Exception as e:
            return "An error occured report on @YBotsSupport\n\n{}".format(e)

    def doronime(self, link):
        try:
            url = f"{self.base_url}/anime/doronime?link={link}"
            response = get(url, timeout=5)
            return response.json()
        except  Exception as e:
            return "An error occured report on @YBotsSupport\n\n{}".format(e)

    def rawkuma(self, link):
        try:
            url = f"{self.base_url}/manga/rawkuma?link={link}"
            response = get(url, timeout=5)
            return response.json()
        except  Exception as e:
            return "An error occured report on @YBotsSupport\n\n{}".format(e)

    def doudesu(self, link):
        try:
            url = f"{self.base_url}/manga/doudesu?link={link}"
            response = get(url, timeout=5)
            return response.json()
        except  Exception as e:
            return "An error occured report on @YBotsSupport\n\n{}".format(e)

    def anipics(self, category, tags):
        """
        Available category: nsfw
        Available tags: ahegao, waifu, neko, trap, bj
        """
        try:
            url = f"{self.base_url}/anime/{category}/{tags}"
            response = get(url, timeout=5)
            return response.json()
        except  Exception as e:
            return "An error occured report on @YBotsSupport\n\n{}".format(e)

    def genshin(self, path, query):
        """
        Available path: user, character, enemy, artifact, element, weapon
        """
        try:
            if path == "user":
                url = f"{self.base_url}/game/gi/user?uid={query}"
            if path == "character":
                url = f"{self.base_url}/game/gi/character?name={query}"
            if path == "enemy":
                url = f"{self.base_url}/game/gi/enemy?name={query}"
            if path == "artifact":
                url = f"{self.base_url}/game/gi/artifact?name={query}"
            if path == "element":
                url = f"{self.base_url}/game/gi/element?name={query}"
            if path == "weapon":
                url = f"{self.base_url}/game/gi/weapon?name={query}"
            else:
                return "Not a valid path.\nAvailable path: user, character, enemy, artifact, element, weapon"
            response = get(url, timeout=5)
            return response.json()
        except  Exception as e:
            return "An error occured report on @YBotsSupport\n\n{}".format(e)

    def brawl(self, path, query):
        """
        Available path: player, playerlog, club, clubmember, event
        """
        try:
            if path == "player":
                url = f"{self.deprecated_url}/game/brawl/player?playerTag={query}"
            if path == "playerlog":
                url = f"{self.deprecated_url}/game/brawl/player/log?playerTag={query}"
            if path == "club":
                url = f"{self.deprecated_url}/game/brawl/club?clubTag={query}"
            if path == "clubmember":
                url = f"{self.deprecated_url}/game/brawl/club/member?clubTag={query}"
            if path == "event":
                url = f"{self.deprecated_url}/game/brawl/event"
            else:
                return "Not a valid path.\nAvailable path: player, playerlog, club, clubmember, event"
            response = get(url, timeout=5)
            return response.json()
        except  Exception as e:
            return "An error occured report on @YBotsSupport\n\n{}".format(e)

    def google(self, query):
        try:
            url = f"{self.base_url}/google/search?query={query}"
            response = get(url, timeout=5)
            return response.json()
        except  Exception as e:
            return "An error occured report on @YBotsSupport\n\n{}".format(e)

    def lk21(self, query):
        try:
            url = f"{self.base_url}/lk21/search?title={query}"
            response = get(url, timeout=5)
            return response.json()
        except  Exception as e:
            return "An error occured report on @YBotsSupport\n\n{}".format(e)
