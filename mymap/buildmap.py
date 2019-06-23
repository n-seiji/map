import os
import re
import glob
import folium
from os.path import expanduser
#Downloadsまでのパス取得
def buildmap (request):
    downloads = expanduser("~/Downloads")
###後で変更
#gpxファイルを取得
    files = glob.glob("/Users/seiji/program/strava/map/map_test/*.gpx")

#パターンの定義
    pattern_ido = 'lat="[0-9]+.[0-9]*"'
    pattern_keido = 'lon="[0-9]+.[0-9]*"'
#地図の作成
    osm = folium.Map(location=[35.681382, 139.76608399999998], zoom_start=9)
# 行ごとにすべて読み込んでリストデータにする
    for file in files:
        test_data = open(file, "r")
        lines = test_data.readlines()
        gps_list = []
# 一行ずつ表示する
        for line in lines:
            gps = []
            ido = re.search(pattern_ido, line)
            keido = re.search(pattern_keido, line)
            if ido != None and keido != None:
                ido = ido.group()
                keido = keido.group()
                ido = ido.replace('lat=', '')
                ido = ido.replace('"', '')
                keido = keido.replace('lon=', '')
                keido = keido.replace('"', '')
                gps = [float(ido), float(keido)] #[39.51246234, 139.4123412]
                gps_list.append(gps)
        if  gps_list:
            locations= gps_list
        #点を線へ
            line = folium.PolyLine(locations=locations)
        #最初に用意した地図に追加
            osm.add_child(line)
# ファイルをクローズする
    test_data.close()
##応急処置
#ファイルの作成
    f = open(os.path.join(downloads, 'map.html'),'a')
###どうにか追記か読み込んで保存したい
    osm.save(os.path.join(downloads, 'map.html'))
    f.close()
    osm




#どうにか追記したい
#ido,keidoの処理をもっとスマートに
#線の色を変えたい。いっぱい通ってたら赤とか
#ファイルの取得を変える
