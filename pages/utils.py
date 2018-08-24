import requests
from . import gsheets
# import json
# import ast
# from urllib.request import urlopen


def gsheets_worksheets(sheet_id):
    worksheets_url = 'https://spreadsheets.google.com/feeds/worksheets/'+ sheet_id +'/public/values?alt=json'

    # json_string = urlopen(worksheets_url).read().decode('utf8')
    # parsed_json = json.loads(json_string)

    json_string = requests.get(worksheets_url)
    parsed_json = json_string.json()

    # data = parsed_json['feed']['entry'][0]
    # data = parsed_json['feed']['entry'][0]['title']
    sheet0_url = parsed_json['feed']['entry'][0]['link'][0]['href']
    data =  google_sheets_json_to_dict(f'{sheet0_url}?alt=json')

    # print(parsed_json)
    print(type(parsed_json))
    # print(type(parsed_json['feed']['entry']))
    # print(type(data))
    # print(data)
    # pprint.pprint(parsed_json)

    # for element in parsed_json['feed']['entry']:
    #     print(element['title'])

    return data

# def iterload(string_or_fp, cls=json.JSONDecoder, **kwargs):
#     if isinstance(string_or_fp, file):
#         string = string_or_fp.read()
#     else:
#         string = str(string_or_fp)

#     decoder = cls(**kwargs)
#     idx = WHITESPACE.match(string, 0).end()
#     while idx < len(string):
#         obj, end = decoder.raw_decode(string, idx)
#         yield obj
#         idx = WHITESPACE.match(string, end).end()

#     return data

def google_sheets_json_to_dict(sheet_url):
    # sheet_url = 'https://spreadsheets.google.com/feeds/list/' + sheet_id + '/1/public/values?alt=json'

    json_string = requests.get(sheet_url)
    parsed_json = json_string.json()

    # json_string = urlopen(url).read().decode('utf8')
    # parsed_json = json.loads(json_string)

    # data_dict = ast.literal_eval(json_string)

    # del data_dict['version'], data_dict['encoding']

    # data = data_dict
    # data = data_dict['feed']
    # data = data_dict['feed']['entry']

    data = parsed_json['feed']['entry']

    data = data[0]
    del data['id'], data['updated'], data['category'], data['title'], data['content'], data['link']

    data2 = dict()

    for key, value in data.items():
        data2.update({key[4:]: value['$t']})

    return parsed_json
