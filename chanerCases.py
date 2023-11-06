import partSpeech
import changerBlade
import takeTarget
import spacy
import requests
import os
import signal
import SAver



def case_updater(s):
    psa_l = partSpeech.part_speach(s)
    psa = '  '
    if len(psa_l) == 1:
        psa = psa_l[0]
    if len(psa_l) > 1:
        co = 0
        for r in psa_l:

            RZ = changerBlade.check_v_list(r, 'rzeczownik')
            PRZ = changerBlade.check_v_list(r, 'przymiotnik')
            # print(RZ, PRZ)
            if RZ or PRZ:
                psa = r
            co += 1

    pss = psa[1]
    sus = changerBlade.sufix(pss)
    sus_len = len(sus)

    too_short_no_suf = len(pss)
    if too_short_no_suf < 1:
        pss = ''
        sus = s
    try:
        with open('Casser.neural', 'r+', encoding='utf-8') as f:
            suf_file = f.readlines()
    except FileNotFoundError:
        suf_file = []

    suf_dict = {}
    for sf in suf_file:
        # print(sf)
        sf_split = sf.strip().split(':')
        s = sf_split[0]
        f_split= sf_split[1].replace(' ', '').split(',')
        suf_dict[s] = f_split
    # print(suf_dict)

    try:
        suf_dict[sus]
        sus_is = True
    except KeyError:
        sus_is = False
    if sus_is:
        cor = input(f'odmiana dla słowa {s} istnieje. \nNaciśnij <enter> żeby zupdateować. \nNapisz NIE żeby pominąć')
    else:
        cor = ''
    if cor != 'NIE':
        MIA = sus
        print(f'UPDATE słowa LP {pss}')
        print(f'Mianownik: kto / co to jest? {pss[:len(pss)-sus_len]} {sus}')
        DOP = input(f'Dopełniacz: kogo / czego niema? \n{pss[:len(pss)-sus_len]} ')
        CEL = input(f'Celownik: komu / czemu się przyglądam? \n{pss[:len(pss)-sus_len]} ')
        BIE = input(f'Biernik: kogo / co widzę? \n{pss[:len(pss)-sus_len]} ')
        NAR = input(f'Narzędnik: z kim / z czym idę? \n{pss[:len(pss)-sus_len]} ')
        MIE = input(f'Miejscownik: o kim / o czym  myślę? \n{pss[:len(pss)-sus_len]} ')
        WOL = input(f'Wołacz: o! hey! ty? \n{pss[:len(pss)-sus_len]} ')

        
        M_MIA = input(f'Mianownik LM: kto / co to są? \n{pss[:len(pss)-sus_len]} ')
        M_DOP = input(f'Dopełniacz LM: kogo / czego niema? \n{pss[:len(pss)-sus_len]} ')
        M_CEL = input(f'Celownik LM: komu / czemu się przyglądam? \n{pss[:len(pss)-sus_len]} ')
        M_BIE = input(f'Biernik LM: kogo / co widzę? \n{pss[:len(pss)-sus_len]} ')
        M_NAR = input(f'Narzędnik LM: z kim / z czym idę? \n{pss[:len(pss)-sus_len]} ')
        M_MIE = input(f'Miejscownik LM: o kim / o czym  myślę? \n{pss[:len(pss)-sus_len]} ')
        M_WOL = input(f'Wołacz LM: o! hey! wy? \n{pss[:len(pss)-sus_len]} ')
        suf_dict[MIA] = [DOP, CEL, BIE, NAR, MIE, WOL, M_MIA, M_DOP, M_CEL, M_BIE, M_NAR, M_MIE, M_WOL]

        answer = ''
        for k,v in suf_dict.items():
            answer += f'{k}:{v}\n'.replace('[', '').replace(']', '').replace("'", '')
        with open('Casser.neural', 'w+', encoding='utf-8') as f:
            f.write(answer)

def if_case(word):
    psa_l = partSpeech.part_speach(word, True)
    psa = '  '
    if len(psa_l) == 1:
        psa = psa_l[0]
    if len(psa_l) > 1:
        co = 0
        for r in psa_l:
            RZ = changerBlade.check_v_list(r, 'rzeczownik')
            PRZ = changerBlade.check_v_list(r, 'przymiotnik')
            # print(RZ, PRZ)
            if RZ or PRZ:
                psa = r
            co += 1
    w_s = psa[0]
    allow_speach = ['rzeczownik', 'przymiotnik']
    allow_exp = False
    for ax in allow_speach:
        if ax == w_s:
            allow_exp = True
    return allow_exp

def manual_case(target, L,):
    list_1 = [aa for aa in target]
    list_2 = [f'{L}-MIA', f'{L}-DOP', f'{L}-CEL', f'{L}-BIE', f'{L}-NAR', f'{L}-MIE', f'{L}-WOL']
    build_1 = {}
    build_2 = {}
    c = 0
    for l1 in list_1:
        build_1[c] = l1
        c += 1
    c = 0
    for l2 in list_2:
        build_2[c] = l2
        c += 1
    dopas_list = []
    wyb = [x for x in build_1.keys()]
    for k,v in build_2.items():
        for ak, bk in build_1.items():
            if ak in wyb:
                v = v.replace('MIA', 'Mianownik: kto / co jest/są? - ').replace('DOP', 'Dopełniacz: kogo / czego niema? - '
                        ).replace('CEL', 'Celownik: komu / czemu się przyglądam? - ').replace('BIE', 'Biernik: kogo / co widzę? - '
                            ).replace('NAR', 'Narzędnik: z kim / z czym idę? - ').replace('MIE', 'Miejscownik: o kim / o czym  myślę? - '
                                ).replace('WOL', 'Wołacz: o! hey! ty/wy? - ')
                print(f'[{ak}] - ', bk)
        dopas = input(f'dla {v} ')
        exp = (k, int(dopas))
        dopas_list.append(exp)
    dopas_dict ={}
    for w in dopas_list:
        dopas_dict[list_2[w[0]]] = list_1[w[1]]
    return dopas_dict

def change_cases(w, truck='BACK', update='YES', opt='MIA'):
    if not if_case(w):
        return ['Nieodmienialny']
    
    psa_l = partSpeech.part_speach(w)
    psa = '  '
    # print(psa_l)
    if len(psa_l) == 1:
        psa = psa_l[0]
    if len(psa_l) > 1:
        co = 0
        for r in psa_l:
            
            RZ = changerBlade.check_v_list(r, 'rzeczownik')
            PRZ = changerBlade.check_v_list(r, 'przymiotnik')
            # print(RZ, PRZ)
            if RZ or PRZ:
                psa = r
            co += 1
    # print(psa)
    psw = psa[1]
    suf = changerBlade.sufix(psw)
    suf_l = len(suf)
    w_no_suf = w[:len(w)- suf_l]

    too_short_no_suf = len(w_no_suf)
    if too_short_no_suf < 1:
        w_no_suf = ''
        suf = w

    with open('Casser.neural', 'r+', encoding='utf-8') as f:
        suf_file = f.readlines()
        # f.write(answer)

    suf_dict = {}
    for sf in suf_file:
        sf_split = sf.strip().split(':')
        s = sf_split[0]
        f_split= sf_split[1].replace(' ', '').split(',')
        suf_dict[s] = f_split

    try:
        suf_dict[suf]
        suf_is = True
    except KeyError:
        if update == 'YES':
            case_updater(w)
            return change_cases(w, truck, update, opt)
        suf_is = True
    if truck == 'BACK':
        if opt == 'MIA':
            return [psw]
        if suf_is:
            if opt == 'DOP':
                return [w_no_suf + suf_dict[suf][0]]
            if opt == 'CEL':
                return [w_no_suf + suf_dict[suf][1]]
            if opt == 'BIE':
                return [w_no_suf + suf_dict[suf][2]]
            if opt == 'NAR':
                return [w_no_suf + suf_dict[suf][3]]
            if opt == 'MIE':
                return [w_no_suf + suf_dict[suf][4]]
            if opt == 'WOL':
                return [w_no_suf + suf_dict[suf][5]]
        else:
            return [w_no_suf + '***']
    if truck == 'INFO':
        exp = []
        if psw == w:
            exp.append('Mianownik')
        if suf_is:
            counter = 0
            for v in suf_dict[suf]:
                # print(v)
                if w.endswith(v):
                    if counter == 0:
                        exp.append('Dopełniacz')
                    elif counter == 1:
                        exp.append('Celowni')
                    elif counter == 2:
                        exp.append('Biernik')
                    elif counter == 3:
                        exp.append('Narzędnik')
                    elif counter == 4:
                        exp.append('Miejscownik')
                    elif counter == 5:
                        exp.append('Wołacz')
                counter += 1
                if counter == 5:
                    return exp
        else:
            exp += ['ZRÓB UPDATE']
            return exp

