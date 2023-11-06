import clearLists
import verbFlex
import chanerCases
import checkerBaseOperators

def add_word(base, cat, word):
    last_ID =  base['LID']
    if cat == 'PO' or cat == 'OR' or cat == 'PR' or cat == 'OK' or cat == 'DO'\
         or cat == 'ZA' or cat == 'VO' or cat == 'OZ' or cat == 'HW':
        
        # print(type(last_ID))
        try:
            base[cat][word]
            word_exist = True
        except KeyError:
            word_exist = False
        if word_exist:
            print(f'Słowo {word} istnieje w bazie')
        else:
            idw = len(base[cat])
            base[cat][word] = {'ID' : idw, 'LINKS' : [], 'SENTENS' : [], 'LID' : last_ID}
            # print(base['LID'])
            base['LID'] = int(base['LID']) + 1
            print(f'Słowo {word} zostało dodane')
    elif cat == 'LB':
        try:
            base[cat][word]
            lb_exist = True
        except KeyError:
            lb_exist = False
        if lb_exist:
            print(f'Słowo {word} istnieje w bazie')
        else:
            idw = len(base[cat])
            base[cat][word] = {
                'ID' : idw, 
                'LINKS' : [], 
                'LID' : last_ID
                }
            print(f'Słowo {word} zostało dodane')
            # print(base['LID'])
            base['LID'] = int(base['LID']) + 1
    else:
        print(f'Kategoria {cat} nie jest obsługiwana')
    return base

def add_link(base, cat_id, link_id):
    cat, idw = cat_id.split('_')
    link, idl = link_id.split('_')
    operation = False
    link_id_exist = False
    try:
        base[cat]
        cat_exit = True
    except KeyError:
        cat_exit = False
        print(f'Kategoria {cat} nie istnieje')
    try:
        base[link]
        link_exit = True
    except KeyError:
        link_exit = False
        print(f'Kategoria linku {link} nie istnieje')
    if link_exit:
        for y in base[link].values():
            if y['ID'] == int(idl):
                link_id_exist = True
    if cat_exit and link_id_exist and cat != 'SE' and link != 'SE' and cat != 'SA' and link != 'SA' \
        and link != 'LID' and link != 'BASE':
        for k, v in base[cat].items():
            if v['ID'] == int(idw):
                base[cat][k]['LINKS'].append(link_id)
                base[cat][k]['LINKS'] = clearLists.clear_lists(base[cat][k]['LINKS'])
                operation = True
    else:
        print('Wystapił błąd')
    if operation:
        print(f'Dodano link {link_id} do słowa {cat_id}')
    else:
        print(f'Brak ID dla kategorii {cat}')
    return base

def add_sa(base, cat_id, sa_id):
    cat, idw = cat_id.split('_')
    sa, ids = sa_id.split('_')
    opr = False
    se_id_exist = False
    try:
        base[cat]
        cat_exit = True
    except KeyError:
        cat_exit = False
        print(f'Kategoria {cat} nie istnieje')
    if sa == 'SA':
        try:
            base[sa][int(ids)]
            sa_id_exit = True
        except KeyError:
            sa_id_exit = False
            print(f'Zdanie o ID {sa_id} nie istnieje')
    else:
        print(f'Błędny parametr {sa_id} dla zdania')

    if cat_exit and sa_id_exit and cat != 'SE' and cat != 'LB' and cat != 'LID'\
        and cat != 'BASE' and cat != 'SA':
        for k,v in base[cat].items():
            if v['ID'] == int(idw):
                base[cat][k]['SENTENS'].append(sa_id)
                base[cat][k]['SENTENS']= clearLists.clear_lists(base[cat][k]['SENTENS'])
                opr = True
    else:
        print('Wystąpił błąd')
    if opr:
        print(f'Dodano słowo {cat_id} do zdania {sa_id}')
    else:
        print(f'Brak id {idw} dla kategorii {cat}')
    return base

