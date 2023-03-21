# Wibu-API-Py
[![Repo Size](https://img.shields.io/github/repo-size/zYxDevs/wibu-api-py?style=flat-square)](https://github.com/zYxDevs/wibu-api-py)  [![Languages](https://img.shields.io/github/languages/top/zYxDevs/wibu-api-py?style=flat-square)](https://github.com/zYxDevs/wibu-api-py)  [![CodeFactor](https://www.codefactor.io/repository/github/zYxDevs/wibu-api-py/badge)](https://www.codefactor.io/repository/github/zYxDevs/wibu-api-py)  [![Codacy Badge](https://app.codacy.com/project/badge/Grade/8b87ea2387574f54849805430a9bc9ea)](https://www.codacy.com/gh/zYxDevs/wibu-api-py/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=zYxDevs/wibu-api-py&amp;utm_campaign=Badge_Grade)

_Official Python Wrapper for Wibu API._

## How to install
#### Use pip
```
pip install wibuapi
```

#### Get latest update
```
pip install -U wibuapi
```

#### Install from repo
```bash
root@zyxdevs:~ git clone https://github.com/zYxDevs/wibu-api-py wibuapi
root@zyxdevs:~ cd wibuapi
root@zyxdevs:~ python3 setup.py install
```

## Telegram Bot:
_I've created official telegram bot to interacted with WibuAPI_

**Check here:**
https://wibuapibot.t.me

**Support group:**
https://ybotssupport.t.me

**Update channel:**
https://spreadnetworks.t.me

## Examples:
### Importing modules
```python
from wibuapi import WibuAPI
api = WibuAPI()
```

### Anime
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














## Copyright:
**(c) 2022-2023 by [Yoga Pranata](https://t.me/Yoga_CIC).**
