import automaticTitleSA
import partSentens
import baseTools
import takeTarget
import clearLists

def action(base, sentens, se_id = None, option = 'all'):
    if se_id == None: se_id = f"SE_{len(base['SE'])}"
    se_no_id = int(se_id.split('_')[1])

    s_lista = sentens.strip().split(' ')

    old_base = base
    cur_s = partSentens.part_sentens(base, s_lista)
    # print(cur_s)
    k_cur_s = []
    for k,v in cur_s.items():
        if k != 'CZ':
            for n,s in v.items():
                # print(s)
                try:
                    base[k][s[0]]
                    k_cur_s.append([n, k, True, s[0], s[1], s[2]])
                except KeyError:
                    k_cur_s.append([n, k, False, s[0], s[1], s[2]])
    se_temp = []
    count_k = len(k_cur_s)
    # print(k_cur_s)
    counter = 0
    while (counter != count_k  +1):
        # print(counter, count_k)
        for x in k_cur_s:
            if x[0] == counter:
                if not x[2]:
                    if x[1] == 'OR':
                        if x[3].startswith('nie ') or x[3].startswith('Nie '):
                            negative = x[3].replace('nie ', '').replace('Nie ', '')
                            base = baseTools.add_word(base, x[1] ,negative)
                            base = baseTools.add_word(base, x[1], x[3])
                            base = baseTools.join_ids(base, baseTools.take_id(base, x[1], x[3]), baseTools.take_id(base, x[1], negative))
                            v_lb = takeTarget.take_superTarget(base, negative)[0]
                            base = baseTools.add_word(base, 'LB', v_lb)
                            base = baseTools.complete_LB(base, v_lb, x[5])
                            base = baseTools.join_ids(base, baseTools.take_id(base, 'LB', v_lb), baseTools.take_id(base, x[1], negative))
                            base = baseTools.join_ids(base, baseTools.take_id(base, 'LB', v_lb), baseTools.take_id(base, x[1], x[3]))

                        # elif x[3].startswith('nie') and x[3].count(' ') == 0:
                        #     #należy zaktualizować dla czasowników z pisanym łącznie nie np. niebyć, nienawidzić itp.
                        #     pass
                        else:
                            negative = x[3].replace(x[3], f'nie {x[3].lower()}')
                            base = baseTools.add_word(base, x[1], negative)
                            base = baseTools.add_word(base, x[1], x[3])
                            base = baseTools.join_ids(base, baseTools.take_id(base, x[1], x[3]), baseTools.take_id(base, x[1], negative))
                            # print(x)
                            v_lb = takeTarget.take_superTarget(base, x[3])[0]
                            base = baseTools.add_word(base, 'LB', v_lb)
                            base = baseTools.complete_LB(base, v_lb, x[5])
                            base = baseTools.join_ids(base, baseTools.take_id(base, 'LB', v_lb), baseTools.take_id(base, x[1], negative))
                            base = baseTools.join_ids(base, baseTools.take_id(base, 'LB', v_lb), baseTools.take_id(base, x[1], x[3]))
                    else:
                        # print(x)
                        base = baseTools.add_word(base, x[1], x[3])
                        base = baseTools.add_word(base, 'LB', x[4])
                        base = baseTools.complete_LB(base, x[4], x[5])
                        base = baseTools.join_ids(base, baseTools.take_id(base, 'LB', x[4]), baseTools.take_id(base, x[1], x[3]))
                se_temp.append(x + [baseTools.take_id(base, x[1], x[3])])
        
        counter += 1
    se_done = []
    # print(se_temp)
    for s in se_temp:
        se_done.append(s[6])
        # print(s[5], s[6])
    if option == 'all':
        if len(base['SE']) == se_no_id:
            base['SE'][se_no_id] = se_done
            se_ok = True
        elif len(base['SE']) > se_no_id:
            old_se = baseTools.take_se(base, se_id)
            co = 0
            co_l = len(old_se) - 2
            for o in old_se:
                if co != co_l:
                    base = baseTools.remove_link(base, o, old_se[co + 1])
                co += 1
            se_ok = True
            base = baseTools.update_se(base, se_id, se_done)
        else:
            print(f'SE_{se_no_id} nie istnieje')
            se_ok = False
        if se_ok:
            for x in se_done:
                base = baseTools.add_se(base, x, se_id)
            return base
        else:
            return old_base
    if option == 'only_se_done':
        return {'SE_DONE' : se_done, 'BASE' : base}


