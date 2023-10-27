# (c) 2022-2023 Yoga Pranata a.k.a zYxDevs
# This file contains all api path from wibuapi.

from .utils import getwibu


class AsyncWibuAPI:
    def __init__(self, apikey: str = ""):
        self.base_url = "https://wibu-api.eu.org/api"
        self.deprecated_url = "https://api.wibu-api.eu.org/api"
        self.headers = {"x-wibu-key": apikey}

    # Anime, Donghua, Hentai
    async def lendrive(self, link: str):
        try:
            url = f"{self.base_url}/anime/lendrive?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def donghua(self, link: str):
        try:
            url = f"{self.base_url}/anime/donghua?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def anixlife(self, link: str):
        try:
            url = f"{self.base_url}/anime/anixlife?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def kazefuri(self, link: str):
        try:
            url = f"{self.base_url}/anime/kazefuri?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def anichin(self, link: str):
        try:
            url = f"{self.base_url}/anime/anichin?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def nekopoi(self, link: str):
        try:
            url = f"{self.base_url}/anime/nekopoi?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def hentaiguru(self, link: str):
        try:
            url = f"{self.base_url}/anime/hentaiguru?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def kusonime(self, link: str):
        try:
            url = f"{self.base_url}/anime/kusonime?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def doronime(self, link: str):
        try:
            url = f"{self.base_url}/anime/doronime?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def samehadaku(self, link: str):
        try:
            url = f"{self.base_url}/anime/samehadaku?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def kuramanime(self, link: str):
        try:
            url = f"{self.base_url}/anime/kuramanime?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def moenime(self, link: str):
        try:
            url = f"{self.base_url}/anime/moenime?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Manga, Manhua, Manhwa, Doujin
    async def rawkuma(self, link: str):
        try:
            url = f"{self.base_url}/manga/rawkuma?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def yumekomik(self, link: str):
        try:
            url = f"{self.base_url}/manga/yumekomik?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def westmanga(self, link: str):
        try:
            url = f"{self.base_url}/manga/westmanga?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def komikindo(self, link: str):
        try:
            url = f"{self.base_url}/manga/komikindo?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def mangatale(self, link: str):
        try:
            url = f"{self.base_url}/manga/mangatale?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def kiryuu(self, link: str):
        try:
            url = f"{self.base_url}/manga/kiryuu?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def masterkomik(self, link: str):
        try:
            url = f"{self.base_url}/manga/masterkomik?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def mangakita(self, link: str):
        try:
            url = f"{self.base_url}/manga/mangakita?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def doujindesu(self, link: str):
        try:
            url = f"{self.base_url}/manga/doudesu?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def crotpedia(self, link: str):
        try:
            url = f"{self.base_url}/manga/crotpedia?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Drama, Film
    async def wibusubs(self, link: str):
        try:
            url = f"{self.base_url}/drama/wibusubs?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def adikfilm(self, link: str):
        try:
            url = f"{self.base_url}/film/adikfilm?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def mydramalist_search(self, query: str):
        try:
            url = f"{self.base_url}/drama/search?query={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Novel
    async def novelupdates_search(self, query: str):
        try:
            url = f"{self.base_url}/novel/novelupdates/search?query={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def noveltoon_search(self, query: str, language: str):
        try:
            url = f"{self.base_url}/novel/noveltoon/search?query={query}&language={language}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def noveltoon_chapter(self, link: str):
        try:
            url = f"{self.base_url}/novel/noveltoon/chapter?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def noveltoon_read(self, link: str):
        try:
            url = f"{self.base_url}/novel/noveltoon/read?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Anime Ost, Theme Song, Anime Song
    async def sukidesuost_search(self, query: str, page: int):
        try:
            url = f"{self.base_url}/music/sukidesuost/search?query={query}&page={page}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def sukidesuost(self, link: str):
        try:
            url = f"{self.base_url}/music/sukidesuost?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def hikarinoakari(self, link: str):
        try:
            url = f"{self.base_url}/music/hikarinoakari?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Search Engine and Web Search Parser
    async def google(self, query: str):
        try:
            url = f"{self.base_url}/google/search?query={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def lk21(self, query: str):
        try:
            url = f"{self.base_url}/lk21/search?title={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Reverse Image Search
    async def yandex_reverse_image(self, image_url: str):
        try:
            url = f"{self.base_url}/yandex/reverse_image?image_url={image_url}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Lyrics Search
    async def anilyrics_search(self, query: str):
        try:
            url = f"{self.base_url}/anime/lyrics/search?query={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def anilyrics(self, link: str, type: str):
        """
        Available lyrics type: romaji, kanji, english
        """
        try:
            url = f"{self.base_url}/anime/lyrics?link={link}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def lyrics(self, query: str):
        try:
            url = f"{self.base_url}/lyrics/search?query={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Anipics, Porn, JAV, Booru
    async def anipics(self, tags: str, category: str):
        if tags not in ("sfw", "nsfw"):
            return f"Tags {tags} is unknown. Available tags: sfw, nsfw"
        try:
            url = f"{self.base_url}/anipics/{tags}/{category}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def jav(self):
        try:
            url = f"{self.base_url}/porn/jav"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def porn_gif(self):
        try:
            url = f"{self.base_url}/porn/gif"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def realbooru_nsfw(self):
        try:
            url = f"{self.base_url}/booru/nsfw/rb"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def gelbooru_nsfw(self):
        try:
            url = f"{self.base_url}/booru/nsfw/gb"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def gelbooru_sfw(self):
        try:
            url = f"{self.base_url}/booru/sfw/gb"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def safebooru_sfw(self):
        try:
            url = f"{self.base_url}/booru/sfw/sb"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Genshin Impact Game
    async def giUser(self, uid: int):
        try:
            url = f"{self.base_url}/game/gi/user?uid={uid}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def giWeapon(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/weapon?name={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def giEnemy(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/enemy?name={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def giElement(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/element?name={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def giCharacter(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/character?name={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def giArtifact(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/artifact?name={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Brawlstars Game
    async def brawlClub(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/club?clubTag={tag}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def brawlClubMember(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/club?clubTag={tag}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def brawlEvent(self):
        try:
            url = f"{self.deprecated_url}/game/brawl/event"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def brawlPlayer(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/player?playerTag={tag}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def brawlPlayerLog(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/player/log?playerTag={tag}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Urban Dictionary
    async def ud(self, query: str):
        try:
            url = f"{self.base_url}/etc/ud?query={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Other Endpoints
    async def youtube(self, url: str):
        """https://www.youtube.com/watch?v=a1V0UbBNliM"""
        try:
            url = f"{self.base_url}/etc/youtube?url={url}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def facebook(self, url: str):
        """https://www.facebook.com/groups/247539486825123/permalink/628642412048160"""
        try:
            url = f"{self.base_url}/etc/facebook?url={url}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def device(self, query: str):
        try:
            url = f"{self.base_url}/etc/gsm/search?query={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def device(self, query: str):
        try:
            url = f"{self.base_url}/etc/gsm/search?query={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def slug(self, query: str):
        try:
            url = f"{self.base_url}/etc/gsm/slug?query={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Encode and Decode
    async def b64encode(self, query: str):
        try:
            url = f"{self.base_url}/encode/base64?query={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def b64decode(self, query: str):
        try:
            url = f"{self.base_url}/decode/base64?query={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Tools
    async def ip_lookup(self, ip: str):
        try:
            url = f"{self.base_url}/lookup/ip?ip={ip}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def pypi_search(self, query: str, page: int):
        try:
            url = f"{self.base_url}/pypi/search?query={query}&page={page}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def npm_search(self, query: str):
        try:
            url = f"{self.base_url}/npm/search?query={query}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Bypasser
    async def terabox(self, url: str):
        try:
            url = f"{self.base_url}/bypass/terabox?url={url}"
            return await getwibu(url, headers=self.headers, timeout=15)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    # Chatbot AI
    async def bard(self, query: str, cookie: str = ""):
        try:
            url = f"{self.base_url}/chatbot/bard?query={query}&cookie={cookie}"
            return await getwibu(url, headers=self.headers, timeout=50)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"

    async def gpt(self, query: str, gpt_key: str = ""):
        try:
            url = f"{self.base_url}/chatbot/gpt?query={query}&gpt_key={gpt_key}"
            return await getwibu(url, headers=self.headers, timeout=50)
        except Exception as e:
            return f"ERROR: {str(e)}. Report to https://t.me/YBotsSupport"
