list = [2,-2,3,4,5,-1,-5,-3,-3,-2,-5,2]
def neg_and_pos_lists(list):
    pos_list = []
    neg_list = []
    for num in list:
        if num >= 0:
            pos_list.append(num)
        else:
            num < 0
            neg_list.append(num)
    return pos_list, neg_list


print(neg_and_pos_lists(list))
