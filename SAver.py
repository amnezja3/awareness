import os
import importlib.util

def isnotkeyword(sector_name):
    not_allow_sectors = [
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
        'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with',
        'yield'
    ]
    if str(sector_name) in not_allow_sectors: return False
    else: return True

def isimportin(import_name):
    folder_path = f'./saver_memories/'
    file_list = os.listdir(folder_path)
    if f'{import_name}.py' in file_list:
        return True
    else:
        return False

def isvartrue(ver):
    if isinstance(ver, str):
        return 'STR'
    elif isinstance(ver, list):
        return 'LIS'
    elif isinstance(ver, dict):
        return 'DIC'
    elif isinstance(ver, set):
        return 'SET'
    elif isinstance(ver, int):
        return 'INT'
    elif isinstance(ver, float):
        return 'FLT'
    elif isinstance(ver, bool):
        return 'BOOL'
    elif isinstance(ver, type):
        return 'CLA'
    else:
        return 'OBJ'

def open_ver(import_name, sector_name):
    if isimportin(import_name) and \
        sector_name in [x for x in open_all(import_name, True).keys()] and \
            isnotkeyword(sector_name):
        # print(f'Projekt {import_name} istnieje!')
        module_name = f'dynamiczny_modul_{import_name}'
        module_spec = importlib.util.spec_from_loader(module_name, loader=None)
        module = importlib.util.module_from_spec(module_spec)
        with open(f'./saver_memories/{import_name}.py', 'r', encoding='UTF-8') as file:
            code = file.read()
        exec(code, module.__dict__)
        function = getattr(module, sector_name)
        return function()
    else:
        # print(f'Projekt {import_name} lub zmienna {sector_name} nie istnieje!')
        return False
    
def open_all(import_name, silence = False):
    if isimportin(import_name):
        if not silence:
            print(f'Projekt {import_name} istnieje!\nWszystkie zmienne zostały zwrócone w formie słownika.')
        with open(f'./saver_memories/{import_name}.py', 'r', encoding='UTF-8') as file:
            secotores_all = file.readlines()
        saved_vers = []
        for sector in secotores_all:
            if sector.count('def ') == 1 and sector.count('():') == 1:
                sector_n = sector.strip().split('():')[0].split(' ')[1]
                saved_vers.append(sector_n)
        full_saved_ver = {}
        for sv in saved_vers:
            module_name = f'dynamiczny_modul_{import_name}'
            module_spec = importlib.util.spec_from_loader(module_name, loader=None)
            module = importlib.util.module_from_spec(module_spec)
            code = ''.join(secotores_all)
            exec(code, module.__dict__)
            function = getattr(module, sv)
            full_saved_ver[sv] = function()
        return full_saved_ver
    else:
        # print(f'Projekt {import_name} nie istnieje!')
        return False