def change_case_SP(base, word, target='rzeczownik', manual = True):
    target_n = takeTarget.take_superTarget(base, word, target)

    with open('cases_words_noun.neural', 'r', encoding='utf-8') as f:
        f_list = f.readlines()
    read_dict = {}
    for f in f_list:
        f_k = f.split('@KEY!')
        read_dict[f_k[0]] = f_k[1]

    with open('cases_sufix_noun.neural', 'r', encoding='utf-8') as f:
        s_list = f.readlines()
    sufix_dict = {}
    for s in s_list:
        s_k = s.split(':')
        sufix_dict[s_k[0]] = s_k[1]
    
    word_suf = changerBlade.sufix(target_n[0])
    if word_suf in [k for k in sufix_dict.keys()]:
        palette = sufix_dict[word_suf].strip().split(', ')
        case_group_noun = {
            "LP-SI" : {
                'LP-MIA' : [word_suf, []],
                'LP-DOP' : [palette[0], []],
                'LP-CEL' : [palette[1], []],
                'LP-BIE' : [palette[0], []],
                'LP-NAR' : [palette[3], []],
                'LP-MIE' : [palette[4], []],
                'LP-WOL' : [palette[5], []],
                        },
            "LP-SI" : {
                'LP-MIA' : [word_suf, []],
                'LP-DOP' : [palette[0], []],
                'LP-CEL' : [palette[1], []],
                'LP-BIE' : [word_suf, []],
                'LP-NAR' : [palette[3], []],
                'LP-MIE' : [palette[4], []],
                'LP-WOL' : [palette[5], []],
                        },
                
            "LM-SI" : {
                'LM-MIA' : [palette[6], []],
                'LM-DOP' : [palette[7], []],
                'LM-CEL' : [palette[8], []],
                'LM-BIE' : [palette[9], []],
                'LM-NAR' : [palette[10], []],
                'LM-MIE' : [palette[11], []],
                'LM-WOL' : [palette[12], []],
                    },
        }
    else:
        case_group_noun = {
        "LP-MZI" : {
                'LP-MIA' : [0, []],
                'LP-DOP' : ['a', []],
                'LP-CEL' : ['owi', []],
                'LP-BIE' : ['a', []],
                'LP-NAR' : ['iem', []],
                'LP-MIE' : ['u', []],
                'LP-WOL' : ['u', []],
                        },
        "LP-MZII" : {
                'LP-MIA' : [0, []],
                'LP-DOP' : ['a', []],
                'LP-CEL' : ['owi', []],
                'LP-BIE' : ['a', []],
                'LP-NAR' : ['em', ['iem']],
                'LP-MIE' : ['e', ['owie']],
                'LP-WOL' : ['e', ['owie']],
                        },
        "LP-MZIII" : {
                'LP-MIA' : [0, []],
                'LP-DOP' : ['a', []],
                'LP-CEL' : ['u', []],
                'LP-BIE' : ['a', []],
                'LP-NAR' : ['em', ['iem']],
                'LP-MIE' : ['e', ['owie']],
                'LP-WOL' : ['e', ['owie']],
                        },
        "LP-MZIV" : {
                'LP-MIA' : ['a', []],
                'LP-DOP' : ['y', []],
                'LP-CEL' : ['e', ['owie']],
                'LP-BIE' : ['ę', []],
                'LP-NAR' : ['ą', []],
                'LP-MIE' : ['e', ['owie']],
                'LP-WOL' : ['o', []],
                        },
        
        "LP-MNI" : {
                'LP-MIA' : [0, []],
                'LP-DOP' : ['u', []],
                'LP-CEL' : ['owi', []],
                'LP-BIE' : [0, []],
                'LP-NAR' : ['em', ['iem']],
                'LP-MIE' : ['e', ['owie']],
                'LP-WOL' : ['e', ['owie']],
                        },
        "LP-MNII" : {
                'LP-MIA' : [0, []],
                'LP-DOP' : ['a', []],
                'LP-CEL' : ['owi', []],
                'LP-BIE' : [0, []],
                'LP-NAR' : ['em', ['iem']],
                'LP-MIE' : ['e', ['owie']],
                'LP-WOL' : ['e', ['owie']],
                        },
        "LP-MNIII" : {
                'LP-MIA' : [0, []],
                'LP-DOP' : ['a', []],
                'LP-CEL' : ['u', []],
                'LP-BIE' : [0, []],
                'LP-NAR' : ['em', ['iem']],
                'LP-MIE' : ['e', ['owie']],
                'LP-WOL' : ['e', ['owie']],
                        },

        "LP-ZI" : {
                'LP-MIA' : ['a', []],
                'LP-DOP' : ['y', []],
                'LP-CEL' : ['e', ['owie']],
                'LP-BIE' : ['ę', []],
                'LP-NAR' : ['ą', []],
                'LP-MIE' : ['e', ['owie']],
                'LP-WOL' : ['o', []],
                        },
        "LP-ZII" : {
                'LP-MIA' : ['a', []],
                'LP-DOP' : ['i', ['ami', 'owi']],
                'LP-CEL' : ['e', ['owie']],
                'LP-BIE' : ['ę', []],
                'LP-NAR' : ['ą', []],
                'LP-MIE' : ['e', ['owie']],
                'LP-WOL' : ['o', []],
                        },
        "LP-ZIII" : {
                'LP-MIA' : ['i', ['ami', 'owi']],
                'LP-DOP' : ['i', ['ami', 'owi']],
                'LP-CEL' : ['i', ['ami', 'owi']],
                'LP-BIE' : ['ą', []],
                'LP-NAR' : ['ą', []],
                'LP-MIE' : ['i', ['ami', 'owi']],
                'LP-WOL' : ['i', ['ami', 'owi']],
                        },
        "LP-ZIV" : {
                'LP-MIA' : [0, []],
                'LP-DOP' : ['y', []],
                'LP-CEL' : ['y', []],
                'LP-BIE' : [0, []],
                'LP-NAR' : ['ą', []],
                'LP-MIE' : ['y', []],
                'LP-WOL' : ['y', []],
                        },
        "LP-ZV" : {
                'LP-MIA' : [0, []],
                'LP-DOP' : ['i', ['ami', 'owi']],
                'LP-CEL' : ['i', ['ami', 'owi']],
                'LP-BIE' : [0, []],
                'LP-NAR' : ['ą', []],
                'LP-MIE' : ['i', ['ami', 'owi']],
                'LP-WOL' : ['i', ['ami', 'owi']],
                        },
        "LP-ZVI" : {
                'LP-MIA' : ['a', []],
                'LP-DOP' : ['i', ['owi', 'ami']],
                'LP-CEL' : ['i', ['ami', 'owi']],
                'LP-BIE' : ['ę', []],
                'LP-NAR' : ['ą', []],
                'LP-MIE' : ['i', ['ami', 'owi']],
                'LP-WOL' : ['u', []],
                        },

        "LP-NI" : {
                'LP-MIA' : ['o', []],
                'LP-DOP' : ['a', []],
                'LP-CEL' : ['u', []],
                'LP-BIE' : ['o', []],
                'LP-NAR' : ['em', ['iem']],
                'LP-MIE' : ['e', ['owie']],
                'LP-WOL' : ['o', []],
                        },
        "LP-NII" : {
                'LP-MIA' : ['e', []],
                'LP-DOP' : ['a', []],
                'LP-CEL' : ['u', []],
                'LP-BIE' : ['e', ['owie']],
                'LP-NAR' : ['em', ['iem']],
                'LP-MIE' : ['u', []],
                'LP-WOL' : ['e', []],
                        },
        "LP-NIII" : {
                'LP-MIA' : ['ę', []],
                'LP-DOP' : ['a', []],
                'LP-CEL' : ['u', []],
                'LP-BIE' : ['ę', []],
                'LP-NAR' : ['em', []],
                'LP-MIE' : ['u', []],
                'LP-WOL' : ['ę', []],
                        },
        "LP-NIV" : {
                'LP-MIA' : ['um', []],
                'LP-DOP' : ['um', []],
                'LP-CEL' : ['um', []],
                'LP-BIE' : ['um', []],
                'LP-NAR' : ['um', []],
                'LP-MIE' : ['um', []],
                'LP-WOL' : ['um', []],
                        },



        "LM-MOI" : {
                'LM-MIA' : ['owie', []],
                'LM-DOP' : ['ów', []],
                'LM-CEL' : ['om', []],
                'LM-BIE' : ['ów', []],
                'LM-NAR' : ['ami', []],
                'LM-MIE' : ['ach', []],
                'LM-WOL' : ['owie', []],
                    },
        "LM-MOII" : {
                'LM-MIA' : ['y', []],
                'LM-DOP' : ['ów', []],
                'LM-CEL' : ['om', []],
                'LM-BIE' : ['ów', []],
                'LM-NAR' : ['ami', []],
                'LM-MIE' : ['ach', []],
                'LM-WOL' : ['y', []],
                    },
        "LM-MOIII" : {
                'LM-MIA' : ['e', []],
                'LM-DOP' : ['i', ['ami', 'owi']],
                'LM-CEL' : ['om', []],
                'LM-BIE' : ['i', ['ami', 'owi']],
                'LM-NAR' : ['ami', []],
                'LM-MIE' : ['ach', []],
                'LM-WOL' : ['e', []],
                    },
        "LM-MOIV" : {
                'LM-MIA' : ['i', ['ami', 'owi']],
                'LM-DOP' : ['ów', []],
                'LM-CEL' : ['om', []],
                'LM-BIE' : ['ów', []],
                'LM-NAR' : ['ami', []],
                'LM-MIE' : ['ach', []],
                'LM-WOL' : ['i', ['ami', 'owi']],
                    },

        "LM-MNOI" : {
                'LM-MIA' : ['y', []],
                'LM-DOP' : ['ów', []],
                'LM-CEL' : ['om', []],
                'LM-BIE' : ['y', []],
                'LM-NAR' : ['ami', []],
                'LM-MIE' : ['ach', []],
                'LM-WOL' : ['y', []],
                    },
        "LM-MNOII" : {
                'LM-MIA' : ['e', []],
                'LM-DOP' : ['y', []],
                'LM-CEL' : ['om', []],
                'LM-BIE' : ['e', []],
                'LM-NAR' : ['mi', ['ami']],
                'LM-MIE' : ['ach', []],
                'LM-WOL' : ['e', []],
                    },


        "LM-ZI" : {
                'LM-MIA' : ['y', []],
                'LM-DOP' : ['', ['y', 'om', 'mi', 'ach','um', 'ę', 'a', 'ą', 'u', 'ę', 'em', 'i', 'owi', 'iem']],
                'LM-CEL' : ['om', []],
                'LM-BIE' : ['y', []],
                'LM-NAR' : ['mi', ['ami']],
                'LM-MIE' : ['ach', []],
                'LM-WOL' : ['y', []],
                    },
        "LM-ZII" : {
                'LM-MIA' : ['i', ['ami', 'owi']],
                'LM-DOP' : ['', ['y', 'om', 'mi', 'ach','um', 'ę', 'a', 'ą', 'u', 'ę', 'em', 'i', 'owi', 'iem']],
                'LM-CEL' : ['om', []],
                'LM-BIE' : ['i', ['ami', 'owi']],
                'LM-NAR' : ['mi', ['ami']],
                'LM-MIE' : ['ach', []],
                'LM-WOL' : ['i', ['ami', 'owi']],
                    },
        "LM-ZIII" : {
                'LM-MIA' : ['nie', []],
                'LM-DOP' : ['ń', []],
                'LM-CEL' : ['om', []],
                'LM-BIE' : ['nie', []],
                'LM-NAR' : ['ami', []],
                'LM-MIE' : ['ach', []],
                'LM-WOL' : ['nie', []],
                    },

        "LM-NI" : {
                'LM-MIA' : ['a', []],
                'LM-DOP' : ['', ['y', 'om', 'mi', 'ach','um', 'ę', 'a', 'ą', 'u', 'ę', 'em', 'i', 'owi', 'iem']],
                'LM-CEL' : ['om', []],
                'LM-BIE' : ['a', []],
                'LM-NAR' : ['ami', []],
                'LM-MIE' : ['ach', []],
                'LM-WOL' : ['a', []],
                    },
        "LM-NII" : {
                'LM-MIA' : ['a', []],
                'LM-DOP' : ['ów', []],
                'LM-CEL' : ['om', []],
                'LM-BIE' : ['a', []],
                'LM-NAR' : ['ami', []],
                'LM-MIE' : ['ach', []],
                'LM-WOL' : ['a', []],
                    },
    }

    count_LP = 0
    selected_items = {}
    key_selected = 0
    key_selected_LM = 10
    for k in case_group_noun.keys():
        if k.startswith('LP'):
            count_LP = 0
            temp = {}
            for key, test in case_group_noun[k].items():
                if key.startswith('LP'):
                    for t in target_n:
                        if test[0] != 0 and t.endswith(test[0]):
                            nn = False
                            for n in test[1]:
                                if t.endswith(n):
                                    nn = True
                            if not nn:
                                count_LP += 1
                                temp[key] = t
                            if len(temp) == 7:
                                break
                    if test[0] == 0:
                        count_LP += 1
                        temp[key] = t
                    if len(temp) == 7:
                        selected_items[key_selected] = {}
                        print(f'\nOption LP: {key_selected}')
                        for s, av in temp.items():
                            print(f'{s} {av}')
                            selected_items[key_selected][s] = av
                        key_selected += 1
    exp_dict_LP = {}
    if key_selected > 1:
        select_LP = input('Która deklinacja jest najlepsza dla Liczby Pojedyńczej\n[100] - Manual: ')
        try: int(select_LP)
        except KeyError: select_LP = int(input('To nie jest liczba. Wybierz jeszcze raz.\n[100] - Manual\nKtóra deklinacja jest najlepsza dla ciebie: '))
        if int(select_LP) != 100:
            exp_dict_LP = selected_items[int(select_LP)]
        else:
            exp_dict_LP = manual_case(target_n, 'LP')
    elif key_selected == 0:
        exp_dict_LP = manual_case(target_n, 'LP')

    elif key_selected == 1:
        exp_dict_LP = selected_items[0]
        select_LP = input('Zmień\n[100] - Manual: ')
        try: int(select_LP)
        except KeyError: select_LP = int(input('To nie jest liczba. Wybierz jeszcze raz.\n[100] - Manual\nKtóra deklinacja jest najlepsza dla ciebie: '))
        if int(select_LP) == 100:
            exp_dict_LP = manual_case(target_n, 'LP')

    for k in case_group_noun.keys():
        if k.startswith('LM'):
            count_LM = 0
            temp_LM = {}
            for key, test in case_group_noun[k].items():
                if key.startswith('LM'):
                    for t in target_n:
                        if t.endswith(test[0]):
                            nn = False
                            for n in test[1]:
                                if t.endswith(n):
                                    nn = True
                            if not nn:
                                count_LM += 1
                                temp_LM[key] = t
                            if len(temp_LM) == 7:
                                break
                    if len(temp_LM) == 7:
                        selected_items [key_selected_LM] = {}
                        print(f'\nOption LM: {key_selected_LM}')
                        for s, av in temp_LM.items():
                            print(f'{s} {av}')
                            selected_items[key_selected_LM][s] = av
                        key_selected_LM += 1
    exp_dict_LM ={}
    if key_selected_LM > 11:
        select_LM = input('Która deklinacja jest najlepsza dla Liczby Mnogiej\n[100] - Manual: ')
        try: int(select_LM)
        except KeyError: select_LM = int(input('To nie jest liczba. Wybierz jeszcze raz.\n[100] - Manual\nKtóra deklinacja jest najlepsza dla ciebie: '))
        if int(select_LM) != 100:
            exp_dict_LM = selected_items[int(select_LM)]
        else:
            exp_dict_LM = manual_case(target_n, 'LM')
    elif key_selected_LM == 10:
        exp_dict_LM = manual_case(target_n, 'LM')
    elif key_selected_LM == 11:
        exp_dict_LM = selected_items[10]
        select_LM = input('Zmień\n[100] - Manual: ')
        try: int(select_LM)
        except KeyError: select_LM = int(input('To nie jest liczba. Wybierz jeszcze raz.\n[100] - Manual\nKtóra deklinacja jest najlepsza dla ciebie: '))
        if int(select_LM) == 100:
            exp_dict_LM = manual_case(target_n, 'LM')

    exp_dict = {}
    select_RODZ = input('Wprowadź rodzaj\n[0] - Męski, [1] -Żeńskie, [2] - Nijaki: ')
    try: int(select_RODZ)
    except KeyError: select_RODZ = int(input('To nie jest liczba. Wybierz jeszcze raz.\nWprowadź rodzaj\n[0] - Męski, [1] - Żeńskie, [2] - Nijaki: '))
    if int(select_RODZ) == 0:
        exp_dict['RODZ'] = 'M'
    if int(select_RODZ) == 1:
        exp_dict['RODZ'] = 'Ż'
    if int(select_RODZ) == 2:
        exp_dict['RODZ'] = 'N'

    select_KATE = input('Wprowadź cechę\n[0] - Żywy, [1] - Niezywy: ')
    try: int(select_KATE)
    except KeyError: select_KATE = int(input('To nie jest liczba. Wybierz jeszcze raz.\nWprowadź cechę\n[0] - Żywy, [1] - Niezywy: '))
    if int(select_KATE) == 0:
        exp_dict['CECH'] = 'LIVE'
    if int(select_KATE) == 1:
        exp_dict['CECH'] = 'notLIVE'

    answer = f'{exp_dict_LP["LP-MIA"]}@KEY!'
    for s,x in exp_dict.items():
        answer += f'{s}:{x}!'    
    for s,x in exp_dict_LP.items():
        answer += f'{s}:{x}!'    
    for s,x in exp_dict_LM.items():
        answer += f'{s}:{x}!'
    answer = answer[:len(answer) - 1] + '\n'
    a_k = answer.split('@KEY!')
    read_dict[a_k[0]] = a_k[1]
    save_f = ''
    for k,v in read_dict.items():
        save_f += f'{k}@KEY!{v}'
    signal.signal(signal.SIGINT, signal.SIG_IGN) # tutaj niech wyłączy CTRL+C
    os.system('color 4E')
    with open('cases_words_noun.neural', 'w+', encoding='utf-8') as f:
        f.write(save_f)
    os.system('color 07')
    signal.signal(signal.SIGINT, signal.SIG_DFL) # tutaj niech włączy CTRL+C
    sufix_wr = f"{changerBlade.sufix(exp_dict_LP['LP-MIA'])}:{changerBlade.sufix(exp_dict_LP['LP-DOP'])}, {changerBlade.sufix(exp_dict_LP['LP-CEL'])}, {changerBlade.sufix(exp_dict_LP['LP-BIE'])}, {changerBlade.sufix(exp_dict_LP['LP-NAR'])}, {changerBlade.sufix(exp_dict_LP['LP-MIE'])}, {changerBlade.sufix(exp_dict_LP['LP-WOL'])}, {changerBlade.sufix(exp_dict_LM['LM-MIA'])}, {changerBlade.sufix(exp_dict_LM['LM-DOP'])}, {changerBlade.sufix(exp_dict_LM['LM-CEL'])}, {changerBlade.sufix(exp_dict_LM['LM-BIE'])}, {changerBlade.sufix(exp_dict_LM['LM-NAR'])}, {changerBlade.sufix(exp_dict_LM['LM-MIE'])}, {changerBlade.sufix(exp_dict_LM['LM-WOL'])}\n"
    sufix_wr_split = sufix_wr.split(':')
    sufix_dict[sufix_wr_split[0]] = sufix_wr_split[1]

    save_s = ''
    for k,v in sufix_dict.items():
        save_s += f'{k}:{v}'
    signal.signal(signal.SIGINT, signal.SIG_IGN) # tutaj niech wyłączy CTRL+C
    os.system('color 4E')
    with open('cases_sufix_noun.neural', 'w+', encoding='utf-8') as f:
        f.write(save_s)
    os.system('color 07')
    signal.signal(signal.SIGINT, signal.SIG_DFL) # tutaj niech włączy CTRL+C
