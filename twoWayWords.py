
def two_way_words(word):
    dwubiegunowe = [
        ['ciepły', 'zimny'], ['zimny', 'gorący'], ['jasny', 'mętny'], ['ciemny', 'jasny'], ['powolny', 'szybki'], 
        ['szybki', 'wolny'], ['przyjaciel', 'wróg'], ['wróg', 'przyjaciel'], ['mokry', 'suchy'], ['suchy', 'mokry'], 
        ['sztuczny', 'naturalny'], ['naturalny', 'sztuczny'], ['duży', 'mały'], ['mały', 'duży'], ['wysoki', 'niski'], 
        ['niski', 'wysoki'], ['głośny', 'cisza'], ['cichy', 'głośny'], ['miękki', 'twardy'], ['twardy', 'miękki'], 
        ['wolny', 'szybki'], ['stary', 'nowy'], ['młody', 'stary'], ['gorący', 'zimny'], ['szczęśliwy', 'nieszczęśliwy'], 
        ['smutny', 'radosny'], ['bogaty', 'ubogi'], ['biedny', 'bogaty'], ['lewy', 'prawy'], ['prawy', 'lewy'],
        ['świeży', 'znoszony'], ['znoszony', 'świeży'], ['wesoły', 'smutny'], ['prosty', 'skomplikowany'], 
        ['skomplikowany', 'prosty'], ['nowy', 'stary'], ['ubogi', 'bogaty'], ['mocny', 'słaby'], ['słaby', 'potężny'], 
        ['cisza', 'głośny'], ['mądry', 'głupi'], ['głupi', 'mądry'], ['przyjemny', 'nieprzyjemny'], 
        ['nieprzyjemny', 'przyjemny'], ['zdrowy', 'chory'], ['chory', 'zdrowy'], ['nieszczęśliwy', 'szczęśliwy'], 
        ['święty', 'grzeszny'], ['grzeszny', 'święty'], ['pewny', 'niepewny'], ['niepewny', 'pewny'], 
        ['czysty', 'brudny'], ['brudny', 'czysty'], ['rzadki', 'pospolity'], ['pospolity', 'rzadki'], 
        ['zdolny', 'niezdolny'], ['niezdolny', 'zdolny'], ['ciekawy', 'nudny'], ['nudny', 'błyskotliwy'], 
        ['męczący', 'odprężający'], ['odprężający', 'męczący'], ['przyjazny', 'wrogi'], ['wrogi', 'przyjazny'], 
        ['ciepło', 'zimno'], ['zimno', 'ciepło'], ['jednostajny', 'zmienność'], ['zmienność', 'jednostajny'], 
        ['ruch', 'spokój'], ['spokój', 'ruch'], ['dobra', 'zła'], ['zła', 'dobra'], ['rozwaga', 'ryzyko'], 
        ['ryzyko', 'rozwaga'], ['wiedza', 'ignorancja'], ['ignorancja', 'nauka'], ['nadzieja', 'rozpacz'], 
        ['rozpacz', 'nadzieja'], ['słodki', 'kwaśny'], ['kwaśny', 'słodki'], ['ładny', 'brzydki'], ['brzydki', 'ładny'], 
        ['nawet', 'nawet nie'], ['nawet nie', 'nawet'], ['uczciwy', 'nieuczciwy'], ['nieuczciwy', 'uczciwy'], 
        ['nowoczesny', 'przestarzały'], ['przestarzały', 'nowoczesny'], ['optymistyczny', 'pesymistyczny'], 
        ['pesymistyczny', 'optymistyczny'], ['zdumiewający', 'zwyczajny'], ['zwyczajny', 'cudowny'], ['szlachetny', 'podły'], 
        ['podły', 'szlachetny'], ['delikatny', 'grubiański'], ['grubiański', 'delikatny'], ['energiczny', 'słaby'], 
        ['komfortowy', 'niewygodny'], ['niewygodny', 'komfortowy'], ['dobry', 'zły'], ['zły', 'dobry'], 
        ['nadmiar', 'brak'], ['brak', 'nadmiar'], ['obfity', 'skromny'], ['skromny', 'zarozumiały'], 
        ['bezpieczny', 'niebezpieczny'], ['niebezpieczny', 'bezpieczny'], ['miły', 'niemiły'], ['niemiły', 'miły'], 
        ['wierny', 'niewierny'], ['nierzetelny', 'wierny'], ['dynamiczny', 'statyczny'], ['statyczny', 'dynamiczny'], 
        ['idealny', 'niedoskonały'], ['niedoskonały', 'idealny'], ['kreatywny', 'niedomyślny'], ['niedomyślny', 'kreatywny'], 
        ['właściwy', 'nieodpowiedni'], ['niewłaściwy', 'właściwy'], ['prawda', 'fałsz'], ['fałsz', 'prawda'], 
        ['uporządkowany', 'chaos'], ['chaos', 'uporządkowany'], ['życie', 'śmierć'], ['śmierć', 'życie'], 
        ['szczery', 'obłudny'], ['kłamliwy', 'szczery'], ['cudowny', 'zwyczajny'], ['mroczny', 'jasny'], 
        ['praca', 'lenistwo'], ['lenistwo', 'praca'], ['odpowiedzialny', 'nieodpowiedzialny'], 
        ['nieodpowiedzialny', 'odpowiedzialny'], ['prawdziwy', 'fałszywy'], ['fałszywy', 'prawdziwy'], 
        ['beztroski', 'troskliwy'], ['troskliwy', 'beztroski'], ['nauka', 'ignorancja'], ['radosny', 'smutny'], 
        ['dzielny', 'bojaźliwy'], ['tchórzliwy', 'dzielny'], ['oszukańczy', 'uczciwy'], ['odważny', 'strachliwy'], 
        ['strachliwy', 'odważny'], ['odpowiedni', 'niewłaściwy'], ['słuszny', 'niesłuszny'], ['niesłuszny', 'słuszny'], 
        ['mętny', 'jasny'], ['udany', 'nieudany'], ['nieudany', 'udany'], ['obłudny', 'szczery'], ['chętny', 'niechętny'], 
        ['niechętny', 'chętny'], ['łatwy', 'trudny'], ['trudny', 'łatwy'], ['śmiały', 'nieśmiały'], ['nieśmiały', 'śmiały'], 
        ['taktowny', 'nietaktowny'], ['nietaktowny', 'taktowny'], ['błyskotliwy', 'nudny'], ['bojaźliwy', 'dzielny'], 
        ['zrównoważony', 'niestabilny'], ['niestabilny', 'zrównoważony'], ['uczynny', 'bezczynny'], ['bezczynny', 'uczynny'], 
        ['grzeczny', 'niegrzeczny'], ['niegrzeczny', 'grzeczny'], ['nieodpowiedni', 'właściwy'], ['oryginalny', 'nietypowy'], 
        ['nietypowy', 'oryginalny'], ['potężny', 'słaby'], ['przyzwoity', 'nieprzyzwoity'], ['nieprzyzwoity', 'przyzwoity'], 
        ['bezradny', 'zdolny'], ['niewierny', 'wierny'], ['cenny', 'bezcenny'], ['bezcenny', 'cenny'], 
        ['spokojny', 'nerwowy'], ['nerwowy', 'spokojny'], ['niezrównoważony', 'zrównoważony'], ['normalny', 'nieprawidłowy'],
        ['nieprawidłowy', 'normalny'], ['zwykły', 'niezwykły'], ['niezwykły', 'zwykły'], ['rozważny', 'lekceważący'], 
        ['lekceważący', 'rozważny'], ['inteligentny', 'głupi'], ['celowy', 'przypadkowy'], ['przypadkowy', 'celowy'], 
        ['konkretny', 'abstrakcyjny'], ['abstrakcyjny', 'konkretny'], ['otwarty', 'zamknięty'], ['zamknięty', 'otwarty'], 
        ['niezawodny', 'niewiarygodny'], ['niewiarygodny', 'niezawodny'], ['nieskazitelny', 'wadliwy'], 
        ['wadliwy', 'nieskazitelny'], ['gorzki', 'słodki'], ['pamiętliwy', 'zapominalski'], ['zapominalski', 'pamiętliwy'], 
        ['determinowany', 'niezdecydowany'], ['niezdecydowany', 'determinowany'], ['wydajny', 'niewydajny'], 
        ['niewydajny', 'wydajny'], ['lojalny', 'nieuczciwy'], ['zarozumiały', 'skromny'], ['poważny', 'niepoważny'], 
        ['niepoważny', 'poważny'], ['równy', 'nierówny'], ['nierówny', 'równy'], ['zmyślony', 'rzeczywisty'], 
        ['rzeczywisty', 'zmyślony'], ['pełny', 'pusty'], ['pusty', 'pełny']
    ]

    dwubiegunowe_dict = {}
    for word_PN in dwubiegunowe:
        dwubiegunowe_dict[word_PN[0]] = word_PN[1]
        dwubiegunowe_dict[word_PN[1]] = word_PN[0]
    dwubiegunowe_actives = []
    for key in dwubiegunowe_dict.keys():
        dwubiegunowe_actives.append(key)
    try:
        tww_wotd = dwubiegunowe_dict[word]
        return {'RESULT' : True, 'WORD': tww_wotd, 'WORDS' : dwubiegunowe_actives}
    except KeyError:
        return {'RESULT' : False, 'WORDS' : dwubiegunowe_actives}
    
if __name__ == '__main__':
    import awareness
    print(two_way_words('wadliwy')['RESULT']) # znaleziono słowo True
    print(two_way_words('wadliwy')['WORD']) # drugi biegun słowa
    print(two_way_words('wadliwy')['WORDS']) # wszystkie słowa obsługiwane przez funkcje