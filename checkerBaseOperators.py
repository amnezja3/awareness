import partSpeech
import takeTarget
import verbFlex
import baseTools
import chanerCases
import clearLists
import action
import addionalisAwe

def whatIsThat(keyword):
    import requests
    urlAddress = f'https://sjp.pwn.pl/szukaj/{keyword}.html'
    phraseList = ['Słownik języka polskiego PWN', 'Wielki słownik ortograficzny PWN', 'Synonimy', 'Podobne wyszukiwania']
    phraseEndTAGList = ['Słownik języka polskiego pod red. W. Doroszewskiego', 'Słownik języka polskiego PWN', '</article>', '</div>']

    EXPORT = []
    def searchString(url, faze):
        while True:
            try:
                r = requests.get(url)
                htmlSTR = r.text
                break
            except:
                print('Połączenie zostało zerwane. ponowna próba nawiązania połączenia!')
        lenhtmlSTR = len(htmlSTR)
        lenFaze = len(faze)
        export = []
        for i in range(lenhtmlSTR):
            x = i+lenFaze
            if faze == htmlSTR[i:x]:
                export.append((i, x))
        return export, htmlSTR

    for phrase in range(len(phraseList)):
        allHtml = searchString(urlAddress, phraseList[phrase])[1]
        try:partHtml = allHtml[searchString(urlAddress, phraseList[phrase])[0][0][1]+1:]
        except:break
        rangeStart =  len(allHtml[searchString(urlAddress, phraseList[phrase])[0][0][1]:])
        lenPhraseEnd = len(phraseEndTAGList[phrase])
        for x in range(rangeStart):
            if partHtml[x:x+lenPhraseEnd] == phraseEndTAGList[phrase]:
                closerTAGindex = searchString(urlAddress, phraseList[phrase])[0][0][0] + x + lenPhraseEnd+1
                break
        soupSelected = str(allHtml[searchString(urlAddress, phraseList[phrase])[0][0][1]:closerTAGindex])
        sS = soupSelected.split('<li>')
        valuesAi = []
        for s in sS:
            s=s.strip()
            s1 = s.split('>')
            for c in s1:
                c=c.strip()
                s2 = c.split('<')
                try:inti = int(s2[0][0])
                except:inti=True
                if s2[0] != '' and s2[0] != ', ' and s2[0] != ' ' and s2[0] != '•\xa0' and s2[0] != 'pot.' and s2[0] != '1.\xa0' and inti==True:
                    valuesAi.append(s2[0].strip())
        newBrain = {phraseList[phrase]:valuesAi}
        EXPORT.append(newBrain)
    return EXPORT


