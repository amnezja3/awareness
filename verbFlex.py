import takeTarget
import os
import signal

def set_gr(base, w, option=None):
    with open(f'spec_verbs.neural', 'r', encoding='utf-8') as userFile:
        firle_word = userFile.readlines()
    spec_verbs = {}
    for all in firle_word:
        al = all.strip().replace(' ', '').split('$')
        spec_verbs[al[0]] = {}
        for dl in al[1].strip().split(','):
            d = dl.split(':')
            spec_verbs[al[0]][d[0]] = d[1]

    if option != None:
        return spec_verbs

    target_list = takeTarget.take_superTarget(base, w)
    gr_tf = {
        'I' : {'True' : 'ać', 'False' : ['ować', 'ywać', 'iwać'], 'Dif' : ['asz', ['ę']]},
        'II' : {'True' : 'eć', 'False' : [], 'Dif' : ['em', ['ałem', 'niem']]},
        'III' : {'True' : 'eć', 'False' : [], 'Dif' : ['eję', []]},
        'IV' : {'True' : 'ować', 'False' : [], 'Dif' : ['uję', []]},
        'VA' : {'True' : 'nąć', 'False' : [], 'Dif' : ['nięci', []]},
        'VB' : {'True' : 'nąć', 'False' : [], 'Dif' : ['ń' , []]},
        'VC' : {'True' : 'nąć', 'False' : [], 'Dif' : ['ąc', []]},
        'VIA' : {'True' : 'ć', 'False' : ['ać', 'eć', 'ąć', 'yć'], 'Dif' : ['isz', []]},
        'VIB' : {'True' : 'yć', 'False' : [], 'Dif' : ['ysz', []]},
        'VIIA' : {'True' : 'eć', 'False' : [], 'Dif' : ['imy', []]},
        'VIIB' : {'True' : 'eć', 'False' : [], 'Dif' : ['yszy', []]},
        'VIIIA' : {'True' : 'ywać', 'False' : [], 'Dif' : ['ywany', []]},
        'VIIIB' : {'True' : 'iwać', 'False' : [], 'Dif' : ['iwał', []]},
        'IX' : {'True' : 'ać', 'False' : ['ować', 'ywać', 'iwać'], 'Dif' : ['ę', []]},
        'XA' : {'True' : 'ć', 'False' : ['ać', 'eć', 'ąć', 'yć'], 'Dif' : ['jesz', []]},
        'XB' : {'True' : 'ąć', 'False' : ['nąć'], 'Dif' : ['mę', []]},
        'XC' : {'True' : 'ąć', 'False' : ['nąć'], 'Dif' : ['nę', []]},
        'XIA' : {'True' : 'c', 'False' : [], 'Dif' : ['eni', []]},
        'XIB' : {'True' : 'ć', 'False' : ['ać', 'eć', 'ąć', 'yć'], 'Dif' : ['łszy', []]},
    }

    b = target_list[0]
    try:
        spec_verbs[b]
        sv_false = True
    except KeyError:
        sv_false = False
    if sv_false:
        return 'spec'
    else:
        for k,v in gr_tf.items():
            # print(v['True'])
            main_end_true = b.endswith(v['True'])
            main_end_false = False

            for x in v['False']:
                # print(x)p;
                if b.endswith(x):
                    main_end_false = True

            # print(main_end_true, main_end_false)
            if main_end_true and not main_end_false:
                for t in target_list:
                    main_dif_false = False
                    for x in v['Dif'][1]:
                        if t.endswith(x):
                            main_dif_false = True
                    if t.endswith(v['Dif'][0]) and not main_dif_false:
                        # print(t, v['Dif'][0], x)
                        return k
            
        return 'spec-none'

