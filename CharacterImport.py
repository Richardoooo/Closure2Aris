import json

def ChangeName(Name):
    SplitedName = Name.split(" ",1)
    return SplitedName[-1].lower()

with open("MolluTalk角色数据.json",'r',encoding='utf-8') as chr:
    CharacterData = json.loads(chr.read())

CharacterList = {}

for Schools in CharacterData:
    # CharacterList[Schools["en"]] = {}

    for Clubs in Schools["club"]:
        # CharacterList[Schools["en"]][Clubs["zh_cn"]] = []

        for Character in Clubs["characters"]:
            CharacterList[ChangeName(Character['en'])] = Character['zh_cn']

print(CharacterList)

with open("CharacterName.json","w",encoding='utf-8') as N:
    N.write(json.dumps(CharacterList,ensure_ascii=False, indent=4, separators=(',', ': ')))
    
# with open("CharacterName.json",'r',encoding='utf-8') as Name:
#     CharacterName = json.loads(Name.read())
#     Name.close()

# Name_and_ClubList = {}

# Clubs = CharacterName.values()

# # print(Clubs)
# for name in Clubs:
#     Name_and_ClubList.update(name)

# FinalList = {}

# for item in Name_and_ClubList.items():
#     for name in item[1]:
#         FinalList[name] = item[0]

# with open("CharacterName.json",'w',encoding='utf-8') as Name:
#     Name.write(json.dumps(FinalList,ensure_ascii=False, indent=4, separators=(',', ': ')))