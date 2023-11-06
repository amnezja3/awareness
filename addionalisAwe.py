import baseTools
import checkerBaseOperators
import action

def stats_part(base, cat_id):
    part_links = baseTools.take_links(base, cat_id)
    part_sees = baseTools.take_links(base, cat_id)
    part_in = checkerBaseOperators.part_split_IN_OUT(base, cat_id)['IN']
    part_out = checkerBaseOperators.part_split_IN_OUT(base, cat_id)['OUT']
    
    export_dict = {
        'SENTENS' : len(part_sees),
        'LINKS' : len(part_links),
        'PART-IN' : len(part_in),
        'PART-OUT' : len(part_out),
        'TOTAL' : len(part_links) + len(part_sees) + len(part_in) + len(part_out)
        }
    return export_dict

def generator_AI_most_popular(base, cat_start_id, no_words = 5, exceping_part = None):
    '------ ------ ------ ------ ------ ------ ------ ------ ----- ----- -'
    'Generator słów, oparty o ststs --> działa dobrze ale jest tendencyjny'
    '------ ------ ------ ------ ------ ------ ------ ------ ----- ----- -'
    cat_word = baseTools.take_word(base, cat_start_id)
    publish_string = f'{cat_word} '
    publish_list = [cat_start_id]
    for _ in range(no_words):
        classic_set = checkerBaseOperators.part_split_IN_OUT(base, cat_start_id)['OUT']
        if len(classic_set) > 0 and cat_start_id != None:
            links = [this for this in classic_set]
            cat_start_id = checkerBaseOperators.part_most_popular(base, links, exceping_part)
        else:
            break
        if cat_start_id != None:
            if not cat_start_id in publish_list:
                publish_list.append(cat_start_id)
            cat_word = baseTools.take_word(base, cat_start_id)
            count_word_in = publish_string.count(cat_word)
        else:
            break
        if count_word_in == 0:
            publish_string += f'{cat_word} '
    publish_string = publish_string[:len(publish_string)-1]
    return {'STRING' : publish_string, 'ID' : publish_list}

