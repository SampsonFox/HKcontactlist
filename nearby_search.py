import requests
import json
import Settings
import csv

def NearbySearch(next_page_token, loop):

    center_point = Settings.center_point
    radius = Settings.radius
    keyword = Settings.keyword
    google_token = Settings.google_token

    # 使用nearbysearch工具在香港中心以半径20km搜索名字里带有distributor的地点
    nearby_search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + center_point + '&radius=' + radius + '&keyword=' + keyword + '&key=' + google_token + '&pagetoken=' + next_page_token
    print(nearby_search_url)
    nearby_search_result = requests.get(nearby_search_url)
    nearby_search_json = nearby_search_result.json()

    # next_page_token = nearby_search_json['next_page_token']
    # print(next_page_token)

    # 把result单独保存
    loop += 1
    print(str(loop) + '#####################################################')

    return nearby_search_json