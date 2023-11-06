import partSpeech
import changerBlade
import verbFlex
import chanerCases
from tqdm import tqdm
def part_sentens(base, x_list):
    # len_x_list = len(x_list)
    # print(f'Trwa proces analizy zdania, to może potrwać około {len_x_list * 10} sekund.')

    p_exp = {
        'OR' : {},
        'PO' : {},
        'PR' : {},
        'OZ' : {},
        'OK' : {},
        'DO' : {},
        'CZ' : {},
        'ZA' : {},
        'VO' : {},
        'HW' : {}
    }

    # count_pos = 1
    Count_c = 0

    b_verb = True
    b_noun = True
    n_active = False
    n = False
    bez = False
    os = None
    l = None
    tryb = None
    czas = None
    rodz = None
    

    temp_dict = {}
    
    # for xcs in tqdm(x_list, desc=f"Progress: ", leave=False):
    # for xcs in x_list:
    for xcs in tqdm(x_list, desc=f"Prepare process: ", leave=True):
        Count_a = 0
        in_temp_dict = {}
        if xcs == '': continue
        part_SC = partSpeech.part_speach(xcs)
        # print(xcs, part_SC)
        case_list = [
        'przymiotnik', 'przyimek', 'przysłówek', 'czasownik', # czasownik posiłkowy
        'spójnik','determiner', 'wykrzyknik', 'rzeczownik', 'liczebnik', 'partykuła',
        'zaimek', 'nazwa własna', 'znak interpunkcyjny', 'symbol', 'onim'
        ]
        # case_list = ['rzeczownik', 'liczebnik', 'symbol', 'litera',
        #  'czasownik', 'przymiotnik', 'przysłówek', 'wykrzyknik', 'skrót',
        #  'przyimek', 'zaimek', 'partykuła', 'spójnik', 'onim']
        temp_dict[Count_c] = {'used': 'None', f'MAIN_{Count_a}' : 'None', f'CASE_{Count_a}': 'None'}
        for sc in part_SC:
            for cl in case_list:
                c_a = changerBlade.check_v_list(sc, cl, 'True')
                # print(sc[0], sc[1], xcs)
                # print(len(sc))
                if c_a:
                    in_temp_dict[f'MAIN_{Count_a}'] = sc[1]
                    in_temp_dict[f'CASE_{Count_a}'] = sc[0] 
                    in_temp_dict['used'] = xcs
                    Count_a += 1
                    temp_dict[Count_c] = in_temp_dict
        Count_c += 1
        # print(temp_dict)
    final_temp_dict = {}
    # print(temp_dict)
    id_c = 0
    # for xcs in tqdm(x_list, desc=f"Progress: ", leave=False):
    for key_sym, val_sym in tqdm(temp_dict.items(), desc=f"Senten clasification: ", leave=True):
        sym_len = len(val_sym)
        # print(sym_len)
        checker_key = False
        try: 
            temp_dict[key_sym + 1][f'CASE_0']
            checker_key = True
        except KeyError: checker_key = False
        if sym_len == 3:
            final_temp_dict[key_sym] = {'used' : val_sym['used'], 'CASE' : val_sym['CASE_0'], 'MAIN' : val_sym['MAIN_0']}
        else:
            # należy dopisać wiecej wariantów
            found_opt = False
            if key_sym > 0 and temp_dict[key_sym - 1][f'CASE_0'] == 'przysłówek':
                for k_cs, v_cs in temp_dict[key_sym].items():
                    if v_cs == 'przymiotnik' or v_cs == 'czasownik':
                        id_c = int(k_cs.split('_')[1])
                        final_temp_dict[key_sym] = {'used' : val_sym['used'], 'CASE' : val_sym[f'CASE_{id_c}'], 'MAIN' : val_sym[f'MAIN_{id_c}']}
                        found_opt = True
                        break
            if key_sym > 0 and temp_dict[key_sym - 1][f'CASE_0'] == 'przymiotnik':
                for k_cs, v_cs in temp_dict[key_sym].items():
                    if v_cs == 'rzeczownik' or v_cs != 'czasownik':
                        id_c = int(k_cs.split('_')[1])
                        final_temp_dict[key_sym] = {'used' : val_sym['used'], 'CASE' : val_sym[f'CASE_{id_c}'], 'MAIN' : val_sym[f'MAIN_{id_c}']}
                        found_opt = True
                        break
            if key_sym > 0 and temp_dict[key_sym - 1][f'CASE_0'] == 'onim':
                for k_cs, v_cs in temp_dict[key_sym].items():
                    if v_cs == 'czasownik':
                        id_c = int(k_cs.split('_')[1])
                        final_temp_dict[key_sym] = {'used' : val_sym['used'], 'CASE' : val_sym[f'CASE_{id_c}'], 'MAIN' : val_sym[f'MAIN_{id_c}']}
                        found_opt = True
                        break
            if key_sym > 0 and temp_dict[key_sym - 1][f'CASE_0'] == 'rzeczownik':
                for k_cs, v_cs in temp_dict[key_sym].items():
                    if v_cs == 'czasownik':
                        id_c = int(k_cs.split('_')[1])
                        final_temp_dict[key_sym] = {'used' : val_sym['used'], 'CASE' : val_sym[f'CASE_{id_c}'], 'MAIN' : val_sym[f'MAIN_{id_c}']}
                        found_opt = True
                        break
            
            if checker_key and key_sym < sym_len - 1 and temp_dict[key_sym + 1][f'CASE_0'] == 'rzeczownik':
                for k_cs, v_cs in temp_dict[key_sym].items():
                    if v_cs == 'przymiotnik':
                        id_c = int(k_cs.split('_')[1])
                        final_temp_dict[key_sym] = {'used' : val_sym['used'], 'CASE' : val_sym[f'CASE_{id_c}'], 'MAIN' : val_sym[f'MAIN_{id_c}']}
                        found_opt = True
                        break
            if not found_opt:
                final_temp_dict[key_sym] = {'used' : val_sym['used'], 'CASE' : val_sym[f'CASE_0'], 'MAIN' : val_sym[f'MAIN_0']}
    # print(final_temp_dict)
    
    for x,y in tqdm(final_temp_dict.items(), desc=f"Verb verification: ", leave=True):
        if y['CASE'] == 'czasownik':
            c_flex = verbFlex.verb_flex(base, y['used'].lower())
            if c_flex == None:
                c_flex = 'NONE-NONE-NONE-NONE-NONE'
            if c_flex.count('IMIESŁÓW') > 0 and c_flex.count('BIERNY'):
                final_temp_dict[x]['CASE'] = 'imiesłów_bierny'
            if c_flex.count('IMIESŁÓW') > 0 and c_flex.count('PRZYSŁÓWKOWY'):
                final_temp_dict[x]['CASE'] = 'imiesłów_przysłówkowy'
            if c_flex.count('IMIESŁÓW') > 0 and c_flex.count('PRZYMIOTNIKOWY'):
                final_temp_dict[x]['CASE'] = 'imiesłów_przymiotnikowy'
            if c_flex.count('RZECZOWNIK') > 0:
                final_temp_dict[x]['CASE'] = 'rzeczownik'
            # print(c_flex)
    przy_list = ['o', 'na', 'nad', 'przed', 'przez', 'za', 'po', 'w', 'pod']
    # print(final_temp_dict)
    for x,y in tqdm(final_temp_dict.items(), desc=f"Parts sentens sorting: ", leave=True):
        if y['CASE'] == None or y['CASE'] == 'None':
            part_S_C = ['onim', 'unknow']
        else:
            part_S_C = [y['CASE'], y['MAIN']]
        
        c_flex = verbFlex.verb_flex(base, y['used'].lower())
        if c_flex == None:
            c_flex = 'NONE-NONE-NONE-NONE-NONE'
        
        colidions = ['lub', 'lecz', ',']

        if part_S_C[0] == 'czasownik' and not final_temp_dict[x]['used'] in colidions:
            if x > 0 and final_temp_dict[x -1]['used'] == 'nie':
                # print(check_v_list(przy_list, final_temp_dict[x -2]['used']))
                if x > 1 and changerBlade.check_v_list(przy_list, final_temp_dict[x -2]['used']):
                     p_exp['OR'][x] = [final_temp_dict[x]['used'], c_flex, part_S_C[0]]
                else:
                    p_exp['OR'][x] = [f'{final_temp_dict[x -1]["used"]} {final_temp_dict[x]["used"]}', c_flex, part_S_C[0]]
                    n_active = True
                    if n: n = False
                    else: n = True
            elif x > 0 and final_temp_dict[x -1]['used'] != 'nie':
                p_exp['OR'][x] = [final_temp_dict[x]['used'], c_flex, part_S_C[0]]
            else:
                p_exp['OR'][x] = [final_temp_dict[x]['used'], c_flex, part_S_C[0]]
    il_OR = len(p_exp['OR'])
    # print(p_exp['OR'])
    for xsc in tqdm(p_exp['OR'].values(), desc=f"Progress: ", leave=True):
        # print(xsc)
        xss = xsc[1].split('-')
        if il_OR > 1:
            if xss.count('IMIESŁÓW') == 0 and xss.count('RZECZOWNIK') == 0 and xsc[1] != 'NONE-NONE-NONE-NONE-NONE':
                if xss[0] == 'BEZOKOLICZNIK':
                    bez = True
                else:
                    if os == None: os = xss[0]
                    if l == None or l == 'LP': l = xss[1]
                    if tryb == None: tryb = xss[2]
                    if czas == None: czas = xss[3]
                    if czas == 'PRZY' and xss[3] == 'PRZE': czas = xss[3]
                    if czas == 'TEZ' and xss[3] == 'PRZY': czas = xss[3]
                    if czas == 'TER' and xss[3] == 'PRZE': czas = xss[3]
                    if rodz == None: rodz = xss[4]
        else:
            if xss[0] == 'BEZOKOLICZNIK':
                bez = True
            else:
                os, l, tryb, czas, rodz = xss
    # print(l)
    selected_as_OR = [a[0] for a in p_exp['OR'].values()]
    # print(selected_as_OR)
    # print(final_temp_dict)
    for x, y in tqdm(final_temp_dict.items(), desc=f"Finishing: ", leave=True):
        if y['CASE'] == None or y['CASE'] == 'None':
            part_S_C = ['onim', 'unknow', ]
        else:
            part_S_C = [y['CASE'], y['MAIN']]

        # part_S_C = [y['CASE'], y['MAIN']]
        # print(y['used'], part_S_C)
        # print(b_noun, b_verb)
        if y['used'].lower() in ['o', 'w', 'u', 'z', 'na', 'za', 'po', 
                         'od', 'do', 'nad', 'pod', 'przed', 
                         'przez', 'przy', 'obok']:
            p_exp['ZA'][x] = [y['used'], part_S_C[1], part_S_C[0]]
            continue
        elif  y['used'].lower() in ['a', 'i', 'oraz', 'tudzież', ',',
                            'albo', 'bądź', 'czy', 'lub',
                            'ani', 'ni', 
                            'aczkolwiek', 'ale', 'jednak', 'lecz', 'natomiast', 'zaś',
                            'czyli', 'mianowicie', 'ponieważ', 'to', 
                            'dlatego', 'przeto', 'tedy', 'więc', 'zatem', 'toteż',
                            'aby', 'by', 'bowiem', 'choć', 'jeżeli', 'ponieważ', 'że']:
            p_exp['HW'][x] = [y['used'], part_S_C[1], part_S_C[0]]
            continue
        elif y['used'] in selected_as_OR:
            b_verb = False
            # continue
        else:
            # print(l)
            if l != 'LP' and l !='LM':
                l = 'LP'
            # print(l)
            # print(b_noun, b_verb, y['used'], part_S_C)
            # input(y)
            if y['CASE'] != 'onim':
                if part_S_C[0] == 'czasownik':
                    b_verb = False

                # if part_S_C[0] == 'rzeczownik':
                #     # TESTOWANIE RZECZOWNIKÓW 
                #     print('tutaj ---->', y['used'])
                #     ggg = str(change_cases_SP(y['used'].lower(), 'BACK', 'MIA', l, 'rzeczownik', 'NO'))
                #     print(len(ggg))
                #     print(ggg)
                #     print('tutaj <---_', len(y['used'].lower()), y)

                if part_S_C[0] == 'rzeczownik':
                    noun_case_SP = chanerCases.change_cases_SP(base, y['used'].lower(), 'BACK', 'MIA', l, 'rzeczownik', 'NO')
                    if noun_case_SP == y['used'].lower():
                    # print(a.change_cases_SP(y['used'].lower(), 'BACK', 'MIA', l, 'rzeczownik', 'NO'))
                        if b_verb and b_noun:
                            p_exp['PO'][x] = [y['used'], part_S_C[1], part_S_C[0]]
                            # print('PO', str(b_verb), str(b_noun))
                            b_noun = False
                        elif  not b_verb and not b_noun:
                            p_exp['DO'][x] = [y['used'], part_S_C[1], part_S_C[0]]
                            # print('DO1', str(b_verb), str(b_noun))
                        elif  not b_verb and b_noun:
                            p_exp['DO'][x] = [y['used'], part_S_C[1], part_S_C[0]]
                        else:
                            p_exp['DO'][x] = [y['used'], part_S_C[1], part_S_C[0]]
                            # print('DO2', str(b_verb), str(b_noun))
                        # print('''1 b_noun = False | p_exp['PO'][x] = [y['used'], part_S_C[1], part_S_C[0]]''')
                    elif noun_case_SP != y['used'].lower():
                        p_exp['DO'][x] = [y['used'], part_S_C[1], part_S_C[0]]
                        # print('DO3', str(b_verb), str(b_noun))
                if os == 'Ios' or os == 'IIos': b_noun = False
                if b_noun and b_verb:
                    if part_S_C[0] == 'przymiotnik' or part_S_C[0] == 'przysłówek' or part_S_C[0] == 'liczebnik' or part_S_C[0].startswith('imiesłów'):
                        p_exp['PR'][x] = [y['used'], part_S_C[1], part_S_C[0]]
                        # print('''2 p_exp['PR'][x] = [y['used'], part_S_C[1], part_S_C[0]]''')
                elif not b_noun and b_verb:
                    if  part_S_C[0] == 'przymiotnik' or part_S_C[0] == 'przysłówek' or part_S_C[0] == 'liczebnik' or part_S_C[0].startswith('imiesłów'):
                        # print('''3 p_exp['OZ'][x] = [y['used'], part_S_C[1], part_S_C[0]]''')
                        p_exp['OZ'][x] = [y['used'], part_S_C[1], part_S_C[0]]
                elif not b_noun and not b_verb:
                    if part_S_C[0] == 'przymiotnik' or part_S_C[0] == 'przysłówek' or part_S_C[0] == 'liczebnik' or part_S_C[0].startswith('imiesłów'):
                        p_exp['OK'][x] = [y['used'], part_S_C[1], part_S_C[0]]
                        # print('OK', str(b_verb), str(b_noun))
                        # print('''4 p_exp['OK'][x] = [y['used'], part_S_C[1], part_S_C[0]]''')
                else:
                    if part_S_C[0] == 'przymiotnik' or part_S_C[0] == 'przysłówek' or part_S_C[0] == 'liczebnik' or part_S_C[0].startswith('imiesłów'):
                        p_exp['OK'][x] = [y['used'], part_S_C[1], part_S_C[0]]
                        # print('''4 p_exp['OK'][x] = [y['used'], part_S_C[1], part_S_C[0]]''')
                
                    # print('''5 p_exp['DO'][x] = [y['used'], part_S_C[1], part_S_C[0]]''')

                # elif b_noun and b_verb and part_S_C[0] == 'rzeczownik' and change_cases_SP(y['used'], 'BACK', 'MIA', l, 'rzeczownik', 'NO') == y['used']:
                #     p_exp['DO'][x] = [y['used'], part_S_C[1], part_S_C[0]]

                if part_S_C[0] != 'przymiotnik' and part_S_C[0] != 'przysłówek' and part_S_C[0] != 'liczebnik' \
                    and part_S_C[0] != 'rzeczownik' and part_S_C[0] != 'czasownik':
                    if part_S_C[0] == 'zaimek' or part_S_C[0] == 'przyimek' or part_S_C[0] == 'partykuła'\
                        or part_S_C[0] == 'symbol':
                        if not n_active:
                            p_exp['ZA'][x] = [y['used'], part_S_C[1], part_S_C[0]]
                        elif y['used'] != 'nie':
                            p_exp['ZA'][x] = [y['used'], part_S_C[1], part_S_C[0]]
                            # print('''6 p_exp['ZA'][x] = [y['used'], part_S_C[1], part_S_C[0]]''')
                if part_S_C[0] == 'zaimek' or part_S_C[0] == 'symbol':
                    if not n_active:
                        p_exp['ZA'][x] = [y['used'], part_S_C[1], part_S_C[0]]
                        # print('''6 p_exp['ZA'][x] = [y['used'], part_S_C[1], part_S_C[0]]''')
                    elif y['used'] != 'nie':
                            p_exp['ZA'][x] = [y['used'], part_S_C[1], part_S_C[0]]
            else:
                p_exp['VO'][x] = [y['used'], part_S_C[1], part_S_C[0]]
    p_exp['CZ'] = {'OS' : os, 'L' : l, 'TRYB' : tryb, 'CZAS' : czas, 'RODZ' : rodz, 'BEZ' : bez, 'N' : n}
    # print(p_exp)
    return p_exp

if __name__ == '__main__':
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    lista = ['Telefon', 'ma', 'dzwonić', 'cały', 'dzień']
    print(part_sentens(base, lista))