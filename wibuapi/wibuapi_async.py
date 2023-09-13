from .utils import getwibu


class AsyncWibuAPI:
    def __init__(self):
        self.base_url = "https://wibu-api.eu.org/api"
        self.deprecated_url = "https://api.wibu-api.eu.org/api"

    # Anime, Donghua, Hentai
    async def lendrive(self, link: str):
        try:
            url = f"{self.base_url}/anime/lendrive?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def donghua(self, link: str):
        try:
            url = f"{self.base_url}/anime/donghua?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def anixlife(self, link: str):
        try:
            url = f"{self.base_url}/anime/anixlife?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def kazefuri(self, link: str):
        try:
            url = f"{self.base_url}/anime/kazefuri?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def anichin(self, link: str):
        try:
            url = f"{self.base_url}/anime/anichin?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def nekopoi(self, link: str):
        try:
            url = f"{self.base_url}/anime/nekopoi?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def hentaiguru(self, link: str):
        try:
            url = f"{self.base_url}/anime/hentaiguru?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def kusonime(self, link: str):
        try:
            url = f"{self.base_url}/anime/kusonime?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def doronime(self, link: str):
        try:
            url = f"{self.base_url}/anime/doronime?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def samehadaku(self, link: str):
        try:
            url = f"{self.base_url}/anime/samehadaku?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def kuramanime(self, link: str):
        try:
            url = f"{self.base_url}/anime/kuramanime?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def moenime(self, link: str):
        try:
            url = f"{self.base_url}/anime/moenime?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Manga, Manhua, Manhwa, Doujin
    async def rawkuma(self, link: str):
        try:
            url = f"{self.base_url}/manga/rawkuma?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def yumekomik(self, link: str):
        try:
            url = f"{self.base_url}/manga/yumekomik?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def westmanga(self, link: str):
        try:
            url = f"{self.base_url}/manga/westmanga?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def komikindo(self, link: str):
        try:
            url = f"{self.base_url}/manga/komikindo?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def mangatale(self, link: str):
        try:
            url = f"{self.base_url}/manga/mangatale?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def kiryuu(self, link: str):
        try:
            url = f"{self.base_url}/manga/kiryuu?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def masterkomik(self, link: str):
        try:
            url = f"{self.base_url}/manga/masterkomik?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def mangakita(self, link: str):
        try:
            url = f"{self.base_url}/manga/mangakita?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def doujindesu(self, link: str):
        try:
            url = f"{self.base_url}/manga/doudesu?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def crotpedia(self, link: str):
        try:
            url = f"{self.base_url}/manga/crotpedia?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Drama, Film
    async def wibusubs(self, link: str):
        try:
            url = f"{self.base_url}/drama/wibusubs?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def adikfilm(self, link: str):
        try:
            url = f"{self.base_url}/film/adikfilm?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def mydramalist_search(self, query: str):
        try:
            url = f"{self.base_url}/drama/search?query={query}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Anime Ost, Theme Song, Anime Song
    async def sukidesuost_search(self, query: str, page: int):
        try:
            url = f"{self.base_url}/music/sukidesuost/search?query={query}&page={page}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def sukidesuost(self, link: str):
        try:
            url = f"{self.base_url}/music/sukidesuost?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def hikarinoakari(self, link: str):
        try:
            url = f"{self.base_url}/music/hikarinoakari?link={link}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Search Engine and Web Search Parser
    async def google(self, query: str):
        try:
            url = f"{self.base_url}/google/search?query={query}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def lk21(self, query: str):
        try:
            url = f"{self.base_url}/lk21/search?title={query}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Reverse Image Search
    async def yandex_reverse_image(self, image_url: str):
        try:
            url = f"{self.base_url}/yandex/reverse_image?image_url={image_url}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Lyrics Search
    async def anilyrics_search(self, query: str):
        try:
            url = f"{self.base_url}/anime/lyrics/search?query={query}"
            return await getwibu(url, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async
