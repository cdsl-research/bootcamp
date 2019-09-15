old_list=[2,6,12,19,27,32,39,42,49,52,59,63,69,70]
for old in old_list:
    if 0 <= old <= 4:
        print(old, "幼年期")
    elif 5 <= old <= 14:
        print(old, "少年期")
    elif 15 <= old <= 24:
        print(old, "青年期")
    elif 25 <= old <= 44:
        print(old, "壮年期")
    elif 45 <= old <= 64:
        print(old, "中年期")
    else:
        print(old, "高年期")