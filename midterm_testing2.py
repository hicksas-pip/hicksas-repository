def s_t( lst, acc=0 ):
    if lst:
        tmp1 = lst[1:]
        tmp2 = lst[0]
        tmp3 = tmp2 + acc
        tmp4 = s_t( tmp1, tmp3)

        return tmp4

    else:

        return acc
        
