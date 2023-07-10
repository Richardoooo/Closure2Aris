import json
import time
import os
import sys

CharacterClub = {
    "shiroko": "对策委员会",
    "hoshino": "对策委员会",
    "serika": "对策委员会",
    "nonomi": "对策委员会",
    "ayane": "对策委员会",
    "prefect-team-member": "风纪委员会",
    "hina": "风纪委员会",
    "iori": "风纪委员会",
    "ako": "风纪委员会",
    "chinatsu": "风纪委员会",
    "mutsuki": "便利屋68",
    "haruka": "便利屋68",
    "kayoko": "便利屋68",
    "aru": "便利屋68",
    "izumi": "美食研究会",
    "junko": "美食研究会",
    "akari": "美食研究会",
    "haruna": "美食研究会",
    "makoto": "万魔殿",
    "iroha": "万魔殿",
    "ibuki": "万魔殿",
    "satsuki": "万魔殿",
    "pandemonium-member": "万魔殿",
    "fuuka": "给食部",
    "juri": "给食部",
    "kasumi": "温泉开发部",
    "megu": "温泉开发部",
    "development member": "温泉开发部",
    "sena": "救急医学部",
    "medicine member": "救急医学部",
    "elika": "归宅部",
    "kilala": "归宅部",
    "arius-student": "学生",
    "akane": "Cleaning & Clearing",
    "neru": "Cleaning & Clearing",
    "asuna": "Cleaning & Clearing",
    "karin": "Cleaning & Clearing",
    "toki": "Cleaning & Clearing",
    "aris": "游戏开发部",
    "key": "游戏开发部",
    "momoi": "游戏开发部",
    "midori": "游戏开发部",
    "yuzu": "游戏开发部",
    "himari": "真理部",
    "hare": "真理部",
    "kotama": "真理部",
    "chihiro": "真理部",
    "maki": "真理部",
    "hibiki": "工程师部",
    "utaha": "工程师部",
    "kotori": "工程师部",
    "utahaturret": "工程师部",
    "rio": "研讨会",
    "yuuka": "研讨会",
    "koyuki": "研讨会",
    "noa": "研讨会",
    "eimi": "特异现象搜查部",
    "sumire": "健身部",
    "natsu": "放学后甜品部",
    "yoshimi": "放学后甜品部",
    "airi": "放学后甜品部",
    "kazusa": "放学后甜品部",
    "teaparty": "茶话会",
    "mika": "茶话会",
    "seia": "茶话会",
    "nagisa": "茶话会",
    "azusa": "补习部",
    "koharu": "补习部",
    "hifumi": "补习部",
    "hanako": "补习部",
    "justice-task-force-member": "正义实现委员会",
    "mashiro": "正义实现委员会",
    "tsurugi": "正义实现委员会",
    "hasumi": "正义实现委员会",
    "ichika": "正义实现委员会",
    "sisterhood": "修女会",
    "hinata": "修女会",
    "mari": "修女会",
    "sakurako": "修女会",
    "serina": "救护骑士团",
    "hanae": "救护骑士团",
    "mine": "救护骑士团",
    "shimiko": "图书委员会",
    "ui": "图书委员会",
    "suzumi": "圣三一自警团",
    "reisa": "圣三一自警团",
    "pina": "庆典运营委员会",
    "shizuko": "庆典运营委员会",
    "umika": "庆典运营委员会",
    "mimori": "修行部",
    "tsubaki": "修行部",
    "kaede": "修行部",
    "chise": "阴阳部",
    "niya": "阴阳部",
    "kaho": "阴阳部",
    "izuna": "忍术研究部",
    "michiru": "忍术研究部",
    "tsukuyo": "忍术研究部",
    "hatsune-miku": "所属不详",
    "kanna": "公安局",
    "miria": "所属不详",
    "nao": "所属不详",
    "rone": "所属不详",
    "yukari": "所属不详",
    "francis": "所属不详",
    "anubis": "所属不详",
    "???": "所属不详",
    "the-nameless-priests": "所属不详",
    "akira": "所属不详",
    "kuzunoha": "百花缭乱纷争调停委员会",
    "nagusa": "百花缭乱纷争调停委员会",
    "kissaki": "玄龙门",
    "mina": "玄龙门",
    "genryumon-member": "玄龙门",
    "saya": "炼丹术研究会",
    "rumi": "玄武商会",
    "reizo": "玄武商会",
    "genbu-shokai-employee": "玄武商会",
    "shun": "教育支援部「梅花园」",
    "kokona": "教育支援部「梅花园」",
    "cherino": "红冬事务局",
    "tomoe": "红冬事务局",
    "marina": "红冬事务局",
    "member-of-the-ss": "红冬事务局",
    "shigure": "227号特别班",
    "nodoka": "227号特别班",
    "meru": "知识解放战线",
    "momiji": "知识解放战线",
    "minori": "工务部",
    "construction-department-member": "工务部",
    "kirino": "生活安全局",
    "fubuki": "生活安全局",
    "saki": "RABBIT小队",
    "miyako": "RABBIT小队",
    "miyu": "RABBIT小队",
    "moe": "RABBIT小队",
    "yukino": "FOX 小队",
    "niko": "FOX 小队",
    "otogi": "FOX 小队",
    "kurumi": "FOX 小队",
    "saori": "阿里乌斯特殊小队",
    "atsuko": "阿里乌斯特殊小队",
    "hiyori": "阿里乌斯特殊小队",
    "misaki": "阿里乌斯特殊小队",
    "president": "联邦学生会",
    "rin": "联邦学生会",
    "momoka": "联邦学生会",
    "ayumu": "联邦学生会",
    "kaya": "联邦学生会",
    "aoi": "联邦学生会",
    "student-council-officer": "联邦学生会",
    "mai": "克洛诺斯报道部",
    "shinon": "克洛诺斯报道部",
    "bunnygirl-guard": "金羊毛",
    "black-suit": "数秘术",
    "golconde": "数秘术",
    "décalcomanie": "数秘术",
    "maestro": "数秘术",
    "beatrice": "数秘术",
    "perorozilla": "无限怪谈图书馆",
    "automata": "黑龟组",
    "goro": "黑龟组",
    "thugs": "看门人",
    "hod": "十字神名",
    "chesed": "十字神名",
    "binah": "十字神名",
    "peroro-sama": "Momo Friends",
    "nyantenmaru": "百鬼夜行商店街",
    "shiro": "斯兰皮亚",
    "kuro": "斯兰皮亚",
    "goz": "斯兰皮亚",
    "kivotos-citizen": "市民",
    "android": "市民",
    "shibaseki-master": "柴关拉面",
    "sora": "天使24",
    "chimi-ichiza": "魑魅一座・路上流",
    "kaiser-pmc-director": "凯撒 PMC",
    "kaiser-pmc-general": "凯撒 PMC",
    "kaiser-president": "凯撒 PMC",
    "kaiser-sof": "凯撒 PMC",
    "kaiten-fx-mk.0": "凯坦泽",
    "kaitenranger": "凯坦泽",
    "helmet-gang": "咔哒咔哒 头盔团",
    "rabu": "哗啦哗啦头盔团",
    "hieronymus": "诸圣相通",
    "frenapates": "色彩",
    "yongha": "蔚蓝档案",
    "arona": "什庭之匣",
    "plana": "什庭之匣",
    "sensei": "联邦搜查社团「夏莱」"
}