def generator_AI_se(base, word, settings = 'PR, PO, OZ, OR, OR, ZA, OK, DO'):
    '------ ------ ------ ------ ------ ------ ------ ------ -----'
    'Generator słów, oparty o random i ststs --> średnio to działa'
    '------ ------ ------ ------ ------ ------ ------ ------ -----'
    def pick_side_part(cat, item_list):
        import random

        words_dict = {}
        for item in item_list:
            if not item.startswith('LB') and item.startswith(cat):
                if not item.startswith('OR'):
                    total_word = stats_part(base, item)["TOTAL"]
                    words_dict[item] = total_word
        ccounter = 0
        for v in words_dict.values():
            if v > ccounter:
                ccounter = v
        for k, v in words_dict.items():
            if v == ccounter and v > 4:
                print(cat, k, v, ccounter)
                return k
            
        i_set = set()
        for item in item_list:
            if item.startswith(cat):
                i_set.add(item)
        if len(i_set) != 0:
            for item in item_list:
                if not item.startswith('LB') and not item.startswith('OR'):
                    i_set.add(item)
        if len(i_set) != 0:
            choice_list = []
            for x in i_set:
                choice_list.append(x)
            return random.choice(choice_list)
        else: return 'False'
        
    setts = settings.replace(' ', '').split(',')
    setts_list = [[setts[x], None] for x in range(len(setts))]
    word_id = None
    cat_start = None
    choice_list = []
    word_ID_pick_left = 'False'
    word_ID_pick_right = 'False'
    for b_CAT in base.keys():
        if b_CAT != 'SE' and b_CAT != 'LB' and b_CAT != 'ZA' and b_CAT != 'LID' \
            and b_CAT != 'BASE' and b_CAT != 'SA':
            for v in base[b_CAT]:
                if v == word:
                    # print(b_CAT)
                    counter_index = 0
                    for x in setts:
                        if x.startswith(b_CAT):
                            cat_start = counter_index
                            break
                        counter_index += 1
                    if cat_start != None:
                        word_id = baseTools.take_id(base, b_CAT, word)
                        setts_list[cat_start] = [b_CAT, word_id]
                        choice_list.append(word_id)
                    else:
                        print(f'Nie znaleziono ID dla słowa: {word}')
                    break
    if cat_start != None:
        if cat_start != 0 and cat_start != len(setts_list) -1:
            top_part = setts_list[cat_start][1]
            words_link = baseTools.take_links(base, top_part)

            for _ in range(len(words_link)  * 5):
                word_ID_pick_left = pick_side_part(setts[cat_start - 1], words_link)
                if word_ID_pick_left != 'False':
                    if not word_ID_pick_left in choice_list:
                        choice_list.append(word_ID_pick_left)
                        break
            for _ in range(len(words_link) * 5):
                word_ID_pick_right = pick_side_part(setts[cat_start + 1], words_link)
                if word_ID_pick_right != 'False':
                    if not word_ID_pick_right in choice_list:
                        choice_list.append(word_ID_pick_right)
                        break

            if word_ID_pick_left != word_ID_pick_right:
                setts_list[cat_start + 1][1] = word_ID_pick_right
                setts_list[cat_start - 1][1] = word_ID_pick_left

            for back in range(cat_start -1, 0, -1):
                fron_part_id = setts_list[back + 1][1]
                # print(fron_part_id)
                if fron_part_id != 'False' and fron_part_id != None:
                    links_front = baseTools.take_links(base, fron_part_id)
                    for _ in range(len(links_front)  * 5):
                        word_ID_pick_left = pick_side_part(setts[back -1], links_front)
                        if word_ID_pick_left != 'False':
                            if not word_ID_pick_left in choice_list:
                                choice_list.append(word_ID_pick_left)
                                
                                break
                    
                    setts_list[back - 1][1] = word_ID_pick_left
                else: break
            for front in range(cat_start + 1, len(setts) - 1, 1):
                fron_part_id = setts_list[front - 1][1]
                if fron_part_id != 'False' and fron_part_id != None:
                    links_front = baseTools.take_links(base, fron_part_id)
                    for _ in range(len(links_front) * 5):
                        word_ID_pick_right = pick_side_part(setts[front -1], links_front)
                        if word_ID_pick_right != 'False':
                            if not word_ID_pick_right in choice_list:
                                choice_list.append(word_ID_pick_right)
                                break
                    setts_list[front + 1][1] = word_ID_pick_right
                else: break
        if cat_start == 0:
            top_part = setts_list[cat_start][1]
            words_link = baseTools.take_links(base, top_part)
            for _ in range(len(words_link) * 5):
                word_ID_pick_right = pick_side_part(setts[cat_start + 1], words_link)
                if word_ID_pick_right != 'False':
                    if not word_ID_pick_right in choice_list:
                        choice_list.append(word_ID_pick_right)
                        break
            setts_list[cat_start + 1][1] = word_ID_pick_right
            for front in range(cat_start + 1, len(setts) - 1, 1):
                fron_part_id = setts_list[front - 1][1]
                if fron_part_id != 'False' and fron_part_id != None:
                    links_front = baseTools.take_links(base, fron_part_id)
                    for _ in range(len(links_front) * 5):
                        word_ID_pick_right = pick_side_part(setts[front  + 1], links_front)
                        if word_ID_pick_right != 'False':
                            if not word_ID_pick_right in choice_list:
                                choice_list.append(word_ID_pick_right)
                                
                                break
                    setts_list[front + 1][1] = word_ID_pick_right
                else: break
        if cat_start == len(setts_list) -1:
            top_part = setts_list[cat_start][1]
            words_link = baseTools.take_links(base, top_part)
            for _ in range(len(words_link) * 5):
                word_ID_pick_left = pick_side_part(setts[cat_start - 1], words_link)
                if word_ID_pick_left != 'False':
                    if not word_ID_pick_left in choice_list:
                        choice_list.append(word_ID_pick_left)
                        
                        break
            setts_list[cat_start - 1][1] = word_ID_pick_left
            for back in range(cat_start -1, 0, -1):
                fron_part_id = setts_list[back + 1][1]
                if fron_part_id != 'False' and fron_part_id != None:
                    links_front = baseTools.take_links(base, fron_part_id)
                    for _ in range(len(links_front) * 5):
                        word_ID_pick_left = pick_side_part(setts[back -1], links_front)
                        if word_ID_pick_left != 'False':
                            if not word_ID_pick_left in choice_list:
                                choice_list.append(word_ID_pick_left)
                                
                                break
                    setts_list[back - 1][1] = word_ID_pick_left
                else: break
        # print(choice_list)
    final_list = []
    for ex in setts_list:
        if ex[1] != 'False' and ex[1] != None:
            if not ex[1] in final_list:
                final_list.append(ex[1]) 

    final_string = ''
    # print(setts_list)
    for ex in final_list:
        if ex != 'False' and ex != None:
            final_string += f'{baseTools.take_word(base, ex)} '
    final_string = final_string[:len(final_string) -1]

    return final_string

