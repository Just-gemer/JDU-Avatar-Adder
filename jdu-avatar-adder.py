#JDU AVATAR ADDER BY Just gemer
import os
print("JDU AVATAR ADDER BY Just gemer")
mapname = str(input("mapname: "))
jdver = str(input("jdVersion: "))
price = str(input("mojoPrice(type 0 if you dont want it): "))
unlock = str(input("unlockType: "))
url = str(input("url: "))
idd = str(input("avatar id: "))
qid = str(input("relativeQuestID: "))
wid = str(input("relativeWDFBossName: "))
sfy = str(input("soundFamily: "))

# Avatar Adder 
avatar = open("avatars.json", "w", encoding="utf-8")
avatar.write('''{
    "''' + idd + '''": {
        "Id": ''' + idd + ''',
        "JDNowVersion": 1,
        "__class": "OnlineCustomizableItem",
        "jdVersion": ''' + jdver + ''',
        "mojoPrice": ''' + price + ''',
        "relativeQuestID": "''' + qid + '''",
        "relativeSongName": "''' + mapname + '''",
        "relativeWDFBossName": "''' + wid + '''",
        "soundFamily": "''' + sfy + '''",
        "status": 1,
        "unlockType": ''' + unlock + ''',
        "url": "''' + url + '''",
        "itemType": 0,
        "visibility": 1
    }
}''')
skin.close()
