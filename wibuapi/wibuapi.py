from requests import get


class WibuAPI:
    def __init__(self):
        self.base_url = "https://wibu-api.eu.org/api"
        self.deprecated_url = "https://api.wibu-api.eu.org/api"

    def lendrive(self, link):
        try:
            url = f"{self.base_url}/anime/lendrive?link={link}"
            response = get(url, timeout=15)
            return response.json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    """
    def anichin(self, link):
        try:
            url = f"{self.base_url}/anime/anichin?link={link}"
            response = get(url, timeout=15)
            return response.json()
        except Exception as e:
            return "An error occured report on @YBotsSupport\n\n{}".format(e)
    """

    def kusonime(self, link):
        try:
            url = f"{self.base_url}/anime/kusonime?link={link}"
            response = get(url, timeout=15)
            return response.json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def doronime(self, link):
        try:
            url = f"{self.base_url}/anime/doronime?link={link}"
            response = get(url, timeout=15)
            return response.json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def rawkuma(self, link):
        try:
            url = f"{self.base_url}/manga/rawkuma?link={link}"
            response = get(url, timeout=15)
            return response.json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def westmanga(self, link):
        try:
            url = f"{self.base_url}/manga/westmanga?link={link}"
            response = get(url, timeout=15)
            return response.json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def doujindesu(self, link):
        try:
            url = f"{self.base_url}/manga/doudesu?link={link}"
            response = get(url, timeout=15)
            return response.json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def wibusubs(self, link):
        try:
            url = f"{self.base_url}/drama/wibusubs?link={link}"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def anipics(self, category, tags):
        """
        Available category: nsfw
        Available tags: ahegao, waifu, neko, trap, bj
        """
        try:
            if tags not in ["ahegao", "waifu", "neko", "trap", "bj"]:
                return (
                    "Not a valid tags.\nAvailable tags: ahegao, waifu, neko, trap, bj"
                )
            elif category != "nsfw":
                return "Not a valid category.\nAvailable category: nsfw"
            url = f"{self.base_url}/anime/{category}/{tags}"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def genshin(self, path, query):
        """
        Available path: user, character, enemy, artifact, element, weapon
        """
        try:
            if path == "artifact":
                url = f"{self.base_url}/game/gi/artifact?name={query}"
            elif path == "character":
                url = f"{self.base_url}/game/gi/character?name={query}"
            elif path == "element":
                url = f"{self.base_url}/game/gi/element?name={query}"
            elif path == "enemy":
                url = f"{self.base_url}/game/gi/enemy?name={query}"
            elif path == "user":
                url = f"{self.base_url}/game/gi/user?uid={query}"
            elif path == "weapon":
                url = f"{self.base_url}/game/gi/weapon?name={query}"
            else:
                return "Not a valid path.\nAvailable path: user, character, enemy, artifact, element, weapon"
            response = get(url, timeout=15)
            return response.json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def brawl(self, path, query):
        """
        Available path: player, playerlog, club, clubmember, event
        """
        try:
            if path == "club":
                url = f"{self.deprecated_url}/game/brawl/club?clubTag={query}"
            elif path == "clubmember":
                url = f"{self.deprecated_url}/game/brawl/club/member?clubTag={query}"
            elif path == "event":
                url = f"{self.deprecated_url}/game/brawl/event"
            elif path == "player":
                url = f"{self.deprecated_url}/game/brawl/player?playerTag={query}"
            elif path == "playerlog":
                url = f"{self.deprecated_url}/game/brawl/player/log?playerTag={query}"
            else:
                return "Not a valid path.\nAvailable path: player, playerlog, club, clubmember, event"
            response = get(url, timeout=15)
            return response.json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def google(self, query):
        try:
            url = f"{self.base_url}/google/search?query={query}"
            response = get(url, timeout=15)
            return response.json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def lk21(self, query):
        try:
            url = f"{self.base_url}/lk21/search?title={query}"
            response = get(url, timeout=15)
            return response.json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"