nlp = spacy.load('pl_core_news_sm')

def spacy_gender(noun):
    doc = nlp(noun)
    token = doc[0]
    split_data = str(token.morph).split('|')

    exp_dict = {}
    if 'Gender=Fem' in split_data:
        exp_dict['GENDER'] = 'Z'
        # return {'GENDER' : 'Z', 'LIFE' : 'notLIVE'}
    elif 'Gender=Masc' in split_data:
        exp_dict['GENDER'] = 'M'
    elif 'Gender=Neut' in split_data:
        exp_dict['GENDER'] = 'N'
    else:
        exp_dict['GENDER'] = 'N'

    if 'Animacy=Inan' in split_data:
        exp_dict['LIFE'] = 'notLIVE'
    elif 'Animacy=Hum' in split_data:
        exp_dict['LIFE'] = 'LIVE'
    else:
        exp_dict['LIFE'] = 'notLIVE'
    return exp_dict


def part_Speech_2(word):
    import requests
    def brain(witch):
        witch = str(witch)
        if witch == 'brain':
            MAIN_FILE_BRAIN = 'brain.neural'
            return MAIN_FILE_BRAIN
        if witch == 'wiki':
            TMP_FILE_WIKI = 'filter_wiki.recognizer'
            return TMP_FILE_WIKI

    signal.signal(signal.SIGINT, signal.SIG_IGN) # tutaj niech wyłączy CTRL+C
    os.system('color 4E')
    with open('cases_words_noun.neural', 'r', encoding='utf-8') as f:
        f_list = f.readlines()
    os.system('color 07')
    signal.signal(signal.SIGINT, signal.SIG_DFL) # tutaj niech włączy CTRL+C
    read_dict = {}
    for f in f_list:
        f_k = f.split('@KEY!')
        read_dict[f_k[0]] = f_k[1]
    
    try:
        read_dict[word]
        print(f'Użyto part_Speech_2 [word exist] dla słowa: {word}')
        return True
    except KeyError:
        TMP_WIKI = str(brain('wiki'))

        url = f'https://pl.wiktionary.org/wiki/{word}'
        while True:
            try:
                r = requests.get(url)
                htmlSTR = r.text
                break
            except:
                print('Ponowna próba nawiązania połączenia internetowego!')
        
        dict_exp = {}
        fi=open(TMP_WIKI, 'w+', encoding='utf-8')    
        for ch in htmlSTR:
            try:fi.write(ch)
            except:pass
        fi.close()
        fi=open(TMP_WIKI, 'r', encoding='utf-8')
        fil = fi.readlines()
        fi.close()
        ind = 0
        dict_exp['LP-MIA'] = word
        for f in fil:
            f = str(f).strip()
            if f.count('liczba mnoga') > 0:
                ff = f.split('<td class="') #[1].replace('</td>', '')
                for ax in ff:
                    if ax.startswith('mianownik">'):
                        try: mianownik = ax.replace('mianownik">', '').replace('</td>', '').replace('</tr><tr class="forma">', '') # .split('<')[0]
                        except: mianownik = ''
                        if mianownik.count('>') > 0:
                            listMianownik = mianownik.split('>')
                            for lm in listMianownik:
                                if lm.startswith(word[:int(len(word) * 0.7)]):
                                    mianownik = lm.split('<')[0].replace(' / ', '')
                                    if len(mianownik) > 0 and len(mianownik) < len(word) + 4:
                                        dict_exp['LM-MIA'] = mianownik
                                        break
                        else:
                            if len(mianownik) > 0 and len(mianownik) < len(word) + 4:
                                dict_exp['LM-MIA'] = mianownik
                aa = f.split('title="')
                for aq in aa:
                    if aq.startswith('dopełniacz'):
                        try: dopelniaczLP = aq.replace('dopełniacz">dopełniacz</a></td><td>', '').split('</td><td>')[0]
                        except: dopelniaczLP = ''
                        try: dopelniaczLM = aq.replace('dopełniacz">dopełniacz</a></td><td>', '').split('</td><td>')[1].split('<')[0].replace(' / ', '')
                        except: dopelniaczLM = ''
                        if len(dopelniaczLP) > 0 and len(dopelniaczLP) < len(word) + 4:
                            dict_exp['LP-DOP'] = dopelniaczLP
                        if len(dopelniaczLM) > 0 and len(dopelniaczLM) < len(word) + 4:
                            dict_exp['LM-DOP'] = dopelniaczLM

                    if aq.startswith('celownik'):
                        try: celownikLP = aq.replace('celownik">celownik</a></td><td>', '').split('</td><td>')[0]
                        except: celownikLP = ''
                        try: celownikLM = aq.replace('celownik">celownik</a></td><td>', '').split('</td><td>')[1].split('<')[0].replace(' / ', '')
                        except: celownikLM = ''
                        if len(celownikLP) > 0 and len(celownikLP) < len(word) + 4:
                            dict_exp['LP-CEL'] = celownikLP
                        if len(celownikLM) > 0 and len(celownikLM) < len(word) + 4:
                            dict_exp['LM-CEL'] = celownikLM

                    if aq.startswith('biernik'):
                        try: biernikLP = aq.replace('biernik">biernik</a></td><td>', '').split('</td><td>')[0]
                        except: biernikLP = ''
                        try: biernikLM = aq.replace('biernik">biernik</a></td><td>', '').split('</td><td>')[1].split('<')[0].replace(' / ', '')
                        except: biernikLM = ''
                        if len(biernikLP) > 0 and len(biernikLP) < len(word) + 4:
                            dict_exp['LP-BIE'] = biernikLP
                        if len(biernikLM) > 0 and len(biernikLM) < len(word) + 4:
                            dict_exp['LM-BIE'] = biernikLM

                    if aq.startswith('narzędnik'):
                        try: narzednikLP = aq.replace('narzędnik">narzędnik</a></td><td>', '').split('</td><td>')[0]
                        except: narzednikLP = ''
                        try: narzednikLM = aq.replace('narzędnik">narzędnik</a></td><td>', '').split('</td><td>')[1].split('<')[0].replace(' / ', '')
                        except: narzednikLM = ''
                        if len(narzednikLP) > 0 and len(narzednikLP) < len(word) + 4:
                            dict_exp['LP-NAR'] = narzednikLP
                        if len(narzednikLM) > 0 and len(narzednikLM) < len(word) + 4:
                            dict_exp['LM-NAR'] = narzednikLM

                    if aq.startswith('miejscownik'):
                        try: miejscownikLP = aq.replace('miejscownik">miejscownik</a></td><td>', '').split('</td><td>')[0]
                        except: miejscownikLP = ''
                        try: miejscownikLM = aq.replace('miejscownik">miejscownik</a></td><td>', '').split('</td><td>')[1].split('<')[0].replace(' / ', '')
                        except: miejscownikLM = ''
                        if len(miejscownikLP) > 0 and len(miejscownikLP) < len(word) + 4:
                            dict_exp['LP-MIE'] = miejscownikLP
                        if len(miejscownikLM) > 0 and len(miejscownikLM) < len(word) + 4:
                            dict_exp['LM-MIE'] = miejscownikLM

                    if aq.startswith('wołacz'):
                        try: wolaczLP = aq.replace('wołacz">wołacz</a></td><td>', '').split('</td><td>')[0]
                        except: wolaczLP = ''
                        try: wolaczLM = aq.replace('wołacz">wołacz</a></td><td>', '').split('</td><td>')[1].split('<')[0].replace(' / ', '')
                        except: wolaczLM = ''
                        if len(wolaczLP) > 0 and len(wolaczLP) < len(word) + 4:
                            dict_exp['LP-WOL'] = wolaczLP
                        if len(wolaczLM) > 0 and len(wolaczLM) < len(word) + 4:
                            dict_exp['LM-WOL'] = wolaczLM
            ind +=1
        try:
            dict_exp['LM-WOL']
            good = True
        except KeyError:
            good = False
        if good:
            rodz_cech = spacy_gender(word)
            RODZ = rodz_cech['GENDER']
            CECH = rodz_cech['LIFE']
            answer = f'{dict_exp["LP-MIA"]}@KEY!RODZ:{RODZ}!CECH:{CECH}!'
            for s,x in dict_exp.items():
                answer += f'{s}:{x}!'
            answer = answer[:len(answer) - 1] + '\n'
            a_k = answer.split('@KEY!')
            read_dict[a_k[0]] = a_k[1]

            save_f = ''
            for k,v in read_dict.items():
                save_f += f'{k}@KEY!{v}'
            # print(save_f)
            signal.signal(signal.SIGINT, signal.SIG_IGN) # tutaj niech wyłączy CTRL+C
            os.system('color 4E')
            with open('cases_words_noun.neural', 'w+', encoding='utf-8') as f:
                f.write(save_f)
            os.system('color 07')
            signal.signal(signal.SIGINT, signal.SIG_DFL) # tutaj niech włączy CTRL+C
            print(f'Użyto part_Speech_2 [word not exist] dla słowa: {word}')
            return good
        else:
            return good