def check_list_to_list(item_list, checking_list):
    on_the_list = False
    for item in item_list:
        if item in checking_list:
            on_the_list = True
    return on_the_list

def sentens_generator_AI(base, sentens):
    'znajduje słowa w konkretnym przypadku w zdaniach i łączy dwa zdania ze sobą'
    'nie działa dobrze bo gada głupoty'
    sentens = action.string_cleaner(sentens)
    sentens_list = sentens.split(' ')
    PO_DO = []
    final_set = set()
    wor_dict = {}
    for word in sentens_list:
        word_ids = checkerBaseOperators.find_pharse_in_part(base, word)
        wor_dict[word] = []
        wor_dict[word] += word_ids
        for wi in word_ids:
            if wi.startswith('PO') or wi.startswith('DO') or wi.startswith('OR')\
                or wi.startswith('PR') or wi.startswith('OK') or wi.startswith('OZ'):
                PO_DO.append(wi)

    se_LIST = []
    mem_dict = {}
    for p in PO_DO:
        gener = generator_AI_most_popular(base, p, 3, 'HW')
        gs = gener['STRING']
        final_set.add(gs)
        se_LIST.append(gener['ID'])
        mem_dict[gs] = gener['ID']

    export_list = []
    for gen in final_set:
        se_SET = set()
        for x in checkerBaseOperators.searcher_phrase(base, gen):
            se_SET.add(x)
        if len(se_SET) > 1:
            sides = []
            se_left = set()
            se_right= set()
            for se_i in se_SET:
                se_words = baseTools.take_se(base, se_i)
                for sl in se_words:
                    for se_l in se_LIST:
                        if sl == se_l[0]:
                            se_left.add(se_i)
                            sides += [se_l[0]]
                        if sl == se_l[len(se_l) - 1]:
                            se_right.add(se_i)
                            sides += [se_l[len(se_l) - 1]]

            l_len = len(se_left)
            r_len = len(se_right)
            if l_len > 0 and r_len > 0:
                se_le = se_left.intersection(se_right)
                se_ri = se_right.intersection(se_left)
                if len(se_ri) == 0: se_ri = se_le
                counter_left = 0
                sentens_left = None
                for ssl in se_le:
                    left_len = len(ssl)
                    if left_len > counter_left:
                        sentens_left = ssl
                # print('przed', sentens_left, se_ri)
                if len(se_ri) > 0 and sentens_left != None:
                    se_ri.remove(sentens_left)
                if len(se_ri) == 0:
                    se_ri = se_le
                # print('po', sentens_left, se_ri)
                counter_right = 0
                sentens_right = None
                for ssr in se_ri:
                    right_len = len(ssr)
                    if right_len > counter_right:
                        sentens_right = ssr
                if sentens_left != None and sentens_right != None:
                    left_word_id = mem_dict[gen][0]
                    right_word_id = mem_dict[gen][len(mem_dict[gen]) -1]
                    left_sentens_ids = baseTools.take_se(base, sentens_left)
                    right_sentens_ids = baseTools.take_se(base, sentens_right)

                    if left_word_id in left_sentens_ids:
                        left_sentens_ids = left_sentens_ids[:left_sentens_ids.index(left_word_id)]
                    else: left_sentens_ids = []
                    if right_word_id in right_sentens_ids:
                        right_sentens_ids = right_sentens_ids[right_sentens_ids.index(right_word_id) + 1:]
                    else: right_sentens_ids = []
                    ready_list = left_sentens_ids + mem_dict[gen] + right_sentens_ids
                    ready_string = ''
                    for wo in ready_list:
                        ready_string += f'{baseTools.take_word(base, wo)} '
                    exp = ready_string[:len(ready_string) - 1].capitalize() + '.'
                    export_list.append(exp)

    return {
        'LIST' : export_list, 
        'DICT-ID' : mem_dict, 
        'SENTENS' : sentens, 
        'WORDS' : wor_dict, 
    }

if __name__ == '__main__':
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(sentens_generator_AI(base, 'łączy dwa zdania ze sobą'))
    