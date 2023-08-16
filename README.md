# Wibu-API-Py
[![Downloads](https://static.pepy.tech/badge/wibuapi)](https://pepy.tech/project/wibuapi)  [![Repo Size](https://img.shields.io/github/repo-size/zYxDevs/wibu-api-py?style=flat-square)](https://github.com/zYxDevs/wibu-api-py)  [![Languages](https://img.shields.io/github/languages/top/zYxDevs/wibu-api-py?style=flat-square)](https://github.com/zYxDevs/wibu-api-py)  [![CodeFactor](https://www.codefactor.io/repository/github/zYxDevs/wibu-api-py/badge)](https://www.codefactor.io/repository/github/zYxDevs/wibu-api-py)  [![Codacy Badge](https://app.codacy.com/project/badge/Grade/8b87ea2387574f54849805430a9bc9ea)](https://www.codacy.com/gh/zYxDevs/wibu-api-py/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=zYxDevs/wibu-api-py&amp;utm_campaign=Badge_Grade)

_Official Python Wrapper for Wibu API._

[![wibu-api-py](https://socialify.git.ci/zYxDevs/wibu-api-py/image?description=1&font=Source%20Code%20Pro&forks=1&issues=1&language=1&logo=https%3A%2F%2F1000logos.net%2Fwp-content%2Fuploads%2F2021%2F04%2FTelegram-logo.png&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Light)](https://t.me/SpreadNetworks)

## How to install
#### Use pip
```
pip3 install wibuapi
```
```
pip3 install git+https://github.com/zYxDevs/wibu-api-py
```

#### Get latest update
```
pip3 install -U wibuapi
```

#### Install from repo
```shell
root@zyxdevs:~ git clone https://github.com/zYxDevs/wibu-api-py wibuapi
root@zyxdevs:~ cd wibuapi
root@zyxdevs:~ python3 setup.py install
```

## Telegram Bot:
_There's many useful features in bot but it required big resource, so i make it for paid users only. If you interest to buy PM me on Telegram._

**Paid Features:**

- [x] All features on WibuAPI
- [x] LH Translation ziper
- [x] Shinigami ziper
- [x] Worldmanhwas ziper
- [x] Maid Manga ziper
- [x] Mangayaro ziper
- [x] Cosmicscans ziper
- [x] nHentai ziper
- [x] Sheakomik, Sheamanga ziper
- [x] Komikindo.info ziper
- [x] Mikoroku ziper
- [x] Mangakakalot ziper
- [x] OnlyWaifu ziper
- [x] Manhwatop ziper
- [x] Manhuafast ziper
- [x] Onlylama
  - [x] Download link scraper
  - [x] Photo album ziper
- [x] Otomi Games
  - [x] Search parser
  - [x] Download link scraper
- [x] Javhd
  - [x] Search parser
  - [x] Download link scraper
- [x] Other incoming features

[![WibuAPI Bot](https://img.shields.io/badge/WibuAPI-Bot-blue?&logo=telegram)](https://wibuapibot.t.me)
[![Yoga Pranata](https://img.shields.io/badge/Yoga-Pranata-blue?&logo=telegram)](https://t.me/Yoga_CIC)
[![Supoort Chat](https://img.shields.io/badge/Support-Chat-blue?&logo=telegram)](https://ybotssupport.t.me)
[![Update Channel](https://img.shields.io/badge/Update-Channel-blue?&logo=telegram)](https://spreadnetworks.t.me)

## Examples:
### Importing modules
```python
from wibuapi import WibuAPI
api = WibuAPI()
```

### Anime, Hentai, Donghua
_For nekopoi search only works in [bot](https://t.me/wibuapibot)._

| Website | Params |
| :-: | :-: |
| [Lendrive](https://github.com/zYxDevs/wibu-api-py#lendrive)| link |
| [Anichin](https://github.com/zYxDevs/wibu-api-py#anichin) | link |
| [Donghua](https://github.com/zYxDevs/wibu-api-py#donghua) | link |
| [Anixlife](https://github.com/zYxDevs/wibu-api-py#anixlife) | link |
| [Kazefuri](https://github.com/zYxDevs/wibu-api-py#kazefuri) | link |
| [Kusonime](https://github.com/zYxDevs/wibu-api-py#kusonime) | link |
| [Doronime](https://github.com/zYxDevs/wibu-api-py#doronime) | link |
| [Samehadaku](https://github.com/zYxDevs/wibu-api-py#samehadaku) | link |
| [Kuramanime](https://github.com/zYxDevs/wibu-api-py#kuramanime) | link |
| [Moenime](https://github.com/zYxDevs/wibu-api-py#moenime) | link |
| [Nekopoi](https://github.com/zYxDevs/wibu-api-py#nekopoi) | link |
| [HentaiGuru](https://github.com/zYxDevs/wibu-api-py#hentaiguru) | link |

#### [Lendrive](https://lendrive.web.id)
```python
# works with batch, bd, and single eps link
url = "https://lendrive.web.id/tondemo-skill-de-isekai-hourou-meshi-ep-04-dual-subs-x265-hevc-subtitle-indonesia-english/"
res = api.lendrive(url)
print(res)
```

#### [Anichin](https://anichin.vip)
```python
# works with batch, bd, and single eps link
url = "https://anichin.vip/soul-land-season-2-episode-226-252-subtitle-indonesia/"
res = api.anichin(url)
print(res)
```

#### [Donghua](https://donghua.web.id)
```python
# works with batch, bd, and single eps link
url = "https://donghua.web.id/soul-land-season-2-episode-224-250"
res = api.donghua(url)
print(res)
```

#### [Anixlife](https://anixverse.com)
```python
# works with batch, bd, and single eps link
url = "https://anixverse.com/battle-through-the-heavens-season-5-episode-56-subtitle-indonesia/"
res = api.anixlife(url)
print(res)
```

#### [Kazefuri](https://kazefuri.vip)
```python
# works with batch, bd, and single eps link
url = "https://kazefuri.vip/shrouding-the-heavens-episode-17-subtitle-indonesia/"
res = api.kazefuri(url)
print(res)
```

#### [Kusonime](https://kusonime.com)
```python
# works with batch, bd, and single eps link
url = "https://kusonime.com/isekai-ojisan-batch-subtitle-indonesia/"
res = api.kusonime(url)
print(res)
```

#### [Doronime](https://doroni.me)
```python
# works with batch, bd, and single eps link
url = "https://doroni.me/anime/om-ke-isekai/batch"
res = api.doronime(url)
print(res)
```

#### [Samehadaku](https://samehadaku.run)
```python
# works with batch, bd, and single eps link
url = "https://samehadaku.run/nierautomata-ver1-1a-episode-8/"
res = api.samehadaku(url)
print(res)
```

#### [Kuramanime](https://kuramalink.my.id)
```python
# works with batch, bd, and single eps link
url = "https://kuramanime.art/anime/2004/mushoku-tensei-isekai-ittara-honki-dasu-shugo-jutsushi-fitz/episode/1"
res = api.kuramanime(url)
print(res)
```

#### [Moenime](https://moenime.com)
```python
# works with batch, bd, and single eps link
url = "https://moenime.com/liar-liar-sub-indo/"
res = api.moenime(url)
print(res)
```

#### [Nekopoi](https://nekopoi.care)
```python
# works with single eps link (hentai, jav)
url = "https://nekopoi.care/koumi-jima-shuu-7-de-umeru-mesu-tachi-episode-1-subtitle-indonesia/"
res = api.nekopoi(url)
print(res)
```

#### [HentaiGuru](https://hentai.guru)
```python
# works with single eps link (hentai, jav)
url = "https://hentai.guru/hentai/fushigi-no-kuni-no-succubus/"
res = api.hentaiguru(url)
print(res)
```

### Manga, Doujin, Manhua, Manhwa

| Website | Params |
| :-: | :-: |
| [Rawkuma](https://github.com/zYxDevs/wibu-api-py#rawkuma) | link |
| [Yumekomik](https://github.com/zYxDevs/wibu-api-py#yumekomik) | link |
| [Westmanga](https://github.com/zYxDevs/wibu-api-py#westmanga) | link |
| [Komikindo](https://github.com/zYxDevs/wibu-api-py#komikindo) | link |
| [Mangatale](https://github.com/zYxDevs/wibu-api-py#mangatale) | link |
| [Kiryuu](https://github.com/zYxDevs/wibu-api-py#kiryuu) | link |
| [Masterkomik](https://github.com/zYxDevs/wibu-api-py#masterkomik) | link |
| [Mangakita](https://github.com/zYxDevs/wibu-api-py#mangakita) | link |
| [Doujindesu](https://github.com/zYxDevs/wibu-api-py#doujindesu) | link |
| [Crotpedia](https://github.com/zYxDevs/wibu-api-py#crotpedia) | link |

#### [Rawkuma](https://rawkuma.com)
```python
# works with list and single chapter
# list: https://rawkuma.com/manga/guilty-circle/
# single: https://rawkuma.com/guilty-circle-chapter-83/
url = "https://rawkuma.com/manga/guilty-circle/"
res = api.rawkuma(url)
print(res)
```

#### [Yumekomik](https://yumekomik.com)
```python
# works with list and single chapter
# list: https://yumekomik.com/manga/watashi-yori-tsuyoi-otoko-to-kekkon-shitai-no/
# single: https://yumekomik.com/watashi-yori-tsuyoi-otoko-to-kekkon-shitai-no-chapter-08-bahasa-indonesia/
url = "https://yumekomik.com/manga/watashi-yori-tsuyoi-otoko-to-kekkon-shitai-no/"
res = api.yumekomik(url)
print(res)
```

#### [Westmanga](https://westmanga.info)
```python
# works with list and single chapter
# list: https://westmanga.info/manga/kaifuku-jutsushi-no-yarinaoshi/
# single: https://westmanga.info/kaifuku-jutsushi-no-yarinaoshi-chapter-52-1-bahasa-indonesia/
url = "https://westmanga.info/manga/kaifuku-jutsushi-no-yarinaoshi/"
res = api.westmanga(url)
print(res)
```

#### [Komikindo](https://komikindo.co)
```python
# work with list and single chapter
# list: https://komikindo.co/manga/yuusha-ni-zenbu-ubawareta-ore-wa-yuusha-no-hahaoya-to-party-wo-kumimashita/
# single: https://komikindo.co/yuusha-ni-zenbu-ubawareta-ore-wa-yuusha-no-hahaoya-to-party-wo-kumimashita-chapter-04/
url = "https://komikindo.co/manga/yuusha-ni-zenbu-ubawareta-ore-wa-yuusha-no-hahaoya-to-party-wo-kumimashita/"
res = api.komikindo(url)
print(res)
```

#### [Mangatale](https://mangatale.co)
```python
# work with list and single chapter
# list: https://mangatale.co/manga/dungeon-odyssey/
# single: https://mangatale.co/dungeon-odyssey-chapter-40/
url = "https://mangatale.co/manga/dungeon-odyssey/"
res = api.mangatale(url)
print(res)
```

#### [Kiryuu](https://kiryuu.id)
```python
# work with list and single chapter
# list: https://kiryuu.id/manga/a-rank-boukensha-no-slow-life/
# single: https://kiryuu.id/a-rank-boukensha-no-slow-life-chapter-39-3/
url = "https://kiryuu.id/manga/a-rank-boukensha-no-slow-life/"
res = api.kiryuu(url)
print(res)
```

#### [Masterkomik](https://masterkomik.com)
```python
# work with list and single chapter
# list: https://masterkomik.com/manga/max-level-player/
# single: https://masterkomik.com/max-level-player-chapter-07/
url = "https://masterkomik.com/manga/max-level-player/"
res = api.masterkomik(url)
print(res)
```

#### [Mangakita](https://mangakita.net)
```python
# works with list and single chapter
# list: https://mangakita.net/manga/please-go-home-akutsu-san/
# single: https://mangakita.net/please-go-home-akutsu-san-chapter-137/
url = "https://mangakita.net/manga/please-go-home-akutsu-san/"
res = api.mangakita(url)
print(res)
```

#### [Doujindesu](https://212.32.226.234)
```python
# works with list and single chapter
# list: https://212.32.226.234/manga/i-cant-stand-it-ajumma/
# single: https://212.32.226.234/i-cant-stand-it-ajumma-chapter-20/
url = "https://212.32.226.234/manga/i-cant-stand-it-ajumma/"
res = api.doujindesu(url)
print(res)
```

#### [Crotpedia](https://38.242.194.12)
```python
# works with list chapter
# list: https://38.242.194.12/baca/series/young-housemaid/
url = "https://38.242.194.12/baca/series/young-housemaid/"
res = api.crotpedia(url)
print(res)
```

**Note:**
```
You can see more endpoints on https://wibu-api.eu.org/docs or wibuapi.py file.

Sometimes their will change domains, that will make some endpoints wont works.
Please let me know when their sites change domains, I will asap fix dead endpoints.

If you find any bugs or requests a new sites,
You can ping me on telegram or make new issue.
```

## Copyright:
```
© 2022-2023 Yoga Pranata
```
