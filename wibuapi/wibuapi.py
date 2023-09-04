# (c) 2022-2023 Yoga Pranata a.k.a zYxDevs
# This file contains all api path from wibuapi.

from requests import get


class WibuAPI:
    def __init__(self):
        self.base_url = "https://wibu-api.eu.org/api"
        self.deprecated_url = "https://api.wibu-api.eu.org/api"

    # Anime, Donghua, Hentai
    def lendrive(self, link: str):
        try:
            url = f"{self.base_url}/anime/lendrive?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def donghua(self, link: str):
        try:
            url = f"{self.base_url}/anime/donghua?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def anixlife(self, link: str):
        try:
            url = f"{self.base_url}/anime/anixlife?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def kazefuri(self, link: str):
        try:
            url = f"{self.base_url}/anime/kazefuri?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def anichin(self, link: str):
        try:
            url = f"{self.base_url}/anime/anichin?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def nekopoi(self, link: str):
        try:
            url = f"{self.base_url}/anime/nekopoi?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def hentaiguru(self, link: str):
        try:
            url = f"{self.base_url}/anime/hentaiguru?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def kusonime(self, link: str):
        try:
            url = f"{self.base_url}/anime/kusonime?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def doronime(self, link: str):
        try:
            url = f"{self.base_url}/anime/doronime?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def samehadaku(self, link: str):
        try:
            url = f"{self.base_url}/anime/samehadaku?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def kuramanime(self, link: str):
        try:
            url = f"{self.base_url}/anime/kuramanime?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def moenime(self, link: str):
        try:
            url = f"{self.base_url}/anime/moenime?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # Manga, Manhua, Manhwa, Doujin
    def rawkuma(self, link: str):
        try:
            url = f"{self.base_url}/manga/rawkuma?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def yumekomik(self, link: str):
        try:
            url = f"{self.base_url}/manga/yumekomik?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def westmanga(self, link: str):
        try:
            url = f"{self.base_url}/manga/westmanga?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def komikindo(self, link: str):
        try:
            url = f"{self.base_url}/manga/komikindo?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def mangatale(self, link: str):
        try:
            url = f"{self.base_url}/manga/mangatale?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def kiryuu(self, link: str):
        try:
            url = f"{self.base_url}/manga/kiryuu?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def masterkomik(self, link: str):
        try:
            url = f"{self.base_url}/manga/masterkomik?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def mangakita(self, link: str):
        try:
            url = f"{self.base_url}/manga/mangakita?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def doujindesu(self, link: str):
        try:
            url = f"{self.base_url}/manga/doudesu?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def crotpedia(self, link: str):
        try:
            url = f"{self.base_url}/manga/crotpedia?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # Drama, Film
    def wibusubs(self, link: str):
        try:
            url = f"{self.base_url}/drama/wibusubs?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def adikfilm(self, link: str):
        try:
            url = f"{self.base_url}/film/adikfilm?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def mydramalist_search(self, query: str):
        try:
            url = f"{self.base_url}/drama/search?query={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # Anime Ost, Theme Song, Anime Song
    def sukidesuost_search(self, query: str, page: int):
        try:
            url = f"{self.base_url}/music/sukidesuost/search?query={query}&page={page}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def sukidesuost(self, link: str):
        try:
            url = f"{self.base_url}/music/sukidesuost?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def hikarinoakari(self, link: str):
        try:
            url = f"{self.base_url}/music/hikarinoakari?link={link}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # Search Engine and Web Search Parser
    def google(self, query: str):
        try:
            url = f"{self.base_url}/google/search?query={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def lk21(self, query: str):
        try:
            url = f"{self.base_url}/lk21/search?title={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # Reverse Image Search
    def yandex_reverse_image(self, image_url: str):
        try:
            url = f"{self.base_url}/yandex/reverse_image?image_url={image_url}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # Lyrics Search
    def anilyrics_search(self, query: str):
        try:
            url = f"{self.base_url}/anime/lyrics/search?query={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def anilyrics(self, link: str, type: str):
        """
        Available lyrics type: romaji, kanji, english
        """
        try:
            url = f"{self.base_url}/anime/lyrics?link={link}&type={type}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def lyrics(self, query: str):
        try:
            url = f"{self.base_url}/lyrics/search?query={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # Lewd Pics
    def anipics(self, category: str, tags: str):
        """
        Available category: nsfw
        Available tags: ahegao, waifu, neko, trap, bj
        """
        try:
            url = f"{self.base_url}/anime/{category}/{tags}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # Genshin Impact Game
    def giUser(self, uid: int):
        try:
            url = f"{self.base_url}/game/gi/user?uid={uid}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def giWeapon(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/weapon?name={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def giEnemy(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/enemy?name={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def giElement(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/element?name={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def giCharacter(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/character?name={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def giArtifact(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/artifact?name={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # Brawlstars Game
    def brawlClub(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/club?clubTag={tag}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def brawlClubMember(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/club/member?clubTag={tag}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def brawlEvent(self):
        try:
            url = f"{self.deprecated_url}/game/brawl/event"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def brawlPlayer(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/player?playerTag={tag}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def brawlPlayerLog(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/player/log?playerTag={tag}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # Urban Dictionary
    def ud(self, query: str):
        try:
            url = f"{self.base_url}/etc/ud?query={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # Other Endpoints
    def youtube(self, url: str):
        """
        https://www.youtube.com/watch?v=a1V0UbBNliM
        """
        try:
            url = f"{self.base_url}/etc/youtube?url={url}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def facebook(self, url: str):
        try:
            url = f"{self.base_url}/etc/facebook?url={url}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def device(self, query: str):
        try:
            url = f"{self.base_url}/etc/gsm/search?query={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def slug(self, query: str):
        try:
            url = f"{self.base_url}/etc/gsm/slug?query={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # Encode and Decode
    def b64encode(self, query: str):
        try:
            url = f"{self.base_url}/encode/base64?query={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    def b64decode(self, query: str):
        try:
            url = f"{self.base_url}/decode/base64?query={query}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # IP Lookup
    def ip_lookup(self, ip: str):
        try:
            url = f"{self.base_url}/lookup/ip?ip={ip}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"

    # Bypasser
    def terabox(self, url: str):
        try:
            url = f"{self.base_url}/bypass/terabox?url={url}"
            response = get(url, timeout=15).json()
            return response
        except Exception as e:
            return f"An error occured report on https://t.me/YBotsSupport\n\n{e}"
