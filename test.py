import requests
import json
import Settings
import csv

center_point = Settings.center_point
radius = Settings.radius
keyword = Settings.keyword
title_row = ['name','rating','formatted_phone_number','international_phone_number','website','user_ratings_total','types','formatted_address']

#创建csv文件
f = open('HKcontactlist' + keyword + '.csv','w',encoding='utf-8',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(title_row)

google_token = Settings.google_token
row_info = ['','','','','','','','']
next_page_token = ''
number = 0
loop = 0

place_id = 'ChIJszRlZuIHBDQRRn2sPf72DN8'
print(place_id)

# 把地点id带入details工具得到具体位置的详细信息
place_detail_url = 'https://maps.googleapis.com/maps/api/place/details/json?place_id=' + str(
    place_id) + '&fields=name,rating,formatted_phone_number,international_phone_number,website,review,user_ratings_total,types,formatted_address&key=AIzaSyAImTTWPxluqyu-_ynfcRyhc9ABa7VA2Fk'
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

print(row_info)

# 写入csv文件
csv_writer.writerow(row_info)