def whatSentention(sentention):
    sentention = str(sentention)
    # print(sentention)
    '''
    polskim wyróżnia się:
    spójniki współrzędne (parataktyczne):
    łączne, np. a, i, oraz, tudzież
    rozłączne, np. albo, bądź, czy, lub
    wykluczające, np. ani, ni
    przeciwstawne, np. a, aczkolwiek, ale, jednak, lecz, natomiast, zaś
    wyjaśniające, np. czyli, mianowicie, ponieważ, to jest
    wynikowe, np. dlatego, i, przeto, tedy, więc, zatem, toteż
    spójniki podrzędne (hipotaktyczne), np. aby, bowiem, choć, czy, jeżeli, ponieważ, że.
    '''
    categoryS = {
        'łączne' : [],
        'rozłączne' : [],
        'wykluczające' : [],
        'przeciwstawne' : [],
        'wyjaśniające' : [],
        'wynikowe' : [],
        'hipotaktyczne' : [],

        'sentention' : sentention
             }

    a = sentention.count(' a ')
    i = sentention.count(' i ')
    oraz = sentention.count(' oraz ')
    tudziez = sentention.count(' tudzież ')
    laczne = a + i + oraz + tudziez
    if laczne > 0:
        exp = f'łączne, a({a}), i({i}), oraz({oraz}), tudzież({tudziez})'
        # print(exp)
        if a > 0: categoryS['łączne'] = categoryS['łączne'] + ['a ']
        if i > 0: categoryS['łączne'] = categoryS['łączne'] + ['i ']
        if oraz > 0: categoryS['łączne'] = categoryS['łączne'] + ['oraz ']
        if tudziez > 0: categoryS['łączne'] = categoryS['łączne'] + ['tudzież ']

    albo = sentention.count(' albo ')
    badz = sentention.count(' bądź ')
    czy = sentention.count(' czy ')
    lub = sentention.count(' lub ')
    rozlaczne = albo + badz + czy + lub
    if rozlaczne > 0:
        exp = f'rozłączne, albo({albo}), bądź({badz}), czy({czy}), lub({lub})'
        # print(exp)
        if albo > 0: categoryS['rozłączne'] = categoryS['rozłączne'] + ['albo ']
        if badz > 0: categoryS['rozłączne'] = categoryS['rozłączne'] + ['bądź ']
        if czy > 0: categoryS['rozłączne'] = categoryS['rozłączne'] + ['czy ']
        if lub > 0: categoryS['rozłączne'] = categoryS['rozłączne'] + ['lub ']

    ani = sentention.count(' ani ')
    ni = sentention.count(' ni ')
    wykluczajace = ani + ni
    if wykluczajace > 0:
        exp = f'wykluczające, ani({ani}), ni({ni})'
        # print(exp)
        if ani > 0: categoryS['wykluczające'] = categoryS['wykluczające'] + ['ani ']
        if ni > 0: categoryS['wykluczające'] = categoryS['wykluczające'] + ['ni ']

    aP = sentention.count(' a ')
    aczkolwiek = sentention.count(' aczkolwiek ')
    ale = sentention.count(' ale ')
    jednak = sentention.count(' jednak ')
    lecz = sentention.count(' lecz')
    natomiast = sentention.count(' natomiast ')
    zas = sentention.count(' zaś ')
    przeciwstawne = aP + aczkolwiek + ale + jednak + lecz + zas
    if przeciwstawne > 0:
        exp = f'przeciwstawne, np. a({aP}), aczkolwiek({aczkolwiek}), ale({ale}), jednak({jednak}), lecz({lecz}), natomiast({natomiast}), zas({zas})'
        # print(exp)
        if aP > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + ['a ']
        if aczkolwiek > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + ['aczkolwiek ']
        if ale > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + ['ale ']
        if jednak > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + ['jednak ']
        if lecz > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + ['lecz ']
        if natomiast > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + ['natomiast ']
        if zas > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + ['zaś ']

    czyli = sentention.count(' czyli ')
    mianowicie = sentention.count(' mianowicie')
    poniewaz = sentention.count(' ponieważ ')
    tojest = sentention.count(' to ')
    wyjasniajace = czyli + mianowicie + poniewaz + tojest
    if wyjasniajace > 0:
        exp = f'wyjaśniające, czyli({czyli}), mianowicie({mianowicie}), poniewaz({poniewaz}), to jest({tojest})'
        # print(exp)
        if czyli > 0: categoryS['wyjaśniające'] = categoryS['wyjaśniające'] + ['czyli ']
        if mianowicie > 0: categoryS['wyjaśniające'] = categoryS['wyjaśniające'] + ['mianowicie ']
        if poniewaz > 0: categoryS['wyjaśniające'] = categoryS['wyjaśniające'] + ['ponieważ ']
        if tojest > 0: categoryS['wyjaśniające'] = categoryS['wyjaśniające'] + ['to ']

    dlatego = sentention.count(' dlatego ')
    iW = sentention.count(' i ')
    przeto = sentention.count(' przeto ')
    tedy = sentention.count(' tedy ')
    wiec = sentention.count(' więc ')
    zatem = sentention.count(' zatem ')
    totez = sentention.count(' toteż ')
    bo = sentention.count(' bo ')
    wynikowe = dlatego + iW + przeto + tedy + wiec + zatem + totez + bo
    if wynikowe > 0:
        exp = f'wynikowe, dlatego({dlatego}), i({iW}), przeto({przeto}), tedy({tedy}) wiec({wiec}) zatem({zatem}) toteż({totez}) '
        # print(exp)
        if dlatego > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + ['dlatego ']
        if iW > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + ['i ']
        if przeto > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + ['przeto ']
        if tedy > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + ['tedy ']
        if wiec > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + ['więc ']
        if zatem > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + ['zatem ']
        if totez > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + ['toteż ']
        if bo > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + ['bo ']

    aby = sentention.count(' aby ')
    by = sentention.count(' by ')
    bowiem = sentention.count(' bowiem ')
    choc = sentention.count(' choć ')
    czyP = sentention.count(' czy ')
    jezeli = sentention.count(' jeżeli ')
    poniewaz = sentention.count(' ponieważ ')
    ze = sentention.count(' że ')
    podrzedne = aby + by + bowiem + choc + czyP + jezeli + poniewaz + ze
    if podrzedne > 0:
        exp = f'spójniki podrzędne (hipotaktyczne), np. aby({aby}), bowiem({bowiem}), choć({choc}) czy({czyP}) jeżeli({jezeli}) ponieważ({poniewaz}) że({ze}) '
        # print(exp)
        if aby > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + ['aby ']
        if by > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + ['by ']
        if bowiem > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + ['bowiem ']
        if choc > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + ['choć ']
        if jezeli > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + ['jeżeli ']
        if poniewaz > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + ['ponieważ ']
        if ze > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + ['że ']
    return categoryS