def add_se(base, cat_id, se_id):
    cat, idw = cat_id.split('_')
    se, ids = se_id.split('_')
    opr = False
    se_id_exist = False
    try:
        base[cat]
        cat_exit = True
    except KeyError:
        cat_exit = False
        print(f'Kategoria {cat} nie istnieje')
    if se == 'SE':
        try:
            base[se][int(ids)]
            se_id_exit = True
        except KeyError:
            se_id_exit = False
            print(f'Zdanie o ID {se_id} nie istnieje')
    else:
        print(f'Błędny parametr {se_id} dla zdania')

    if cat_exit and se_id_exit and cat != 'SE' and cat != 'LB' and cat != 'LID'\
        and cat != 'BASE' and cat != 'SA':
        for k,v in base[cat].items():
            if v['ID'] == int(idw):
                base[cat][k]['SENTENS'].append(se_id)
                base[cat][k]['SENTENS']= clearLists.clear_lists(base[cat][k]['SENTENS'])
                opr = True
    else:
        print('Wystąpił błąd')
    if opr:
        print(f'Dodano słowo {cat_id} do zdania {se_id}')
    else:
        print(f'Brak id {idw} dla kategorii {cat}')
    return base

def take_word(base, cat_id):
    cat, idw = cat_id.split('_')
    word = None
    if cat == 'PO' or cat == 'OR' or cat == 'PR' or cat == 'OK' \
         or cat == 'DO' or cat == 'ZA' or cat == 'VO' or cat == 'OZ' \
            or cat == 'HW' or cat == 'LB':
        for k,v in base[cat].items():
            if v['ID'] == int(idw):
                word = k
    else:
        print(f'Kategoria {cat} nie istnieje')
    if word == None:
        print(f'Słowo pod ID {cat_id} nie istnieje')
    return word

def take_LID(base, cat_id):
    cat, idw = cat_id.split('_')
    LID = None
    if cat == 'PO' or cat == 'OR' or cat == 'PR' or cat == 'OK' \
         or cat == 'DO' or cat == 'ZA' or cat == 'VO' or cat == 'OZ' \
            or cat == 'HW' or cat == 'LB':
        for k,v in base[cat].items():
            if v['ID'] == int(idw):
                LID = base[cat][k]['LID']
    else:
        print(f'Kategoria {cat} nie istnieje')
    if LID == None:
        print(f'Słowo pod ID {cat_id} nie istnieje')
    return LID

def join_ids(base, cat_id, join_id):
    cat = cat_id.split('_')[0]
    join = cat_id.split('_')[0]
    try:
        base[cat]
        cat_exist = True
    except KeyError:
        cat_exist = False
        print(f'Błędny parametr {cat}')
    try:
        base[join]
        join_exist = True
    except KeyError:
        join_exist = False
        print(f'Błędny parametr {join}')
    if cat_exist and join_exist and cat != 'SE' and cat != 'LID' and cat != 'BASE'\
            and cat != 'SA' and join != 'SE' and join != 'LID'and join != 'BASE' \
                and join != 'SA':
        base = add_link(base, cat_id, join_id)
        base = add_link(base, join_id, cat_id)
        print(f'Słowa {take_word(base, cat_id)} i {take_word(base, join_id)} zostały połączone.')
    return base

def take_se_words(base, se_id, option = 'LIST'):
    se, ids = se_id.split('_')
    if se == 'SE':
        try:
            base[se][int(ids)]
            se_exist = True
        except KeyError:
            se_exist = False
        if se_exist:
            words = []
            words_string = ''
            se_len = len(base[se][int(ids)])
            co = 0
            for w in base[se][int(ids)]:
                word = take_word(base, w)
                words.append(word)
                words_string += word
                co += 1
                if co != se_len:
                    words_string += ' '
            if option == 'LIST':
                return words
            elif option == 'STR':
                return words_string.replace(' , ', ', ')
            else:
                print(f'Parametr opcji {option} jest niewłaściwy. Użyj LIST lub STR')
        else:
            print(f'Parametr {se_id} jest błędny')

