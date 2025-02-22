# Protected achievements checker

### Launch

You need configured python env with installed openpyxl, sortedcontainers and vdf.

`pip install openpyxl sortedcontainers vds`

Then launch:

`python __main__.py`

You can use args to configure output location, etc:

linux:
`python __main__.py --oldresult=/home/user/output.xlsx --output=/home/user/output.xlsx`

windows:
`python __main__.py --oldresult=c:\\users\\user\\output.xlsx --output=c:\\users\\user\\output.xlsx`

Following string backup original output.xlsx file and write new result to same path.