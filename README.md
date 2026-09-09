# Protected achievements checker

### Launch

To launch need [uv](https://docs.astral.sh/uv/) and Steam Web API [Key](https://steamcommunity.com/dev/apikey).

`uv sync`

Then launch:

linux:
`uv run main.py --steam-api-key=YOUR_KEY --oldresult=/home/user/output.xlsx --output=/home/user/output.xlsx`

windows:
`uv run main.py --steam-api-key=YOUR_KEY --oldresult=c:\\users\\user\\output.xlsx --output=c:\\users\\user\\output.xlsx`

> **Note:** Following command backs up original `output.xlsx` file and writes the new result to the same path.