def splitSententionNum(sentention):
    sentention = str(sentention)
    exp = set()
    whatWho = whatSentention(sentention)
    for k, v in whatWho.items():
        if len(whatWho[k]) > 0 and k != 'sentention':
            for a in v:
                a = ' ' + a
                exp.add(a)
    if len(exp) > 0:
        for b in exp:
            sentention = sentention.replace(b, f'|{b}').replace(' - ', ' -|').replace(', ', ' ,|').replace(',', ' ,|').replace('||', '|').replace(' |', '|')
    else:
        sentention = sentention.replace(' - ', ' -|').replace(',', ' ,|').replace(', ', ' ,|').replace('||', '|').replace(' |', '|')
    expB = sentention.split('|')
    expA = []
    for i in expB:
        if i.startswith(' '):
            i = i[1:]
        if i.endswith(' ') or i.endswith('.') or i.endswith(':') or i.endswith(';'): # or i.endswith(',')
            i = i[:len(i) - 1]
        expA.append(i)

    return expA, exp, whatWho

def string_cleaner(text):
    allow_chracters = ['a', 'A', 'ą', 'Ą', 'b', 'B', 'c', 'C', 'ć', 'Ć', 'd', 'D', 'e', 'E',
                       'ę', 'Ę', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J',
                       'k', 'K', 'l', 'L', 'ł', 'Ł', 'm', 'M', 'n', 'N', 'ń', 'Ń',
                       'o', 'O', 'ó', 'Ó', 'p', 'P', 'r', 'R', 's', 'S', 'ś', 'Ś',
                       't', 'T', 'q', 'Q', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X',
                       'y', 'Y', 'z', 'Z', 'ź', 'Ź', 'ż', 'Ż', ' ', '.', ',', '!',
                       '?', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
                       ]
    temp_string = ''
    for t in text:
        if t in allow_chracters:
            temp_string += f'{t}'
        elif t == ')':
            temp_string += f' '
        elif t == '–':
            temp_string += f'-'
        else:
            temp_string += f' '
    temp_string_split = temp_string.replace('  ', ' ').split(' ')
    clear_string = ''
    for ts in temp_string_split:
        if ts != '':
            clear_string += f'{ts} '
    clear_string = clear_string[:len(clear_string) -1]
    return clear_string

