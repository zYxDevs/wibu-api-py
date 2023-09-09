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
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def donghua(self, link: str):
        try:
            url = f"{self.base_url}/anime/donghua?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def anixlife(self, link: str):
        try:
            url = f"{self.base_url}/anime/anixlife?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def kazefuri(self, link: str):
        try:
            url = f"{self.base_url}/anime/kazefuri?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def anichin(self, link: str):
        try:
            url = f"{self.base_url}/anime/anichin?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def nekopoi(self, link: str):
        try:
            url = f"{self.base_url}/anime/nekopoi?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def hentaiguru(self, link: str):
        try:
            url = f"{self.base_url}/anime/hentaiguru?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def kusonime(self, link: str):
        try:
            url = f"{self.base_url}/anime/kusonime?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def doronime(self, link: str):
        try:
            url = f"{self.base_url}/anime/doronime?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def samehadaku(self, link: str):
        try:
            url = f"{self.base_url}/anime/samehadaku?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def kuramanime(self, link: str):
        try:
            url = f"{self.base_url}/anime/kuramanime?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def moenime(self, link: str):
        try:
            url = f"{self.base_url}/anime/moenime?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Manga, Manhua, Manhwa, Doujin
    def rawkuma(self, link: str):
        try:
            url = f"{self.base_url}/manga/rawkuma?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def yumekomik(self, link: str):
        try:
            url = f"{self.base_url}/manga/yumekomik?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def westmanga(self, link: str):
        try:
            url = f"{self.base_url}/manga/westmanga?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def komikindo(self, link: str):
        try:
            url = f"{self.base_url}/manga/komikindo?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def mangatale(self, link: str):
        try:
            url = f"{self.base_url}/manga/mangatale?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def kiryuu(self, link: str):
        try:
            url = f"{self.base_url}/manga/kiryuu?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def masterkomik(self, link: str):
        try:
            url = f"{self.base_url}/manga/masterkomik?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def mangakita(self, link: str):
        try:
            url = f"{self.base_url}/manga/mangakita?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def doujindesu(self, link: str):
        try:
            url = f"{self.base_url}/manga/doudesu?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def crotpedia(self, link: str):
        try:
            url = f"{self.base_url}/manga/crotpedia?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Drama, Film
    def wibusubs(self, link: str):
        try:
            url = f"{self.base_url}/drama/wibusubs?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def adikfilm(self, link: str):
        try:
            url = f"{self.base_url}/film/adikfilm?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def mydramalist_search(self, query: str):
        try:
            url = f"{self.base_url}/drama/search?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Anime Ost, Theme Song, Anime Song
    def sukidesuost_search(self, query: str, page: int):
        try:
            url = f"{self.base_url}/music/sukidesuost/search?query={query}&page={page}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def sukidesuost(self, link: str):
        try:
            url = f"{self.base_url}/music/sukidesuost?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def hikarinoakari(self, link: str):
        try:
            url = f"{self.base_url}/music/hikarinoakari?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Search Engine and Web Search Parser
    def google(self, query: str):
        try:
            url = f"{self.base_url}/google/search?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def lk21(self, query: str):
        try:
            url = f"{self.base_url}/lk21/search?title={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Reverse Image Search
    def yandex_reverse_image(self, image_url: str):
        try:
            url = f"{self.base_url}/yandex/reverse_image?image_url={image_url}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Lyrics Search
    def anilyrics_search(self, query: str):
        try:
            url = f"{self.base_url}/anime/lyrics/search?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def anilyrics(self, link: str, type: str):
        """
        Available lyrics type: romaji, kanji, english
        """
        try:
            url = f"{self.base_url}/anime/lyrics?link={link}&type={type}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def lyrics(self, query: str):
        try:
            url = f"{self.base_url}/lyrics/search?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Anipics, Porn, JAV, Booru
    def anipics(self, category: str, tags: str):
        """
        Available category: nsfw
        Available tags: ahegao, waifu, neko, trap, bj
        """
        try:
            url = f"{self.base_url}/anime/{category}/{tags}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def jav(self):
        try:
            url = f"{self.base_url}/porn/jav"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def porn_gif(self):
        try:
            url = f"{self.base_url}/porn/gif"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def realbooru_nsfw(self):
        try:
            url = f"{self.base_url}/booru/nsfw/rb"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def gelbooru_nsfw(self):
        try:
            url = f"{self.base_url}/booru/nsfw/gb"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def gelbooru_sfw(self):
        try:
            url = f"{self.base_url}/booru/sfw/gb"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def safebooru_sfw(self):
        try:
            url = f"{self.base_url}/booru/sfw/sb"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Genshin Impact Game
    def giUser(self, uid: int):
        try:
            url = f"{self.base_url}/game/gi/user?uid={uid}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def giWeapon(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/weapon?name={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def giEnemy(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/enemy?name={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def giElement(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/element?name={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def giCharacter(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/character?name={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def giArtifact(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/artifact?name={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Brawlstars Game
    def brawlClub(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/club?clubTag={tag}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def brawlClubMember(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/club/member?clubTag={tag}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def brawlEvent(self):
        try:
            url = f"{self.deprecated_url}/game/brawl/event"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def brawlPlayer(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/player?playerTag={tag}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def brawlPlayerLog(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/player/log?playerTag={tag}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Urban Dictionary
    def ud(self, query: str):
        try:
            url = f"{self.base_url}/etc/ud?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Other Endpoints
    def youtube(self, url: str):
        """
        https://www.youtube.com/watch?v=a1V0UbBNliM
        """
        try:
            url = f"{self.base_url}/etc/youtube?url={url}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def facebook(self, url: str):
        try:
            url = f"{self.base_url}/etc/facebook?url={url}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def device(self, query: str):
        try:
            url = f"{self.base_url}/etc/gsm/search?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def slug(self, query: str):
        try:
            url = f"{self.base_url}/etc/gsm/slug?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Encode and Decode
    def b64encode(self, query: str):
        try:
            url = f"{self.base_url}/encode/base64?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def b64decode(self, query: str):
        try:
            url = f"{self.base_url}/decode/base64?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Tools
    def ip_lookup(self, ip: str):
        try:
            url = f"{self.base_url}/lookup/ip?ip={ip}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def pypi_search(self, query: str, page: int):
        try:
            url = f"{self.base_url}/pypi/search?query={query}&page={page}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    def npm_search(self, query: str):
        try:
            url = f"{self.base_url}/npm/search?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Bypasser
    def terabox(self, url: str):
        try:
            url = f"{self.base_url}/bypass/terabox?url={url}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"
