from json import dumps
from requests import get


class WibuAPI:
    def __init__(self):
        self.base_url = "https://wibu-api.eu.org/api"
        self.deprecated_url = "https://api.wibu-api.eu.org/api"

    def status(self):
        try:
            url = f"{self.base_url}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def lendrive(self, link: str):
        try:
            url = f"{self.base_url}/anime/lendrive?link={link}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    """
    def anichin(self, link: str):
        try:
            url = f"{self.base_url}/anime/anichin?link={link}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return "An error occured report on @YBotsSupport\n\n{}".format(e)
    """

    def kusonime(self, link: str):
        try:
            url = f"{self.base_url}/anime/kusonime?link={link}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def doronime(self, link: str):
        try:
            url = f"{self.base_url}/anime/doronime?link={link}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def rawkuma(self, link: str):
        try:
            url = f"{self.base_url}/manga/rawkuma?link={link}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def westmanga(self, link: str):
        try:
            url = f"{self.base_url}/manga/westmanga?link={link}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def doujindesu(self, link: str):
        try:
            url = f"{self.base_url}/manga/doudesu?link={link}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def wibusubs(self, link: str):
        try:
            url = f"{self.base_url}/drama/wibusubs?link={link}"
            response = get(url, timeout=5).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def anipics(self, category: str, tags: str):
        """
        Available category: nsfw
        Available tags: ahegao, waifu, neko, trap, bj
        """
        try:
            url = f"{self.base_url}/anime/{category}/{tags}"
            response = get(url, timeout=5).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def giUser(self, uid: int):
        try:
            url = f"{self.base_url}/game/gi/user?uid={uid}"
            response = get(url, timeout=5).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def giWeapon(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/weapon?name={query}"
            response = get(url, timeout=5).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def giEnemy(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/enemy?name={query}"
            response = get(url, timeout=5).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def giElement(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/element?name={query}"
            response = get(url, timeout=5).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def giCharacter(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/character?name={query}"
            response = get(url, timeout=5).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def giArtifact(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/artifact?name={query}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def brawlClub(self, tag: str):
        try:
            url = f"{self.deprecated_url}/game/brawl/club?clubTag={query}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def brawlClubMember(self, tag: str):
        try:
            url = f"{self.deprecated_url}/game/brawl/club/member?clubTag={tag}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def brawlEvent(self):
        try:
            url = f"{self.deprecated_url}/game/brawl/event"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def brawlPlayer(self, tag: str):
        try:
            url = f"{self.deprecated_url}/game/brawl/player?playerTag={tag}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def brawlPlayerLog(self, tag: str):
        try:
            url = f"{self.deprecated_url}/game/brawl/player/log?playerTag={query}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def google(self, query: str):
        try:
            url = f"{self.base_url}/google/search?query={query}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def lk21(self, query: str):
        try:
            url = f"{self.base_url}/lk21/search?title={query}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def ud(self, query: str):
        try:
            url = f"{self.base_url}/etc/ud?query={query}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def wall(self, query: str):
        try:
            url = f"{self.base_url}/etc/wallhd?query={query}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def youtube(self, url: str):
        try:
            url = f"{self.base_url}/etc/youtube?query={url}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def device(self, query: str):
        try:
            url = f"{self.base_url}/etc/gsm/search?query={query}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def slug(self, query: str):
        try:
            url = f"{self.base_url}/etc/gsm/slug?query={query}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"