def advanced_action(base, full_text, source = 'automatic', word = 'nieznane'):
    full_text = string_cleaner(full_text)
    full_text = str(full_text).strip().replace('. ', '#$%$#').replace('.', '#$%$#')\
        .replace('? ', '#$%$#').replace('?', '#$%$#').replace('! ', '#$%$#').replace('!', '#$%$#')


    full_senten_list = full_text.split('#$%$#')
    sa_dict = {'TITLE' : [], 'SENTENS' : [], 'CLOUDS' : [], 'REACTION' : {}}

    exist = False
    if source == 'wiki':
        if full_senten_list[0].count('-') > 0:
            title_sa = full_senten_list[0].split(' - ')[0]
        else:
            title_sa = full_senten_list[0].split(' ')[0].lower()
        act_dict = action(base, title_sa, None, 'only_se_done')

    if source == 'manual':
        act_dict = action(base, word, None, 'only_se_done')

    if source == 'automatic':
        auto_Titile = automaticTitleSA.pick_contextTarget(base, full_senten_list[0])
        if auto_Titile['PICKED']:
            title = baseTools.take_word(
                base, baseTools.take_sa(
                    base, auto_Titile['PICKED'])['TITLE'][0]
                    )
            # print(title)
            act_dict = action(base, title, None, 'only_se_done')
        else:
            read_sen = action(base, full_senten_list[0], None, 'only_se_done')
            'dodaje se_done i wybiera najpiew PO jak niema to DO jak niema to OR itd  i bierze LB jako title'
            se_done_sentens_read = read_sen['SE_DONE']
            base = read_sen['BASE']
            picked_title_SA = None
            for cate_id in se_done_sentens_read:
                if str(cate_id).startswith('PO'):
                    picked_title_SA = baseTools.take_lb(base, cate_id)
                    break
                elif str(cate_id).startswith('DO'):
                    picked_title_SA = baseTools.take_lb(base, cate_id)
                    break
                elif str(cate_id).startswith('OR'):
                    picked_title_SA = baseTools.take_lb(base, cate_id)
                    break
                elif str(cate_id).startswith('PR'):
                    picked_title_SA = baseTools.take_lb(base, cate_id)
                    break
                elif str(cate_id).startswith('OK'):
                    picked_title_SA = baseTools.take_lb(base, cate_id)
                    break
                elif str(cate_id).startswith('OZ'):
                    picked_title_SA = baseTools.take_lb(base, cate_id)
                    break
                elif str(cate_id).startswith('VO'):
                    picked_title_SA = baseTools.take_lb(base, cate_id)
                    break

            if picked_title_SA is not None:
                lb_word_picked = baseTools.take_word(base, picked_title_SA)
                act_dict = action(base, lb_word_picked, None, 'only_se_done')
            else:
                print('Błąd rodzaju podczas dodawania automatycznego tytułu SA\nSA nie zostało utworzone.')
                return base


    base = act_dict['BASE']
    se_done_title_generator = act_dict['SE_DONE']
    se_done_title = []
    for testing_se_t in se_done_title_generator:
        if str(testing_se_t).count('_') == 1 and testing_se_t is not None:
            se_done_title.append(testing_se_t)

    sa_id_temp = []
    for sano, x in base['SA'].items():
        # allow_all_words_in = False
        count_case = 0
        for x_val in x['TITLE']:
            for sd in se_done_title:
                if sd is not None:
                    lb_for_sd = baseTools.take_lb(base, sd)
                    # print(x_val, x['TITLE'], lb_for_sd)
                    if lb_for_sd is not None and isinstance(lb_for_sd, str) and isinstance(x_val, str) and lb_for_sd in x_val:
                        count_case += 1

        if count_case == len(x['TITLE']) and count_case != 0:
            allow_all_words_in = True
        else:
            allow_all_words_in = False
        if allow_all_words_in:
            sa_id_temp.append(sano)
            break
    # print(sa_id_temp)
    if len(sa_id_temp) == 1:
        exist = True
        sa_id_number = sa_id_temp[0]
    
    if exist:
        old_sa_data = base['SA'][sa_id_number]

        sa_dict['TITLE'] = old_sa_data['TITLE']
        sa_dict['SENTENS'] = old_sa_data['SENTENS']
        sa_dict['CLOUDS'] = old_sa_data['CLOUDS']
        try: sa_dict['REACTION'] = old_sa_data['REACTION']
        except KeyError: sa_dict['REACTION'] = {}
    else:
        for sa in se_done_title:
            if sa.startswith('PO') or sa.startswith('DO') or sa.startswith('OR')\
                or sa.startswith('PR') or sa.startswith('OZ') or sa.startswith('OK'):
                lb_for_sa = baseTools.take_lb(base, sa)
                if lb_for_sa is not None:
                    sa_dict['TITLE'].append(lb_for_sa)
                    sa_dict['TITLE'] = clearLists.clear_lists(sa_dict['TITLE'])

    for sentencein in full_senten_list:
        if sentencein == '': continue
        ssn = splitSententionNum(sentencein)[0]
        # print(ssn)
        c_sen = len(ssn)
        
        new_se = []
        allow = False
        if c_sen > 1:
            for l in ssn:
                '! ? . ...'
                act_dict = action(base, l, None, 'only_se_done')
                se_done = act_dict['SE_DONE']
                C_se_done =[]
                for c in se_done:
                    if str(c).count('_') == 1:
                        C_se_done.append(c)
                base = act_dict['BASE']
                new_se += C_se_done
            allow = True
        else:
            base = action(base, ssn[0])
            se_after = len(base['SE']) - 1
            sa_dict['SENTENS'].append(f'SE_{se_after}')
            allow = False
            # print('allow = False')
        if allow:
            se_after = len(base['SE'])
            base['SE'][se_after] = new_se
            base = baseTools.join_ids_list(base, new_se)
            sa_dict['SENTENS'].append(f'SE_{se_after}')
            sa_dict['SENTENS'] = clearLists.clear_lists(sa_dict['SENTENS'])
            for i in new_se:
                base = baseTools.add_se(base, i, f'SE_{se_after}')
    # print(base['SE'])
    for clo in sa_dict['SENTENS']:
        part_se = baseTools.take_se(base, clo)
        for cl in part_se:
            if cl.startswith('PO') or cl.startswith('DO'):
                lb_for_cl = baseTools.take_lb(base, cl)
                if lb_for_cl is not None and sa_dict['TITLE'] != [] and lb_for_cl not in sa_dict['TITLE']:
                    sa_dict['CLOUDS'].append(lb_for_cl)
                    sa_dict['CLOUDS'] = clearLists.clear_lists(sa_dict['CLOUDS'])

    

    if sa_dict['TITLE'] != []  and sa_dict['CLOUDS'] != []:
        if exist:
            base['SA'][sa_id_number] = sa_dict
        else:
            last_sa = len(base['SA'])
            base['SA'][last_sa] = sa_dict
    return base
if __name__ == '__main__':
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    few_senetes = 'Kilka długich zdań. Mogą być wielkorotnie złożone. Funkcja rozpozna poszczególne części zdania, podzieli na zdania podrzedne i inne. Następnie dopisze do kategorii z biorze SA wszystkie zdania oraz buduje dla nich dane.'
    advanced_action(base, few_senetes)
    # source = 'automatic', 'manual', 'wiki', (sposób przydzielania kategorii SA)
    # word = 'nieznane' dotyczny manual, należy wpisać kategorię
    
    # action(base, 'Doświadczony górnik spokojnie odkrywa kolejne złoża miedzi', option='only_se_done') # dodaje kolejne se do base i zwraca zaktualizowaną bazę
    # print(action(base, 'Doświadczony górnik spokojnie odkrywa kolejne złoża miedzi', option='only_se_done')['SE_DONE'])