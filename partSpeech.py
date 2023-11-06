import chanerCases
import json
import wordProcessing as wp
import os
import signal

target_dict_segregation = wp.target_dict_segregation
target_dict_words = wp.target_dict_words

def part_speach(word, option = True, multi = 'main'):
    with open(f'word_cases.json', 'r', encoding='UTF-8') as file:
        wird_dict = json.load(file)
    # wird_dict = a.open_ver('word_cases', 'wird_dict')
    if not wird_dict: wird_dict = {}
    try:
        wird_dict[word]
        word_exist = True
    except KeyError:
        wird_dict[word] = []
        word_exist = False
    if not word_exist and option:
        main_words = []
        word_upper = word.upper()
        first_le_small = word_upper[0].lower() + word[1:]
        word_cap = word.capitalize()
        word_lower = word.lower()
        possible_options = [word_lower, word_cap, first_le_small, word_upper]
        for po in possible_options:
            try:
                main_words = target_dict_words[po]
            except KeyError:
                continue
        exp = []
        if len(main_words) > 0:
            for m in main_words:
                easy_c = chanerCases.part_check(m, multi)
                if easy_c != None and easy_c != 'przymiotnik':
                    exp.append((easy_c , m))
                elif easy_c != None and easy_c == 'przymiotnik':
                    easy_p = chanerCases.part_check(word, multi)
                    if easy_p != None and easy_p == 'przymiotnik':
                        exp.append((easy_p , m))
                    elif easy_p != None and easy_p == 'przysłówek':
                        exp.append((easy_p , word))
                    else:
                        exp.append((easy_c , m))
                else:
                    exp.append(('onim' , m))
            for e in exp:
                wird_dict[word].append(e)
        else:
            wird_dict[word].append(('onim', word))
        signal.signal(signal.SIGINT, signal.SIG_IGN) # tutaj niech wyłączy CTRL+C
        os.system('color 4E')
        with open(f'word_cases.json', 'w+', encoding='UTF-8') as file:
            json.dump(wird_dict, file, indent=4)
        os.system('color 07')
        signal.signal(signal.SIGINT, signal.SIG_DFL) # tutaj niech włączy CTRL+C
        # a.save_ver('word_cases', 'wird_dict', wird_dict)
    return wird_dict[word]

if __name__ == '__main__':
    import awareness
    print(part_speach('samochód'))