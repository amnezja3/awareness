import partSpeech
import wordProcessing as wp
import clearLists
import changerBlade

def take_target(w, target='czasownik'):
    with open(f'./odm.neural', 'r', encoding='utf-8') as userFile:
        firle_word = userFile.readlines()
    
    new_contenet = []
    for all in firle_word:
        al = all.strip().split(', ')
        new_contenet.append(al)
    for a5 in new_contenet:
        x = w.upper()
        x1 = x[0].lower() + x[1:]
        y = w.capitalize()
        z = w.lower()
        # print(w, x, x1, y, z, a)
        if w in a5 or x in a5 or x1 in a5 or y in a5 or z in a5:
            pc = partSpeech.part_speach(a5[0])
            # print(pc)
            pc_true = False
            for l_pc in pc:
                if not pc_true:
                    pc_true = changerBlade.check_v_list(l_pc, target, 'True')
                else:
                    break
            if pc_true:
                return a5
            else:
                return ['a','b']
    return ['a','b']


target_dict_segregation = wp.target_dict_segregation
target_dict_words = wp.target_dict_words

def take_superTarget(base, word, target='czasownik', what='WORDS-LISTS'):
    if what == 'MAIN-WORDS':
        x = word.lower()
        if len(x) > 1: x1 = x[0].lower() + x[1:]
        elif x != '': x1 = x[0]
        else:return False
        y = word.capitalize()
        z = word.upper()
        possible_options = [x, x1, y, z]
        for po in possible_options:
            try:
                return target_dict_words[po]
            except KeyError:
                continue
        return False
    elif what == 'WORDS-LISTS':
        try:
            x = word.lower()
            if len(x) > 1: x1 = x[0].lower() + x[1:]
            elif x != '': x1 = x[0]
            else:return ['a','b']
            y = word.capitalize()
            z = word.upper()
            possible_options = [x, x1, y, z]
            # print(possible_options)
            for po in possible_options:
                altA5 = False
                for a5 in target_dict_words[po]:
                    try:
                        case = base['LB'][a5]['KIND']['PART']
                        if case == target:
                            pc = [(case, a5)]
                            altA5 = a5
                            break
                        else:
                            pc = partSpeech.part_speach(a5)
                            altA5 = a5
                        # break
                    except KeyError:
                        pc = partSpeech.part_speach(a5)
                pc_true = False
                for l_pc in pc:
                    if not pc_true:
                        pc_true = changerBlade.check_v_list(l_pc, target, 'True')
                    else:
                        break
                if pc_true and altA5:
                    if altA5 not in target_dict_segregation[altA5]:
                        ready_target = [altA5] + target_dict_segregation[altA5]
                        return ready_target
                    try:
                        new_tds = target_dict_segregation[altA5]
                        index_a5 = new_tds.index(altA5)
                        new_tds.pop(index_a5)
                    except ValueError:
                        new_tds = target_dict_segregation[altA5]
                        ready_target = [altA5] + new_tds
                        return ready_target
                else:
                    return ['a','b']
        except KeyError:
            return ['a','b']

if __name__ == '__main__':
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(take_superTarget(base, 'rowerem', 'rzeczownik', what='MAIN-WORDS'))
    print(take_superTarget(base, 'rower', 'rzeczownik', what='WORDS-LISTS'))