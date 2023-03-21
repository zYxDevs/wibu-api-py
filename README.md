# Wibu-API-Py
[![Repo Size](https://img.shields.io/github/repo-size/zYxDevs/wibu-api-py?style=flat-square)](https://github.com/zYxDevs/wibu-api-py)  [![Languages](https://img.shields.io/github/languages/top/zYxDevs/wibu-api-py?style=flat-square)](https://github.com/zYxDevs/wibu-api-py)  [![CodeFactor](https://www.codefactor.io/repository/github/zYxDevs/wibu-api-py/badge)](https://www.codefactor.io/repository/github/zYxDevs/wibu-api-py)  [![Codacy Badge](https://app.codacy.com/project/badge/Grade/8b87ea2387574f54849805430a9bc9ea)](https://www.codacy.com/gh/zYxDevs/wibu-api-py/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=zYxDevs/wibu-api-py&amp;utm_campaign=Badge_Grade)

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
```bash
root@zyxdevs:~ git clone https://github.com/zYxDevs/wibu-api-py wibuapi
root@zyxdevs:~ cd wibuapi
root@zyxdevs:~ python3 setup.py install
```

## Telegram Bot:
_I've created official telegram bot to interacted with WibuAPI_

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
_For nekopoi scrapper only works in [bot](#telegram-bot)._

| Website | Params |
| :-: | :-: |
| [Lendrive](#lendrive)| link |
| [Donghua](#donghua) | link |
| [Kusonime](#kusonime) | link |
| [Doronime](#doronime) | link |
| [Samehadaku](#samehadaku) | link |

#### [Lendrive](https://lendrive.web.id)
```python
# works with batch, bd, and single eps link
url = "https://lendrive.web.id/tondemo-skill-de-isekai-hourou-meshi-ep-04-dual-subs-x265-hevc-subtitle-indonesia-english/"
res = api.lendrive(url)
print(res)
```

#### [Donghua](https://donghua.web.id)
```python
# works with batch, bd, and single eps link
url = "https://donghua.web.id/soul-land-season-2-episode-224-250"
res = api.donghua(url)
print(res)
```

#### [Kusonime](https://kusonime.com)
```python
# works with batch, bd, and single eps link
url = "https://kusonime.com/isekai-ojisan-batch-subtitle-indonesia/"
res = api.kusonime(url)
print(res)
```

#### [Doronime](https://doronime.id)
```python
# works with batch, bd, and single eps link
url = "https://doronime.id/anime/om-ke-isekai/batch"
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

### Manga, Doujin, Manhua, Manhwa

| Website | Params |
| :-: | :-: |
| [Rawkuma](#rawkuma) | link |
| [Westmanga](#westmanga) | link |
| [Komikindo](#komikindo) | link |
| [Mangatale](#mangatale) | link |
| [Kiryuu](#kiryuu) | link |
| [Doujindesu](#doujindesu) | link |

#### [Rawkuma](https://rawkuma.com)
```python
# works with list and single chapter
# list: https://rawkuma.com/manga/guilty-circle/
# single: https://rawkuma.com/guilty-circle-chapter-83/
url = "https://rawkuma.com/manga/guilty-circle/"
res = api.rawkuma(url)
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

#### [Doujindesu](https://212.32.226.234)
```python
# works with list and single chapter
# list: https://212.32.226.234/manga/i-cant-stand-it-ajumma/
# single: https://212.32.226.234/i-cant-stand-it-ajumma-chapter-20/
url = "https://212.32.226.234/manga/i-cant-stand-it-ajumma/"
res = api.doujindesu(url)
print(res)
```

## Copyright:
```
© 2022-2023 Yoga Pranata
```