def take_sa(base, sa_id):
    se, ids = sa_id.split('_')
    if se == 'SA':
        try:
            se_exp = base[se][int(ids)]
            return se_exp
        except KeyError:
            print(f'Błędny parametr {sa_id}')
    else:
        print(f'Parametr {se} nie jest obsługiwany')

def take_se(base, se_id):
    se, ids = se_id.split('_')
    if se == 'SE':
        try:
            se_exp = base[se][int(ids)]
            return se_exp
        except KeyError:
            print(f'Błędny parametr {se_id}')
    else:
        print(f'Parametr {se} nie jest obsługiwany')

def take_re(base, re_id):
    re, ids = re_id.split('_')
    if re == 'RE':
        try:
            se_exp = base[re][int(ids)]
            return se_exp
        except KeyError:
            print(f'Błędny parametr {re_id}')
    else:
        print(f'Parametr {re} nie jest obsługiwany')


def take_links(base, cat_id):
    # print('Tutaj', cat_id)
    if cat_id is not None:
        cat, idc = cat_id.split('_')
        if cat != 'SE' and cat != 'SA' and cat != 'LID' and cat != 'BASE':
            try:
                base[cat]
                cat_exist = True
            except KeyError:
                cat_exist = False
            if cat_exist:
                idc_exist = False
                l_exp = []
                for k,v in base[cat].items():
                    if v['ID'] == int(idc):
                        l_exp = base[cat][k]['LINKS']
                        idc_exist = True
                if idc_exist:
                    return l_exp
                else:
                    print(f'Brak ID {idc} dla kategorii {cat}')
                    return []
            else:
                print(f'Katagoria {cat} nie istnieje')
                return []
        else:
            print(f'kategoria {cat} nie jest obsługiwana')
            return []
    else:
        return []

def take_sentens(base, cat_id):
    cat, idc = cat_id.split('_')
    if cat != 'SE' and cat != 'LID' and cat != 'BASE' and cat != 'SA':
        try:
            base[cat]
            cat_exist = True
        except KeyError:
            cat_exist = False
        if cat_exist:
            idc_exist = False
            l_exp = []
            for k,v in base[cat].items():
                if v['ID'] == int(idc):
                    l_exp = base[cat][k]['SENTENS']
                    idc_exist = True
            if idc_exist:
                return l_exp
            else:
                print(f'Brak ID {idc} dla kategorii {cat}')
        else:
            print(f'Katagoria {cat} nie istnieje')
    else:
        print(f'kategoria {cat} nie jest obsługiwana')

def take_id(base, cat, word):
    if cat == 'PO' or cat == 'OR' or cat == 'PR' or cat == 'OK' \
         or cat == 'DO' or cat == 'ZA' or cat == 'VO' or cat == 'OZ' \
            or cat == 'HW' or cat == 'LB':
        try:
            id_wd = base[cat][word]['ID']
            return f'{cat}_{id_wd}'
        except KeyError:
            print(f'Słowo {word} nie istnieje w kategorii {cat}')
    else:
        print(f'kategoria {cat} jest błędna')

def update_sa(base, sa_id, sa_new_list):
    sa, ids = sa_id.split('_')
    if sa == 'SA':
        try:
            base[sa][int(ids)] = sa_new_list
            return base
        except KeyError:
            print(f'Podane ID {ids} nie istnieje')
            return base
    else:
        print(f'Parametr {sa} nie istnieje')
        return base

def update_se(base, se_id, se_new_list):
    se, ids = se_id.split('_')
    if se == 'SE':
        try:
            base[se][int(ids)] = se_new_list
            return base
        except KeyError:
            print(f'Podane ID {ids} nie istnieje')
            return base
    else:
        print(f'Parametr {se} nie istnieje')
        return base