def noun_adj_case_detector(sentence):
    doc = nlp(sentence)
    results = {}
    tech_dict_noun = {
        'Nom': 'MIA',  # mianownik
        'Gen': 'DOP',  # dopełniacz
        'Dat': 'CEL',  # celownik
        'Acc': 'BIE',  # biernik
        'Ins': 'NAR',  # narzędnik
        'Loc': 'MIE',  # miejscownik
        'Voc': 'WOL',  # wołacz
        'Sing': 'LP',  # liczba pojedyncza
        'Plur': 'LM',  # liczba mnoga
        }

    tech_dict_adj = {
        'Nom': 'MIA',  # mianownik
        'Gen': 'DOP',  # dopełniacz
        'Dat': 'CEL',  # celownik
        'Acc': 'BIE',  # biernik
        'Ins': 'NAR',  # narzędnik
        'Loc': 'MIE',  # miejscownik
        'Voc': 'WOL',  # wołacz
        'Sing-Male-Anim': 'LP-MOSZW',  # liczba pojedyncza, rodzaj męski, żywy 
        'Sing-Male-Inan': 'LP-MRZ', # liczba pojedyncza, rodzaj męski, nieżywy 
        'Sing-Female': 'LP-Z', # liczba pojedyncza, rodzaj żeński
        'Sing-Neut': 'LP-N', # liczba pojedyncza, rodzaj nijaki
        'Plur-Male': 'LM-MOS', # liczba pojedyncza, rodzaj męskoosobowy
        'Plur-Female-Neut': 'LM-NMOS', # liczba pojedyncza, rodzaj niemęskoosobowy
        }
    for token in doc:
        # print(token.text, token.morph)
        if token.pos_ == 'NOUN':
            number = token.morph.get('Number', [])[0]
            case = token.morph.get('Case', [])[0]
            if number == 'Ptan':
                number= 'Sing'
            results[token.text] = f"{tech_dict_noun[number]}-{tech_dict_noun[case]}"
        elif token.pos_ == 'ADJ':
            case = token.morph.get('Case', [])[0]
            number = token.morph.get('Number', [''])[0]
            gender = token.morph.get('Gender', [''])[0]
            animacy = token.morph.get('Animacy', [''])[0]
            if token.text.lower().startswith('nie'):
                negation = 'NEG'
            else:
                negation = 'POZ'
            case = tech_dict_adj[case]
            if number == 'Sing' and gender == 'Masc':
                if animacy == 'Inan':
                    numgen = tech_dict_adj['Sing-Male-Inan']
                else:
                    numgen = tech_dict_adj['Sing-Male-Anim']
            elif number == 'Sing' and gender == 'Female':
                numgen = tech_dict_adj['Sing-Female']
            elif number == 'Sing' and gender == 'Neut':
                numgen = tech_dict_adj['Sing-Neut']
            elif number == 'Plur' and gender == 'Masc':
                numgen = tech_dict_adj['Plur-Male']
            else:
                numgen = tech_dict_adj['Plur-Female-Neut']
            results[token.text] = f"{case}-{numgen}-{negation}"
        else:
            results[token.text] = False
    return results

