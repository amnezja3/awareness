import baseTools
import random as r
from tqdm import tqdm
import action

def dicson_brain(base, ask_str):
    ask = str(ask_str).replace('?', '').replace('!', '').replace('.', '')
    ask_seDone = action.action(base, ask, None, 'only_se_done')
    ask_list = ask_seDone['SE_DONE']
    base = ask_seDone['BASE']
    quest_mark = baseTools.questions_mark(base, 'zaimki_pytajace')
    modal_mark = baseTools.questions_mark(base, 'operatory_modalne')
    modalny_ask = []
    for cat_n in ask_list:
        if cat_n not in quest_mark:
            modalny_ask.append(cat_n)

    modal_ask_split = []
    the_point = []
    for ma in modalny_ask:
        if ma not in modal_mark:
            the_point.append(ma)
        else:
            modal_ask_split.append(ma)

    the_point_clear = []
    for x in the_point:
        tlb = baseTools.take_lb(base, x)
        if tlb is not None:
            the_point_clear.append(tlb)

    se_set_point = set()
    for lb_point in the_point_clear:
        lb_links = baseTools.take_links(base, lb_point)
        for link in lb_links:
            ses = baseTools.take_sentens(base, link)
            for se_id in ses:
                se_set_point.add(se_id)

    spearator_word = baseTools.take_id(base, 'HW', 'to')
    extra_spearator_word = baseTools.take_id(base, 'ZA', 'też')

    se_dict_splittes = {}
    se_dict_splittes_cat = {}
    se_dict_splittes_lb = {}

    for se in tqdm(se_set_point, desc=f"Looking for sentens: ", leave=True):
        start_sparator_index = 0
        stop_sparator_index = 0
        se_took = baseTools.take_se(base, se)
        for loop_no in range(len(se_took)):
            if loop_no < len(se_took) - 1 and spearator_word == se_took[loop_no] and se_took[loop_no + 1] == extra_spearator_word:
                start_sparator_index = loop_no
                stop_sparator_index = loop_no + 2
                break
            elif loop_no < len(se_took) -1 and spearator_word == se_took[loop_no]:
                start_sparator_index = loop_no
                stop_sparator_index = loop_no + 1
                break

        list_PRPO = [baseTools.take_word(base, x) for x in se_took[:start_sparator_index]]
        list_DOOK = [baseTools.take_word(base, x) for x in  se_took[stop_sparator_index:]]
        se_dict_splittes[se] = {
                                'LEFT' : list_PRPO, 'RIGHT' : list_DOOK, 
                                }
        list_PRPO_LB = []
        for x in se_took[:start_sparator_index]:
            tlb = baseTools.take_lb(base, x)
            if tlb is not None:
                list_PRPO_LB.append(tlb)

        list_DOOK_LB = []
        for x in se_took[stop_sparator_index:]:
            tlb = baseTools.take_lb(base, x)
            if tlb is not None:
                list_DOOK_LB.append(tlb)

        se_dict_splittes_lb[se] = {
                                'LEFT' : list_PRPO_LB, 'RIGHT' : list_DOOK_LB, 
                                }
        se_dict_splittes_cat[se] = {
                                'LEFT' :se_took[:start_sparator_index], 'RIGHT' : se_took[stop_sparator_index:], 
                                }

    technical_dict_ans = {}
    operation_dict_ans = {}
    for k, b in tqdm(se_dict_splittes_lb.items(), desc=f"Preapare asnwers: ", leave=True):
        perfect = []
        for element in the_point_clear:
            if element in b['LEFT']:
                perfect.append(element)
        len_perfect = len(perfect)
        if the_point_clear == perfect and len_perfect < 4:
            technical_dict_ans[k] = se_dict_splittes_cat[k]['LEFT'] + modal_ask_split + se_dict_splittes_cat[k]['RIGHT']
            operation_dict_ans[k] = [se_dict_splittes_cat[k]['LEFT'], modal_ask_split, se_dict_splittes_cat[k]['RIGHT']]
        else:
            perfect = []
            for element in the_point_clear:
                if element in b['RIGHT']:
                    perfect.append(element)

            len_perfect = len(perfect)
            len_point = len(the_point_clear)
            score_perfect_point = len_point - len_perfect
            if score_perfect_point < 2 and len_point > 3:
                technical_dict_ans[k] = se_dict_splittes_cat[k]['RIGHT'] + modal_ask_split + se_dict_splittes_cat[k]['LEFT']
                operation_dict_ans[k] = [se_dict_splittes_cat[k]['RIGHT'], modal_ask_split, se_dict_splittes_cat[k]['LEFT']]

    aswers = set()
    for se, cat in technical_dict_ans.items():
        senten = ''
        for c in cat:
            word = baseTools.take_word(base, c)
            senten += f'{word} '
        aswers.add(senten.capitalize())
    answer_list = [asx for asx in aswers]
    
    random_answer = ''
    if len(answer_list) > 0:
        random_answer = r.choice(answer_list)
        found = True
    else:
        found = False

    return {
        'ASK-LIST' : ask_list,
        'OPERATION' : operation_dict_ans,
        'TECHNICAL' : technical_dict_ans,
        'ANSWERS-LIST' : answer_list,
        'RANDOM-ANSWER' : random_answer,
        'FOUND' : found
    }
if __name__ == '__main__':
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(dicson_brain(base, 'co robi samochód'))
