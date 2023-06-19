def list_double_item(lst:list, tutle_list:bool = False, ignor_simvols:str ='') -> list:
    lst.sort(key=str)
    lst_len = len(lst)
    res = []
    if lst_len < 2:
        return res
    pos = 1
    base_item = 0
    count = 0
    while pos < lst_len:
        if ignor_simvols != '' and ignor_simvols.find(str(lst[pos])) > -1:
            pos += 1
            continue
        if lst[pos] != lst[base_item]:
            if count and tutle_list:
                res.append((lst[base_item], count + 1))
            elif count:
                res.append(lst[base_item])
            count = 0
            base_item = pos
        else:
            count += 1
        pos += 1

    if count and tutle_list:
        res.append((lst[base_item], count + 1))
    elif count:
        res.append(lst[base_item])

    return res