def part_check(word, multi = 'main'):
    case_dict = {
    'ADJ': 'przymiotnik',
    'ADP': 'przyimek',
    'ADV': 'przysłówek',
    'AUX': 'czasownik', # czasownik posiłkowy
    'CONJ': 'spójnik',
    'CCONJ': 'spójnik', # spójnik spójny
    'DET': 'determiner',
    'INTJ': 'wykrzyknik',
    'NOUN': 'rzeczownik',
    'NUM': 'liczebnik',
    'PART': 'partykuła',
    'PRON': 'zaimek',
    'PROPN': 'nazwa własna',
    'PUNCT': 'znak interpunkcyjny',
    'SCONJ': 'spójnik', # spójnik podrzędny
    'SYM': 'symbol',
    'VERB': 'czasownik',
    'X': 'onim'
    }
    
    # nlp = spacy.load("pl_core_news_sm")
    doc = nlp(word)
    if len(doc) > 0:
        token = doc[0]
        pos_tag = token.pos_
        if pos_tag in case_dict:
            return case_dict[pos_tag]
    return "onim"

def change_cases_SP_adjective(base, word, truck='BACK', opt='MIA', numb='LM', rodz = 'MOS', direct = 'POZ', target='przymiotnik', update='YES'):
    # if not if_case(word):
    #     if truck == 'ALL':
    #         return {}
    #     else:
    #         return 'Nieodmienialny'
    
    target_n = takeTarget.take_superTarget(base, word, target)
    word_0 = target_n[0]
    if word_0 == 'a': 
        if truck == 'ALL':
            return {}
        else:
            return 'Nieodmienialny'
    read_dict = SAver.open_ver('cases_words_adjective', 'read_dict')
    if not read_dict: 
        SAver.save_ver('cases_words_adjective', 'read_dict', {})
        read_dict = {}

    if word_0 in [k for k in read_dict.keys()]:
        word_dict = read_dict[word_0]
    else:
        automatic_casses = part_Speech_3(word_0)
        if not automatic_casses:
            if update == 'YES':
                return change_cases_SP_adjective(base, word, truck, opt, numb, rodz, direct, target, update)
            else:
                if truck == 'ALL':
                    return {}
                else:
                    return 'MAKE-UPDATE'
        else:
            return change_cases_SP_adjective(base, word, truck, opt, numb, rodz, direct, target, update)
    if truck == 'BACK':
        for k in word_dict.keys():
            if k.count(opt) == 1 and k.count(numb) == 1 and k.count(rodz) == 1 and k.count(direct) == 1:
                return word_dict[k]
    
    exp_dict = {'CASE' : []}
    if truck == 'INFO':
        for wik, wiv in word_dict.items():
            if wiv == word:
                exp_dict['CASE'].append(wik)
        return exp_dict
    if truck == 'ALL':
        return word_dict

