import requests
import json
import Settings
import csv

center_point = Settings.center_point
radius = Settings.radius
keyword = Settings.keyword

#创建csv文件
f = open('HKcontactlist' + keyword + '.csv','w',encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(['name','rating','formatted_phone_number','international_phone_number','website','user_ratings_total','types','formatted_address'])

google_token = Settings.google_token
row_info = ['','','','','','','','']
next_page_token = ''
number = 0
loop = 0

while 1:

    #使用nearbysearch工具在香港中心以半径20km搜索名字里带有distributor的地点
    nearby_search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + center_point + '&radius=' + radius + '&keyword=' + keyword + '&key=' + google_token + '&pagetoken' + next_page_token
    nearby_search_result = requests.get(nearby_search_url)
    nearby_search_json = nearby_search_result.json()
    print(nearby_search_json)


    next_page_token = nearby_search_json['next_page_token']
    print(next_page_token)

    #把result单独保存
    items = nearby_search_json['results']
    loop += 1
    print(str(loop) + '#####################################################')

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
                type += item
            row_info[6] = type

        if response_json.__contains__('formatted_address'):
            row_info[7] = response_json['formatted_address']

        print(row_info)

        #写入csv文件
        csv_writer.writerow(row_info)
        print(response_json)
        number = number + 1
        print(number)


