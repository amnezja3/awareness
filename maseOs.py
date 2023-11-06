import takeTarget
import verbFlex
import baseTools
def make_OS(base, se_id, oso = 'Ios-LP-NDKTER-DKPRZY', frend = 'PR', main = 'PO', neubor = 'ZAI'):
    def pick_verb_target(w):
        import random
        if w.startswith('nie '):
            w = w.replace('nie ', '')
        bez = takeTarget.take_target(w)[0]
        selected_list = []
        for k, v in verbFlex.set_gr('a', True)[bez].items():
            if k.startswith(oso):
                selected_list.append(k)
        if len(selected_list) > 0:
            return random.choice(selected_list)
        else:
            return 'CAN-NOT-TO-BE'

    se_list = baseTools.take_se(base, se_id)
    counter_OR = 0
    new_sentens = []
    se_item_OR = ''
    for se_item in se_list:
        take_verb_word = verbFlex.verb_flex(baseTools.take_word(base, se_item), 'TAKE')
        if take_verb_word == None: take_verb_word = 'NOT_VERB'
        if se_item.startswith('OR') and not take_verb_word.startswith('BEZOKOLICZNIK-NONE-NONE-NONE-NONE'):
            counter_OR += 1
            new_sentens.append('HERE')
            se_item_OR = se_item
        if se_item.startswith('OR') and take_verb_word.startswith('BEZOKOLICZNIK-NONE-NONE-NONE-NONE'):
            new_sentens.append(se_item)
        if not se_item.startswith(frend) and not se_item.startswith(main) and not se_item.startswith(neubor) and not se_item.startswith('OR'):
            new_sentens.append(se_item)

    if counter_OR == 1:
        word_or = baseTools.take_word(base, se_item_OR)

        new_verb_IOS = pick_verb_target(word_or)

        if new_verb_IOS != 'CAN-NOT-TO-BE':
            changed_word = verbFlex.verb_flex(word_or, 'CHANGE', new_verb_IOS)
            base = baseTools.add_word(base, 'OR', changed_word)
            changed_word_ID = baseTools.take_id(base, 'OR', changed_word)
            complete_list_id = []
            for w_id in new_sentens:
                if w_id == 'HERE':
                    complete_list_id.append(changed_word_ID)
                else:
                    complete_list_id.append(w_id)
            final_string = ''
            for word_str in complete_list_id:
                word_string = baseTools.take_word(base, word_str)
                final_string += f'{word_string} '
            final_string = final_string[:len(final_string) -1]
            return final_string

    else: return 'CAN-NOT-TO-BE'