def part_Speech_3(word):
    read_dict = SAver.open_ver('cases_words_adjective', 'read_dict')
    if not read_dict: read_dict = {}
    try:
        read_dict[word]
        return True
    except KeyError:
        dict_exp = case_adj_dict_generator(word)
        # print(dict_exp)
        if not dict_exp: dict_exp = {}
        if len(dict_exp) > 0:
            for no_of_dict_word in dict_exp.keys():
                read_dict[
                    dict_exp[no_of_dict_word]['MIA-LP-MOSZW-POZ']
                    ] = dict_exp[no_of_dict_word]
        try:
            read_dict[word]['MIA-LP-MOSZW-POZ']
            read_dict[word]['MIE-LP-MRZ-NEG']
            good = True
        except KeyError:
            good = False
        if good:
            SAver.save_ver('cases_words_adjective', 'read_dict', read_dict)
            return good
        else:
            return good

def case_adj_dict_generator(word):
    url_sjp = f'https://sjp.pl/{word}'
    while True:
        try:
            sjp = requests.get(url_sjp)
            htmlSTR_sjp = sjp.text
            with open('sjp_temp_scrapper.tmp', 'w+', encoding='UTF-8') as sjp:
                sjp.write(htmlSTR_sjp)
            break
        except:
            print('Ponowna próba nawiązania połączenia internetowego!')
    with open('sjp_temp_scrapper.tmp', 'r', encoding='UTF-8') as sjp:
        htmlSTR_sjp_list = sjp.readlines()
    word_true = word
    for line in htmlSTR_sjp_list:
        line_split = line.split('>')
        for li in line_split:
            if str(li).startswith("stopień"):
                try: 
                    lin = li.split('<')[0].split(': ')[1]
                    word_true = lin
                    break
                except IndexError:
                    word_true = word
                    break

    if word != word_true:
        word = word_true
    url_wiki = f'https://pl.wiktionary.org/wiki/{word}'
    while True:
        try:
            r = requests.get(url_wiki)
            htmlSTR_wiki = r.text
            with open('wiki_temp_scrapper.tmp', 'w+', encoding='UTF-8') as wiki:
                wiki.write(htmlSTR_wiki)
            break
        except:
            print('Ponowna próba nawiązania połączenia internetowego!')
    with open('wiki_temp_scrapper.tmp', 'r', encoding='UTF-8') as wiki:
        htmlSTR_wiki_list = wiki.read()
    scrp_parts = htmlSTR_wiki_list.split('title="przypadek">')[1:4]
    gr_dict_inside = {}
    grads_adj_count = 1
    for part in scrp_parts:
        part_split = part.split('<a href="/wiki/')
        gr_dict_convert = {
            'mianownik' : 'MIA', 'dopełniacz' : 'DOP', 'celownik' : 'CEL',
            'biernik' : 'BIE', 'narzędnik' : 'NAR', 'miejscownik' : 'MIE', 
            'wołacz' : 'WOL'
            }
        gr_list_name = [mont for mont in gr_dict_convert.keys()]
        gr_dict_inside[grads_adj_count] = {}
        for p_split in part_split:
            p_spi = p_split.split('</td>')
            count_gr = 0
            gr_list_kind = ['CASE', 'LP-MOSZW-POZ', 'LP-MRZ-POZ', 'LP-Z-POZ', 'LP-N-POZ', 
                            'LM-MOS-POZ', 'LM-NMOS-POZ']
            model_construct = None
            for p_si in p_spi:
                if p_si.count('title="'):
                    label_Case = p_si.split('"')[2]
                    if label_Case in gr_list_name:
                        model_construct = f'{gr_dict_convert[label_Case]}-'
                        count_gr += 1
                if p_si.count('title="') == 0 and p_si.count('<td colspan="2">') and model_construct is not None:
                    gr_dict_inside[grads_adj_count][
                        model_construct + gr_list_kind[count_gr]
                                            ] = p_si.replace('<td colspan="2">', '')
                    gr_dict_inside[grads_adj_count][
                        model_construct + gr_list_kind[count_gr + 1]
                                            ] = p_si.replace('<td colspan="2">', '')
                    
                    gr_dict_inside[grads_adj_count][
                        model_construct + gr_list_kind[count_gr].replace('POZ', 'NEG')
                                            ] = 'nie' + p_si.replace('<td colspan="2">', '')
                    gr_dict_inside[grads_adj_count][
                        model_construct + gr_list_kind[count_gr + 1].replace('POZ', 'NEG')
                                            ] = 'nie' + p_si.replace('<td colspan="2">', '')
                    count_gr += 2
                elif p_si.count('title="') == 0 and p_si.count('<td>')and model_construct is not None:
                    gr_dict_inside[grads_adj_count][
                        model_construct + gr_list_kind[count_gr]
                                            ] = p_si.replace('<td>', '')
                    gr_dict_inside[grads_adj_count][
                        model_construct + gr_list_kind[count_gr].replace('POZ', 'NEG')] = 'nie' + p_si.replace('<td>', '')
                    count_gr += 1
                if count_gr >= 6:
                    model_construct = None

        if grads_adj_count == 3:
            break
        grads_adj_count += 1
    
    final_dict_exp = {}
    for x_key in range(1, 4):
        try:
            gr_dict_inside[x_key]['MIA-LP-MOSZW-POZ']
        except KeyError:
            continue

        final_dict_exp[gr_dict_inside[x_key]['MIA-LP-MOSZW-POZ']] = gr_dict_inside[x_key]
    
    return final_dict_exp