def synonimus_sentenses(base, sentens_list):
    try:
        with open(f'synonimus.neural', 'r', encoding='utf-8') as userFile:
            words_Content = userFile.readlines()
    except FileNotFoundError:
        words_Content = []
    new_contenet = {}

    for x_w in words_Content:
        x_w_S = x_w.strip().split(', ')
        if x_w_S[1:] != []:
            new_contenet[x_w_S[0]] = []
            new_contenet[x_w_S[0]].append(x_w_S[1:])

    sym_list = []
    new_dict_sentenses = {}
    word_count = 0
    for word in sentens_list:
        syn_true = False
        new_dict_sentenses[word_count] = []
        word_part_speach = partSpeech.part_speach(word)
        word_part_list = []
        print(word_part_speach)
        for word_part in word_part_speach:
            word_part_list.append(word_part[0])
        
        noun_true = False
        noun_case_list = []
        verb_true = False
        word_verb_flex = ''
        if 'rzeczownik' in word_part_list:
            word_cases = chanerCases.change_cases_SP(base, word, 'INFO')
            noun_case_list = word_cases['CASE']
            noun_true = True
        elif 'czasownik' in word_part_list:
            word_verb_flex = verbFlex.verb_flex(base, word, 'TAKE')
            verb_true = True
        try:
            new_contenet[word]
            syn_list_generation = [{'Synonimy' : new_contenet[word][0]}]
        except KeyError:
            syn_list_generation = whatIsThat(word)
        for synonim in syn_list_generation:
            try:
                synonim['Synonimy']
                found = True
            except KeyError:
                found = False
            if found:
                complet = set()
                for f_sym in synonim['Synonimy']:
                    if f_sym.count(' ') == 0 and f_sym.count('(') == 0\
                        and f_sym.count(')') == 0 and f_sym.count('.') == 0\
                            and f_sym.count('-') == 0 and f_sym.count(',') == 0\
                                and word != f_sym:
                        syn_part = partSpeech.part_speach(f_sym)
                        for part in syn_part:
                            syn_targ = takeTarget.take_target(word, part[0])
                            if syn_targ[0] != 'a':
                                if not f_sym in syn_targ:
                                    if part[0] in word_part_list:
                                        if noun_true:
                                            for case_noun in noun_case_list:
                                                case_noun_name = case_noun.split('-')
                                                new_case = chanerCases.change_cases_SP(
                                                                            base,
                                                                            f_sym, 'BACK', 
                                                                            case_noun_name[1], 
                                                                            case_noun_name[0], 
                                                                            'rzeczownik', 
                                                                            'NO')
                                                if new_case != 'MAKE-UPDATE' and new_case != 'Nieodmienialny'\
                                                    and new_case != 'None' and new_case != 'a' and new_case != None:
                                                    complet.add(new_case)
                                        elif verb_true:
                                            new_flex_word = verbFlex.verb_flex(base, f_sym, 'CHANGE', word_verb_flex)
                                            if new_flex_word != 'WRONG-KEY'\
                                                and new_flex_word != None and new_flex_word != 'None'\
                                                    and new_flex_word != 'a':
                                                complet.add(new_flex_word)
                                        else:
                                            complet.add(f_sym)
                complet_list = []
                for cl in complet:
                    complet_list.append(cl)
                sym_list = [word] + complet_list
                syn_true = True
                break

        if not syn_true:
            sym_list = [word]

        for s in sym_list:
            new_dict_sentenses[word_count].append(s)
        word_count += 1

    converteing_dict = {}
    llen = len(sentens_list)

    sym_save_list = []
    item_string = ''
    for selecting in range(0, llen):
        converteing_dict[selecting] = len(new_dict_sentenses[selecting])
        this_list = new_dict_sentenses[selecting]
        temp_string_item = ''
        for this in this_list:
            sym_save_list.append(this)
            temp_string_item += f'{this}, '
        temp_string_item = temp_string_item[:len(temp_string_item) -2] + '\n'
        if temp_string_item.count(',') > 0:
            item_string += temp_string_item

    old_string_data = ''
    for k, vals in new_contenet.items():
        if vals[0] != []:
            old_string_data += f'{k}, '

            for v in vals[0]:
                old_string_data += f'{v}, '
        old_string_data = old_string_data[:len(old_string_data) - 2] + '\n'
        
    save_string = old_string_data + item_string

    with open('synonimus.neural', 'w+', encoding='utf-8') as sun_file:
        sun_file.write(save_string)

    string_exp_List = []
    new_list = [] + sentens_list
    for loop in range(0, len(sentens_list)):
        for index_syn in range(0, converteing_dict[loop]):
            new_list[loop] = new_dict_sentenses[loop][index_syn]
            x = [] + new_list
            string_exp = ''
            for x_ex in x:
                string_exp += f'{x_ex} '
            string_exp = string_exp[:len(string_exp)- 1]
            string_exp_List.append(string_exp)
        new_list = [] + sentens_list
    finally_string = clearLists.clear_lists(string_exp_List)
    # print(finally_string)

    count = 0
    exp_dict = {}
    exp = []
    for fs in finally_string:
        f = fs.split(' ')
        exp_dict[count] = f
        count += 1
        exp.append(f)

    return {'DICT' : exp_dict, 'LIST' : exp, 'STRINGES' : finally_string}

