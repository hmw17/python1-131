def swap_list(list):
    if len(list) == 1:
        return list
    else:
        pos1 = (len(list) - 1) // 2
        pos2 = len(list) - 1
        list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
