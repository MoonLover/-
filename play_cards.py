import random

# 定义牌型
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
jokers = ("blackJoker", "redJoker")


# cards_list = cards * 4
# # 所有的牌
# cards_list.extend(jokers)
# print("所有的牌 %s" % cards_list)
# print("总牌数 %d" % len(cards_list))


def get_cards(cards_list):
    tmpList = []
    i = 0
    while i < 17:
        m = random.randint(0, len(cards_list) - 1)
        # print("取得随机数m的值是%d" % m)
        tmpStr = cards_list[m]
        tmpList.append(tmpStr)
        del cards_list[m]
        i += 1
    return tmpList


def deal_card(cards_list):
    playerOne = get_cards(cards_list)
    playerOne.sort()
    print("玩家一的牌：%s" % playerOne)
    # print(playerOne)
    # print("剩余 %d 张的牌 %s：" % (len(cards_list),cards_list))

    playerTwo = get_cards(cards_list)
    playerTwo.sort()
    print("玩家二的牌：%s" % playerTwo)
    # print("剩余 %d 张的牌 %s：" % (len(cards_list),cards_list))

    playerThree = get_cards(cards_list)
    playerThree.sort()
    print("玩家三的牌：%s" % playerThree)
    print("剩余 %d 张的牌 %s：" % (len(cards_list), cards_list))


def wash_cards():
    card_all = cards * 4
    card_all.extend(jokers)
    return card_all


# card_all = wash_cards()
# print(card_all)
# deal_card(wash_cards())
