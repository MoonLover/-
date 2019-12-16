import random



# 定义牌型
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
jokers = ("blackJoker", "redJoker")

cards_list = cards * 4
# 所有的牌
cards_list.extend(jokers)
print("所有的牌 %s"%cards_list)
print("总牌数 %d" % len(cards_list))

# j = 0

# list_param = []
rule_dic = {"redJoker": 0, "blackJoker": 1, "2": 2, "A": 3,"K": 4, "Q": 5, "J": 6, "10": 7, "9": 8, "8": 9, "7": 10, "6": 11, "5": 12,
            "4": 13, "3": 14 }


def sort(list_tmp):
    new_list = sorted(list_tmp, key=lambda x: rule_dic[x])
    # print("排序后的列表%s"%new_list)
    return new_list


def get_cards():
    tmp_list = []
    i = 0
    while i < 17:
        m = random.randint(0, len(cards_list) - 1)
        # print("取得随机数m的值是%d" % m)
        tmp_str = cards_list[m]
        tmp_list.append(tmp_str)
        del cards_list[m]
        i += 1
    return tmp_list


playerOne = get_cards()
playerOne = sort(playerOne)
print("玩家一的牌：%s" % playerOne)
# print(playerOne)
# print("剩余 %d 张的牌 %s：" % (len(cards_list),cards_list))


playerTwo = get_cards()
playerTwo = sort(playerTwo)
print("玩家二的牌：%s" % playerTwo)
# print("剩余 %d 张的牌 %s：" % (len(cards_list),cards_list))


playerThree = get_cards()
playerThree = sort(playerThree)
print("玩家三的牌：%s" % playerThree)
print("剩余 %d 张的牌 %s：" % (len(cards_list),cards_list))

