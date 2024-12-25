import json
from typing import Any
from urllib import request
from urllib.error import URLError

from sortedcontainers import SortedDict

from model import Achievement, Game


def get_localized_vals(value, display_schema) -> tuple[str, str | None]:
    if isinstance(display_schema[value], dict):
        orig_val = display_schema[value]["english"]
    else:
        orig_val = display_schema[value]

    return orig_val


def parse_achievement_schema(vdf_schema: dict) -> Achievement | None:
    achievement_data = Achievement()

    if "display" in vdf_schema:
        achievement_data.name = get_localized_vals("name", vdf_schema["display"])
    if "permission" in vdf_schema:
        achievement_data.protected = True

    return achievement_data


def get_apps_info() -> dict[str, Game]:
    request_url = "https://api.steampowered.com/ISteamApps/GetAppList/v0002/?format=json"

    data = request.urlopen(request_url)
    result = json.loads(data.read().decode())

    _games_database = SortedDict()
    if result.get("applist") and result["applist"].get("apps"):
        for app in result["applist"]["apps"]:
            _games_database[app["appid"]] = Game(
                name=app["name"],
                appid=app["appid"],
            )
    return _games_database


def request_price(appid_game: str) -> dict[str, Any] | None:
    print(f"Requesting {appid_game}...")
    try:
        all_url = f"https://store.steampowered.com/api/appdetails?appids={appid_game}&cc=us"

        data = request.urlopen(all_url)
        result = json.loads(data.read().decode())

        if result[appid_game]["success"]:
            return result[appid_game]
        else:
            price_url = f"https://store.steampowered.com/api/appdetails?appids={appid_game}&cc=us&filters=name,price_overview"
            data = request.urlopen(price_url)
            result = json.loads(data.read().decode())

        return result[appid_game]
    except URLError:
        print(f"Failed {appid_game}...")

    return None
