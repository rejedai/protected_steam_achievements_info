import json
from typing import Any
from urllib import request
from urllib.error import URLError

from sortedcontainers import SortedDict

from model import Achievement, Game


def get_localized_vals(value, display_schema) -> str:
    if isinstance(display_schema[value], dict):
        if "english" in display_schema[value]:
            return display_schema[value]["english"]
        elif len(display_schema[value].keys()) > 0:
            return display_schema[value][list(display_schema[value].keys())[0]]
    elif isinstance(display_schema[value], str):
        return display_schema[value]

    return "none"


def parse_achievement_schema(vdf_schema: dict) -> Achievement | None:
    achievement_data = Achievement()

    if "display" in vdf_schema:
        achievement_data.name = get_localized_vals("name", vdf_schema["display"])
    if "permission" in vdf_schema:
        achievement_data.protected = True

    return achievement_data


def get_apps_info(steam_api_key: str, last_appid: int = 0, _games_database=None) -> dict[str, Game]:
    request_url = (
        f"https://api.steampowered.com/IStoreService/GetAppList/v1/?key={steam_api_key}"
        "&include_games=true&include_dlc=false&include_software=false&include_videos=false"
        "&include_hardware=false&max_results=50000"
        f"&last_appid={str(last_appid)}"
    )

    data = request.urlopen(request_url)
    result = json.loads(data.read().decode())

    if _games_database is None:
        _games_database = SortedDict()

    if result.get("response") and "apps" in result.get("response"):
        for app in result["response"]["apps"]:
            _games_database[app["appid"]] = Game(
                name=app["name"],
                appid=app["appid"],
            )
        if "last_appid" in result["response"] and result["response"].get("have_more_results", False):
            return get_apps_info(steam_api_key, result["response"]["last_appid"], _games_database)

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
