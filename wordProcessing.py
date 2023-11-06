import clearLists
from tqdm import tqdm
with open(f'./odm.neural', 'r', encoding='utf-8') as userFile:
    words_Content = userFile.readlines()

new_contenet = []
for x_w in words_Content:
    x_w_S = x_w.strip().split(', ') 
    new_contenet.append(x_w_S)

target_dict_segregation = {}
for n_c_list in tqdm(new_contenet, desc=f"Words processing progress: ", leave=False):
    nc = n_c_list[0]
    try:
        target_dict_segregation[nc]
        target_dict_segregation[nc] = target_dict_segregation[nc] + n_c_list
        target_dict_segregation[nc] = clearLists.clear_lists(target_dict_segregation[nc])
    except KeyError:
        target_dict_segregation[nc] = n_c_list

target_dict_words = {}
for n_c_list in tqdm(new_contenet, desc=f"Words processing progress: ", leave=True):
    for nc in n_c_list:
        try:
            target_dict_words[nc]
            target_dict_words[nc].append(n_c_list[0])
            target_dict_words[nc] = clearLists.clear_lists(target_dict_words[nc])
        except KeyError:
            target_dict_words[nc] = []
            target_dict_words[nc].append(n_c_list[0])