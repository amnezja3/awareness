
import baseTools
import takeTarget
from tqdm import tqdm
import AiRandsChoice_class
aiRand = AiRandsChoice_class.AiRandsChoice()

def pick_contextTarget(base, string):
    main_words = set()
    for word in tqdm(str(string)\
        .replace('?', '').replace('.', '')\
            .replace('!', '').split(' '),
                desc=f"Looking for context: ",
                    leave=True):
        case_list = [
            'przymiotnik', 'czasownik', 
            'rzeczownik', 'liczebnik', 
            'onim' ]
        for case_word in case_list:
            main = takeTarget.take_superTarget(base, word, case_word, what='MAIN-WORDS')
            if main:
                for m in main: main_words.add(m)

    lb_list = []
    for sdt in main_words:
        lb_sym = baseTools.take_id(base, 'LB', sdt)
        if lb_sym is not None:
            lb_list.append(lb_sym)
    sa_list = []
    sa_dict = {}
    for nomber_sa, values_sa in base['SA'].items():
        sa_id = f'SA_{nomber_sa}'
        lb_dict = {}
        for ll in lb_list:
            lb_dict[ll] = 0
            if ll in values_sa['CLOUDS']:
                lb_dict[ll] += 1
        score = 0
        for amou in lb_dict.values():
            score += amou
        if score > 0:
            sa_dict[sa_id] = score
            sa_list.append(sa_id)
    if len(sa_list) > 1:
        picked = aiRand.weighted_choice(
            [sa_sym for sa_sym in sa_dict.keys()], 
            [sa_presents for sa_presents in sa_dict.values()]
        )
    elif len(sa_list) == 1:
        picked = sa_list[0]
    else:
        picked = None
    return {'SA-LIST' : sa_list, 'PICKED' : picked}