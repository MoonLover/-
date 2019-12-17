from mn_base import play_cards


def deal_times(y):
    p = 1
    if y == 88:
        print("发牌结束，谢谢！")
    else:
        while p < y:
            print("**********************共发牌 %d 次，第 %d 次发牌开始**********************" % (y,p))
            all_cards = play_cards.wash_cards()
            play_cards.deal_card(all_cards)
            print("**********************共发牌 %d 次，第 %d 次发牌结束**********************" % (y,p))
            p += 1


times = "0"
while times != "88":
    times = input("请输入发牌次数：")
    if times.isdigit():
        deal_times(int(times))
    else:
        print("请输入数字！")
