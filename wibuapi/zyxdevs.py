# (c) 2022-2023 Yoga Pranata a.k.a zYxDevs
# This file contains some learning stuff, don't care it.

from requests import get


class Etc:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.deprecated_url = "https://api.wibu-api.eu.org/api"

    def stats(self):
        try:
            main = get(self.base_url, timeout=15).json()
            old = get(self.deprecated_url, timeout=15).json()
            return [{"main": main}, {"deprecated": old}]
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"