def remove_sentens(base, cat_id, se_id):
    cat = cat_id.split('_')[0]
    ids = se_id.split('_')[1]
    cat_word = take_word(base, cat_id)
    cur_sentens = take_sentens(base, cat_id)
    cus_se = take_se(base, se_id)
    try:
        base[cat][cat_word]
        base['SE'][int(ids)]
        opt = True
    except KeyError:
        opt = False
    if opt:
        new_sentens = []
        new_se = []
        for s in cur_sentens:
            if s != se_id:
                new_sentens.append(s)
        for c in cus_se:
            if c != cat_id:
                new_se.append(c)
        base[cat][cat_word]['SENTENS'] = new_sentens
        base['SE'][int(ids)] = new_se
    else:
        print('Wystąpił błąd')
    return base

def remove_link(base, cat_id, link_id):
    cat = cat_id.split('_')[0]
    link = link_id.split('_')[0]
    link_cat_exist = False
    cat_link_exist = False
    cat_word = take_word(base, cat_id)
    link_word = take_word(base, link_id)
    try:
        base[cat][cat_word]
        cat_exist = True
        base[link][link_word]
        link_exist = True
    except KeyError:
        cat_exist = False
        link_exist = False
        print(f'Jeden z parametrów ({cat} / {link}) albo słowo ({cat_word} / {link_word}) są błędny')
    if link_exist and cat_exist and cat != 'SE' and link != 'SE' and cat != 'LID' and link != 'LID'\
            and cat != 'BASE' and link != 'BASE' and cat != 'SA' and link != 'SA':
        for l in base[link][link_word]['LINKS']:
            if l == cat_id:
                link_cat_exist = True
        for c in base[cat][cat_word]['LINKS']:
            if c == link_id:
                cat_link_exist = True
    else:
        print(f'Wystąpił błąd parametru {cat_id} lub {link_id}')
    if link_cat_exist and cat_link_exist:
        old_links = take_links(base, link_id)
        old_cats = take_links(base, cat_id)
        new_links = []
        new_cats = []
        for ol in old_links:
            if ol == cat_id:
                print(f'Słowo o ID {cat_id} zostało usunięte z {link_id}')
            else:
                new_links.append(ol)
        for oc in old_cats:
            if oc == link_id:
                print(f'Słowo o ID {link_id} zostało usunięte z {cat_id}')
            else:
                new_links.append(oc)
        base[cat][cat_word]['LINKS'] = new_cats
        base[link][link_word]['LINKS'] = new_links
    return base

def join_ids_list(base, ids_list):
    llids = len(ids_list)
    counter = 0
    if llids > 1:
        for i in ids_list:
            # print(counter, llids - 1)
            if counter != llids -1:
                base = join_ids(base, i, ids_list[counter +1])
                print(f'Połączono {i} z {ids_list[counter +1]}!')
            counter += 1
    else:
        print(f'Lista musi zawirać przynajmniej dwa paramatry. Podana lista zawiera {llids} parametr/ów.')
    return base

def remove_word_from_se(base, word, se_id):
    ts = take_se(base, se_id)
    word_id = None
    for t in ts:
        word_check = take_word(base, t)
        if word_check == word:
            word_id = t
            break
    if word_id != None:
        base = remove_sentens(base, word_id, se_id)
        print(f'Słowo {word} zostało usuniete ze zdania {se_id}')
    else:
        print(f'Słowo {word} nie znajduje się w zdaniu {se_id}')
    return base

def take_lb(base, cat_id, take = 'ID'):
    for l in take_links(base, cat_id):
        if l.startswith('LB'):
            if take == 'ID':
                return l
            if take == 'WORD':
                return take_word(base, l)

