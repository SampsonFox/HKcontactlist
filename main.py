import requests
import json
import Settings
import csv
from nearby_search import NearbySearch

center_point = Settings.center_point
radius = Settings.radius
keyword = Settings.keyword

title_row = ['name','rating','formatted_phone_number','international_phone_number','website','user_ratings_total','types','formatted_address','keyword']

with open('HK list', 'w') as hk:
    json.dump(title_row, hk)
print(title_row)

#创建csv文件
f = open('HKcontactlist' + keyword + '.csv','w',encoding='utf-8',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(title_row)

google_token = Settings.google_token
row_info = ['','','','','','','','','']
next_page_token = ''
number = 0
loop = 0

while number <= 4000:

    nearby_search_json = NearbySearch(next_page_token, loop)

    # nearby_search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + center_point + '&radius=' + radius + '&keyword=' + keyword + '&key=' + google_token + '&pagetoken' + next_page_token
    # nearby_search_result = requests.get(nearby_search_url)
    # nearby_search_json = nearby_search_result.json()

    next_page_token = nearby_search_json['next_page_token']
    print(next_page_token)

    # 把result单独保存
    loop += 1
    print(str(loop) + '#####################################################')

    items = nearby_search_json['results']

    #列出地点的id
    for item in items:
        place_id = item['place_id']
        print(place_id)

        #把地点id带入details工具得到具体位置的详细信息
        place_detail_url = 'https://maps.googleapis.com/maps/api/place/details/json?place_id=' + str(place_id) + '&fields=name,rating,formatted_phone_number,international_phone_number,website,review,user_ratings_total,types,formatted_address&key=AIzaSyAImTTWPxluqyu-_ynfcRyhc9ABa7VA2Fk'
        print(place_detail_url)
        response = requests.get(place_detail_url)
        response_json_1 = response.json()
        response_json = response_json_1['result']
        type = ''

        if response_json.__contains__('name'):
            row_info[0] = response_json['name']

        if response_json.__contains__('rating'):
            row_info[1] = response_json['rating']

        if response_json.__contains__('formatted_phone_number'):
            row_info[2] = response_json['formatted_phone_number']

        if response_json.__contains__('international_phone_number'):
            row_info[3] = response_json['international_phone_number']

        if response_json.__contains__('website'):
            row_info[4] = response_json['website']

        if response_json.__contains__('user_ratings_total'):
            row_info[5] = response_json['user_ratings_total']

        if response_json.__contains__('types'):
            for item in response_json['types']:
                type = type + ' ' + item
            row_info[6] = type

        if response_json.__contains__('formatted_address'):
            row_info[7] = response_json['formatted_address']

        row_info[8] = keyword

        print(row_info)

        with open('HK list', 'a') as hk:
            json.dump(row_info, hk)
        print(row_info)

        # 写入csv文件
        csv_writer.writerow(row_info)

        number = number + 1
        print(number)

with open('pagetoken', 'w') as pt:
    json.dump(next_page_token, pt)

