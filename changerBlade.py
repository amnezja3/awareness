import partSpeech
def sam_g(x):
    SG = ['a', 'A', 'ą', 'Ą', 'e', 'E', 'ę', 'Ę', 'i', 'I',
            'o', 'O', 'ó', 'Ó', 'u', 'U', 'y', 'Y']
    exp =False
    for s in SG:
        if x == s:
            exp=True
    return exp

def sufix(word):
    ost_sm = len(word) -1
    while (ost_sm > 0):
        if sam_g(word[ost_sm]):
            break
        else:
            ost_sm -= 1

    if sam_g(word[ost_sm -1]):
        if word[ost_sm - 2] != 'ż' or word[ost_sm -2] != 'ź' or word[ost_sm -2] != 'z' \
            or word[ost_sm -2 ] != 'h':
            return word[ost_sm -2:]
        else:
            if word[ost_sm - 2] == 'ż' and word[ost_sm - 3] == 'd':
                return word[ost_sm -3:]
            elif word[ost_sm - 2] == 'z' and word[ost_sm - 3] == 'd':
                return word[ost_sm -3:]
            elif word[ost_sm - 2] == 'z' and word[ost_sm - 3] == 'c':
                return word[ost_sm -3:]
            elif word[ost_sm - 2] == 'z' and word[ost_sm - 3] == 'r':
                return word[ost_sm -3:]
            elif word[ost_sm - 2] == 'h' and word[ost_sm - 3] == 'c':
                return word[ost_sm -3:]
            else:
                return word[ost_sm -2:]
    else:
        if word[ost_sm - 1] != 'ż' or word[ost_sm -1] != 'ź' or word[ost_sm -1] != 'z' \
            or word[ost_sm -1 ] != 'h':
            return word[ost_sm -2:]
        else:
            if word[ost_sm - 1] == 'ż' and word[ost_sm - 2] == 'd':
                return word[ost_sm -2:]
            elif word[ost_sm - 1] == 'z' and word[ost_sm - 2] == 'd':
                return word[ost_sm -2:]
            elif word[ost_sm - 1] == 'z' and word[ost_sm - 2] == 'c':
                return word[ost_sm -2:]
            elif word[ost_sm - 1] == 'z' and word[ost_sm - 2] == 'r':
                return word[ost_sm -2:]
            elif word[ost_sm - 2] == 'h' and word[ost_sm - 2] == 'c':
                return word[ost_sm -2:]
            else:
                return word[ost_sm -1:]

def check_v_list(x_list, v, option = 'True'):
    count = 0
    exist = False
    for x in x_list:
        if option == 'True':
            if x == v:
                exist = True
        if option == 'Count':
            if x == v:
                count += 1
    if option == 'True':
        return exist
    if option == 'Count':
        return count

def kind_sex_word(word):
    psa_l = partSpeech.part_speach(word)
    psa = '  '
    if len(psa_l) == 1:
        psa = psa_l[0]
    if len(psa_l) > 1:
        co = 0
        for r in psa_l:
            RZ = check_v_list(r, 'rzeczownik')
            PRZ = check_v_list(r, 'przymiotnik')
            # print(RZ, PRZ)
            if RZ or PRZ:
                psa = r
            co += 1
    rodz = None
    if psa[0] == 'rzeczownik' or psa[0] == 'przymiotnik' or psa[0] == 'imiesłów':
        if psa[1].endswith('a') or psa[1].endswith('ść') or psa[1].endswith('wi') \
            or psa[1].endswith('rew'):
            if psa[1] !='kuba' or psa[1] != 'sól':
                rodz = 'Z'
        elif psa[1].endswith('o'):
            rodz = 'N'
        else:
            rodz = 'M'
    return rodz

def lpm(word):
    ksw = kind_sex_word(word)
    if ksw != None:
        if ksw == 'Z':
            if word.endswith('i') or word.endswith('y'):
                return 'LM'
            else:
                return 'LP'
        elif ksw == 'N':
            if word.endswith('i') or word.endswith('a'):
                return 'LM'
            else:
                return 'LP'
        else:
            if word.endswith('y') or word.endswith('e'):
                return 'LM'
            else:
                return 'LP'
    else:
        return 'LN'
if __name__ == '__main__':
    import awareness
    print(lpm('samochód'))
    print(lpm('kobiety'))

    lista = [1, 2, 4, 5, 5, 6]
