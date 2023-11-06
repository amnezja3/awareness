import SAver
import json
from tqdm import tqdm
import os
import signal
def restore_keys_to_int(data_from_json):
    restored_data = {}
    for key, value in data_from_json.items():
        restored_key = int(key)
        restored_data[restored_key] = value
    return restored_data

def take_base(file_name='base'):
    base = {
        'BASE': file_name,
        'PO': {},
        'PR': {},
        'OR': {},
        'DO': {},
        'OK': {},
        'VO': {},
        'OZ': {},
        'ZA': {},
        'LB': {},
        'HW': {},
        'SE': {},
        'SA': {},
        'RE': {},
        'LID': 0,
    }

    try:
        with tqdm(total=100, desc="Loading Base") as pbar:
            full_base_loaded = {}
            progress = 0
            for key in base.keys():
                with open(f'./base/{key}{file_name}.json', 'r', encoding='UTF-8') as file:
                    progress += 5
                    pbar.update(progress)
                    open_base_part = json.load(file)
                full_base_loaded[key] = open_base_part
            pbar.update(progress)
            SE = restore_keys_to_int(full_base_loaded['SE'])
            pbar.update(progress + 10)
            SA = restore_keys_to_int(full_base_loaded['SA'])
            pbar.update(progress + 10)
            try: RE = restore_keys_to_int(full_base_loaded['RE'])
            except KeyError: RE = {}
            full_base_loaded['SE'] = SE
            pbar.update(70)
            full_base_loaded['SA'] = SA
            pbar.update(84)
            full_base_loaded['RE'] = RE
            pbar.update(100)
            return full_base_loaded
    except FileNotFoundError:
        return base

def save_base(base):
    base_name = base['BASE']
    base_labels = [
        'BASE','PO', 'PR', 'OR', 'DO',
        'OK', 'VO', 'OZ', 'ZA', 'LB',
        'HW', 'SE', 'SA', 'RE', 'LID',
        ]

    signal.signal(signal.SIGINT, signal.SIG_IGN) # tutaj niech wyłączy CTRL+C
    os.system('color 4E')
    for label in base_labels:
        base_part = base[label]
        with open(f'./base/{label}{base_name}.json', 'w', encoding='UTF-8') as file:
            json.dump(base_part, file, indent=0)
    print(f'Baza została zapisana w plików {base_name}')
    os.system('color 07')
    signal.signal(signal.SIGINT, signal.SIG_DFL) # tutaj niech włączy CTRL+C
    return True



def take_base3(file_name='base'):
    base = {
        'BASE': file_name,
        'PO': {},
        'PR': {},
        'OR': {},
        'DO': {},
        'OK': {},
        'VO': {},
        'OZ': {},
        'ZA': {},
        'LB': {},
        'HW': {},
        'SE': {},
        'SA': {},
        'LID': 0,
    }

    try:
        with tqdm(total=100, desc="Loading Base") as pbar:
            with open(f'{file_name}.json', 'r', encoding='UTF-8') as file:
                pbar.update(10)
                open_base = json.load(file)
                pbar.update(34)
                SE = restore_keys_to_int(open_base['SE'])
                pbar.update(45)
                SA = restore_keys_to_int(open_base['SA'])
                pbar.update(60)
                try: RE = restore_keys_to_int(open_base['RE'])
                except KeyError: RE = {}
                open_base['SE'] = SE
                pbar.update(70)
                open_base['SA'] = SA
                pbar.update(84)
                open_base['RE'] = RE
                pbar.update(100)
                return open_base
    except FileNotFoundError:
        return base

def save_base3(base):
    base_name = base['BASE']

    signal.signal(signal.SIGINT, signal.SIG_IGN) # tutaj niech wyłączy CTRL+C
    os.system('color 4E')
    with open(f'{base_name}.json', 'w', encoding='UTF-8') as file:
        json.dump(base, file, indent=0)
    print(f'Baza została zapisana w pliku {base_name}')
    os.system('color 07')
    signal.signal(signal.SIGINT, signal.SIG_DFL) # tutaj niech włączy CTRL+C
    return True

def take_base_saver(file_name = 'base'):
    base = {'BASE' : file_name,
     'PO' : {},
     'PR' : {},
     'OR' : {},
     'DO' : {},
     'OK' : {},
     'VO' : {},
     'OZ' : {},
     'ZA' : {},
     'LB' : {},
     'HW' : {},
     'SE' : {},
     'SA' : {},
     'LID' : 0,
    }
    open_base = SAver.open_ver(file_name, 'base')
    if open_base == False:
        return base
    else:
        return open_base

def save_base_saver(base):
    base_name = base['BASE']
    SAver.save_ver(base_name, 'base', base)
    print(f'baza została zapisana w pliku {base_name}')
    return True

def take_base_json(file_name='base'):
    base = {
        'BASE': file_name,
        'PO': {},
        'PR': {},
        'OR': {},
        'DO': {},
        'OK': {},
        'VO': {},
        'OZ': {},
        'ZA': {},
        'LB': {},
        'HW': {},
        'SE': {},
        'SA': {},
        'LID': 0,
    }
    try:
        with open(f'{file_name}.json', 'r', encoding='UTF-8') as file:
            open_base = json.load(file)
            SE = restore_keys_to_int(open_base['SE'])
            SA = restore_keys_to_int(open_base['SA'])
            open_base['SE'] = SE
            open_base['SA'] = SA
            return open_base
    except FileNotFoundError:
        return base

def save_base_json(base):
    base_name = base['BASE']
    with open(f'{base_name}.json', 'w', encoding='UTF-8') as file:
        json.dump(base, file, indent=4)
    print(f'Baza została zapisana w pliku {base_name}')
    return True


if __name__ == '__main__':
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    # awareness.save_base(base)