CharacterName = {
        "shiroko": "砂狼 白子",
        "hoshino": "小鸟游 星野",
        "serika": "黑见 芹香",
        "nonomi": "十六夜 野宫",
        "ayane": "奥空 绫音",
        "prefect-team-member": "风纪委员",
        "hina": "空崎 日奈",
        "iori": "银镜 伊织",
        "ako": "天雨 亚子",
        "chinatsu": "火宫 千夏",
        "mutsuki": "浅黄 睦月",
        "haruka": "伊草 遥香",
        "kayoko": "鬼方 佳代子",
        "aru": "陆八魔 阿露",
        "izumi": "狮子堂 泉",
        "junko": "赤司 淳子",
        "akari": "鳄渊 明里",
        "haruna": "黑馆 羽留奈",
        "makoto": "羽沼 真琴",
        "iroha": "枣 伊吕波",
        "ibuki": "伊吹",
        "satsuki": "皋月",
        "pandemonium-member": "万魔殿干部",
        "fuuka": "爱清 枫香",
        "juri": "牛牧 朱莉",
        "kasumi": "霞",
        "megu": "下仓 惠",
        "development member": "温泉开发部成员",
        "sena": "冰室 濑名",
        "medicine member": "急救医学人员",
        "elika": "旗见 艾丽嘉",
        "kilala": "绮良",
        "gehenna-student": "格黑娜-学生",
        "akane": "室笠 朱音",
        "neru": "美甘 尼禄",
        "asuna": "一之濑 明日奈",
        "karin": "角楯 花凛",
        "toki": "飞鸟马 时",
        "aris": "天童 爱丽丝",
        "key": "Key",
        "momoi": "才羽 桃井",
        "midori": "才羽 绿",
        "yuzu": "花冈 柚子",
        "himari": "明星 日鞠",
        "hare": "小钩 晴",
        "kotama": "音濑 小玉",
        "chihiro": "各务 千寻",
        "maki": "小涂 真纪",
        "hibiki": "猫塚 响",
        "utaha": "白石 歌原",
        "kotori": "丰见 亚都梨",
        "utahaturret": "乌塔哈塔雷特",
        "rio": "调月 莉音",
        "yuuka": "早濑 优香",
        "koyuki": "黑崎 小雪",
        "noa": "生盐 诺亚",
        "eimi": "和泉元 英美",
        "sumire": "乙花 菫",
        "millennium-student": "千禧-学生",
        "natsu": "柚鸟 夏",
        "yoshimi": "伊原木 喜美",
        "airi": "栗村 爱莉",
        "kazusa": "杏山 和纱",
        "teaparty": "茶会",
        "mika": "圣园 未花",
        "seia": "百合园 圣娅",
        "nagisa": "桐藤 渚",
        "azusa": "白洲 梓",
        "koharu": "下江 小春",
        "hifumi": "阿慈谷 日富美",
        "hanako": "浦和 花子",
        "justice-task-force-member": "正义实现委员会组员",
        "mashiro": "静山 真白",
        "tsurugi": "剑先 鹤城",
        "hasumi": "羽川 莲实",
        "ichika": "一花",
        "sisterhood": "修女会",
        "hinata": "若叶 日向",
        "mari": "伊落 玛丽",
        "sakurako": "歌住 樱子",
        "serina": "鹫见 芹奈",
        "hanae": "朝颜 花绘",
        "mine": "苍森 美弥",
        "shimiko": "円堂 志美子",
        "ui": "古関 忧",
        "suzumi": "守月 铃美",
        "reisa": "宇泽 玲纱",
        "trinity-student": "圣三一-学生",
        "pina": "朝日奈 菲娜",
        "shizuko": "河和 静子",
        "umika": "海夏",
        "mimori": "水羽 三森",
        "tsubaki": "春日 椿",
        "kaede": "勇美 枫",
        "chise": "和乐 知世",
        "niya": "天地 妮娅",
        "kaho": "桑上 果穗",
        "izuna": "久田 伊树菜",
        "michiru": "千鸟 满",
        "tsukuyo": "大野 月咏",
        "wakamo": "狐坂 若藻",
        "kuzunoha": "库兹诺哈",
        "nagusa": "五陵 名草",
        "kissaki": "咲妃",
        "mina": "近卫 南",
        "genryumon-member": "玄龙门高级管理人员",
        "saya": "药子 沙耶",
        "rumi": "朱城 瑠美",
        "reizo": "鹿山 丽情",
        "genbu-shokai-employee": "玄武商会职员",
        "shun": "春原 瞬",
        "kokona": "春原 心奈",
        "pei": "支付",
        "kai": "申谷 启",
        "cherino": "连河 切里诺",
        "tomoe": "佐城 智惠",
        "marina": "池仓 玛丽娜",
        "member-of-the-ss": "党卫军",
        "shigure": "间宵 时雨",
        "nodoka": "天见 和香",
        "meru": "姬木 梅露",
        "momiji": "秋泉 红叶",
        "minori": "安守 实里",
        "construction-department-member": "劳务人员",
        "kirino": "中务 桐乃",
        "fubuki": "合欢垣 吹雪",
        "kanna": "坎纳",
        "valkyrie-student": "瓦尔基里学生",
        "saki": "空井 咲希",
        "miyako": "月雪 宫子",
        "miyu": "霞泽 美游",
        "moe": "风仓 萌惠",
        "yukino": "雪乃",
        "niko": "妮可",
        "otogi": "音葵",
        "kurumi": "胡桃",
        "saori": "锭前 纱织",
        "atsuko": "秤 亚津子",
        "hiyori": "槌永 日和",
        "misaki": "戒野 美咲",
        "arius-student": "阿里乌斯学生",
        "president": "联邦学生会会长",
        "rin": "七神 凛",
        "momoka": "由良木 桃香",
        "ayumu": "岩柜 步梦",
        "kaya": "不知火 花耶",
        "aoi": "扇喜 葵",
        "student-council-officer": "联邦学生会成员",
        "mai": "舞",
        "shinon": "川流 诗乃",
        "bunnygirl-guard": "兔女郎守卫",
        "black-suit": "黑服",
        "golconde": "戈尔孔达",
        "décalcomanie": "印花釉法",
        "maestro": "巨匠",
        "beatrice": "贝阿朵莉切",
        "perorozilla": "佩洛洛斯拉",
        "automata": "奥马塔",
        "goro": "龟岛 五郎",
        "thugs": "看门人",
        "hod": "霍德",
        "chesed": "凯赛德",
        "binah": "薇娜",
        "peroro-sama": "佩洛洛博士",
        "nyantenmaru": "喵天丸",
        "shiro": "白",
        "kuro": "黑",
        "goz": "戈兹",
        "kivotos-citizen": "基沃托斯市民",
        "android": "机器人",
        "shibaseki-master": "柴大将",
        "sora": "空",
        "chimi-ichiza": "二流魅剧团",
        "kaiser-pmc-director": "凯撒PMC理事",
        "kaiser-pmc-general": "凯泽PMC将军",
        "kaiser-president": "凯泽主席",
        "kaiser-sof": "凯泽SOF",
        "kaiten-fx-mk.0": "KAITEN-FX-Mk.0",
        "kaitenranger": "KaitenRanger",
        "helmet-gang": "头盔团",
        "rabu": "和驹风 良舞",
        "hieronymus": "希罗尼姆斯",
        "hatsune-miku": "初音未来",
        "miria": "米莉亚",
        "nao": "纳奥",
        "rone": "罗内",
        "yukari": "由香里",
        "francis": "弗朗西斯",
        "anubis": "阿努比斯",
        "???": "???",
        "the-nameless-priests": "无名司祭",
        "akira": "阿基拉",
        "frenapates": "普雷纳瓦德斯",
        "yongha": "龙河",
        "arona": "阿罗娜",
        "plana": "普拉娜",
        "sensei": "老师"
}