def case_adj_dict_generator_spacy_erroring(word_adj, nlp):
    target = takeTarget.take_target(word_adj, 'przymiotnik')
    if target == ['a', 'b']:
        return False
    # print(target)

    final_dict = {}
    for word in target:
        doc = nlp(word)
        token = doc[0]
        if not word.startswith('nie'):
            
            # Gender=Neut, Fem, Masc
            # Number=Sing, Plur
            # Animacy=Hum, Inan
            
            split_data = str(token.morph).split('|')
            if 'Case=Nom' in split_data:
                if 'Number=Plur' in split_data:
                    final_dict['MIA-LM-X'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['MIA-LP-N'] = token.text
                        final_dict['WOL-LP-N'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['MIA-LP-Z'] = token.text
                        final_dict['WOL-LP-Z'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['MIA-LP-M'] = token.text
                        final_dict['WOL-LP-M'] = token.text
                    
            # print('DOP')
            if 'Case=Gen' in split_data:
                if 'Number=Plur' in split_data:
                    final_dict['DOP-LM-X'] = token.text
                    final_dict['BIE-LM-X'] = token.text
                    final_dict['MIE-LM-X'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['DOP-LP-N'] = token.text
                        final_dict['DOP-LP-M'] = token.text
                        final_dict['BIE-LP-M'] = token.text
                        final_dict['BIE-LP-N'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['DOP-LP-Z'] = token.text
                        final_dict['CEL-LP-Z'] = token.text
                        final_dict['BIE-LP-Z'] = token.text
                        final_dict['MIE-LP-Z'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['DOP-LP-M'] = token.text
            # Dat, Acc, Ins, Loc, Voc
            # print('CEL')
            if 'Case=Dat' in split_data:
                if 'Number=Plur' in split_data:
                    final_dict['CEL-LM-X'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['CEL-LP-N'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['CEL-LP-Z'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['CEL-LP-M'] = token.text
                        final_dict['CEL-LP-N'] = token.text
            # print('BIE')
            if 'Case=Acc' in split_data:
                if 'Number=Plur' in split_data:
                    final_dict['BIE-LM-X'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['BIE-LP-N'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['BIE-LP-Z'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['BIE-LP-M'] = token.text
            # print('NAR')
            if 'Case=Ins' in split_data:
                if 'Number=Plur' in split_data:
                    final_dict['NAR-LM-X'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['NAR-LP-N'] = token.text
                        final_dict['CEL-LM-X'] = token.text
                        final_dict['NAR-LP-M'] = token.text
                        final_dict['MIE-LP-M'] = token.text
                        final_dict['MIE-LP-N'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['NAR-LP-Z'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['NAR-LP-M'] = token.text
            # print('MIE')
            if 'Case=Loc' in split_data:
                if 'Number=Plur' in split_data:
                    final_dict['MIE-LM-X'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['MIE-LP-N'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['MIE-LP-Z'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['MIE-LP-M'] = token.text
            # print('WOL')
            if 'Case=Nom' in split_data:
                if 'Animacy=Hum' in split_data and str(token.tag_) == 'SUBST':
                    final_dict['WOL-LM-X'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['WOL-LP-N'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['WOL-LP-Z'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['WOL-LP-M'] = token.text
        else:
            split_data = str(token.morph).split('|')
            if 'Case=Nom' in split_data:
                if 'Number=Plur' in split_data:
                    final_dict['MIA-LM-X-NEG'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['MIA-LP-N-NEG'] = token.text
                        final_dict['WOL-LP-N-NEG'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['MIA-LP-Z-NEG'] = token.text
                        final_dict['WOL-LP-Z-NEG'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['MIA-LP-M-NEG'] = token.text
                        final_dict['WOL-LP-M-NEG'] = token.text
                    
            # print('DOP')
            if 'Case=Gen' in split_data:
                if 'Number=Plur' in split_data:
                    final_dict['DOP-LM-X-NEG'] = token.text
                    final_dict['BIE-LM-X-NEG'] = token.text
                    final_dict['MIE-LM-X-NEG'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['DOP-LP-N-NEG'] = token.text
                        final_dict['DOP-LP-M-NEG'] = token.text
                        final_dict['BIE-LP-M-NEG'] = token.text
                        final_dict['BIE-LP-N-NEG'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['DOP-LP-Z-NEG'] = token.text
                        final_dict['CEL-LP-Z-NEG'] = token.text
                        final_dict['BIE-LP-Z-NEG'] = token.text
                        final_dict['MIE-LP-Z-NEG'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['DOP-LP-M-NEG'] = token.text
            # Dat, Acc, Ins, Loc, Voc
            # print('CEL')
            if 'Case=Dat' in split_data:
                if 'Number=Plur' in split_data:
                    final_dict['CEL-LM-X-NEG'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['CEL-LP-N-NEG'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['CEL-LP-Z-NEG'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['CEL-LP-M-NEG'] = token.text
                        final_dict['CEL-LP-N-NEG'] = token.text
            # print('BIE')
            if 'Case=Acc' in split_data:
                if 'Number=Plur' in split_data:
                    final_dict['BIE-LM-X-NEG'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['BIE-LP-N-NEG'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['BIE-LP-Z-NEG'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['BIE-LP-M-NEG'] = token.text
            # print('NAR')
            if 'Case=Ins' in split_data:
                if 'Number=Plur' in split_data:
                    final_dict['NAR-LM-X-NEG'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['NAR-LP-N-NEG'] = token.text
                        final_dict['CEL-LM-X-NEG'] = token.text
                        final_dict['NAR-LP-M-NEG'] = token.text
                        final_dict['MIE-LP-M-NEG'] = token.text
                        final_dict['MIE-LP-N-NEG'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['NAR-LP-Z-NEG'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['NAR-LP-M-NEG'] = token.text
            # print('MIE')
            if 'Case=Loc' in split_data:
                if 'Number=Plur' in split_data:
                    final_dict['MIE-LM-X-NEG'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['MIE-LP-N-NEG'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['MIE-LP-Z-NEG'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['MIE-LP-M-NEG'] = token.text
            # print('WOL')
            if 'Case=Nom' in split_data:
                if 'Animacy=Hum' in split_data and str(token.tag_) == 'SUBST':
                    final_dict['WOL-LM-X-NEG'] = token.text
                else:
                    if 'Gender=Neut' in split_data:
                        final_dict['WOL-LP-N-NEG'] = token.text
                    if 'Gender=Fem' in split_data:
                        final_dict['WOL-LP-Z-NEG'] = token.text
                    if 'Gender=Masc' in split_data:
                        final_dict['WOL-LP-M-NEG'] = token.text
    return final_dict

def part_Speech_4(word):
    # print(word)
    with open('cases_words_adjective.neural', 'r', encoding='utf-8') as f:
        f_list = f.readlines()
    read_dict = {}
    for f in f_list:
        f_k = f.split('@KEY!')
        read_dict[f_k[0]] = f_k[1]
    try:
        read_dict[word]
        return True
    except KeyError:
        dict_exp = case_adj_dict_generator(word, nlp)
        if not dict_exp: dict_exp = {}
        try:
            dict_exp['WOL-LP-M']
            dict_exp["MIA-LP-M"]
            good = True
        except KeyError:
            good = False

        if good:
            answer = f'{dict_exp["MIA-LP-M"]}@KEY!RODZ:N!CECH:notLIVE!'
            for s, x in dict_exp.items():
                answer += f'{s}:{x}!'
            answer = answer[:len(answer) - 1] + '\n'
            a_k = answer.split('@KEY!')
            read_dict[a_k[0]] = a_k[1]

            save_f = ''
            for k, v in read_dict.items():
                save_f += f'{k}@KEY!{v}'

            with open('cases_words_adjective.neural', 'w+', encoding='utf-8') as f:
                f.write(save_f)

            return good
        else:
            return good

def change_cases_SP_adjective_old_spacy_error(word, truck='BACK', opt='MIA', numb='LM', rodz = 'M', target='przymiotnik', update='YES'):
    if not if_case(word):
        return 'Nieodmienialny'
    
    target_n = takeTarget.take_target(word, target)
    word_0 = target_n[0]
    with open('cases_words_adjective.neural', 'r', encoding='utf-8') as f:
        f_list = f.readlines()
    

    read_dict = {}
    for f in f_list:
        f_k = f.split('@KEY!')
        read_dict[f_k[0]] = f_k[1]

    word_dict = {}
    if word_0 in [k for k in read_dict.keys()]:
        works_c = read_dict[word_0].strip().split('!')
        for wc in works_c:
            c = wc.split(':')
            word_dict[c[0]] = c[1].strip()
    else:
        automatic_casses = part_Speech_4(word_0)
        if not automatic_casses:
            if update == 'YES':
                return change_cases_SP_adjective(word, truck, opt, numb, rodz, target, update)
            else:
                return 'MAKE-UPDATE'
        else:
            return change_cases_SP_adjective(word, truck, opt, numb, rodz, target, update)
    # print(word_dict)
    if truck == 'BACK':
        for k in word_dict.keys():
            if k.count(opt) == 1 and k.count(numb) == 1 and k.count(rodz) == 1:
                # print(word_dict)
                return word_dict[k]
    
    exp_dict = {'CASE' : []}
    if truck == 'INFO':
        for wik, wiv in word_dict.items():
            if wiv == word:
                exp_dict['CASE'].append(wik)
        return exp_dict
    
    if truck == 'ALL':
        return word_dict

def change_cases_SP(base, word, truck='BACK', opt='MIA', numb='LP', target='rzeczownik', update='YES'):
    # if not if_case(word):
    #     if truck == 'ALL':
    #         return {}
    #     else:
    #         return 'Nieodmienialny'
    
    target_n = takeTarget.take_superTarget(base, word, target)
    word_0 = target_n[0]
    # print(word_0)
    if word_0 == 'a': 
        word_0 = word
        
    with open('cases_words_noun.neural', 'r', encoding='utf-8') as f:
        f_list = f.readlines()

    read_dict = {}
    for f in f_list:
        f_k = f.split('@KEY!')
        read_dict[f_k[0]] = f_k[1]

    word_dict = {}
    if word_0 in [k for k in read_dict.keys()]:
        
        works_c = read_dict[word_0].strip().split('!')
        for wc in works_c:
            c = wc.split(':')
            word_dict[c[0]] = c[1].strip()
    else:
        automatic_casses = part_Speech_2(word_0)
        
        if not automatic_casses:
            if update == 'YES':
                change_case_SP(base, word_0)
                return change_cases_SP(base, word, truck, opt, numb, target, update)
            else:
                if truck == 'ALL':
                    return {}
                else:
                    return 'MAKE-UPDATE'
        else:
            return change_cases_SP(base, word, truck, opt, numb, target, update)
        
    if truck == 'BACK':
        for k in word_dict.keys():
            if k.count(opt) == 1 and k.count(numb) == 1:
                # print(word_dict)
                return word_dict[k]
    
    exp_dict = {'CASE' : [], 'RODZ' : word_dict['RODZ'], 'CECH' : word_dict['CECH'] }
    if truck == 'INFO':
        for wik, wiv in word_dict.items():
            if wiv == word:
                exp_dict['CASE'].append(wik)
        return exp_dict
    
    if truck == 'ALL':
        return word_dict
 
def what_prefix_target(word):
    if len(word) <= 2:
        return word[0]
    if len(word) == 3:
        return word[:2]
    if len(word) == 4 or len(word) == 5:
        return word[:3]
    if len(word) > 5:
        return word[:4]

if __name__ == '__main__':
    import awareness
    print(part_Speech_2('rower'))

    # base = awareness.take_base('memory_CLO_v2010')
    
