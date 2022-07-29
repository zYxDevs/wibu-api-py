import re
from json import dumps
from requests import get


class zYxDevs:
    def stats(site: str):
        try:
            url = "https://wibu-api.eu.org/api"
            if site == "deprecated":
                url = "https://api.wibu-api.eu.org/api"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"

    def xCode(url: str):
        """
        Personal site parser(lazy to make new repo) so i add this to here.
        https://xcodebasisdrive.blogspot.com
        """
        try:
            response = get(url)
            parse = re.findall(
                "window.location[ ]{0,}=[ ]{0,}[(|\)](.*?)[(|\)]", response.text
            )[0].replace('"', "")
            return parse
        except Exception as e:
            return f"An error occured report on @YBotsSupport\n\n{e}"
