import json

import pymysql

if __name__ == '__main__':
    # 数据插入
    db = pymysql.Connect(host="localhost", user="root", password="123456", database="tpp", charset="utf8")
    cursor = db.cursor()
    # 数据读取
    with open("City.json") as city:
        cities = json.load(city)
        print(cities)
        # JsonArray   list
        returnValues = cities.get("returnValue")
        print(type(returnValues))
        letters = returnValues.keys()
        for letter in letters:
            # print(letter)

            db.begin()
            cursor.execute("INSERT INTO letter(letter) VALUES ('" + letter + "');")
            db.commit()

            db.begin()
            resultNum = cursor.execute("SELECT * FROM letter WHERE letter='" + letter + "'")
            print(resultNum)
            result = cursor.fetchone()
            print(result)
            db.commit()

            fistLetter = result[0]

            cities = returnValues.get(letter)
            for city in cities:
                regionName = city.get("regionName")
                pinYin = city.get("pinYin")
                cityCode = city.get("cityCode")
                db.begin()
                cursor.execute("INSERT INTO city(regionName, cityCode, pinYin, fistLetter) VALUES ('%s','%d','%s','%d')" % (regionName, cityCode, pinYin, fistLetter))
                db.commit()

    # cursor.execute("select * from city")

    # print(cursor.fetchone())

    # db.begin()
    # cursor.execute(
    #             "INSERT INTO city(regionName, cityCode, pinYin, firstLetter) VALUES ('%s','%d','%s','%d')" % (
    #             "阿坝", 110, "", 1))
    # db.commit()