if hasattr(sys, 'frozen'):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(application_path)

txt = ""

print("在Windows系统自带终端中，把文件拖入终端会自带引号，请务必去掉。")
print("拖入终端后按回车，如果空着则直接按回车。")
InputPath = input("请输入要转换的ClosureTalk.json的文件路径>>")
OutputPath = input("请输入保存的txt路径，如果为空则默认和该文件相同，建议为空>>")

#Delete " symbol

if InputPath[-1] == '"':
    InputPath = InputPath.split('"')[1]

if OutputPath:
    if OutputPath[-1] == '"':
        OutputPath = OutputPath.split('"')[1]
    

with open(InputPath,'r',encoding='utf-8') as f:
    Talk = json.loads(f.read())

#Processing data

ChatList = Talk["chat"]

CharacterList = [Chr['img'].lower() for Chr in Talk["chars"]]

#Loading spring

for Chr in CharacterList:
    txt = txt + "load spr {} {}".format(Chr, Chr+"_spr") + "\n"

txt += "load end\n"

#Adding chats
 
state = ''

ChoiceState = 0

for Chat in ChatList:

    # If type = text
    
    if Chat['yuzutalk']['type'] == "TEXT":
        if "img" in Chat:
            Name = Chat["img"].lower()
            if state == Name:
                pass
            else:

                # Let character hide then show if previous character isn't same

                if state != '':
                    txt += "spr hide {}\n".format(state)
                txt += "spr show {}\n".format(Name)
            content = Chat["content"].split("\n")
            for text in content:

                # Iterate by every return, cuz there's a bug on showing \n in aris studio
                # Student chat in chinese <Name> <Club>

                txt = txt + "txt '{}' '{}' '{}'\n".format(CharacterName[Name],CharacterClub[Name],text)
            state = Name
        else:

            # Use button to show sensei's chat
            # Every choice must follow a taget
            # Target <> is the event number after pressing button
            # I use self-add int

            txt += "button '{}' '{}'\n".format(Chat["content"],str(ChoiceState))
            txt += "target {}\n".format(str(ChoiceState))
            ChoiceState += 1

            # Not change if sensei say sth

        # Use \n for every part

        txt += '\n'

    # If type = narration

    elif Chat['yuzutalk']['type'] == "NARRATION":

        # Add chat with no name
        # Easiest one

        txt += "txt '' '' '{}'".format(Chat["content"])
        txt += '\n'

    # Choice
    elif Chat['yuzutalk']['type'] == "CHOICES":

        # In ClosureTalk, Choice is splited by \n
        # Iterate in content to add each choice
        # Every choice is point to one event

        content = Chat["content"].split("\n")
        txt += "button"
        for text in content:
            txt = txt + " '{}' '{}'".format(Name,str(ChoiceState))
        txt += "target {}".format(str(ChoiceState))
        ChoiceState += 1
        txt += "\n"

    else:
        pass

# Save by time

if OutputPath:
    with open("{}ArisStudio-{}.txt".format(OutputPath,time.strftime("%Y-%m-%d-%H-%M",time.gmtime())),'w',encoding='utf-8') as file:
        file.write(txt)
else:
    with open("ArisStudio-{}.txt".format(time.strftime("%Y-%m-%d-%H-%M",time.gmtime())),'w',encoding='utf-8') as file:
        file.write(txt)

print("转换完毕")
time.sleep(3)

# 防止有人看不到转换结果所以加了个 sleep 3

# 因为懒所以没做函数封装(被打)