def fix_cat_list(list_to_fix):
    clear_list_cat = []
    for x in list_to_fix:
        if x is not None and str(x).count('_') == 1:
            clear_list_cat.append(x)
    return clear_list_cat

def neuralSentensPrepare(base):

    """
    PO@!D1V3r^ID:0|LINKS:LB_0~|SENTENS:SE_0~|LID:1|
    PR@!D1V3r^ID:0|LINKS:LB_0~|SENTENS:SE_0~|LID:2|
    OR@!D1V3r^ID:0|LINKS:LB_0~|SENTENS:~SE_0~|LID:3|
    DO@!D1V3r^ID:0|LINKS:LB_0~|SENTENS:~SE_0~|LID:4|
    OK@!D1V3r^ID:0|LINKS:LB_0~|SENTENS:SE_0~|LID:5|
    VO@!D1V3r^ID:0|LINKS:LB_0~|SENTENS:SE_0~|LID:6|
    OZ@!D1V3r^ID:0|LINKS:LB_0~|SENTENS:SE_0~|LID:7|
    ZA@!D1V3r^ID:0|LINKS:LB_0~|SENTENS:SE_0~|LID:8|
    HW@!D1V3r^ID:0|LINKS:LB_0~|SENTENS:SE_0~|LID:9|
    LB@!D1V3r^ID:0|LINKS:PR_0~PO_0~OR_0~DO_0~OK_0~VO_0~OZ_0~ZA_0~HW_0~|LID:10|
    SE@!0^PR_0~PO_0~OR_0~DO_0~OK_0~VO_0~OZ_0~ZA_0~HW_0~!
    SA@!0^|TITLE:LB_0~|SENTENS:~SE_0~|CLOUDS:~|
    LID@!10
    """
    base_words_LID_dict = {}
    base_cat_LID_dict = {}

    cat_symbols = ['PR', 'PO', 'ZA', 'HW', 'OZ', 'OR', 'OK', 'DO', 'VO', 'LB']
    for kay_base, val_base in base.items():
        if kay_base in cat_symbols:
            for kay_ind in val_base.keys():
                id_LID = base[kay_base][kay_ind]['LID']
                id_part = f"{kay_base}_{base[kay_base][kay_ind]['ID']}"

                base_words_LID_dict[id_LID] = kay_ind
                base_cat_LID_dict[id_LID] = id_part
    
    all_se_id_dict = {}
    all_se_LID_dict = {}
    for se_id, se_cat in base['SE'].items():
        all_se_id_dict[f'SE_{se_id}'] = se_cat
        all_se_LID_dict[f'SE_{se_id}'] = [baseTools.take_LID(base, lid) for lid in fix_cat_list(se_cat)]
        

    return {
        'SLOWNIK_SLOW' : base_words_LID_dict, 
        'SLOWNIK_CAT' : base_cat_LID_dict,
        'ALL_SENTENSES_LID' : all_se_LID_dict,
        'ALL_SENTENSES' : all_se_id_dict
        }

def stats_se(base, se_id, zero = True):
    se_list = baseTools.take_se(base, se_id)
    export_dict = {
        'PO' : 0,
        'PR' : 0,
        'OR' : 0,
        'DO' : 0,
        'OK' : 0,
        'VO' : 0,
        'OZ' : 0,
        'ZA' : 0,
        'HW' : 0,
        }
    for ps in se_list:
        for k in export_dict.keys():
            if ps.startswith(k):
                export_dict[k] += 1
    if zero:
        return export_dict
    else:
        exp_without_zero = {}
        for k, v in export_dict.items():
            if v > 0:
                exp_without_zero[k] = v
        return exp_without_zero

