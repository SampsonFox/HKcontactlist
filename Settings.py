
import csv


#创建csv文件
f = open('HKcontactlist.csv','w',encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(['name','rating','formatted_phone_number','international_phone_number','website','user_ratings_total','types','formatted_address'])



center_point = '22.3143393,114.1648461'
radius = '20000'
keyword = 'distributor'
google_token = 'AIzaSyAImTTWPxluqyu-_ynfcRyhc9ABa7VA2Fk'