def complete_LB(base, word_LB, kind):
    try:
        base['LB'][word_LB]['KIND']
        print(f'Baza była już uzupełniana o odmiany dla słowa: {word_LB}.')
        return base
    except KeyError:
        def build_dict_KVVK(dict_in):
            # print(dict_in)
            exp_dict ={}
            try:
                for k, v in dict_in.items():
                    exp_dict[k] = v
                for k, v in dict_in.items():
                    exp_dict[v] = k
            except:
                print(dict_in)
                print(f'[BŁĄD przetwarzania słownika!] - Baza NIE zosła uzupełniona.')
            return exp_dict
            
        try:
            if kind == 'czasownik' or kind == 'imiesłów_bierny' or kind == 'imiesłów_przysłówkowy'\
                or kind == 'imiesłów_przymiotnikowy':
                word_cases_dict = build_dict_KVVK(
                    verbFlex.verb_flex(base, word_LB, 'ALL')
                    )
                word_cases_dict['PART'] = kind
                print(f'Baza zosła uzupełniona o odmiany dla słowa: {word_LB}.')
            elif  kind == 'rzeczownik':
                
                word_cases_dict = build_dict_KVVK(
                    chanerCases.change_cases_SP(base, word_LB, 'ALL', None, None, kind, 'NO')
                    )
                word_cases_dict['PART'] = kind
            elif  kind == 'przymiotnik':
                word_cases_dict = build_dict_KVVK(
                    chanerCases.change_cases_SP_adjective(base, word_LB, 'ALL', None, None, None ,None, kind, 'NO')
                    )
                word_cases_dict['PART'] = kind
            else:
                word_cases_dict = {}
                word_cases_dict['PART'] = kind
            base['LB'][word_LB]['KIND'] = word_cases_dict
        except KeyError:
            print(f'Podana etykietka LB: {word_LB} nie isnieje.')
    return base

def questions_mark(base, moder = 'zaimki_pytajace'):
    if moder == 'zaimki_pytajace':
        modern_list = [
            "kto", "co", "jaki", "jaka", "jakie", "którego", 
            "której", "którzy", "które", "czego", "komu", 
            "kim", "czym", "czy", "czyż", "czyli", "albo", "ani",
            "aż", "czyj", "czyja", "czyje", "kiedy", "gdzie", "ile",
            "kimże", "któż", "który", "któryż", "niech", "nim"
            ]
    elif  moder == 'operatory_modalne':
        modern_list = ['jest', 'są', 'być', 'jestem', 'jesteś',
                       'może', 'mogą', 'można', 'mogę', 'możesz', 'możliwe',
                       'znaczy', 'znaczą', 'znaczyć', 'znaczę', 'znaczysz',
                       'nazywa', 'nazywają', 'nazywać', 'nazywam', 'nazywamy',
                       'oznacza', 'oznaczają', 'oznaczać', 'oznaczam', 'oznaczasz',
                       'da', 'dają', 'daje', 'dać', 'dam', 'dasz', 'dadzą',
                       'robi', 'robią', 'robić', 'robisz', 'robię', 
                       'się', 'to', 'ten', 'taki', 'celu', 'radę', 'ta', 'to', 'ci', 'te']
    elif moder == 'zaimki_wskazujacy':
        modern_list = ['o', 'w', 'u', 'z', 'na', 'za', 'po', 
                         'od', 'do', 'nad', 'pod', 'przed', 
                         'przez', 'przy', 'obok', '']
    
    elif moder == 'zaimki_rodzaju':
        modern_list = [
                        'kogoś', 'coś', 'czegoś', 'czyjeś', 'siebie', 'swoje', 'swojej', 'swojego',
                        'komuś', 'gdzieś', 'kimś', 'czemuś', 'ilość', 'ileś',
                        'jakiś', 'jakiegoś', 'jakąś', 'jakieś', 'dokądś',
                        'czymś', 'ktoś', 'mający', 'mająca', 'mające', ]

    cat_questioner_list = set()
    for za_p in modern_list:
        za_cat_id_list = checkerBaseOperators.find_pharse_in_part(base, za_p)
        if len(za_cat_id_list) > 0:
            for zci in za_cat_id_list:
                cat_questioner_list.add(zci)
        Za_p = za_p.capitalize()
        za_cat_id_list = checkerBaseOperators.find_pharse_in_part(base, Za_p)
        if len(za_cat_id_list) > 0:
            for zci in za_cat_id_list:
                cat_questioner_list.add(zci)
    return [x for x in cat_questioner_list]

if __name__ == '__main__':
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    add_se(base, 'PO_0', 'SE_0')