def golden_se(base, cat_id):
    t_LB = baseTools.take_lb(base, cat_id)
    p_CAT_ID = baseTools.take_links(base, t_LB)
    exp_list = []
    for p in p_CAT_ID:
        t_SE = baseTools.take_sentens(base, p)
        for i in t_SE:
            se = stats_se(base, i, True)
            if se['PO'] > 0 and se['PO'] < 5 and se['OR'] > 0 and se['OR'] < 5 \
                and se['DO'] > 0 and se['DO'] < 10 and se['HW'] > 0 and se['HW'] < 5:
                exp_list.append(i)
                # print(a.take_se_words(base, i, 'LIST'))
                # print(take_se_words(base, i, 'STR'))
    return exp_list

def part_split_IN_OUT(base, cat_id):
    in_out_dict = {
        'IN' : set(),
        'OUT' : set()}
    cat_sentens = baseTools.take_sentens(base, cat_id)
    for se_id in cat_sentens:
        this_se = baseTools.take_se(base, se_id)
        ind = 0
        for part in this_se:
            if cat_id == part and len(this_se) > 1:
                if ind == 0:
                    in_out_dict['OUT'].add(this_se[ind + 1])
                if ind != 0 and ind != len(this_se) -1:
                    in_out_dict['IN'].add(this_se[ind - 1])
                    in_out_dict['OUT'].add(this_se[ind + 1])
                if ind == len(this_se) -1:
                    in_out_dict['IN'].add(this_se[ind - 1])
            ind += 1
    return in_out_dict

def find_part_in_SE(base, cat_id):
    final_list = []
    for s, e in base['SE'].items():
        # print(s, e)
        if cat_id in e:
            writer = f'SE_{s}'
            final_list.append(writer)
    return final_list 

def part_most_popular(base, item_list, exceping_part = None):
    if exceping_part == None: exceping_part = 'FREE'
    words_dict = {}
    for item in item_list:
        if not item.startswith('LB') and not item.startswith(exceping_part):
            total_word = addionalisAwe.stats_part(base, item)["TOTAL"]
            words_dict[item] = total_word
    ccounter = 0
    for v in words_dict.values():
        if v > ccounter:
            ccounter = v
    for k, v in words_dict.items():
        if v == ccounter and v > 4:
            return k

def find_se_by_LB(base, cat_id):
    cat_lb = baseTools.take_lb(base, cat_id,'ID')
    links_lb = baseTools.take_links(base, cat_lb)
    all_se = set()
    for link in links_lb:
        fpis_0 = find_part_in_SE(base, link)
        for ix in fpis_0: all_se.add(ix)
    return all_se

def find_se_by_PO(base, PO_id, cat_id):
    se_PO = find_se_by_LB(base, PO_id)
    se_cat = find_se_by_LB(base, cat_id)
    return se_cat.intersection(se_PO)

def find_pharse_in_part(base, word):
    cat_set = set()
    for b_CAT in base.keys():
        if b_CAT != 'SE' and b_CAT != 'LB' and b_CAT != 'LID' and b_CAT != 'BASE'\
            and b_CAT != 'SA' and b_CAT != 'RE':
            for b_cat in base[b_CAT].keys():
                # print(b_cat)
                if b_cat == word:
                    cat_set.add(b_CAT)
    exp_list = []
    for c_cat in cat_set:
        exp_list.append(baseTools.take_id(base, c_cat, word))
    return exp_list

def searcher_phrase(base, sentens):
    sentens = action.string_cleaner(sentens)
    sentens_list = sentens.split(' ')
    PO_DO = []
    OTHERS = []
    FULL_SET = set()
    for word in sentens_list:
        word_ids = find_pharse_in_part(base, word)
        for wi in word_ids:
            if wi.startswith('PO') or wi.startswith('DO'):
                PO_DO.append(wi)
            else:
                OTHERS.append(wi)
    if len(PO_DO) == 0: PO_DO = [OTHERS[0]]
    for pd in PO_DO:
        for o in OTHERS:
            content_set = find_se_by_PO(base, pd, o)
            for c in content_set:
                FULL_SET.add(c)
    return FULL_SET

if __name__ == "__main__":
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(neuralSentensPrepare(base))