def verb_flex(base, w, option='TAKE', mode = None):
    # print(option, mode)
    negative_verb = False
    if w.startswith('nie '):
        w = w.split(' ')[1]
        negative_verb = True
    # print(w)
    target = takeTarget.take_superTarget(base, w)
    # print(target)
    if target != ['a', 'b']:
        bez = target[0]

        grupy_fleksyjne = {
            'I' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['ać', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['am', ['ałam']],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['asz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['a', ['ąca', 'ała', 'ana', 'nia', ]],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['amy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['acie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ają', []],
                            'Ios-LM-NDKTER-ROZ-NONE' : ['aj', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['ajmy', []],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['ajcie', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ał', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['ała', []],

                            'NONE-LP-NONE-PRZE-N' : ['ało', []],

                            'NONE-LM-NONE-PRZE-M' : ['ali', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['ały', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],

                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['any', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['nego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['emu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['anym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['ana', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['nej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-MIE-BIERNY-M' : ['nych', []],

                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['any', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ana', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['ani', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['ano', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['anie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ałam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ałaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ałem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ałeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['ania', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ani', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['ań', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ań',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nymi', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ani', []],
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['aną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['nymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['nemu', []],

                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['anym', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_1'  : ['nemu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_2'  : ['anej', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_4'  : ['anego', []],

            },
            'II' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['eć', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['em', ['niem', 'łem']],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['esz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['e', ['ące', 'ała', 'ane', 'nie', 'cie', 'że']],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['emy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['ecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['eją', []],
                            'Ios-LM-NDKTER-ROZ-NONE' : ['ej', ['nej', 'cej']],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['ejmy', []],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['ejcie', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ał', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['ała', []],

                            'NONE-LP-NONE-PRZE-N' : ['ało', []],

                            'NONE-LM-NONE-PRZE-M' : ['eli', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['ały', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['any', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['nego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['cemu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['anym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['ana', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['nej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-MIE-BIERNY-M' : ['nych', []],

                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['any', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ana', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['ani', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['ano', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['enie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ałam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ałaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ałem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ałeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['enia', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ani', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['eń', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eń',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['enie', []],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ani', []],                        
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['aną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['nymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['nemu', []],

                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['anym', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['nymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_1'  : ['nemu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_2'  : ['anej', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_4'  : ['anego', []],
            },
            'III' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['eć', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['eję', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['ejesz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['eje', []],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['ejemy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['ejecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['eją', []],
                            'Ios-LM-NDKTER-ROZ-NONE' : ['ej', ['nej', 'cej']],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['ejmy', []],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['ejcie', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ał', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['ała', []],

                            'NONE-LP-NONE-PRZE-N' : ['ało', []],

                            'NONE-LM-NONE-PRZE-M' : ['eli', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['ały', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            # 'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            # 'IMIESŁÓW-LP-MIA-BIERNY-M' : ['any', []],
                            # 'IMIESŁÓW-LP-DOP-BIERNY-M' : ['nego', []],
                            # 'IMIESŁÓW-LP-CEL-BIERNY-M' : ['cemu', []],
                            # 'IMIESŁÓW-LP-NAR-BIERNY-M' : ['anym', []],

                            # 'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['ana', []],
                            # 'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['nej', []],

                            # 'IMIESŁÓW-LP-MIA-BIERNY-N' : ['ane', []],

                            # 'IMIESŁÓW-LM-MIE-BIERNY-M' : ['nych', []],

                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['any', []],
                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ana', []],
                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['ane', []],

                            # 'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['ani', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['ano', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['enie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ałam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ałaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ałem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ałeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['enia', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ni', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['eń', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eń',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['enie', []],
                            # 'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            # 'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ani', []],                        
                            # 'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['aną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['nymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['nemu', []],

                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['anym', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['nymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_1'  : ['nemu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_2'  : ['anej', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_4'  : ['anego', []],
            },
            'IV' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['ować', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['uję', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['ujesz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['uje', []],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['ujemy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['ujecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ują', []],
                            'Ios-LM-NDKTER-ROZ-NONE' : ['uj', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['ujmy', []],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['ujcie', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ał', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['ała', []],

                            'NONE-LP-NONE-PRZE-N' : ['ało', []],

                            'NONE-LM-NONE-PRZE-M' : ['ali', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['ały', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            # 'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            # 'IMIESŁÓW-LP-MIA-BIERNY-M' : ['any', []],
                            # 'IMIESŁÓW-LP-DOP-BIERNY-M' : ['nego', []],
                            # 'IMIESŁÓW-LP-CEL-BIERNY-M' : ['cemu', []],
                            # 'IMIESŁÓW-LP-NAR-BIERNY-M' : ['anym', []],

                            # 'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['ana', []],
                            # 'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['nej', []],

                            # 'IMIESŁÓW-LP-MIA-BIERNY-N' : ['ane', []],

                            # 'IMIESŁÓW-LM-MIE-BIERNY-M' : ['nych', []],

                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['any', []],
                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ana', []],
                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['ane', []],

                            # 'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['ani', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['ano', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['anie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ałam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ałaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ałem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ałeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['ania', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ni', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['ań', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ań',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            # 'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            # 'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ani', []],                        
                            # 'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['aną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []]
            },
            'VA' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['nąć', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['nę', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['niesz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['nie', []],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['niemy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['niecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ną', []],
                            'Ios-LM-NDKTER-ROZ-NONE' : ['nij', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['nijmy', []],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['nijcie', []],

                            # 'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            # 'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            # 'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            # 'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            # 'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            # 'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            # 'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            # 'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            # 'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            # 'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            # 'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['nął', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['nęła', []],

                            'NONE-LP-NONE-PRZE-N' : ['nęło', []],

                            'NONE-LM-NONE-PRZE-M' : ['nęli', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['nęły', []],

                            # 'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            # 'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            # 'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            # 'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['nięty', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['niętego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['niętemu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['niętym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['nięta', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['niętej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['nięte', []],

                            'IMIESŁÓW-LM-MIE-BIERNY-M' : ['niętych', []],

                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['nięty', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['nięta', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['nięte', []],

                            'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['nięci', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['nięto', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['nięcie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ęłam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ęłaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ąłem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ąłeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            # 'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['ania', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ani', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['ań', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            # 'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            # 'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            # 'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            # 'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            # 'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            # 'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            # 'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            # 'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ań',  []],
                            # 'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            # 'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            # 'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            # 'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            # 'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            # # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            # 'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            # 'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ani', []],                        
                            # 'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['aną', []],

                            # 'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            # 'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            # 'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            # 'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            # 'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            # 'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            # 'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            # 'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            # 'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            # 'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['ła', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['ącemu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['ł', ['nął']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_4'  : ['łem', ['ąłem']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_5'  : ['nąc', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_6'  : ['ącymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_7'  : ['łam', ['ęłam']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_8'  : ['ących', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_9'  : ['ące', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_10'  : ['ącej', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_11'  : ['ącą', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_12'  : ['ącymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_13'  : ['ący', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_14'  : ['ącego', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_15'  : ['ącym', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_16'  : ['ły', ['nęły']],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-POZYTYWNY_17'  : ['ęciami', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_18'  : ['li', ['nęli']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_19'  : ['ęcia', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_20'  : ['ęciach', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_21'  : ['nięć', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_22'  : ['ąca', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_23'  : ['łeś', ['ąłeś']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_24'  : ['łaś', ['ęłaś']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_25'  : ['ło', ['ęło']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_26'  : ['ęciom', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_27'  : ['ęciu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_28'  : ['ęciem', []],

                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['ąca', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['ącą', []],
                            

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_1'  : ['ącemu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_2'  : ['ących', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_4'  : ['ącego', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_5'  : ['ącej', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_6'  : ['ącym', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_7'  : ['ącymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_8'  : ['ące', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_9'  : ['ący', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_10'  : ['ęciu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_11'  : ['nięć', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_12'  : ['ęciach', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_13'  : ['ęcia', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_14'  : ['ęciami', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_15'  : ['ęciom', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_16'  : ['ęciem', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_17'  : ['ęcie', []],
                            
            },
            'VB' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['nąć', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['nę', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['niesz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['nie', []],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['niemy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['niecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ną', []],
                            'Ios-LM-NDKTER-ROZ-NONE' : ['ń', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['ńmy', []],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['ńcie', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],
                            
                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['nął', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['nęła', []],

                            'NONE-LP-NONE-PRZE-N' : ['nęło', []],

                            'NONE-LM-NONE-PRZE-M' : ['nęli', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['nęły', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['nięty', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['niętego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['niętemu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['niętym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['nięta', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['niętej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['nięte', []],

                            'IMIESŁÓW-LM-MIE-BIERNY-M' : ['niętych', []],

                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['nięty', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['nięta', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['nięte', []],

                            'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['nięci', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['nięto', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['nięcie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ęłam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ęłaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ąłem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ąłeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            # 'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['ania', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ani', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['ań', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            # 'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            # 'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            # 'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            # 'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            # 'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            # 'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            # 'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            # 'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ań',  []],
                            # 'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            # 'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            # 'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            # 'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            # 'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            # # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            # 'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            # 'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ani', []],                        
                            # 'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['aną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['nięć', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['ętymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['ęć', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_4'  : ['ęciach', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_5'  : ['ęcia', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_6'  : ['nąwszy', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_7'  : ['ętą', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_8'  : ['ęciem', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_9'  : ['ęciom', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_10'  : ['ęciu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_11'  : ['ęciami', []],

                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['nięć', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['ętymi', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_3'  : ['ęć', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_4'  : ['ęciach', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_5'  : ['nąwszy', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_6'  : ['ętą', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_7'  : ['ęciem', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_8'  : ['ęciom', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_9'  : ['ęciu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_10'  : ['ęcie', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_11'  : ['ętego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_12'  : ['ętemu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_13'  : ['ęcia', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_14'  : ['ęci', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_15'  : ['ętych', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_16'  : ['ętym', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_17'  : ['ętej', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_18'  : ['ęciami', []],


            },
            'VC' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['nąć', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['nę', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['niesz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['nie', []],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['niemy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['niecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ną', []],
                            'Ios-LM-NDKTER-ROZ-NONE' : ['nij', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['nijmy', []],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['nijcie', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],
                            
                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['nął', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['nęła', []],

                            'NONE-LP-NONE-PRZE-N' : ['nęło', []],

                            'NONE-LM-NONE-PRZE-M' : ['nęli', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['nęły', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            # 'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            # 'IMIESŁÓW-LP-MIA-BIERNY-M' : ['nięty', []],
                            # 'IMIESŁÓW-LP-DOP-BIERNY-M' : ['niętego', []],
                            # 'IMIESŁÓW-LP-CEL-BIERNY-M' : ['niętemu', []],
                            # 'IMIESŁÓW-LP-NAR-BIERNY-M' : ['niętym', []],

                            # 'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['nięta', []],
                            # 'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['niętej', []],

                            # 'IMIESŁÓW-LP-MIA-BIERNY-N' : ['nięte', []],

                            # 'IMIESŁÓW-LM-MIE-BIERNY-M' : ['niętych', []],

                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['nięty', []],
                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['nięta', []],
                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['nięte', []],

                            # 'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['nięci', []],

                            # 'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['nięto', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['nięcie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ęłam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ęłaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ąłem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ąłeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            # 'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['ania', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ani', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['ań', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            # 'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            # 'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            # 'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            # 'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            # 'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            # 'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            # 'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            # 'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ań',  []],
                            # 'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            # 'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            # 'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            # 'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            # 'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            # # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            # 'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            # 'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ani', []],                        
                            # 'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['aną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['nięć', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['ętymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['ęć', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_4'  : ['ęciach', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_5'  : ['ęcia', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_6'  : ['nąwszy', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_7'  : ['ętą', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_8'  : ['ęciem', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_9'  : ['ęciom', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_10'  : ['ęciu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_11'  : ['ęciami', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_12'  : ['ła', ['nęła']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_13'  : ['ło', ['nęło']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_14'  : ['eś', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_15'  : ['li', ['nęli']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_16'  : ['nięto', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_17'  : ['ąca', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_18'  : ['aś', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_19'  : ['łem', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_20'  : ['ły', ['nęły']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_21'  : ['ł', ['ął']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_22'  : ['am', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_23'  : ['ęcie', []],

                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['nięć', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['ętymi', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_3'  : ['ęć', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_4'  : ['ęciach', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_5'  : ['nąwszy', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_6'  : ['ętą', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_7'  : ['ęciem', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_8'  : ['ęciom', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_9'  : ['ęciu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_10'  : ['ęcie', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_11'  : ['ętego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_12'  : ['ętemu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_13'  : ['ęcia', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_14'  : ['ęci', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_15'  : ['ętych', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_16'  : ['ętym', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_17'  : ['ętej', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_18'  : ['ęciami', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_19'  : ['ęcie', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_20'  : ['ąca', []],

            },
            'VIA' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['ć', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['ę', ['niem', 'łem']],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['isz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['i', ['mi', 'ni', 'ili']],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['imy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['icie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ą', ['ną', 'cą']],
                            'Ios-LM-NDKTER-ROZ-NONE' : [' ', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['my', ['imy', 'śmy']],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['cie', ['icie', 'ście']],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ił', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['iła', []],

                            'NONE-LP-NONE-PRZE-N' : ['iło', []],

                            'NONE-LM-NONE-PRZE-M' : ['ili', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['iły', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['ony', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['nego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['cemu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['onym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['ona', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['nej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['one', []],

                            'IMIESŁÓW-LM-MIE-BIERNY-M' : ['nych', []],

                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['ony', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ona', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['one', []],

                            'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['eni', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['ono', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['enie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ałam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ałaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ałem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ałeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['enia', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['eni', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['eń', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eń',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['enie', []],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eni', []],                        
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['oną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['iłem', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['oną', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['łeś', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_4'  : ['onemu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_5'  : ['iłam', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_6'  : ['nymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_7'  : ['nemu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_8'  : ['łaś', []],
                            


                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['nego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['nymi', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_3'  : ['nej', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_4'  : ['nemu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_5'  : ['onym', []],
                            
            },
            'VIB' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['yć', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['ę', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['ysz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['y', ['cy', 'my', 'by', 'ny', 'ły']],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['ymy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['ycie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ą', ['ną', 'cą']],
                            'Ios-LM-NDKTER-ROZ-NONE' : [' ', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['my', ['imy', 'śmy']],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['cie', ['icie', 'ście']],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ył', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['yła', []],

                            'NONE-LP-NONE-PRZE-N' : ['yło', []],

                            'NONE-LM-NONE-PRZE-M' : ['yli', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['yły', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['ony', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['nego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['cemu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['onym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-ŻN' : ['ona', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['nej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['one', []],
                            
                            
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['ony', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ona', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['one', []],

                            'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['eni', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['ono', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['enie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['yłam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['łaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ałem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ałeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['enia', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['eni', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['eń', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eń',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['enie', []],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eni', []],                        
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['oną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['oną', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['łam', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_4'  : ['łem', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_5'  : ['onemu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_6'  : ['onych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_7'  : ['nymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_8'  : ['łeś', []],

                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['onymi', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['onej', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_3'  : ['onym', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_4'  : ['onemu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_5'  : ['onego', []],
                            

            },
            'VIIA' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['eć', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['ę', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['isz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['i', ['mi', 'eli', 'by', 'ny', 'ły']],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['imy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['icie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ą', ['cą']],
                            'Ios-LM-NDKTER-ROZ-NONE' : [' ', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['my', ['imy', 'śmy']],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['cie', ['icie', 'ście']],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ał', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['ała', []],

                            'NONE-LP-NONE-PRZE-N' : ['ało', []],

                            'NONE-LM-NONE-PRZE-M' : ['eli', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['ały', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['any', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['nego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['cemu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['anym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-ŻN' : ['ana', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['nej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['ane', []],
                            
                            
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['any', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ana', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['ani', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['ano', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['enie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ałam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ałaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ałem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ałeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['enia', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['eni', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['eń', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eń',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['enie', []],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eni', []],                        
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['oną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []]
            },
            'VIIB' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['eć', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['ę', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['zysz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['y', ['cy', 'my', 'by', 'ny', 'ły']],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['ymy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['ycie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ą', ['ną', 'cą']],
                            'Ios-LM-NDKTER-ROZ-NONE' : [' ', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['my', ['imy', 'śmy']],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['cie', ['icie', 'ście']],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ał', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['ała', []],

                            'NONE-LP-NONE-PRZE-N' : ['ało', []],

                            'NONE-LM-NONE-PRZE-M' : ['eli', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['ały', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['any', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['nego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['cemu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['anym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-ŻN' : ['ana', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['nej', []],

                            # 'IMIESŁÓW-LP-MIA-BIERNY-N' : ['one', []],
                            
                            
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['any', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ana', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['ani', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['ano', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['enie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ałam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ałaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ałem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ałeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['enia', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ani', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['eń', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eń',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['enie', []],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eni', []],                        
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['aną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['ane', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['anych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['anymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_4'  : ['anemu', []],

                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['anemu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['anym', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_3'  : ['anej', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_4'  : ['anego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_5'  : ['ani', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_6'  : ['anymi', []],
                            
            },
            'VIIIA' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['ywać', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['uję', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['ujesz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['uje', []],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['ujemy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['ujecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ują', []],
                            'Ios-LM-NDKTER-ROZ-NONE' : ['uj', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['ujmy', []],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['ujcie', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ywał', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['ywała', []],

                            'NONE-LP-NONE-PRZE-N' : ['ywało', []],

                            'NONE-LM-NONE-PRZE-M' : ['ywali', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['ywały', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['ywany', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['ywnego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['cemu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['anym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['ana', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['nej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-MIE-BIERNY-M' : ['nych', []],

                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['any', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ana', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['ani', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['ano', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['anie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ałam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ałaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ałem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ałeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['ania', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ni', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['ań', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            # 'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', ['ywaniu']],
                            'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ań',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ywaniu', []],
                            # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            # 'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ani', []],                        
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['aną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['nego', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['nemu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['nymi', []],


                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['anego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['ani', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_3'  : ['anemu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_4'  : ['anej', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_5'  : ['anymi', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_6'  : ['anym', []],
                            
            },
            'VIIIB' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['iwać', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['uję', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['ujesz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['uje', []],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['ujemy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['ujecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ują', []],
                            'Ios-LM-NDKTER-ROZ-NONE' : ['uj', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['ujmy', []],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['ujcie', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['iwał', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['iwała', []],

                            'NONE-LP-NONE-PRZE-N' : ['iwało', []],

                            'NONE-LM-NONE-PRZE-M' : ['iwali', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['iwały', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['iwany', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['iwnego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['cemu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['anym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['ana', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['nej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-MIE-BIERNY-M' : ['nych', []],

                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['any', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ana', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['ani', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['ano', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['anie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ałam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ałaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ałem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ałeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['ania', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ni', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['ań', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            # 'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', ['ywaniu']],
                            'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ań',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['iwaniu', []],
                            # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            # 'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ani', []],                        
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['aną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['nymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['nemu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['nego', []],


                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['nego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['nym', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_3'  : ['nymi', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_4'  : ['ani', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_5'  : ['nej', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_6'  : ['nemu', []],
                            
            },
            'IX' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['ać', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['ę', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['esz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['e', ['cie', 'ce', 'nie', 'ne', 'że']],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['emy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['ecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ą', ['ną', 'cą']],
                            'Ios-LM-NDKTER-ROZ-NONE' : [' ', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['my', ['śmy', 'emy']],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['cie', ['ście', 'ecie']],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ał', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['ała', []],

                            'NONE-LP-NONE-PRZE-N' : ['ało', []],

                            'NONE-LM-NONE-PRZE-M' : ['ali', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['ały', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            # 'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['any', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['nego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['cemu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['anym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['ana', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['nej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-MIE-BIERNY-M' : ['nych', []],

                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['any', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ana', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['ani', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['ano', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['anie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ałam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ałaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ałem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ałeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['ania', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ni', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['ań', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ań',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['enie', []],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ani', []],                        
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['aną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['nymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['nemu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['ną', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_4'  : ['awszy', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_5'  : ['eli', []],
                            
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['nej', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['nym', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_3'  : ['nemu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_4'  : ['nymi', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_5'  : ['nego', []],
            },
            'XA' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['ć', []],
                            'BEZOKOLICZNIK-NONE-NONE-NONE-ZAPRZECZASJĄCY' : ['ć', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['ję', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['jesz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['je', []],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['jemy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['jecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ją', []],
                            'Ios-LM-NDKTER-ROZ-NONE' : ['j', ['ej']],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['jmy', ['śmy', 'emy']],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['jcie', ['ście', 'ecie']],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ł', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['ła', []],

                            'NONE-LP-NONE-PRZE-N' : ['ło', []],

                            'NONE-LM-NONE-PRZE-M' : ['li', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['ły', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            # 'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['ty', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['tego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['temu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['tym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['ta', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['tej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['te', []],

                            'IMIESŁÓW-LM-MIE-BIERNY-M' : ['tych', []],

                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['ty', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ta', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['te', []],

                            # 'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['ani', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['to', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['anie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ałam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ałaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ałem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ałeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['cia', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ci', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['ań', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['ciach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['ciami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['ciem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['ciom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['ciu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['ciom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['cia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ciu', []],
                            # 'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ań',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['ciami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['ciach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['cie', ['ście', 'jcie', 'ecie']],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['tych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ciu', []],
                            # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ciem', []],
                            'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ci', []],                        
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['tą', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['aś', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['eś', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['łem', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_4'  : ['łam', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_5'  : ['cie', ['ście', 'jcie', 'ecie']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_6'  : ['ą', ['ją', 'ącą']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_7'  : ['mi', ['ami']],

                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['emu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['tej', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_3'  : ['tym', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_4'  : ['ego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_5'  : ['ymi', []],
                            
            },
            'XB' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['ąć', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['mę', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['miesz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['mie', []],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['miemy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['miecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['mą', []],
                            'Ios-LM-NDKTER-ROZ-NONE' : ['mij', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['mijmy', ['śmy', 'emy']],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['jcie', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ął', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['ęła', []],

                            'NONE-LP-NONE-PRZE-N' : ['ęło', []],

                            'NONE-LM-NONE-PRZE-M' : ['ęli', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['ęły', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            # 'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['ty', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['tego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['temu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['tym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['ta', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['tej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['te', []],

                            'IMIESŁÓW-LM-MIE-BIERNY-M' : ['tych', []],

                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['ty', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ta', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['te', []],

                            # 'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['ani', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['to', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['anie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ałam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ałaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ałem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ałeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['cia', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ci', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['ań', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['ciach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['ciami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['ciem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['ciom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['ciu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['ciom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['cia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ciu', []],
                            # 'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ań',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['ciami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['ciach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['cie', ['jcie', 'ście', 'ecie']],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['tych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ciu', []],
                            # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ciem', []],
                            'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ci', []],                        
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['tą', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['cie', ['jcie', 'ście', 'ecie', 'ęcie']],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['ęć', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['ętą', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_4'  : ['ętymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_5'  : ['ąłeś', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_6'  : ['mmy', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_7'  : ['ąłem', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_8'  : ['ąwszy', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_9'  : ['ęłem', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_10'  : ['ęłam', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_11'  : ['m', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_12'  : ['ęłaś', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_13'  : ['ęcie', []],


                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['ętemu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['ętymi', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_3'  : ['ętym', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_4'  : ['ętego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_5'  : ['ętej', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_6'  : ['ęć', []],
                            
            },
            'XC' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['ąć', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['nę', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['niesz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['nie', []],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['niemy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['niecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ną', []],
                            'Ios-LM-NDKTER-ROZ-NONE' : ['nij', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['nijmy', ['śmy', 'emy']],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['nijcie', ['ście', 'ecie']],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ął', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['ęła', []],

                            'NONE-LP-NONE-PRZE-N' : ['ęło', []],

                            'NONE-LM-NONE-PRZE-M' : ['ęli', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['ęły', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            # 'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['ty', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['tego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['temu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['tym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['ta', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['tej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['te', []],

                            'IMIESŁÓW-LM-MIE-BIERNY-M' : ['tych', []],

                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['ty', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ta', []],
                            'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['te', []],

                            # 'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['ani', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['to', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['anie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['ełam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['ełaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['ołem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['ołeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['cia', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ci', []],
                            # 'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['ań', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['ciach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['ciami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['ciem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['ciom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['ciu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['ciom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['cia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ciu', []],
                            # 'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ań',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['ciami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['ciach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['cie', []],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['tych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ciu', []],
                            # 'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['anie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ciem', []],
                            'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ci', []],                        
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['tą', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['ęcie', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['ętymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['ęłaś', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_4'  : ['ętą', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_5'  : ['ąwszy', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_6'  : ['ąłeś', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_7'  : ['ąłem', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_8'  : ['ęć', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_9'  : ['ęłam', []],
                            
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['ętego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['ętym', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_3'  : ['ętymi', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_4'  : ['ętej', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_5'  : ['ętemu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_6'  : ['ęć', []],

            },
            'XIA' : {
                            'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['c', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['ę', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['esz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['e', ['cie', 'ce', 'nie', 'ne', 'że']],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['emy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['ecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ą', ['ną', 'cą']],
                            'Ios-LM-NDKTER-ROZ-NONE' : [' ', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['my', ['śmy', 'emy']],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['cie', ['ście', 'ecie']],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ł', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['ła', []],

                            'NONE-LP-NONE-PRZE-N' : ['ło', []],

                            'NONE-LM-NONE-PRZE-M' : ['li', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['ły', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            # 'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['ony', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['nego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['cemu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['onym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['ona', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['nej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['one', []],

                            'IMIESŁÓW-LM-MIE-BIERNY-M' : ['nych', []],

                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['any', []],
                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ana', []],
                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['eni', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['ono', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['enie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['łam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['łaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['łem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['łeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['enia', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ni', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['eń', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eń',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['enie', []],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['enie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eni', []],                        
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['oną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['onemu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['onymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['oną', []],

                            
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['ona', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['nej', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_3'  : ['ony', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_4'  : ['onemu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_5'  : ['one', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_6'  : ['onymi', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_7'  : ['onym', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_8'  : ['onego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_9'  : ['onymi', []],

            },
            'XIB' : {
                        'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' : ['ć', []],

                            'Ios-LP-NDKTER-DKPRZY-NONE' : ['ę', []],

                            'Ios-LP-DK-ROZ-NONE' : ['eż', []],
                            'IIos-LP-DK-ROZ-NONE' : ['że', []],
                            'IIos-LM-DK-ROZ-NONE' : ['yż', []],

                            'IIos-LP-NDKTER-DKPRZY-NONE' : ['esz', []],
                            'IIIos-LP-NDKTER-DKPRZY-NONE' : ['e', ['cie', 'ce', 'nie', 'ne', 'że']],
                            'Ios-LM-NDKTER-DKPRZY-NONE' : ['emy', []],

                            'IIos-LM-NDKTER-DKPRZY-NONE' : ['ecie',  []],
                            'IIIos-LM-NDKTER-DKPRZY-NONE' : ['ą', ['ną', 'cą']],
                            'Ios-LM-NDKTER-ROZ-NONE' : [' ', []],
                            'IIos-LM-NDKTER-ROZ-NONE' : ['my', ['śmy', 'emy']],
                            'IIIos-LM-NDKTER-ROZ-NONE' : ['cie', ['ście', 'ecie']],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' : ['ący', []],

                            'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' : ['ąca', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' : ['ącą', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' : ['ącej', []],

                            'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' : ['ącego', []],
                            'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' : ['ącemu', []],
                            'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' : ['ących', []],
                            'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' : ['ącym', []],
                            'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' : ['ącymi', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' : ['ące', []],

                            'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' : ['ąc', []],

                            'NONE-LP-NONE-PRZE-M' : ['ł', []],

                            'NONE-LP-NONE-PRZE-Ż' : ['ła', []],

                            'NONE-LP-NONE-PRZE-N' : ['ło', []],

                            'NONE-LM-NONE-PRZE-M' : ['li', []],

                            'NONE-LM-NONE-PRZE-ŻN' : ['ły', []],

                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' : ['cego', []],
                            'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' : ['cej', []],

                            # 'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' : ['aną', []],
                            
                            'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' : ['cymi', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-M' : ['ony', []],
                            'IMIESŁÓW-LP-DOP-BIERNY-M' : ['nego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-M' : ['cemu', []],
                            'IMIESŁÓW-LP-NAR-BIERNY-M' : ['onym', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-Ż' : ['ona', []],
                            'IMIESŁÓW-LP-MIE-BIERNY-Ż' : ['nej', []],

                            'IMIESŁÓW-LP-MIA-BIERNY-N' : ['one', []],

                            'IMIESŁÓW-LM-MIE-BIERNY-M' : ['nych', []],

                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' : ['any', []],
                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' : ['ana', []],
                            # 'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' : ['ane', []],

                            'IMIESŁÓW-LM-NONE-BIERNY-MOS' : ['eni', []],

                            'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' : ['ono', []],

                            'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' : ['enie', []],

                            'Ios-LP-PRZP-TER-M' : ['łbym', []],
                            'IIos-LP-PRZP-TER-M' : ['łbyś', []],
                            'IIIos-LP-PRZP-TER-M' : ['łby', []],

                            'Ios-LP-PRZP-TER-Ż' : ['łabym', []],
                            'IIos-LP-PRZP-TER-Ż' : ['łabyś', []],
                            'IIIos-LP-PRZP-TER-Ż' : ['łaby', []],

                            'IIIos-LP-PRZP-TER-N' : ['łoby', []],

                            'Ios-LM-PRZP-TER-M' : ['libyśmy', []],
                            'IIos-LM-PRZP-TER-M' : ['libyście', []],
                            'IIIos-LM-PRZP-TER-M' : ['liby', []],

                            'Ios-LM-PRZP-TER-Ż' : ['łybyśmy', []],
                            'IIos-LM-PRZP-TER-Ż' : ['łybyście', []],
                            'IIIos-LM-PRZP-TER-Ż' : ['łyby', []],

                            'IIos-LM-PRZP-PRZE-NONE' : ['liśmy', []],
                            'IIIos-LM-PRZP-PRZE-NONE' : ['liście', []],

                            'Ios-LP-ORZ-PRZE-Ż' : ['łam', []],
                            'IIos-LP-ORZ-PRZE-Ż' : ['łaś', []],

                            'Ios-LP-ORZ-PRZE-M' : ['łem', []],
                            'IIos-LP-ORZ-PRZE-M' : ['łeś', []],
                            
                            'IIos-LM-ORZ-PRZE-Ż' : ['łyście', []],
                            'IIIos-LM-ORZ-PRZE-Ż' : ['łyśmy', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' : ['enia', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' : ['ni', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' : ['eń', []],

                            # 'RZECZOWNIK-LP-ODSŁOWNY-DOP-NONE' : ['ania', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' : ['niach', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' : ['niami', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' : ['niem', []],
                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' : ['niom', []],
                            'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' : ['niu', []],

                            'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' : ['niom', []],

                            'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['nia', []],
                            'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['ąca', []],
                            'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eń',  []],
                            'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niami', []],
                            'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' : ['niach', []],
                            
                            'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['enie', []],
                            'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['nych', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niu', []],
                            'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['enie', []],
                            'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['niem', []],
                            'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['eni', []],                        
                            'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  : ['oną', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  : ['ącą', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  : ['ące', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  : ['cego', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  : ['ącej', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  : ['ąc', []],                        
                            'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  : ['ącemu', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  : ['ący', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  : ['ących', []],

                            'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  : ['ącym', []],
                            'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  : ['ącymi', []],

                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_1'  : ['onemu', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  : ['onymi', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_3'  : ['oną', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_4'  : ['łszy', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_6'  : ['eśmy', []],
                            'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_7'  : ['eście', []],

                            
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  : ['ona', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_2'  : ['nej', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_3'  : ['ony', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_4'  : ['onemu', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_5'  : ['one', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_6'  : ['onymi', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_7'  : ['onym', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_8'  : ['onego', []],
                            'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_9'  : ['onymi', []],
            },
            
            
        }
        spec_none = {}
        
        for sgk, sgv in grupy_fleksyjne.items():
            opt_count = 0
            for s,g in sgv.items():
                spec_none[f'{s}_{sgk}_{opt_count}'] = g
                opt_count += 1

        grupy_fleksyjne['spec-none'] = spec_none
        grf = set_gr(base, w)
        # print(grf)
        if grf == 'spec':
            try:
                direct_gr = set_gr(base, w, True)[bez]
                if option =='ALL':
                    return direct_gr
            except KeyError:
                if option =='ALL':
                    return {}
                else:
                    return 'WRONG-KEY-NONE-NONE-NONE'
            if option =='TAKE':
                for k,v in direct_gr.items():
                    if v == w:
                        return k
                return 'WRONG-KEY-NONE-NONE-NONE'
            if option =='CHANGE' and mode != None:
                try:
                    if negative_verb:
                        return f'nie {direct_gr[mode]}'
                    else:
                        return direct_gr[mode]
                except KeyError:
                    return 'WRONG-KEY-NONE-NONE-NONE'
        else:
            gr = grupy_fleksyjne[grf]
            final_dict = {}
            target_v = takeTarget.take_superTarget(base, w)
            # print(target_v)
            temp_set = set()
            for word in target_v:
                seconder = False
                if not word.startswith('nie'):
                    for flex, ends in gr.items():
                        if flex.count('ZAPRZECZASJĄCY') == 0:
                            if word.endswith(ends[0]):
                                neg_check = True
                                for n in ends[1]:
                                    if word.endswith(n):
                                        neg_check = False
                                if neg_check:
                                    # print(word, flex, e)
                                    seconder = True
                                    # input('..')
                                    temp_set.add(word)
                                    final_dict[flex] = word
                                    break
                else:
                    for flex, ends in gr.items():
                        if flex.count('ZAPRZECZASJĄCY') > 0:
                            if word.endswith(ends[0]):
                                neg_check = True
                                for n in ends[1]:
                                    if word.endswith(n):
                                        neg_check = False
                                if neg_check:
                                    # print(word, flex, e)
                                    seconder = True
                                    # input('nie ..')
                                    temp_set.add(word)
                                    final_dict[flex] = word
                                    break
            rest = set()
            for r in target_v:
                rest.add(r)
            try:
                final_dict['Ios-LM-NDKTER-ROZ-NONE']
            except KeyError:
                if len(rest.difference(temp_set)) == 1:
                    for x in rest.difference(temp_set):
                        final_dict['Ios-LM-NDKTER-ROZ-NONE'] = x
                else:
                    count = 0
                    for x in rest.difference(temp_set):
                        if x.startswith('nie'):
                            final_dict[f'NIEZIDENTYFIKOWANY-ZAPRZECZASJĄCY-NONE-NONE-{count}'] = x
                        else:
                            final_dict[f'NIEZIDENTYFIKOWANY-NONE-NONE-NONE-{count}'] = x
                        count += 1


            with open(f'spec_verbs.neural', 'r', encoding='utf-8') as userFile:
                firle_word = userFile.readlines()
            all_words = ''
            for aw in firle_word:
                all_words += aw
            string = f'{bez}$'
            for k,v in final_dict.items():
                string += f'{k}:{v},'
            if string.endswith(','):
                string = string[:len(string) - 1] + '\n'
            firle_word = all_words + string
            signal.signal(signal.SIGINT, signal.SIG_IGN) # tutaj niech wyłączy CTRL+C
            os.system('color 4E')
            with open(f'spec_verbs.neural', 'w+', encoding='utf-8') as writeFile:
                writeFile.write(firle_word)
            os.system('color 07')
            signal.signal(signal.SIGINT, signal.SIG_DFL) # tutaj niech włączy CTRL+C
            if option =='ALL':
                return final_dict
            else:
                return verb_flex(base, w, option, mode)
    else:
        if option =='ALL':
            return {}
        else:
            return 'WRONG-KEY-NONE-NONE-NONE'
        
if __name__ == '__main__':
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(set_gr(base, 'tłuc', option=None))
    print(set_gr(base, 'robić', option=None))
    # print(set_gr(base, 'wysunąć', option=True))

    
    # print(verb_flex(base, 'wysunąć', option='TAKE'))
    # print(verb_flex(base, 'wysunąć', option='CHANGE', mode='IIos-LM-PRZP-PRZE-NONE'))
    # print(verb_flex(base, 'wysunąć', option='ALL')) # Opcja dev
    """
    'BEZOKOLICZNIK-NONE-NONE-NONE-NONE' 
    'Ios-LP-NDKTER-DKPRZY-NONE' 
    'Ios-LP-DK-ROZ-NONE' 
    'IIos-LP-DK-ROZ-NONE' 
    'IIos-LM-DK-ROZ-NONE' 
    'IIos-LP-NDKTER-DKPRZY-NONE' 
    'IIIos-LP-NDKTER-DKPRZY-NONE' 
    'Ios-LM-NDKTER-DKPRZY-NONE' 
    'IIos-LM-NDKTER-DKPRZY-NONE' 
    'IIIos-LM-NDKTER-DKPRZY-NONE' 
    'Ios-LM-NDKTER-ROZ-NONE' 
    'IIos-LM-NDKTER-ROZ-NONE' 
    'IIIos-LM-NDKTER-ROZ-NONE' 
    'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-M' 
    'IMIESŁÓW-WSPÓŁCZENY-MIA-PRZYMIOTNIKOWY-Ż' 
    'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-Ż' 
    'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-Ż' 
    'IMIESŁÓW-WSPÓŁCZENY-DOP-PRZYMIOTNIKOWY-M' 
    'IMIESŁÓW-WSPÓŁCZENY-BIE-PRZYMIOTNIKOWY-M' 
    'IMIESŁÓW-WSPÓŁCZENY-MIE-PRZYMIOTNIKOWY-M' 
    'IMIESŁÓW-WSPÓŁCZENY-CEL-PRZYMIOTNIKOWY-M' 
    'IMIESŁÓW-WSPÓŁCZENY-NAR-PRZYMIOTNIKOWY-M' 
    'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYMIOTNIKOWY-N' 
    'IMIESŁÓW-WSPÓŁCZENY-NDK-PRZYSŁÓWKOWY-NONE' 
    'NONE-LP-NONE-PRZE-M' 
    'NONE-LP-NONE-PRZE-Ż' 
    'NONE-LP-NONE-PRZE-N' 
    'NONE-LM-NONE-PRZE-M' 
    'NONE-LM-NONE-PRZE-ŻN' 
    'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-M' 
    'IMIESŁÓW-LP-PRZYMIOTNIKOWY-PRZE-Ż' 
    'IMIESŁÓW-LM-PRZYMIOTNIKOWY-PRZE-MOS' 
    'IMIESŁÓW-UPRZEDNI-DK-NONE-NONE' 
    'IMIESŁÓW-LP-MIA-BIERNY-M' 
    'IMIESŁÓW-LP-DOP-BIERNY-M' 
    'IMIESŁÓW-LP-CEL-BIERNY-M' 
    'IMIESŁÓW-LP-NAR-BIERNY-M' 
    'IMIESŁÓW-LP-MIA-BIERNY-Ż' 
    'IMIESŁÓW-LP-MIE-BIERNY-Ż' 
    'IMIESŁÓW-LP-MIA-BIERNY-N' 
    'IMIESŁÓW-LM-MIE-BIERNY-M' 
    'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-M' 
    'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-Ż' 
    'IMIESŁÓW-LP-ZAPRZECZASJĄCY-BIERNY-N' 
    'IMIESŁÓW-LM-NONE-BIERNY-MOS' 
    'NIEOSOBOWA-FORMA-NONE-PRZE-NONE' 
    'RZECZOWNIK-LP-ODSŁOWNY-MIA-NONE' 
    'Ios-LP-PRZP-TER-M' 
    'IIos-LP-PRZP-TER-M' 
    'IIIos-LP-PRZP-TER-M' 
    'Ios-LP-PRZP-TER-Ż' 
    'IIos-LP-PRZP-TER-Ż' 
    'IIIos-LP-PRZP-TER-Ż' 
    'IIIos-LP-PRZP-TER-N' 
    'Ios-LM-PRZP-TER-M' 
    'IIos-LM-PRZP-TER-M' 
    'IIIos-LM-PRZP-TER-M' 
    'Ios-LM-PRZP-TER-Ż' 
    'IIos-LM-PRZP-TER-Ż' 
    'IIIos-LM-PRZP-TER-Ż' 
    'IIos-LM-PRZP-PRZE-NONE' 
    'IIIos-LM-PRZP-PRZE-NONE' 
    'Ios-LP-ORZ-PRZE-Ż' 
    'IIos-LP-ORZ-PRZE-Ż' 
    'Ios-LP-ORZ-PRZE-M' 
    'IIos-LP-ORZ-PRZE-M' 
    'IIos-LM-ORZ-PRZE-Ż' 
    'IIIos-LM-ORZ-PRZE-Ż' 
    'RZECZOWNIK-LM-ODSŁOWNY-MIA-NONE' 
    'RZECZOWNIK-LM-ODSŁOWNY-WOL-NONE' 
    'RZECZOWNIK-LM-ODSŁOWNY-DOP-NONE' 
    'RZECZOWNIK-LM-ODSŁOWNY-MIE-NONE' 
    'RZECZOWNIK-LM-ODSŁOWNY-NAR-NONE' 
    'RZECZOWNIK-LP-ODSŁOWNY-NAR-NONE' 
    'RZECZOWNIK-LM-ODSŁOWNY-CEL-NONE' 
    'RZECZOWNIK-LP-ODSŁOWNY-CEL-NONE' 
    'RZECZOWNIK-LM-ODSŁOWNY-CEL-ZAPRZECZASJĄCY' 
    'IMIESŁÓW-LM-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' 
    'IMIESŁÓW-LM-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  
    'IMIESŁÓW-LM-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  
    'IMIESŁÓW-LM-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  
    'IMIESŁÓW-LM-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' 
    'IMIESŁÓW-LM-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY' 
    'IMIESŁÓW-LP-MIA-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  
    'IMIESŁÓW-LP-DOP-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  
    'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  
    'IMIESŁÓW-LP-BIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  
    'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  
    'IMIESŁÓW-LP-MIE-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  
    'IMIESŁÓW-LP-WOL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY'  
    'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-Ż'  
    'IMIESŁÓW-ZAPRZECZASJĄCY-NAR-PRZYMIOTNIKOWY-Ż'  
    'IMIESŁÓW-ZAPRZECZASJĄCY-BIE-PRZYMIOTNIKOWY-Ż'  
    'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-Ż'  
    'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-M'  
    'IMIESŁÓW-ZAPRZECZASJĄCY-CEL-PRZYMIOTNIKOWY-M'  
    'IMIESŁÓW-ZAPRZECZASJĄCY-MIA-PRZYMIOTNIKOWY-M'  
    'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-M'  
    'IMIESŁÓW-ZAPRZECZASJĄCY-DOP-PRZYMIOTNIKOWY-MOS'  
    'IMIESŁÓW-ZAPRZECZASJĄCY-MIE-PRZYMIOTNIKOWY-MOS'  
    'IMIESŁÓW-LP-NAR-PRZYMIOTNIKOWY-POZYTYWNY_1'  
    'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-POZYTYWNY_2'  
    'IMIESŁÓW-LP-CEL-BIERNY-ZAPRZECZASJĄCY_1'  
    'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_1'  
    'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_2'  
    'IMIESŁÓW-LP-CEL-PRZYMIOTNIKOWY-ZAPRZECZASJĄCY_4'
    """