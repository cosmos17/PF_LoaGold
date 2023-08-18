import requests
import json
# from lostark_api_token import Token

Token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAyOTY1MDMifQ.YeGi136-R7RUN-9xBkokFPR0bxhlwcPAiqvjn1M48XuzeEUW9SfmdSTFsDRr-OgzODgydjiutOmhdUdvoca0d57gETvI8QT_Q4yy93Y-nk3Y7XhfhEb0MsegGhu_Z_UQ_1KuzA3JkBdOux2ycmgabyRL_Ev5cRhseS9TeSRQCGWd3b0zB6vvlqJrY3xCHT5CltltKLRWNaZYohZNE_B-SACWeefldO3V0sbgm72TfHh2wuAaNuQPY6MdBDoYubzTzmS5zvAjvwgGESt-X-5Thb01m2So8uqmDyY3VbMkwS7aqeupIVLsEsM1cc-2_RdCXQtuHMNIL1OVaNbZoggFCQ'
Token = 'bearer ' + Token

headers = {
    'accept' : 'application/json',
    'authorization' : Token
    }

# url = 'https://developer-lostark.game.onstove.com/example/api'
# response = requests.get(url, headers=headers)
url_events = 'https://developer-lostark.game.onstove.com/news/events'
response = requests.get(url_events, headers=headers)

# jsObj = response.json()

print(response)
# print(jsObj)