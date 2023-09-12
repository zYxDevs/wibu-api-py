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

