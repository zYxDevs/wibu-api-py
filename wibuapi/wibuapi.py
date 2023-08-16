# (c) 2022-2023 Yoga Pranata a.k.a zYxDevs
# This file contains all api path from wibuapi.

from requests import get


class WibuAPI:
    def __init__(self):
        self.base_url = "https://wibu-api.eu.org/api"
        self.deprecated_url = "https://api.wibu-api.eu.org/api"

    def lendrive(self, link: str):
        """works with batch, bd, and single eps link
        https://lendrive.web.id/tondemo-skill-de-isekai-hourou-meshi-ep-04-dual-subs-x265-hevc-subtitle-indonesia-english/
        """
        try:
            url = f"{self.base_url}/anime/lendrive?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def donghua(self, link: str):
        """works with batch, bd, and single eps link
        https://donghua.web.id/soul-land-season-2-episode-224-250
        """
        try:
            url = f"{self.base_url}/anime/donghua?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def anixlife(self, link: str):
        """works with batch, bd, and single eps link
        https://anixverse.com/battle-through-the-heavens-season-5-episode-56-subtitle-indonesia/
        """
        try:
            url = f"{self.base_url}/anime/anixlife?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def kazefuri(self, link: str):
        """works with batch, bd, and single eps link
        https://kazefuri.vip/shrouding-the-heavens-episode-17-subtitle-indonesia/
        """
        try:
            url = f"{self.base_url}/anime/kazefuri?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def anichin(self, link: str):
        """works with batch, bd, and single eps link
        https://anichin.vip/soul-land-season-2-episode-226-252-subtitle-indonesia/
        """
        try:
            url = f"{self.base_url}/anime/anichin?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def nekopoi(self, link: str):
        """works with single eps link
        https://nekopoi.care/koumi-jima-shuu-7-de-umeru-mesu-tachi-episode-1-subtitle-indonesia/
        """
        try:
            url = f"{self.base_url}/anime/nekopoi?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def hentaiguru(self, link: str):
        """works with batch, bd, and single eps link
        https://hentai.guru/hentai/fushigi-no-kuni-no-succubus/
        """
        try:
            url = f"{self.base_url}/anime/hentaiguru?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def kusonime(self, link: str):
        """works with batch, bd, and single eps link
        https://kusonime.com/isekai-ojisan-batch-subtitle-indonesia/
        """
        try:
            url = f"{self.base_url}/anime/kusonime?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def doronime(self, link: str):
        """works with batch, bd, and single eps link
        https://doroni.me/anime/om-ke-isekai/batch
        """
        try:
            url = f"{self.base_url}/anime/doronime?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def samehadaku(self, link: str):
        """works with batch, bd, and single eps link
        https://samehadaku.run/nierautomata-ver1-1a-episode-8/
        """
        try:
            url = f"{self.base_url}/anime/samehadaku?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def kuramanime(self, link: str):
        """works with batch, bd, and single eps link
        https://kuramanime.art/anime/2004/mushoku-tensei-isekai-ittara-honki-dasu-shugo-jutsushi-fitz/episode/1
        """
        try:
            url = f"{self.base_url}/anime/kuramanime?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def moenime(self, link: str):
        """works with batch, bd, and single eps link
        https://moenime.com/liar-liar-sub-indo/
        """
        try:
            url = f"{self.base_url}/anime/moenime?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def rawkuma(self, link: str):
        """works with list and single chapter
        list: https://rawkuma.com/manga/guilty-circle/
        single: https://rawkuma.com/guilty-circle-chapter-83/
        """
        try:
            url = f"{self.base_url}/manga/rawkuma?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def yumekomik(self, link: str):
        """works with list and single chapter
        list: https://yumekomik.com/manga/watashi-yori-tsuyoi-otoko-to-kekkon-shitai-no/
        single: https://yumekomik.com/watashi-yori-tsuyoi-otoko-to-kekkon-shitai-no-chapter-08-bahasa-indonesia/
        """
        try:
            url = f"{self.base_url}/manga/yumekomik?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def westmanga(self, link: str):
        """works with list and single chapter
        list: https://westmanga.info/manga/kaifuku-jutsushi-no-yarinaoshi/
        single: https://westmanga.info/kaifuku-jutsushi-no-yarinaoshi-chapter-52-1-bahasa-indonesia/
        """
        try:
            url = f"{self.base_url}/manga/westmanga?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def komikindo(self, link: str):
        """work with list and single chapter
        list: https://komikindo.co/manga/yuusha-ni-zenbu-ubawareta-ore-wa-yuusha-no-hahaoya-to-party-wo-kumimashita/
        single: https://komikindo.co/yuusha-ni-zenbu-ubawareta-ore-wa-yuusha-no-hahaoya-to-party-wo-kumimashita-chapter-04/
        """
        try:
            url = f"{self.base_url}/manga/komikindo?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def mangatale(self, link: str):
        """work with list and single chapter
        list: https://mangatale.co/manga/dungeon-odyssey/
        single: https://mangatale.co/dungeon-odyssey-chapter-40/
        """
        try:
            url = f"{self.base_url}/manga/mangatale?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def kiryuu(self, link: str):
        """work with list and single chapter
        list: https://kiryuu.id/manga/a-rank-boukensha-no-slow-life/
        single: https://kiryuu.id/a-rank-boukensha-no-slow-life-chapter-39-3/
        """
        try:
            url = f"{self.base_url}/manga/kiryuu?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def masterkomik(self, link: str):
        """work with list and single chapter
        list: https://masterkomik.com/manga/max-level-player/
        single: https://masterkomik.com/max-level-player-chapter-07/
        """
        try:
            url = f"{self.base_url}/manga/masterkomik?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def mangakita(self, link: str):
        """work with list and single chapter
        list: https://mangakita.net/manga/please-go-home-akutsu-san/
        single: https://mangakita.net/please-go-home-akutsu-san-chapter-137/
        """
        try:
            url = f"{self.base_url}/manga/mangakita?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def doujindesu(self, link: str):
        """works with list and single chapter
        list: https://212.32.226.234/manga/i-cant-stand-it-ajumma/
        single: https://212.32.226.234/i-cant-stand-it-ajumma-chapter-20/
        """
        try:
            url = f"{self.base_url}/manga/doudesu?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def crotpedia(self, link: str):
        """works with list chapter
        list: https://38.242.194.12/baca/series/young-housemaid/
        """
        try:
            url = f"{self.base_url}/manga/crotpedia?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def wibusubs(self, link: str):
        """work with single post link (may bug sometimes)
        https://www.wibusubs.moe/2023/03/brother-trap-2023-09-tamat-subtitle.html
        """
        try:
            url = f"{self.base_url}/drama/wibusubs?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def adikfilm(self, link: str):
        """work with single post link (may bug sometimes)
        https://adikfilm.click/zom-100-bucket-list-of-the-dead-2023/
        """
        try:
            url = f"{self.base_url}/film/adikfilm?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def sukidesuost(self, link: str):
        try:
            url = f"{self.base_url}/music/sukidesuost?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def hikarinoakari(self, link: str):
        try:
            url = f"{self.base_url}/music/hikarinoakari?link={link}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def google(self, query: str):
        try:
            url = f"{self.base_url}/google/search?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def lk21(self, query: str):
        try:
            url = f"{self.base_url}/lk21/search?title={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def sukidesuost_search(self, query: str, page: int):
        try:
            url = f"{self.base_url}/music/sukidesuost/search?query={query}&page={page}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def anilyrics_search(self, query: str):
        try:
            url = f"{self.base_url}/anime/lyrics/search?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def anilyrics(self, link: str, type: str):
        """
        Available lyrics type: romaji, kanji, english
        """
        try:
            url = f"{self.base_url}/anime/lyrics?link={link}&type={type}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def anipics(self, category: str, tags: str):
        """
        Available category: nsfw
        Available tags: ahegao, waifu, neko, trap, bj
        """
        try:
            url = f"{self.base_url}/anime/{category}/{tags}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def giUser(self, uid: int):
        try:
            url = f"{self.base_url}/game/gi/user?uid={uid}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def giWeapon(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/weapon?name={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def giEnemy(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/enemy?name={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def giElement(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/element?name={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def giCharacter(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/character?name={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def giArtifact(self, query: str):
        try:
            url = f"{self.base_url}/game/gi/artifact?name={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def brawlClub(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/club?clubTag={tag}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def brawlClubMember(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/club/member?clubTag={tag}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def brawlEvent(self):
        try:
            url = f"{self.deprecated_url}/game/brawl/event"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def brawlPlayer(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/player?playerTag={tag}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def brawlPlayerLog(self, tag: str):
        try:
            if "#" not in tag:
                tag = f"%23{tag}"
            tag = tag.replace("#", "%23")
            url = f"{self.deprecated_url}/game/brawl/player/log?playerTag={tag}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def ud(self, query: str):
        try:
            url = f"{self.base_url}/etc/ud?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def youtube(self, url: str):
        """tested on youtube video link, other not tested yet
        https://www.youtube.com/watch?v=a1V0UbBNliM
        """
        try:
            url = f"{self.base_url}/etc/youtube?url={url}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def device(self, query: str):
        try:
            url = f"{self.base_url}/etc/gsm/search?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def slug(self, query: str):
        try:
            url = f"{self.base_url}/etc/gsm/slug?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def b64encode(self, query: str):
        try:
            url = f"{self.base_url}/encode/base64?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def b64decode(self, query: str):
        try:
            url = f"{self.base_url}/decode/base64?query={query}"
            return get(url, timeout=15).json()
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"