def save_ver(import_name, sector_name, ver):
    if isnotkeyword(sector_name):
        if isimportin(import_name) and isvartrue(ver) != 'CLA' and isvartrue(ver) != 'OBJ':
            # print(f'Projekt {import_name} istniał')
            with open(f'./saver_memories/{import_name}.py', 'r', encoding='UTF-8') as file:
                secotores_all = file.readlines()
            if isvartrue(ver) == 'STR':
                ver = f'"""{ver}"""'
            saved_vers = []
            for sector in secotores_all:
                if sector.count('def ') == 1 and sector.count('():') == 1:
                    sector_n = sector.strip().split('():')[0].split(' ')[1]
                    saved_vers.append(sector_n)
            if sector_name in saved_vers:
                full_saved_ver = {}
                for sv in saved_vers:
                    if sector_name == sv:
                        full_saved_ver[sv] = ver
                    else:
                        module_name = f'dynamiczny_modul_{import_name}'
                        module_spec = importlib.util.spec_from_loader(module_name, loader=None)
                        module = importlib.util.module_from_spec(module_spec)
                        code = ''.join(secotores_all)
                        exec(code, module.__dict__)
                        function = getattr(module, sv)
                        full_saved_ver[sv] = function()
                preparing_save = ''
                for key, val in full_saved_ver.items():
                    template = f'def {key}():\n\tver = {val}\n\treturn ver'
                    preparing_save += f'\n\n{template}'
                with open(f'./saver_memories/{import_name}.py', 'w+', encoding='UTF-8') as file:
                    file.write(preparing_save)
                return True
            elif isvartrue(ver) == 'CLA' or isvartrue(ver) == 'OBJ':
                print(f'Te typy zmiennych nie są obsługiwane !')
                return False
            else:
                # print(f'W projekcie {import_name} nie istnieje zmienna {sector_name}!')
                full_saved_ver = {}
                for sv in saved_vers:
                    module_name = f'dynamiczny_modul_{import_name}'
                    module_spec = importlib.util.spec_from_loader(module_name, loader=None)
                    module = importlib.util.module_from_spec(module_spec)
                    code = ''.join(secotores_all)
                    exec(code, module.__dict__)
                    function = getattr(module, sv)
                    full_saved_ver[sv] = function()
                full_saved_ver[sector_name] = ver

                preparing_save = ''
                for key, val in full_saved_ver.items():
                    template = f'def {key}():\n\tver = {val}\n\treturn ver'
                    preparing_save += f'\n\n{template}'
                with open(f'./saver_memories/{import_name}.py', 'w+', encoding='UTF-8') as file:
                    file.write(preparing_save)
                return True
        else:
            # print(f'Projekt {import_name} nie istnieje!')
            template = f'def {sector_name}():\n\tver = {ver}\n\treturn ver'
            with open(f'./saver_memories/{import_name}.py', 'w+', encoding='UTF-8') as file:
                file.write(template)
            return True
    else:
        return False

def delete_ver(import_name, sector_name):
    if isimportin(import_name):
        # print(f'Projekt {import_name} istnieje!')
        with open(f'./saver_memories/{import_name}.py', 'r', encoding='UTF-8') as file:
            secotores_all = file.readlines()
        saved_vers = []
        for sector in secotores_all:
            if sector.count('def ') == 1 and sector.count('():') == 1:
                sector_n = sector.strip().split('():')[0].split(' ')[1]
                saved_vers.append(sector_n)
        if sector_name in saved_vers:
            full_saved_ver = {}
            for sv in saved_vers:
                module_name = f'dynamiczny_modul_{import_name}'
                module_spec = importlib.util.spec_from_loader(module_name, loader=None)
                module = importlib.util.module_from_spec(module_spec)
                code = ''.join(secotores_all)
                exec(code, module.__dict__)
                function = getattr(module, sv)
                full_saved_ver[sv] = function()
            del full_saved_ver[sector_name]
            preparing_save = ''
            for key, val in full_saved_ver.items():
                template = f'def {key}():\n\tver = {val}\n\treturn ver'
                preparing_save += f'\n\n{template}'
            with open(f'./saver_memories/{import_name}.py', 'w+', encoding='UTF-8') as file:
                file.write(preparing_save)
            return True
        else:
            # print(f'W projekcie {import_name} nie istnieje zmienna {sector_name}!')
            return False
    else:
        # print(f'Projekt {import_name} nie istnieje!')
        return False

def delete_project(import_name):
    if isimportin(import_name):
        input_str = input(f'Czy napewno chcesz usunąć projekt {import_name}? (Y/n)')
        if input_str == 'Y':
            file_path = f'./saver_memories/{import_name}.py'
            try:
                os.remove(file_path)
                print(f"Plik projektu {import_name} został usunięty.")
                return True
            except OSError as e:
                print(f"Nie można usunąć pliku {import_name}: {e}")
                return False
        else:
            print(f'Usuwanie projektu {import_name} zostało anulowane!')
            return False
if __name__ == '__main__':
    import awareness
    print(delete_ver('project_Name', 'ver'))