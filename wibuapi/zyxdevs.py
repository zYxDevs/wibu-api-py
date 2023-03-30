# (c) 2022-2023 Yoga Pranata a.k.a zYxDevs
# This file contains some learning stuff, don't care it.

import re
from json import dumps
from requests import get


class Etc:
    def __init__(self):
        self.base_url = "https://wibu-api.eu.org/api"
        self.deprecated_url = "https://api.wibu-api.eu.org/api"

    def stats(self):
        try:
            resp1 = get(self.base_url, timeout=15).json()
            resp2 = get(self.deprecated_url, timeout=15).json()
            res = [{"updated": resp1}, {"deprecated": resp2}]
            return dumps(res, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def xCode(self, url: str):
        """
        Personal site parser(lazy to make new repo) so i add this to here.
        https://xcodebasisdrive.blogspot.com
        """
        try:
            response = get(url)
            return re.findall(
                "window.location[ ]{0,}=[ ]{0,}[(|\)](.*?)[(|\)]", response.text
            )[0].replace('"', "")
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"
