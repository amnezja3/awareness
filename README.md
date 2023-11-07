# awareness
The Awareness Library is a versatile Polish text processing tool offering advanced modules for text analysis, content generation, and linguistic research. Key modules include the Action Module for sentence analysis, the Advanced Action Module for complex constructions, and functions for adjective, noun, and verb inflections.

(PL) 

## Biblioteka Awareness: Narzędzie NLP dla Języka Polskiego

(EN) 

## Awareness Library: NLP Tool for the Polish Language

(PL)

Biblioteka Awareness to zaawansowane narzędzie do przetwarzania tekstu w języku polskim, stworzone w celu ułatwienia analizy i manipulacji tekstu. Ta wszechstronna biblioteka oferuje szereg potężnych modułów, które umożliwiają użytkownikom przeprowadzanie głębokiej analizy tekstów, wykonywanie zaawansowanych operacji związanych z językiem polskim. 

### Poniżej przedstawiamy kilka najciekawszych i kluczowych modułów, które wyróżniają bibliotekę Awareness:

#### Moduł Action:

Moduł Action to funkcja klasyfikująca i interpretująca podane zdania. Dzięki temu modułowi można analizować zdania pod względem podziału na części zdania, takie jak podmiot, orzeczenie, dopełnienie, i inne części zdania. Możesz również dodawać analizowane zdania do bazy systemowej.
    
#### Moduł Advanced Action: 

Moduł Advanced Action umożliwia tworzenie bardziej złożonych zdań, łączenie ich z bazą systemową oraz przypisywanie ich do określonych kategorii. To narzędzie idealne do tworzenia i zarządzania bardziej skomplikowanymi konstrukcjami językowymi.

#### Odmiany Przymiotników i Rzeczowników: 

Biblioteka Awareness posiada funkcje do odmiany przymiotników i rzeczowników przez przypadki. Możesz łatwo zmieniać formy tych słów i uzyskiwać propozycje odmiany, z możliwością korekty.

#### Praca z Czasownikami: 

Moduł verb_flex pozwala na odmienianie czasowników w różnych formach i generowanie całych rodzin odmienionych czasowników wraz z flagami.

Potencjalne Wykorzystanie:

#### Analiza Tekstu: 

Biblioteka Awareness może być wykorzystywana do analizy tekstów w celu wydobycia kluczowych informacji, identyfikacji struktury zdania i części mowy.

#### Generowanie Treści:

Moduł Advanced Action może być używany do generowania skomplikowanych konstrukcji językowych, co jest przydatne w tworzeniu treści tekstowej.

#### Lingwistyczne Badania: 

Dzięki funkcjom odmiany przymiotników, rzeczowników i czasowników, biblioteka jest cennym narzędziem w lingwistycznych badaniach nad językiem polskim.

Biblioteka Awareness to narzędzie wszechstronne i potężne, które znalazło swoje zastosowanie w analizie języka polskiego, zarówno w kontekście analizy gramatycznej, jak i generowania treści. Dzięki tym modułom użytkownicy mogą wykonywać zaawansowane operacje na tekście, analizować jego strukturę, a także tworzyć bardziej skomplikowane konstrukcje językowe.

Jeśli potrzebujesz bardziej szczegółowych informacji na temat konkretnych funkcji i ich zastosowań, zapraszamy do konsultacji dokumentacji biblioteki Awareness.

(EN)

The Awareness Library is an advanced tool for processing text in the Polish language, created to facilitate the analysis and manipulation of text. This versatile library offers a range of powerful modules that enable users to perform in-depth analysis of texts and carry out advanced operations related to the Polish language. 

### Below, we present some of the most interesting and key modules that distinguish the Awareness library:

#### Action Module: 

The Action module is a function that classifies and interprets given sentences. With this module, you can analyze sentences in terms of their components, such as subjects, predicates, complements, and other parts of a sentence. You can also add analyzed sentences to the system's database.

#### Advanced Action Module: 

The Advanced Action module allows you to create more complex sentences, link them to the system's database, and assign them to specific categories. This tool is ideal for creating and managing more intricate language constructions.

#### Adjective and Noun Inflections: 

The Awareness Library includes functions for inflecting adjectives and nouns according to cases. You can easily change the forms of these words and receive suggestions for inflection, with the option for corrections.

#### Verb Processing: 

The verb_flex module enables the inflection of verbs in various forms and the generation of complete families of inflected verbs along with flags.

#### Potential Uses:

Text Analysis: The Awareness Library can be used for analyzing texts to extract key information, identify sentence structure, and parts of speech.

#### Content Generation: 

The Advanced Action module can be used to generate complex language constructions, making it useful for creating textual content.

#### Linguistic Research: 

Thanks to the functions for adjective, noun, and verb inflections, the library is a valuable tool for linguistic research on the Polish language.

The Awareness Library is a versatile and powerful tool that has found its applications in the analysis of the Polish language, both in terms of grammatical analysis and content generation. These modules allow users to perform advanced text operations, analyze sentence structures, and construct more complex language constructions.

If you need more detailed information about specific functions and their applications, please refer to the Awareness Library documentation.

(PL)

### Moduł Sam_g (Rozpoznawanie Samogłoski)

Opis: Funkcja sam_g rozpoznaje samogłoski w podanym tekście.

    Funkcja: sam_g(x: Any) -> bool

Przykład:
##### python
    import awareness
    print(awareness.sam_g('x'))  # False
    print(awareness.sam_g('a'))  # True

(EN)

### Sam_g Module (Vowel Recognition)

Description: The sam_g function recognizes vowels in text.

    Function: sam_g(x: Any) -> bool

Example:
##### python
    import awareness
    print(awareness.sam_g('x')) # False
    print(awareness.sam_g('a')) # True

(PL)

### Moduł Sufix (Rozpoznawanie Sufiksów)

Opis: Funkcja sufix zwraca sufiksy dla podanego słowa.

    Funkcja: sufix(word: Any) -> Any

Przykład:
##### python
    import awareness
    print(awareness.sufix('pismo'))  # 'smo'
    print(awareness.sufix('samochód'))  # 'chód'

(EN)

### Sufix Module (Suffix Recognizer)

Description: The suffix function returns suffixes for the given word.

    Function: suffix(word: Any) -> Any
    
Example:

##### python
    import awareness
    print(awareness.sufix('letter')) # 'smo'
    print(awareness.sufix('car')) # 'chód'

(PL)

### Moduł Check_v_list (Sprawdza czy jakiś element znajduje się na liście)

Opis: Funkcja check_v_list sprawdza, czy dany element znajduje się na liście.

    Funkcja: check_v_list(x_list: Any, v: Any, option: str = 'True') -> (bool | int | None)
    
Przykład:

##### python
    import awareness
    lista = [1, 2, 4, 5, 5, 6]
    print(awareness.check_v_list(lista, 3))  # False
    print(awareness.check_v_list(lista, 1))  # True

(EN)

### Check_v_list module (Checks if an item is in the list)

Description: The check_v_list function checks whether an item is in the list.

    Function: check_v_list(x_list: Any, v: Any, option: str = 'True') -> (bool | int | None)
    
Example:

##### python
    import awareness
    list = [1, 2, 4, 5, 5, 6]
    print(awareness.check_v_list(list, 3)) # False
    print(awareness.check_v_list(list, 1)) # True

(PL)

### Moduł Kind_sex_word (Rozpoznawanie Rodzaje Słowa)

Opis: Funkcja kind_sex_word rozpoznaje rodzaj słowa, tj. męski (M), żeński (Z) lub nijaki (N).

    Funkcja: kind_sex_word(word: Any) -> (Literal['Z', 'N', 'M'] | None)
    
Przykład:

##### python
    import awareness
    print(awareness.kind_sex_word('samochód'))  # 'M'
    print(awareness.kind_sex_word('kobieta'))  # 'Z'

(EN)

### Kind_sex_word module (Recognizing Kinds of Words)

Description: The kind_sex_word function recognizes the gender of a word, i.e. masculine (M), feminine (Z), or neuter (N).

    Function: kind_sex_word(word: Any) -> (Literal['Z', 'N', 'M'] | None)

Example:

##### python
    import awareness
    print(awareness.kind_sex_word('car')) # 'M'
    print(awareness.kind_sex_word('woman')) # 'Z'

(PL)

### Moduł LPM (Rozpoznawanie Liczby Słowa)

Opis: Funkcja lpm rozpoznaje, czy liczba słowa jest liczba mnogą (LM), pojedynczą (LP) lub nijaką (LN).

    Funkcja: lpm(word: Any) -> Literal['LM', 'LP', 'LN']
    
Przykład:

##### python
    import awareness
    print(awareness.lpm('samochód'))  # 'LP'
    print(awareness.lpm('kobiety'))  # 'LM'

(EN)

### LPM Module (Word Number Recognition)

Description: The lpm function recognizes whether the number of a word is plural (LM), singular (LP), or neuter (LN).

    Function: lpm(word: Any) -> Literal['LM', 'LP', 'LN']
    
Example:

##### python
    import awareness
    print(awareness.lpm('car')) # 'LP'
    print(awareness.lpm('women')) # 'LM'

(PL)

### Moduł Part_Check (Rozpoznawanie Części Mowy)

Opis: Funkcja part_check oddaje część mowy na podstawie podanego słowa.

    Funkcja: part_check(word: Any, multi: str = 'main') -> str

Przykład:

##### python
    import awareness
    print(awareness.part_check('samochód'))  # 'rzeczownik'

(EN)
### Part_Check Module (Part of Speech Recognition)

Description: The part_check function returns a part of speech based on the given word.

    Function: part_check(word: Any, multi: str = 'main') -> str
    
Example:

##### python
    import awareness
    print(awareness.part_check('car')) # 'noun'

(PL)

### Moduł Case_Updater (Aktualizacja Pliku Słów z Częściami Mowy)

Opis: Funkcja case_updater aktualizuje plik słów z częściami mowy, ale nic nie zwraca.

    Funkcja: case_updater(s: Any) -> None

Przykład:

##### python
    import awareness
    awareness.case_updater('samochód')
    # Aktualizuje plik słów z informacjami o deklinacji słowa 'samochód'

(EN)

### Case_Updater Module (Updating the Word File with Parts of Speech)

Description: The case_updater function updates the part-of-speech word file but returns nothing.

    Function: case_updater(s: Any) -> None
    
Example:

##### python
    import awareness
    awareness.case_updater('car')
    # Updates the word file with information about the declination of the word 'car'

(PL)

### Moduł If_Case (Sprawdzanie, Czy Słowo Jest Deklinacyjne)

Opis: Funkcja if_case sprawdza, czy dane słowo jest deklinacyjne, tj. czy odmienia się przez przypadki.

    Funkcja: if_case(word: Any) -> bool
    
Przykład:

##### python
    import awareness
    print(awareness.if_case('samochód'))  # True
    print(awareness.if_case('być'))  # False

(EN)

### If_Case Module (Checking Whether a Word Is Declinational)

Description: The if_case function checks whether a given word is declensional, i.e. whether it is inflected by cases.

    Function: if_case(word: Any) -> bool
    
Example:

##### python
    import awareness
    print(awareness.if_case('car')) # True
    print(awareness.if_case('be')) # False

(PL)

### Moduł Change_Cases (Odmiana Słowa przez Przypadki)

Opis: Funkcja change_cases zwraca informacje o odmianie podanego rzeczownika lub zwraca pożądaną odmianę.

    Funkcja: change_cases(w: Any, truck: str = 'BACK', update: str = 'YES', opt: str = 'MIA') -> Any

Przykład:

##### python
    import awareness
    print(awareness.change_cases('samochód', truck='BACK', opt='DOP', update='NO'))
    # ['samochodu']

(EN)

### Change_Cases Module (Word Inflection by Cases)

Description: The change_cases function returns information about the declination of the given noun or returns the desired 
declination.

    Function: change_cases(in: Any, truck: str = 'BACK', update: str = 'YES', opt: str = 'MIA') -> Any

Example:

##### python
    import awareness
    print(awareness.change_cases('car', truck='BACK', opt='DOP', update='NO'))
    # ['car']

(PL)

### Moduł Noun_Adj_Case_Detector (Wykrywanie Rzeczowników i Przymiotników w Zdaniu)

Opis: Funkcja noun_adj_case_detector wykrywa rzeczowniki i przymiotniki w podanym zdaniu i określa ich przypadek, liczbę i rodzaj, 
w przypadku przymiotników również zaprzeczenia.

    Funkcja: noun_adj_case_detector(sentence: Any) -> dict

Przykład:

##### python
    import awareness
    print(awareness.noun_adj_case_detector('stary samochód toczy się wolno'))
    # {'stary': 'MIA-LP-MRZ-POZ', 'samochód': 'LP-MIA', 'toczy': False, 'się': False, 'wolno': False}

(EN)

### Noun_Adj_Case_Detector Module (Detecting Nouns and Adjectives in a Sentence)

Description: The noun_adj_case_detector function detects nouns and adjectives in the given sentence and determines their case, number and gender, and in the case of adjectives, also their negation.

    Function: noun_adj_case_detector(sentence: Any) -> dict

Example:

##### python
    import awareness
    print(awareness.noun_adj_case_detector('old car rolls slowly'))
    # {'old': 'MIA-LP-MRZ-POZ', 'car': 'LP-MIA', 'rolling': False, 'running': False, 'slow': False}

(PL)

### Moduł Change_Case_SP (Odmiana Słowa przez Przypadki z Korektą)

Opis: Funkcja change_case_SP odmienia słowo przez przypadki i daje propozycje odmiany z możliwością korekty.

    Funkcja: change_case_SP(base: Any, word: Any, target: str = 'rzeczownik', manual: bool = True) -> Any
    
Przykład:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(awareness.change_case_SP(base, 'rower'))

(EN)
### Change_Case_SP Module (Word Conjugation by Cases with Correction)

Description: The change_case_SP function inflects a word by case and provides inflection suggestions with the possibility of correction.

    Function: change_case_SP(base: Any, word: Any, target: str = 'noun', manual: bool = True) -> Any
    
Example:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(awareness.change_case_SP(base, 'bicycle'))

(PL)

### Moduł Change_Cases_SP_Adjective (Odmiana Przymiotników z Korektą)

Opis: Funkcja change_cases_SP_adjective zarządza przymiotnikami w systemie, odmienia przymiotniki przez przypadki i zwraca informacje o przymiotniku.

    Funkcja: change_cases_SP_adjective(base: Any, word: Any, truck: str = 'BACK', opt: str = 'MIA', numb: str = 'LM', rodz: str = 'MOS', direct: str = 'POZ', target: str = 'przymiotnik', update: str = 'YES') -> (dict | Any | dict[str, list] | Literal['Nieodmienialny', 'MAKE-UPDATE'] | None)

Przykład:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(awareness.change_cases_SP_adjective(base, 'rowerowy', truck='BACK', numb='LM', rodz='MOS', direct='NEG', target='przymiotnik', update='YES'))

(EN)

### Module Change_Cases_SP_Adjective (Conjugation of Adjectives with Correction)

Description: The change_cases_SP_adjective function manages adjectives in the system, inflects adjectives by case, and returns information about the adjective.

    Function: change_cases_SP_adjective(base: Any, word: Any, truck: str = 'BACK', opt: str = 'MIA', numb: str = 'LM', genus: str = 'MOS', direct: str = 'POZ' ', target: str = 'adjective', update: str = 'YES') -> (dict | Any | dict[str, list] | Literal['Unchangeable', 'MAKE-UPDATE'] | None)

Example:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(awareness.change_cases_SP_adjective(base, 'bicycle', truck='BACK', numb='LM', genus='MOS', direct='NEG', target='adjective', update='YES'))

(PL)

### Moduł Part_Speech_2 (Zapisywanie Pliku Systemowego Części Mowy)

Opis: Funkcja part_Speech_2 zapisuje plik systemowy cases_words_noun.neural.

    Funkcja: part_Speech_2(word: Any) -> bool
    
Przykład:

##### python
    import awareness
    print(awareness.part_Speech_2('rower'))  # True

(EN)

### Part_Speech_2 Module (Saving Part of Speech System File)

Description: The part_Speech_2 function writes the cases_words_noun.neural system file.

    Function: part_Speech_2(word: Any) -> bool

Example:

##### python
    import awareness
    print(awareness.part_Speech_2('bicycle')) # True

(PL)

### Moduł Two_Way_Words (Słowa Dwubiegunowe)

Opis: Funkcja two_way_words oddaje słowa dwubiegunowe, czyli słowa, które posiadają przeciwieństwa.

    Funkcja: two_way_words(word: Any) -> dict[str, Any]

Przykład:

##### python
    import awareness
    result = awareness.two_way_words('wadliwy')
    print(result['RESULT'])  # True
    print(result['WORD'])    # Przeciwieństwo słowa 'wadliwy'
    print(result['WORDS'])   # Wszystkie słowa obsługiwane przez funkcję
    Rezultat:
    result['RESULT']: True (znaleziono słowo dwubiegunowe).
    result['WORD']: nieskazitelny (drugie biegunowe słowo do 'wadliwy').
    result['WORDS']: Lista zawierająca wszystkie słowa, które mają przeciwieństwa i są obsługiwane przez funkcję.

Moduł Ten pozwala na znalezienie słów, które posiadają swoje przeciwieństwa, co może być przydatne w różnych analizach językowych lub generowaniu treści.

(EN)

### Two_Way_Words Module

Description: The two_way_words function returns bipolar words, i.e. words that have opposites.

    Function: two_way_words(word: Any) -> dict[str, Any]
    
Example:

##### python
    import awareness
    result = awareness.two_way_words('faulty')
    print(result['RESULT']) # True
    print(result['WORD']) # Opposite of 'defective'
    print(result['WORDS']) # All words supported by the function
    Result:
    result['RESULT']: True (bipolar word found).
    result['WORD']: flawless (second polar word to 'defective').
    result['WORDS']: A list containing all words that have opposites and are supported by the function.

This module allows you to find words that have their opposites, which can be useful in various language analyzes or content generation.

(PL)

### Moduł Take_Target (Słowa z Rodziny)

Opis: Funkcja take_target oddaje wszystkie słowa w formie listy, które należą do rodziny słowa docelowego.

    Funkcja: take_target(w: Any, target: str = 'czasownik') -> (Any | list[str])
    
Przykład:

##### python
    import awareness
    print(awareness.take_target('rower', 'rzeczownik'))
    
Rezultat: 

    Lista słów, które należą do rodziny słowa 'rower'.

(EN)

### Take_Target Module (Family Words)

Description: The take_target function returns all words in a list that belong to the target word family.

    Function: take_target(in: Any, target: str = 'verb') -> (Any | list[str])
    
Example:

##### python
    import awareness
    print(awareness.take_target('bicycle', 'noun'))

Result: 

    A list of words that belong to the word 'bicycle' family.

(PL)

### Moduł Take_SuperTarget (Słowo Główne Rodziny)

Opis: Funkcja take_superTarget robi to samo co take_target, ale znacznie szybciej i potrzebuje słownika z bazy systemu Awareness. Funkcja również może oddać tylko słowo główne rodziny słowa docelowego.

    Funkcja: take_superTarget(base: Any, word: Any, target: str = 'czasownik', what: str = 'WORDS-LISTS') -> Any

Przykład:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(awareness.take_superTarget(base, 'rowerem', 'rzeczownik', what='MAIN-WORDS'))
    print(awareness.take_superTarget(base, 'rower', 'rzeczownik', what='WORDS-LISTS'))
    
Rezultat:

    take_superTarget(base, 'rowerem', 'rzeczownik', what='MAIN-WORDS'): Zwraca słowo główne rodziny słowa 'rowerem'.
    take_superTarget(base, 'rower', 'rzeczownik', what='WORDS-LISTS'): Zwraca listę słów, które należą do rodziny słowa 'rower'.

Moduły te pozwalają na pobieranie słów z rodziny wybranego słowa lub na szybkie uzyskanie słowa głównego rodziny.

(EN)

### Take_SuperTarget Module (Family Root Word)

Description: The take_superTarget function does the same thing as take_target, but much faster and requires a dictionary from the Awareness database. The function can also return only the root word of the target word family.

    Function: take_superTarget(base: Any, word: Any, target: str = 'verb', what: str = 'WORDS-LISTS') -> Any

Example:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(awareness.take_superTarget(base, 'by bike', 'noun', what='MAIN-WORDS'))
    print(awareness.take_superTarget(base, 'bicycle', 'noun', what='WORDS-LISTS'))
    
Result:

    take_superTarget(base, 'by bike', 'noun', what='MAIN-WORDS'): Returns the root word of the word family 'by bike'.
    take_superTarget(base, 'bicycle', 'noun', what='WORDS-LISTS'): Returns a list of words that belong to the word family 'bicycle'.

These modules allow you to retrieve words from the family of a selected word or to quickly obtain the root word of the family.

(PL)

### Moduł Verb_Flex (Odmiana Czasowników)

Opis: Funkcja verb_flex służy do odmiany czasowników. Może zamienić czasownik w dowolnej formie na dowolną formę lub oddać całą rodzinę odmienionych czasowników wraz z przypisanymi flagami.

    Funkcja: verb_flex(base: Any, w: Any, option: str = 'TAKE', mode: Any | None = None) -> Any

Przykład:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(awareness.verb_flex(base, 'wysunąć', option='TAKE'))
    print(awareness.verb_flex(base, 'wysunąć', option='CHANGE', mode='IIos-LM-PRZP-PRZE-NONE'))
    print(awareness.verb_flex(base, 'wysunąć', option='ALL'))

Rezultat:

    option='TAKE': Zwraca bazową formę czasownika (bezokolicznik).
    option='CHANGE': Zamienia czasownik 'wysunąć' na formę 'wysunęliśmy' zgodnie z podanym trybem (mode).
    option='ALL': Opcja deweloperska, zwraca cały zbiór rodziny danego czasownika odmieniony w grupie fleksyjnej.

(EN)

### Verb_Flex (Verb Conjugation) Module

Description: The verb_flex function is used to conjure verbs. It can convert a verb in any form into any form or return an entire family of conjugated verbs with assigned flags.

    Function: verb_flex(base: Any, w: Any, option: str = 'TAKE', mode: Any | None = None) -> Any

Example:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(awareness.verb_flex(base, 'extend', option='TAKE'))
    print(awareness.verb_flex(base, 'eject', option='CHANGE', mode='IIos-LM-PRZP-PRZE-NONE'))
    print(awareness.verb_flex(base, 'extrude', option='ALL'))

Result:

    option='TAKE': Returns the base form of the verb (infinitive).
    option='CHANGE': Changes the verb 'to extend' to the form 'we advanced' according to the given mode.
    option='ALL': Developer option, returns the entire set of the family of a given verb inflected in the inflection group.

(PL)

### Moduł Set_Gr (Wykrywanie Grupy Fleksyjnej)

Opis: Funkcja set_gr służy do wykrywania grupy fleksyjnej czasownika.

    Funkcja: set_gr(base: Any, w: Any, option: Any | None = None) -> (dict | str)

Przykład:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(awareness.set_gr(base, 'tłuc', option=None))
    print(awareness.set_gr(base, 'robić', option=None))
    
Rezultat:

    Dla 'tłuc': Zwraca XIA, co jest oznaczeniem grupy fleksyjnej.
    Dla 'robić': Zwraca spec, co jest oznacza, że odmiana była dokonywana i odmienione formy istnieją w systemie.

Moduły te umożliwiają odmianę czasowników oraz wykrywanie grupy fleksyjnej czasownika, co jest przydatne w analizach gramatycznych i generowaniu treści.

(EN)

### Set_Gr Module (Inflectional Group Detection)

Description: The set_gr function is used to detect the inflection group of a verb.

    Function: set_gr(base: Any, w: Any, option: Any | None = None) -> (dict | str)
    
Example:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(awareness.set_gr(base, 'beat', option=None))
    print(awareness.set_gr(base, 'do', option=None))
    
Result:

    For 'beat': Returns XIA, which is the inflection group designator.
    For 'do': Returns spec, which means that an inflection has been made and inflected forms exist in the system.
    
These modules enable verb conjugation and detection of the verb's inflection group, which is useful in grammatical analysis and content generation.

(PL)

### Moduł Part_Sentens (Analiza Zdania)

Opis: Funkcja part_sentens służy do analizy zdania i zwraca słownik z analizą jego struktury. W słowniku znajdziesz informacje o podmiocie, orzeczeniu, przydawce, dopełnieniu, okolicznościach orzecznikowych, okolicznościach dopełnienia, zaimkach, przyimkach, nazwach własnych oraz partykułach wraz z odpowiadającymi im symbolami. Funkcja przeprowadza również bardziej szczegółową analizę czasownika.

    Funkcja: part_sentens(base: Any, x_list: Any) -> Any
    
Przykład:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    lista = ['Telefon', 'ma', 'dzwonić', 'cały', 'dzień']
    print(awareness.part_sentens(base, lista))
    
Rezultat:

    Funkcja zwraca słownik z analizą zdania, w którym znajdziesz informacje o różnych elementach składni zdania, takie jak podmiot, orzeczenie, przydawka, dopełnienie, okoliczności orzecznikowe, okoliczności dopełnienia, zaimki, przyimki, nazwy własne i partykuły. Ponadto, jest również analiza czasownika zawierająca takie informacje, jak:
    Rodzaj czasownika (osobowy lub nieosobowy).
    Liczba (pojedyncza lub mnoga).
    Tryb czasownika.
    Czas czasownika.
    Rodzaj czasownika.
    Oznaczenie bezokolicznika czasownika.
    Czy czasownik jest czasownikiem nieprzechodnim.
    Czy czasownik jest w czasie niedokonanym.
    
Funkcja part_sentens pozwala na pełną analizę struktury zdania i czasownika, co jest przydatne w zadaniach analizy tekstu i generowania treści.

(EN)

### Part_Sentens (Sentence Analysis) Module

Description: The part_sentens function is used to analyze a sentence and returns a dictionary with an analysis of its structure. In the dictionary you will find information about the subject, predicate, adverb, object, predicate circumstances, object circumstances, pronouns, prepositions, proper names and particles along with the corresponding symbols. The function also performs a more detailed analysis of the verb.

    Function: part_sentens(base: Any, x_list: Any) -> Any
    
Example:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    list = ['Phone', 'ma', 'call', 'all', 'day']
    print(awareness.part_sentens(base, list))
    
Result:

    The function returns a dictionary with sentence analysis, in which you will find information about various elements of the sentence's syntax, such as subject, predicate, adverb, object, predicate circumstances, object circumstances, pronouns, prepositions, proper names and particles. In addition, there is also a verb analysis including information such as:
    Type of verb (personal or impersonal).
    Number (singular or plural).
    Verb mode.
    Verb tense.
    Type of verb.
    Marking the infinitive of a verb.
    Whether the verb is an intransitive verb.
    Is the verb in the imperfect tense?
The part_sentens function allows for full analysis of sentence and verb structure, which is useful in text analysis and content generation tasks.

(PL)

### Moduł BaseTools (Narzędzia Bazy)

Opis: Moduł BaseTools zawiera funkcje, które umożliwiają manipulację danymi w bazie systemowej. Baza systemowa zawiera informacje o słowach, ich kategoriach gramatycznych, linkach, zbiorach znaczeniowych i innych informacjach związanych z analizą języka naturalnego.

Funkcje ogólne:

    Funkcja: take_base(file_name: str = 'base') -> (dict | dict[str, Any])
    
Opis: Funkcja ładuje bazę systemową z plików systemowych i zwraca ją jako słownik.

Przykład:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(len(base))
    print(type(base))
    
Rezultat: 

    Funkcja zwraca słownik zawierający bazę systemową. Przykładowy wynik zawiera 15 wpisów.

Funkcja: 

    save_base(base: Any) -> Literal[True]
    
Opis: Funkcja zapisuje bazę systemową w katalogu systemowym.

Przykład:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    awareness.save_base(base)
    
Rezultat: 

    Funkcja zwraca informację potwierdzającą zapisanie bazy w katalogu systemowym.

(EN)

### BaseTools Module (Base Tools)

Description: The BaseTools module contains functions that enable data manipulation in the system database. The system database contains information about words, their grammatical categories, links, meaning sets and other information related to natural language analysis.

General Features:

    Function: take_base(file_name: str = 'base') -> (dict | dict[str, Any])
    
Description: The function loads the system database from system files and returns it as a dictionary.

Example:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    print(len(base))
    print(type(base))
    
Result: 

    The function returns a dictionary containing the system database. The sample output contains 15 entries.

    Function: save_base(base: Any) -> Literal[True]
    
Description: The function saves the system database in the system directory.

Example:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    awareness.save_base(base)
    
Result: 

    The function returns information confirming that the database is saved in the system directory.

(PL)

### Funkcje manipulacji danymi w bazie:

    Funkcja: add_word(base: Any, cat: Any, word: Any) -> Any
    
Opis: Funkcja dodaje słowo do bazy z określoną kategorią gramatyczną i zwraca zaktualizowaną bazę.

    Funkcja: add_link(base: Any, cat_id: Any, link_id: Any) -> Any

Opis: Funkcja dodaje link (połączenie) do bazy między słowem a innym elementem i zwraca zaktualizowaną bazę.

    Funkcja: add_se(base: Any, cat_id: Any, se_id: Any) -> Any
    
Opis: Funkcja dodaje zbiór SE (zbioru znaczeń) do słowa w bazie i zwraca zaktualizowaną bazę.

    Funkcja: take_word(base: Any, cat_id: Any) -> (Any | None)
    
Opis: Funkcja zwraca informacje o słowie na podstawie jego symbolu (cat_id) lub None, jeśli słowo nie istnieje w bazie.

    Funkcja: take_LID(base: Any, cat_id: Any) -> (Any | None)

Opis: Funkcja zwraca token dla symbolu (cat_id) lub None, jeśli symbol nie istnieje w bazie.

    Funkcja: join_ids(base: Any, cat_id: Any) -> (Any | None)

Opis: Funkcja łączy linki słowa po symbolach i zwraca listę linków, jeśli symbol istnieje w bazie, lub None, jeśli symbol nie istnieje.

    Funkcja: take_se_words(base: Any, cat_id: Any) -> (Any | None)

Opis: Funkcja zwraca słowa w zbiorze SE (zbiorze znaczeń) na podstawie symbolu (cat_id) lub None, jeśli symbol nie istnieje w bazie.

    Funkcja: take_sa(base: Any, sa_id: Any) -> (Any | None)

Opis: Funkcja zwraca zawartość zbioru SA (zbioru atrybutów) na podstawie jego symbolu (sa_id) lub None, jeśli symbol nie istnieje w bazie.

    Funkcja: take_se(base: Any, se_id: Any) -> (Any | None)

Opis: Funkcja zwraca zbiór SE (zbioru znaczeń) na podstawie jego symbolu (se_id) lub None, jeśli symbol nie istnieje w bazie.

    Funkcja: take_re(base: Any, re_id: Any) -> (Any | None)

Opis: Funkcja zwraca zbiór rankingowy RE (zbioru rankingowego) na podstawie jego symbolu (re_id) lub None, jeśli symbol nie istnieje w bazie.

    Funkcja: take_links(base: Any, cat_id: Any) -> (Any | list)

Opis: Funkcja zwraca linki dla słowa na podstawie jego symbolu (cat_id) lub pustą listę, jeśli słowo nie posiada linków.

    Funkcja: take_sentens(base: Any, cat_id: Any) -> (Any | list | None)

Opis: Funkcja zwraca listę symboli SE (zbioru znaczeń) dla danego słowa na podstawie jego symbolu (cat_id) lub None, jeśli symbol nie istnieje.

    Funkcja: take_id(base: Any, cat: Any, word: Any) -> (str | None)

Opis: Funkcja zwraca symbol (cat_id) dla słowa o określonej kategorii gramatycznej i słowie lub None, jeśli słowo nie istnieje w bazie.

    Funkcja: update_sa(base: Any, sa_id: Any, sa_new_list: Any) -> Any

Opis: Funkcja aktualizuje zbiór SA (zbioru atrybutów) na podstawie symbolu (sa_id) i nowej listy atrybutów, a następnie zwraca zaktualizowaną bazę.

    Funkcja: update_se(base: Any, se_id: Any, se_new_list: Any) -> Any

Opis: Funkcja aktualizuje zbiór SE (zbioru znaczeń) na podstawie symbolu (se_id) i nowej listy znaczeń, a następnie zwraca zaktualizowaną bazę.

    Funkcja: remove_sentens(base: Any, cat_id: Any, se_id: Any) -> Any

Opis: Funkcja usuwa zdanie (symbol SE) z każdego zbioru sentens dla słów, w których to zdanie występuje, na podstawie symbolu zdania (se_id). Zwraca zaktualizowaną bazę.

    Funkcja: remove_link(base: Any, cat_id: Any, link_id: Any) -> Any

Opis: Funkcja usuwa link ze zbioru link w słowach zdania na podstawie symbolu linku (link_id) i zwraca zaktualizowaną bazę.

    Funkcja: join_ids_list(base: Any, ids_list: Any) -> Any

Opis: Funkcja łączy całą listę symboli ze sobą i zwraca wynikową listę.

    Funkcja: remove_word_from_se(base: Any, word: Any, se_id: Any) -> Any

Opis: Funkcja usuwa symbol słowa ze zdania w zbiorze SE (zbiorze znaczeń) na podstawie symbolu słowa (word) i zdania (se_id). Zwraca zaktualizowaną bazę.

    Funkcja: take_lb(base: Any, cat_id: Any, take: str = 'ID') -> (Any | None)

Opis: Funkcja pobiera symbol etykietki (LB) dla danego słowa na podstawie symbolu słowa (cat_id) i opcjonalnie zwraca ID lub całą etykietkę.

    Funkcja: complete_LB(base: Any, word_LB: Any, kind: Any) -> Any

Opis: Funkcja aktualizuje etykietkę LB słowa (word_LB) o wszystkie możliwe formy na podstawie kategorii gramatycznej (kind) i zwraca zaktualizowaną bazę.

To są narzędzia umożliwiające manipulację danymi w bazie systemowej w celu odczytywania, dodawania, aktualizacji i usuwania słów, zdań, kategorii, klasyfikatorów oraz różnych atrybutów.

(EN)

Data manipulation functions in the database:

    Function: add_word(base: Any, cat: Any, word: Any) -> Any

Description: The function adds a word to the database with a specific grammatical category and returns the updated database.

    Function: add_link(base: Any, cat_id: Any, link_id: Any) -> Any

Description: The function adds a link (connection) to the database between a word and another element and returns the updated database.

    Function: add_se(base: Any, cat_id: Any, se_id: Any) -> Any

Description: The function adds a set of SE (set of meanings) to a word in the database and returns the updated database.

    Function: take_word(base: Any, cat_id: Any) -> (Any | None)

Description: The function returns information about a word based on its symbol (cat_id) or None if the word does not exist in the database.

    Function: take_LID(base: Any, cat_id: Any) -> (Any | None)

Description: The function returns a token for the symbol (cat_id) or None if the symbol does not exist in the database.

    Function: join_ids(base: Any, cat_id: Any) -> (Any | None)

Description: The function combines word-by-symbol links and returns a list of links if the symbol exists in the database, or None if the symbol does not exist.

    Function: take_se_words(base: Any, cat_id: Any) -> (Any | None)

Description: The function returns words in the SE set (meaning set) based on the symbol (cat_id) or None if the symbol does not exist in the database.

    Function: take_sa(base: Any, sa_id: Any) -> (Any | None)

Description: The function returns the contents of the SA set (attribute set) based on its symbol (sa_id) or None if the symbol does not exist in the database.

    Function: take_se(base: Any, se_id: Any) -> (Any | None)

Description: The function returns a set of SE (set of meanings) based on its symbol (se_id) or None if the symbol does not exist in the database.

    Function: take_re(base: Any, re_id: Any) -> (Any | None)

Description: The function returns the RE ranking set based on its symbol (re_id) or None if the symbol does not exist in the database.

    Function: take_links(base: Any, cat_id: Any) -> (Any | list)

Description: The function returns links for a word based on its symbol (cat_id) or an empty list if the word has no links.

    Function: take_sentens(base: Any, cat_id: Any) -> (Any | list | None)

Description: The function returns a list of SE symbols (set of meanings) for a given word based on its symbol (cat_id) or None if the symbol does not exist.

    Function: take_id(base: Any, cat: Any, word: Any) -> (str | None)

Description: The function returns a symbol (cat_id) for a word with a specific grammatical category and word, or None if the word does not exist in the database.

    Function: update_sa(base: Any, sa_id: Any, sa_new_list: Any) -> Any

Description: The function updates the SA set (set of attributes) based on the symbol (sa_id) and the new list of attributes, and then returns the updated database.

    Function: update_se(base: Any, se_id: Any, se_new_list: Any) -> Any

Description: The function updates the SE set (set of meanings) based on the symbol (se_id) and the new list of meanings, and then returns the updated database.

    Function: remove_sentens(base: Any, cat_id: Any, se_id: Any) -> Any

Description: The function removes a sentence (SE symbol) from each sentens set for words in which this sentence appears, based on the sentence symbol (se_id). Returns the updated database.

    Function: remove_link(base: Any, cat_id: Any, link_id: Any) -> Any

Description: The function removes a link from the set of links in sentence words based on the link symbol (link_id) and returns the updated database.

    Function: join_ids_list(base: Any, ids_list: Any) -> Any

Description: The function combines the entire list of symbols together and returns the resulting list.

    Function: remove_word_from_se(base: Any, word: Any, se_id: Any) -> Any

Description: The function removes a word symbol from a sentence in the SE set (meaning set) based on the word symbol (word) and the sentence (se_id). Returns the updated database.

    Function: take_lb(base: Any, cat_id: Any, take: str = 'ID') -> (Any | None)

Description: The function retrieves the tag symbol (LB) for a given word based on the word symbol (cat_id) and optionally returns the ID or the entire tag.

    Function: complete_LB(base: Any, word_LB: Any, kind: Any) -> Any

Description: The function updates the word's LB label (word_LB) with all possible forms based on the grammatical category (kind) and returns the updated database.

These are tools that enable manipulation of data in the system database in order to read, add, update and delete words, sentences, categories, classifiers and various attributes.

(PL)

### Funkcja change_part_by_part w bibliotece Awareness służy do zamiany wybranej części zdania na inną w oparciu o identyfikatory zbiorów znaczeń (SE). 

Poniżej znajdziesz opis i sposób użycia tej funkcji:

    Funkcja: change_part_by_part(base: Any, take_se_id: Any, take_part_name: Any, put_se_id: Any, put_as_it: Any, put_case: str = 'MIA', action: str = 'START') -> Any

Opis: Funkcja ta umożliwia zamianę wybranej części zdania na inną część na podstawie identyfikatorów zbiorów znaczeń (SE). Możesz wskazać, którą część zdania chcesz usunąć (take_se_id i take_part_name), a także, którą część chcesz wstawić (put_se_id i put_as_it). Ponadto, można określić przypadki (put_case) oraz sposób, w jaki ma być wykonana zamiana (action).

Parametry:

    base: Baza systemowa.
    take_se_id: Identyfikator zbioru znaczeń, z którego zostanie usunięta wybrana część zdania.
    take_part_name: Nazwa części zdania, która ma zostać usunięta (np. 'PO' dla podmiotu).
    put_se_id: Identyfikator zbioru znaczeń, do którego zostanie wstawiona nowa część zdania.
    put_as_it: Nowa część zdania, którą chcesz wstawić (np. 'DO' dla dopełnienia).
    put_case: Opcjonalny parametr określający przypadek nowej części zdania (domyślnie 'MIA' dla mianownika).
    action: Opcjonalny parametr określający sposób wykonania zamiany (domyślnie 'START').

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    take_se_id = 'SE_150'
    put_se_id = 'SE_1200'
    awareness.change_part_by_part(base, take_se_id, 'PO', put_se_id, 'DO', put_case='DOP', action='START')
    
Funkcja ta pozwala na elastyczną manipulację częściami zdania w zbiorach znaczeń (SE). 

(EN)

### The change_part_by_part function in the Awareness library is used to replace a selected part of a sentence with another one based on meaning set identifiers (SE). 

Below you will find a description and how to use this function:

    Function: change_part_by_part(base: Any, take_se_id: Any, take_part_name: Any, put_se_id: Any, put_as_it: Any, put_case: str = 'MIA', action: str = 'START') -> Any

Description: This function allows you to replace a selected part of a sentence with another part based on the meaning set identifiers (SE). You can indicate which part of the sentence you want to remove (take_se_id and take_part_name) and also which part you want to insert (put_se_id and put_as_it). Moreover, you can specify cases (put_case) and how the replacement is to be performed (action).

Parameters:

    base: System base.
    take_se_id: The identifier of the meaning set from which the selected part of the sentence will be removed.
    take_part_name: The name of the part of the sentence to be removed (e.g. 'PO' for subject).
    put_se_id: The identifier of the meaning set into which the new part of the sentence will be inserted.
    put_as_it: The new part of the sentence you want to insert (e.g. 'DO' for object).
    put_case: Optional parameter specifying the case of the new part of the sentence (default 'MIA' for nominative case).
    action: Optional parameter specifying how to perform the replacement (default 'START').

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    take_se_id = 'SE_150'
    put_se_id = 'SE_1200'
    awareness.change_part_by_part(base, take_se_id, 'PO', put_se_id, 'DO', put_case='DOP', action='START')
    
This feature allows flexible manipulation of sentence parts in meaning sets (SE).

(PL)

### Funkcja advanced_action w bibliotece Awareness służy do dodawania zdań złożonych do bazy systemowej oraz przypisywania tych zdań do kategorii w zbiorze znaczeń SA. 

Poniżej znajdziesz opis i sposób użycia tej funkcji:

    Funkcja: advanced_action(base: Any, full_text: Any, source: str = 'wiki', word: str = 'nieznane') -> Any
    
Opis: Funkcja ta umożliwia dodawanie zdań złożonych do bazy systemowej, a także przypisywanie ich do kategorii w zbiorze znaczeń SA. Możesz określić źródło dodawanych zdań (source) oraz nazwę kategorii, do której mają być przypisane związane z nimi zdania (word).

Parametry:

    base: Baza systemowa.
    full_text: Pełny tekst zawierający złożone zdania do dodania do bazy.
    source: Opcjonalny parametr określający źródło dodawanych zdań (domyślnie 'automatic'). Możliwe opcje: 'automatic', 'manual', 'wiki'.
    word: Opcjonalny parametr, który dotyczy przypisywania kategorii do zdań w przypadku źródła 'manual' (domyślnie 'nieznane'). Wprowadź nazwę kategorii, do której mają być przypisane związane z nimi zdania.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    few_sentences = 'Kilka długich zdań. Mogą być wielokrotnie złożone. Funkcja rozpozna poszczególne części zdania, podzieli na zdania podrzędne i inne. Następnie dopisze do kategorii z zbiorze SA, wszystkie zdania oraz zbuduje dla nich dane.'
    awareness.advanced_action(base, few_sentences, source='automatic')
    # source = 'automatic', 'manual', 'wiki' (sposób przydzielania kategorii SA)
    # word = 'nieznane' dotyczy źródła 'manual', należy wpisać kategorię
    
Funkcja ta pozwala na dodawanie i przypisywanie kategorii złożonych zdań do bazy systemowej, co może być przydatne do dalszych analiz i przetwarzania tekstów.

(EN)

### The advanced_action function in the Awareness library is used to add complex sentences to the system database and assign these sentences to categories in the SA meaning set. 

Below you will find a description and how to use this function:

    Function: advanced_action(base: Any, full_text: Any, source: str = 'wiki', word: str = 'unknown') -> Any
    
Description: This function allows you to add complex sentences to the system database and assign them to categories in the SA meaning set. You can specify the source of the added sentences (source) and the name of the category to which the related sentences are to be assigned (word).

Parameters:

    base: System base.
    full_text: Full text containing complex sentences to be added to the database.
    source: Optional parameter specifying the source of added sentences (default 'automatic'). Possible options: 'automatic', 'manual', 'wiki'.
    word: Optional parameter that concerns assigning categories to sentences in the case of the 'manual' source (default 'unknown'). Enter the name of the category to which the related sentences should be assigned.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    few_sentences = 'A few long sentences. They can be folded many times. The function will recognize individual parts of the sentence and divide it into subordinate and other sentences. Then it will add all sentences to the categories from the SA set and build data for them.'
    awareness.advanced_action(base, few_sentences, source='automatic')
    # source = 'automatic', 'manual', 'wiki' (how to assign SA categories)
    # word = 'unknown' refers to the source 'manual', please enter the category
    
This function allows you to add and assign categories of complex sentences to the system database, which may be useful for further analyzes and text processing.

(PL)

    Funkcja: action(base: Any, sentens: Any, se_id: Any | None = None, option: str = 'all') -> (Any | dict[str, Any] | None)
    
Opis: Funkcja action jest używana do analizy zdania. Przyjmuje zdanie jako tekst i zwraca wynik analizy w postaci listy symboli reprezentujących składniki zdania. Może również dodawać zdanie do bazy systemowej, jeśli zostanie podane jako se_id.

Parametry:

    base: Baza systemowa.
    sentens: Tekst zdania do analizy.
    se_id: Opcjonalny parametr określający, do którego zbioru SE należy dodać analizowane zdanie (domyślnie None).
    option: Opcjonalny parametr określający, co zwróci funkcja (domyślnie 'all'). Możliwe opcje: 'all', 'only_se_done', 'only_se_new', 'only_se_now', 'only_se_old'.
    
Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.action(base, 'Doświadczony górnik spokojnie odkrywa kolejne złoża miedzi')
    print(result)
    
Przykład wyniku:

    ['PR_729', 'PO_8059', 'OZ_5969', 'OR_14456', 'OK_1147', 'DO_1982', 'DO_4557']
    
Funkcja action analizuje zdanie i zwraca listę symboli składających się na to zdanie. Może być używana do analizy tekstu i dodawania go do bazy systemowej w celu dalszej analizy.

(EN)

    Function: action(base: Any, sentens: Any, se_id: Any | None = None, option: str = 'all') -> (Any | dict[str, Any] | None)
    
Description: The action function is used to parse a sentence. It accepts a sentence as text and returns the parse result as a list of symbols representing the components of the sentence. It can also add a sentence to the system database if given as se_id.

Parameters:

    base: System base.
    sentens: The text of the sentence to be analyzed.
    se_id: Optional parameter specifying to which SE set the analyzed sentence should be added (default: None).
    option: Optional parameter specifying what the function will return (default 'all'). Possible options: 'all', 'only_se_done', 'only_se_new', 'only_se_now', 'only_se_old'.
    
How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.action(base, 'An experienced miner calmly discovers further copper deposits')
    print(result)
    
Result example:

    ['PR_729', 'PO_8059', 'OZ_5969', 'OR_14456', 'OK_1147', 'DO_1982', 'DO_4557']
    
The action function parses a sentence and returns a list of symbols that make up that sentence. It can be used to analyze text and add it to the system database for further analysis.

(PL)

    Funkcja: splitSententionNum(sentention: Any) -> tuple[list, set, dict[str, Any]
    
Opis: Funkcja splitSententionNum jest używana do analizy i podziału zdania na zdania podrzędne, nadrzędne i równoległe. Przyjmuje zdanie jako tekst i zwraca wynik podziału w formie krotki, która zawiera listę zdan podrzędnych, zbiór zdan nadrzędnych i słownik z informacjami na temat zdan równoległych.

Parametry:

    sentention: 
        Tekst zdania do analizy i podziału.
        
Sposób użycia:

##### python
    import awareness
    sentention = "Doświadczony górnik spokojnie odkrywa kolejne złoża miedzi, a jego kolega bada ich zawartość."
    result = awareness.splitSententionNum(sentention)
    print(result)
    
Przykład wyniku:

    (['Doświadczony górnik spokojnie odkrywa kolejne złoża miedzi', 'a jego kolega bada ich zawartość'], {'a jego kolega bada ich zawartość'}, {1: ['a jego kolega bada ich zawartość']})

Funkcja splitSententionNum analizuje zdanie i dokonuje jego podziału na zdania podrzędne, nadrzędne i równoległe, a następnie zwraca wynik w formie krotki. Zdania podrzędne są przechowywane w liście, zdania nadrzędne w zbiorze, a zdania równoległe w słowniku. 

(EN)

    Function: splitSentenceNum(sentention: Any) -> tuple[list, set, dict[str, Any]

Description: The splitSentenceNum function is used to parse and divide a sentence into subordinate, superordinate and parallel sentences. It accepts a sentence as text and returns the result of the division as a tuple that contains a list of subordinate sentences, a set of parent sentences, and a dictionary with information about parallel sentences.

Parameters:

    senttention: 
        Sentence text to analyze and divide.
        
How to use:

##### python
    import awareness
    senttention = "An experienced miner calmly discovers further copper deposits, and his colleague examines their contents."
    result = awareness.splitSentenceNum(sentention)
    print(result)
    
Result example:

    (['An experienced miner calmly discovers further copper deposits', 'and his colleague examines their contents'], {'and his colleague examines their contents'}, {1: ['his colleague examines their contents']})
    
The splitSentenceNum function parses a sentence and splits it into child, parent, and parallel sentences, and then returns the result as a tuple. Subordinate sentences are stored in a list, parent sentences in a set, and parallel sentences in a dictionary.

(PL)

    Funkcja: make_OS(base: Any, se_id: Any, oso: str = 'Ios-LP-NDKTER-DKPRZY', frend: str = 'PR', main: str = 'PO', neubor: str = 'ZAI') -> str | None
    
Opis: Funkcja make_OS służy do zmiany wybranych zdań w bazie zdaniowej SE na wybraną formę czasownika w zdaniach nadrzędnych. Przyjmuje identyfikator zbioru SE, formę czasownika oso, symbol relacji dla zdania nadrzędnego frend, symbol relacji dla zdania głównego main oraz symbol relacji dla zdania nadrzędnego zdania nadrzędnego neubor.

Parametry:

    base: Baza systemowa, która zawiera zbiory SE.
    se_id: Identyfikator zbioru SE, w którym chcesz dokonać zmiany.
    oso: Forma czasownika, na jaką chcesz zamienić zdania w zbiorze SE. Domyślnie ustawiona na 'Ios-LP-NDKTER-DKPRZY'.
    frend: Symbol relacji dla zdania nadrzędnego. Domyślnie ustawiony na 'PR'.
    main: Symbol relacji dla zdania głównego. Domyślnie ustawiony na 'PO'.
    neubor: Symbol relacji dla zdania nadrzędnego zdania nadrzędnego. Domyślnie ustawiony na 'ZAI'.
    
Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    se_id = 'SE_150'
    result = awareness.make_OS(base, se_id, oso='IIos-LM-DKTOI-DKPRZY', frend='SPO', main='PR', neubor='KON')
    print(result)

Funkcja make_OS pozwala na modyfikację zdaniowego zbioru SE w bazie systemowej, zamieniając zdania na wybraną formę czasownika i ustalając odpowiednie relacje między zdaniem nadrzędnym, zdaniem głównym i zdaniem nadrzędnym zdania nadrzędnego. 

(EN)

    Function: make_OS(base: Any, se_id: Any, oso: str = 'Ios-LP-NDKTER-DKPRZY', frend: str = 'PR', main: str = 'PO', neubor: str = 'ZAI') -> p | None
    
Description: The make_OS function is used to change selected sentences in the SE sentence database to the selected verb form in the parent sentences. It takes the set identifier SE, the verb form oso, the relation symbol for the parent clause frend, the relation symbol for the main clause main, and the relation symbol for the parent clause of the parent clause neubor.

Parameters:

    base: The system database that contains the SE files.
    se_id: The ID of the SE file you want to change.
    oso: The verb form you want to convert the sentences into in SE. Default is set to 'Ios-LP-NDKTER-DKPRZY'.
    frend: Relationship symbol for the parent clause. Default set to 'PR'.
    main: Relationship symbol for the main sentence. Default set to 'PO'.
    neubor: Relationship symbol for the parent clause of a parent clause. Default set to 'ZAI'.
    
How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    se_id = 'SE_150'
    result = awareness.make_OS(base, se_id, oso='IIos-LM-DKTOI-DKPRZY', frend='SPO', main='PR', neubor='KON')
    print(result)
    
The make_OS function allows you to modify the SE sentence set in the system database, replacing the sentences with the selected verb form and establishing appropriate relationships between the parent clause, the main clause and the parent clause of the parent clause.

(PL)

    Funkcja: synonimus_sentenses(base: Any, sentens_list: Any) -> Any
    
Opis: Funkcja synonimus_sentenses zwraca synonimy dla słów w podanym zdaniu. Przyjmuje bazę systemową base oraz listę słów w zdaniu sentens_list.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base()
    sentens_list = ['historia', 'pisze', 'się', 'sama']
    result = awareness.synonimus_sentenses(base, sentens_list)
    print(result)

Przykład wyniku:

    {'DICT': {0: ['historia', 'pisze', 'się', 'sam'], 1: ['historia', 'pisze', 'się', 'jednakowy'], ...}, 'LIST': [['historia', 'pisze', 'się', 'sam'], ['historia', 'pisze', 'się', 'jednakowy'], ...], 'STRINGES': ['historia pisze się sam', 'historia pisze się jednakowy', …]}

(EN)

    Function: synonymus_sentenses(base: Any, sentens_list: Any) -> Any
    
Description: The synonymus_sentenses function returns synonyms for the words in the given sentence. It accepts a system database base and a list of words in the sentens_list sentence.

How to use:

##### python
    import awareness
    base = awareness.take_base()
    sentens_list = ['history', 'is writing', 'itself', 'itself']
    result = awareness.synonimus_sentenses(base, sentens_list)
    print(result)
    
Result example:

    {'DICT': {0: ['history', 'writes', 'itself', 'itself'], 1: ['history', 'it writes', 'itself', 'the same'], ...} , 'LETTER': [['history', 'writes', 'itself', 'itself'], ['history', 'it writes', 'itself', 'the same'], ...], 'STRINGES' : ['history writes itself', 'history writes itself', ...]}

(PL)

    Funkcja: neuralSentensPrepare(base: Any) -> dict[str, dict]
    
Opis: Funkcja neuralSentensPrepare przygotowuje zdania do wprowadzenia do sieci neuronowej, zamieniając słowa na tokeny. Zwraca słowniki z informacjami o słownikach słów, kategoriach, identyfikatorach wszystkich zdań i samych zdaniach.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.neuralSentensPrepare(base)
    print(result)
    
Przykład wyniku:

    {'SLOWNIK_SLOW': {...}, 'SLOWNIK_CAT': {...}, 'ALL_SENTENSES_LID': {...}, 'ALL_SENTENSES': {…}}

(EN)

    Function: neuralSentensPrepare(base: Any) -> dict[str, dict]
    
Description: The neuralSentensPrepare function prepares sentences for input into the neural network by converting words into tokens. Returns dictionaries with information about word dictionaries, categories, all sentence IDs, and the sentences themselves.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.neuralSentensPrepare(base)
    print(result)
    
Result example:

    {'SLOWNIK_SLOW': {...}, 'CAT_DICATORIAL': {...}, 'ALL_SENTENSES_LID': {...}, 'ALL_SENTENSES': {...}}
    
(PL)

    Funkcja: stats_se(base: Any, se_id: Any) -> dict[str, int] | dict

Opis: Funkcja stats_se oddaje statystykę dla danego zbioru SE na podstawie identyfikatora se_id. Zwraca słownik z informacjami o liczbie poszczególnych relacji w danym zbiorze.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.stats_se(base, 'SE_100')
    print(result)
    
Przykład wyniku:

    {'PO': 1, 'PR': 3, 'OR': 3, 'DO': 3, 'OK': 0, 'VO': 1, 'OZ': 0, 'ZA': 3, 'HW': 3}

(EN)

    Function: stats_se(base: Any, se_id: Any) -> dict[str, int] | dict
    
Description: The stats_se function returns statistics for a given SE set based on the se_id. Returns a dictionary with information about the number of individual relations in a given set.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.stats_se(base, 'SE_100')
    print(result)
    
Result example:

    {'PO': 1, 'PR': 3, 'OR': 3, 'DO': 3, 'OK': 0, 'VO': 1, 'OZ': 0, 'ZA': 3, ' HW': 3}

(PL)

    Funkcja: golden_se(base: Any, cat_id: Any) -> list

Opis: Funkcja golden_se znajduje tzw. "złote" zdania w zbiorze SE na podstawie identyfikatora kategorii cat_id. Zwraca listę identyfikatorów zdaniowych, które są uważane za szczególnie wartościowe w danej kategorii.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.golden_se(base, 'PO_100')
    print(result)
    
Przykład wyniku:

    ['SE_32509', 'SE_83880', 'SE_58694', 'SE_67428', 'SE_56169', …]

(EN)
    Function: golden_se(base: Any, cat_id: Any) -> list
    
Description: The golden_se function finds the so-called "golden" sentences in the SE set based on the category identifier cat_id. Returns a list of sentence identifiers that are considered particularly valuable in a given category.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.golden_se(base, 'PO_100')
    print(result)
    
Result example:

    ['SE_32509', 'SE_83880', 'SE_58694', 'SE_67428', 'SE_56169', ...]

(PL)

    Funkcja: part_split_IN_OUT(base: Any, cat_id: Any) -> dict[str, set]
    
Opis: Funkcja part_split_IN_OUT zwraca symbole słów poprzedzających i następujących po wybranym słowie na podstawie jego identyfikatora cat_id. Zwraca słownik, gdzie kluczami są 'IN' (słowa poprzedzające) i 'OUT' (słowa następujące), a wartościami są zbiory symboli słów.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.part_split_IN_OUT(base, 'PO_100')
    print(result)
    
Przykład wyniku:

    {'IN': {'VO_13', 'VO_40', 'HW_3', 'PR_625', 'HW_1', ...}, 'OUT': {'ZA_234', 'OZ_43', 'HW_7', 'DO_5654', …}}

(EN)

    Function: part_split_IN_OUT(base: Any, cat_id: Any) -> dict[str, set]
    
Description: The part_split_IN_OUT function returns the symbols of the words preceding and following the selected word based on its cat_id. Returns a dictionary where the keys are 'IN' (words preceding) and 'OUT' (words following), and the values are sets of word symbols.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.part_split_IN_OUT(base, 'PO_100')
    print(result)
    
Result example:
    {'IN': {'VO_13', 'VO_40', 'HW_3', 'PR_625', 'HW_1', ...}, 'OUT': {'ZA_234', 'OZ_43', 'HW_7', 'DO_5654 ', ...}}

(PL)

    Funkcja: find_part_in_SE(base: Any, cat_id: Any) -> list
    
Opis: Funkcja find_part_in_SE zwraca symbole zdań ze zbioru SE (zestawu zdań) w których występuje dane słowo na podstawie identyfikatora cat_id.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.find_part_in_SE(base, 'PO_100')
    print(result)
    
Przykład wyniku:

    ['SE_131', 'SE_1307', 'SE_1378', 'SE_1508', 'SE_2699', …]

(EN)

    Function: find_part_in_SE(base: Any, cat_id: Any) -> list
    
Description: The find_part_in_SE function returns symbols of sentences from the SE set (set of sentences) in which a given word occurs based on the cat_id identifier.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.find_part_in_SE(base, 'PO_100')
    print(result)
    
Result example:

    ['SE_131', 'SE_1307', 'SE_1378', 'SE_1508', 'SE_2699', ...]

(PL)

    Funkcja: part_most_popular(base: Any, item_list: Any, exceping_part: Any | None = None) -> Any | None
    
Opis: Funkcja part_most_popular zwraca najpopularniejsze słowo z listy, na przykład, zbioru SE, pomijając wyjątkowe (jeśli podane) na podstawie identyfikatorów w item_list.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    items = ['PO_100', 'DO_700']
    result = awareness.part_most_popular(base, items, exceping_part='HW')
    print(result)
    
Przykład wyniku:

    PO_100

(EN)

    Function: part_most_popular(base: Any, item_list: Any, exceping_part: Any | None = None) -> Any | None

Description: The part_most_popular function returns the most popular word in a list of, for example, the SE set, omitting unique ones (if provided) based on the identifiers in the item_list.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    items = ['PO_100', 'DO_700']
    result = awareness.part_most_popular(base, items, exceping_part='HW')
    print(result)
    
Result example:

    PO_100

(PL)

    Funkcja: find_se_by_LB(base: Any, LB_id: Any) -> set
    
Opis: Funkcja find_se_by_LB zwraca zbiór symboli zdań SE, w których występuje słowo o podanym symbolu na podstawie identyfikatora LB_id.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.find_se_by_LB(base, 'PO_100')
    print(result)
    
Przykład wyniku:

    {'SE_131', 'SE_2699', 'SE_11883', 'SE_13512', 'SE_45499', ...}

(EN)

    Function: find_se_by_LB(base: Any, LB_id: Any) -> set
    
Description: The find_se_by_LB function returns a set of SE sentence symbols that contain a word with the given symbol based on the LB_id.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.find_se_by_LB(base, 'PO_100')
    print(result)
    
Result example:

    {'SE_131', 'SE_2699', 'SE_11883', 'SE_13512', 'SE_45499', …}

(PL)

    Funkcja: find_se_by_PO(base: Any, PO_id: Any, cat_id: Any) -> set
    
Opis: Funkcja find_se_by_PO zwraca zbiór symboli zdań SE, w których występują dwa słowa jednocześnie - jedno o symbolu PO_id i drugie o symbolu cat_id.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.find_se_by_PO(base, 'PO_100', 'DO_5654')
    print(result)
    
Przykład wyniku:

    {'SE_6138'}

(EN)

    Function: find_se_by_PO(base: Any, PO_id: Any, cat_id: Any) -> set
    
Description: The find_se_by_PO function returns a set of SE sentence symbols in which two words appear at the same time - one with the PO_id symbol and the other with the cat_id symbol.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.find_se_by_PO(base, 'PO_100', 'DO_5654')
    print(result)
    
Result example:

    {'SE_6138'}

(PL)

    Funkcja: find_pharse_in_part(base: Any, word: Any) -> list
    
Opis: Funkcja find_pharse_in_part zwraca listę symboli zdań zawierających dane słowo (jego symbol) na podstawie symbolu słowa word.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.find_pharse_in_part(base, 'kierować')
    print(result)
    
Przykład wyniku:

    ['OR_584']

(EN)

    Function: find_pharse_in_part(base: Any, word: Any) -> list
    
Description: The find_pharse_in_part function returns a list of symbols for sentences containing a given word (its symbol) based on the symbol of the word word.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.find_pharse_in_part(base, 'direct')
    print(result)
    
Result example:

    ['OR_584']

(PL)

    Funkcja: searcher_phrase(base: Any, sentens: Any) -> set
    
Opis: Funkcja searcher_phrase znajduje zdania, w których występuje podana fraza (słowa oddzielone spacjami).

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.searcher_phrase(base, 'użyć siły')
    print(result)
    
Przykład wyniku:

    {'SE_36750', 'SE_54847', 'SE_51866', 'SE_81097', 'SE_11900', …}

(EN)

    Function: searcher_phrase(base: Any, sentens: Any) -> set
    
Description: The searcher_phrase function finds sentences that contain the given phrase (words separated by spaces).

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.searcher_phrase(base, 'use force')
    print(result)
    
Result example:

    {'SE_36750', 'SE_54847', 'SE_51866', 'SE_81097', 'SE_11900', …}

(PL)

    Funkcja: stats_part(base: Any, cat_id: Any) -> dict
    
Opis: Funkcja stats_part zwraca statystykę dla danego symbolu słowa na podstawie identyfikatora cat_id. Statystyka zawiera informacje na temat liczby zdań, linków, symboli wchodzących i wychodzących, oraz łącznej liczby symboli.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.stats_part(base, 'PO_100')
    print(result)
    
Przykład wyniku:

    {'SENTENS': 21, 'LINKS': 21, 'PART-IN': 7, 'PART-OUT': 13, 'TOTAL': 62}

(EN)

    Function: stats_part(base: Any, cat_id: Any) -> dict
    
Description: The stats_part function returns statistics for a given word symbol based on the cat_id. Statistics include information on the number of sentences, links, incoming and outgoing symbols, and the total number of symbols.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.stats_part(base, 'PO_100')
    print(result)
    
Result example:

    {'SENTENS': 21, 'LINKS': 21, 'PART-IN': 7, 'PART-OUT': 13, 'TOTAL': 62}

(PL)

    Funkcja: generator_AI_most_popular(base: Any, cat_start_id: Any, no_words: int = 5, exceping_part: Any | None = None) -> dict

Opis: Funkcja generator_AI_most_popular zwraca string wygenerowanego zdania i listę symboli dla wygenerowanych słów. Generuje zdanie na podstawie symbolu słowa cat_start_id, używając najpopularniejszych słów (z wyjątkiem tych podanych w exceping_part) jako kontekstu. Możesz określić ilość słów w generowanym zdaniu za pomocą no_words.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.generator_AI_most_popular(base, 'PO_100')
    print(result)
    
Przykład wyniku:

    {'STRING': 'różnica w to', 'ID': ['PO_100', 'ZA_3', 'HW_1']}

(EN)
    
    Function: generator_AI_most_popular(base: Any, cat_start_id: Any, no_words: int = 5, exceping_part: Any | None = None) -> dict

Description: The generator_AI_most_popular function returns a string of the generated sentence and a list of symbols for the generated words. Generates a sentence based on the word symbol cat_start_id, using the most common words (except those provided in exceping_part) as context. You can specify the number of words in the generated sentence using no_words.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.generator_AI_most_popular(base, 'PO_100')
    print(result)
    
Result example:

    {'STRING': 'difference in', 'ID': ['PO_100', 'ZA_3', 'HW_1']}

(PL)

    Funkcja: generator_AI_se(base: Any, seed: str) -> str

Opis: Funkcja generator_AI_se generuje zdanie według określonego schematu odpowiadającego symbolom części zdania. Możesz określić schemat zdania jako ciąg symboli części zdania, np. 'PO, OR, ZA, OK, DO', a funkcja wygeneruje zdanie według tego schematu.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.generator_AI_se(base, 'samochód', 'PO, OR, ZA, OK, DO')
    print(result)
    
Przykład wyniku:

    samochód lub całkowicie samochód

(EN)

    Function: generator_AI_se(base: Any, seed: str) -> str
    
Description: The generator_AI_se function generates a sentence according to a specific pattern corresponding to the symbols of the sentence parts. You can define a sentence schema as a sequence of sentence part symbols, e.g. 'PO, OR, FOR, OK, DO', and the function will generate a sentence according to this schema.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.generator_AI_se(base, 'car', 'PO, OR, ZA, OK, DO')
    print(result)
    
Result example:

    car or completely car

(PL)

    Funkcja: check_list_to_list(list_a: list, list_b: list) -> bool
    
Opis: Funkcja check_list_to_list porównuje dwie listy ze sobą i zwraca True, jeśli przynajmniej jeden element jest wspólny, lub False, jeśli nie ma wspólnych elementów.

Sposób użycia:

##### python
    import awareness
    list_a, list_b = ([1, 2, 3], [3, 4, 5])
    result = awareness.check_list_to_list(list_a, list_b)
    print(result)
    
Przykład wyniku:

    True

(EN)

    Function: check_list_to_list(list_a: list, list_b: list) -> bool

Description: The check_list_to_list function compares two lists with each other and returns True if at least one element is common, or False if there are no common elements.

How to use:

##### python
    import awareness
    list_a, list_b = ([1, 2, 3], [3, 4, 5])
    result = awareness.check_list_to_list(list_a, list_b)
    print(result)
    
Result example:

    True

(PL)

    Funkcja: sentens_generator_AI(base: Any, seed: str) -> dict

Opis: Funkcja sentens_generator_AI generuje zdania na podstawie podanej frazy jako ziarna. Fraza może zawierać słowa oddzielone spacjami. Funkcja zwraca listę wygenerowanych zdań oraz słownik DICT-ID, który pozwala powiązać wygenerowane zdania z symbolami słów użytych w tych zdaniach.

Sposób użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.sentens_generator_AI(base, 'łączy dwa zdania ze sobą')
    print(result)
    
Przykład wyniku:

    {'LIST': ['Orzeczenie to część zdania w którym się znajduje , lub o procesie , któremu podlega.', 'Zdania informująca o w nim możliwości lub kilka naraz.', 'Dwa jej w celu uzyskania potomstwa dziedziczącego nowe cechy.', 'Łączy się w związku chemicznym.'], 'DICT-ID': {'łączy się w': ['OR_430', 'ZA_5', 'ZA_3'], 'dwa jej': ['OZ_70', 'ZA_80', 'ZA_3'], 'dwa przedmioty': ['PR_723', 'DO_184', 'ZA_3'], 'dwa miejsca': ['OK_10', 'DO_12', 'ZA_3'], 'zdania w': ['DO_71', 'ZA_3'], 'zdania informująca w': ['OR_12276', 'OK_2680', 'ZA_11', 'ZA_3']}, 'SENTENS': 'łączy dwa zdania ze sobą', 'WORDS': {'łączy': ['DO_14670', 'OR_430'], 'dwa': ['OZ_70', 'PR_723', 'OK_10'], 'zdania': ['DO_71', 'OR_12276'], 'ze': ['ZA_243'], 'sobą': ['ZA_115']}}

(EN)

    Function: sentens_generator_AI(base: Any, seed: str) -> dict
    
Description: The sentens_generator_AI function generates sentences based on the given phrase as a seed. A phrase can contain words separated by spaces. The function returns a list of generated sentences and a DICT-ID dictionary that allows you to associate the generated sentences with the symbols of the words used in these sentences.

How to use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.sentens_generator_AI(base, 'connects two sentences together')
    print(result)
    
Result example:

    {'LIST': ['A predicate is part of a sentence in which it is found, or about a process to which it is subject.', 'A sentence informing about a possibility in it or several at once.', 'Two of them in order to obtain offspring inheriting new features.', 'Combines in a chemical compound.'], 'DICT-ID': {'combines in': ['OR_430', 'ZA_5', 'ZA_3'], 'two hers': ['OZ_70', 'ZA_80' , 'ZA_3'], 'two items': ['PR_723', 'DO_184', 'ZA_3'], 'two places': ['OK_10', 'DO_12', 'ZA_3'], 'sentences in': [ 'DO_71', 'ZA_3'], 'sentence informing in': ['OR_12276', 'OK_2680', 'ZA_11', 'ZA_3']}, 'SENTENS': 'connects two sentences together', 'WORDS': {'connects': ['DO_14670', 'OR_430'], 'two': ['OZ_70', 'PR_723', 'OK_10'], 'sentences': ['DO_71', 'OR_12276'], 'with' : ['ZA_243'], 'myself': ['ZA_115']}}

(PL)

    Funkcja: save_ver(project_name: str, var_name: str, data: Any) -> bool

Opis: Funkcja save_ver służy do zapisywania danych w określonym projekcie. Dane są skojarzone z określoną nazwą zmiennej var_name w projekcie o nazwie project_name. Zapisuje dowolne struktury danych takie jak string, lista, set, słownik itp.

Sposób użycia:

##### python
    import awareness
    var = 'String'
    result = awareness.save_ver('project_Name', 'ver', var)
    print(result)
    
Przykład wyniku:

    True

(EN)

    Function: save_ver(project_name: str, var_name: str, data: Any) -> bool

Description: The save_ver function is used to save data to a specific project. Data is associated with a specific variable name var_name in the project called project_name. Saves any data structures such as string, list, set, dictionary, etc.

How to use:

##### python
    import awareness
    var = 'String'
    result = awareness.save_ver('project_Name', 'ver', var)
    print(result)

Result example:

    True

(PL)

    Funkcja: open_all(project_name: str) -> dict

Opis: Funkcja open_all otwiera wszystkie dane zapisane w określonym projekcie o nazwie project_name i zwraca je jako słownik, gdzie klucze to nazwy zmiennych, a wartości to dane skojarzone z tymi zmiennymi.

Sposób użycia:

##### python
    import awareness
    result = awareness.open_all('project_Name')
    print(result)
    
Przykład wyniku:

    {'ver': 'String'}

(EN)

    Function: open_all(project_name: str) -> dict

Description: The open_all function opens all data stored in a specific project named project_name and returns it as a dictionary, where keys are variable names and values are data associated with those variables.

How to use:

##### python
    import awareness
    result = awareness.open_all('project_Name')
    print(result)
    
Result example:

    {'ver': 'String'}

(PL)

    Funkcja: open_ver(project_name: str, var_name: str) -> Any

Opis: Funkcja open_ver służy do otwierania wybranych danych z projektu. Możesz podać nazwę projektu project_name i nazwę zmiennej var_name, a funkcja zwróci dane skojarzone z tą nazwą zmiennej w projekcie.

Sposób użycia:

##### python
    import awareness
    result = awareness.open_ver('project_Name', 'ver')
    print(result)
    
Przykład wyniku:

    'String'

(EN)

    Function: open_ver(project_name: str, var_name: str) -> Any

Description: The open_ver function is used to open selected data from the project. You can provide a project name project_name and a variable name var_name, and the function will return the data associated with that variable name in the project.

How to use:

python
    import awareness
    result = awareness.open_ver('project_Name', 'ver')
    print(result)
    
Result example:

    'String'

(PL)

    Funkcja: delete_project(project_name: str) -> bool

Opis: Funkcja delete_project służy do usuwania całego projektu wraz z zapisanymi danymi. Jeśli projekt o nazwie project_name istnieje, zostanie usunięty, a funkcja zwróci True. W przeciwnym przypadku zwróci False.

Sposób użycia:

##### python
    import awareness
    result = awareness.delete_project('project_Name')
    print(result)
    
Przykład wyniku:

    True

(EN)

    Function: delete_project(project_name: str) -> bool
    
Description: The delete_project function is used to delete the entire project along with saved data. If a project named project_name exists, it will be deleted and the function will return True. Otherwise it will return False.

How to use:

##### python
    import awareness
    result = awareness.delete_project('project_Name')
    print(result)
    
Result example:

    True

(PL)

    Funkcja: delete_ver(project_name: str, var_name: str) -> bool
    
Opis: Funkcja delete_ver służy do usuwania danych skojarzonych z określoną nazwą zmiennej var_name w projekcie o nazwie project_name. Jeśli nazwa zmiennej i projektu istnieje, to dane zostaną usunięte, a funkcja zwróci True. W przeciwnym przypadku zwróci False.

Sposób użycia:

##### python
    import awareness
    result = awareness.delete_ver('project_Name', 'ver')
    print(result)
    
Przykład wyniku:

    True

Te funkcje pozwalają na zapisywanie, odczytywanie i zarządzanie danymi w projektach.

(EN)

    Function: delete_ver(project_name: str, var_name: str) -> bool

Description: The delete_ver function is used to delete data associated with the specified var_name variable name in a project named project_name. If the variable and project names exist, the data will be deleted and the function will return True. Otherwise it will return False.

How to use:

##### python
    import awareness
    result = awareness.delete_ver('project_Name', 'ver')
    print(result)
    
Result example:

    True

These functions allow you to save, read and manage data in your projects.

(PL)

### Funkcja part_speach jest używana do rozpoznawania rodzaju części mowy słowa. 

Oto przykład jej użycia:

##### python
    import awareness
    result = awareness.part_speach('samochód')
    print(result)
    
Przykład wyniku:

    [['rzeczownik', 'samochód']]

Funkcja zwraca listę, gdzie pierwszym elementem jest rozpoznany rodzaj części mowy (np. 'rzeczownik'), a drugim elementem jest analizowane słowo (np. 'samochód'). Możesz używać tej funkcji, aby analizować części mowy różnych słów w tekście

(EN)

### The part_speach function is used to recognize the type of part of speech of a word. 

Here is an example of its use:

##### python
    import awareness
    result = awareness.part_speach('car')
    print(result)
    
Result example:

    [['noun', 'car']]
    
The function returns a list, where the first element is the recognized type of part of speech (e.g. 'noun'), and the second element is the word being analyzed (e.g. 'car'). You can use this feature to analyze the parts of speech of different words in text


(PL)
### Funkcja dicson_brain służy do uzyskiwania zestawu danych dotyczących podanego zdania. 

Oto przykład jej użycia:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.dicson_brain(base, 'co robi samochód')
    print(result)
    
Przykład wyniku:

    {
      'ASK-LIST': ['ZA_19', 'OR_2120', 'DO_11952'],
      'OPERATION': {
        'SE_20270': [      ['PO_5344', 'OZ_1796', 'DO_4634'],
          ['OR_2120'],
          ['PO_4230', 'DO_4634', 'OZ_394', 'ZA_3', 'DO_11410', 'ZA_108', 'DO_11411', 'DO_4634', 'OZ_4220']
        ],
        'SE_8387': [      ['PO_2', 'DO_7007'],
          ['OR_2120'],
          ['PO_1', 'HW_2', 'ZA_3', 'ZA_4', 'OR_2', 'DO_6', 'OK_1', 'ZA_3', 'DO_7', 'DO_8', 'DO_9']
        ],
        'SE_3': [      ['PO_2', 'OZ_2'],
          ['OR_2120'],
          ['PO_1', 'OR_4', 'ZA_2', 'DO_10', 'DO_11', 'HW_3', 'VO_1']
        ],
        'SE_2': [      ['PO_2'],
          ['OR_2120'],
          ['PO_1', 'HW_2', 'ZA_3', 'ZA_4', 'OR_2', 'DO_6', 'OK_1', 'ZA_3', 'DO_7', 'DO_8', 'DO_9']
        ],
        'SE_1': [      ['PO_2'],
          ['OR_2120'],
          ['PO_3', 'ZA_1', 'DO_1', 'OZ_1', 'DO_2', 'HW_2', 'PO_4', 'ZA_2', 'DO_3', 'DO_4', 'HW_3', 'DO_5']
        ]
      },
      'TECHNICAL': {
        'SE_20270': [      'PO_5344', 'OZ_1796', 'DO_4634', 'OR_2120', 'PO_4230', 'DO_4634', 'OZ_394', 'ZA_3', 'DO_11410', 'ZA_108', 'DO_11411', 'DO_4634', 'OZ_4220'    ],
        'SE_8387': [      'PO_2', 'DO_7007', 'OR_2120', 'PO_1', 'HW_2', 'ZA_3', 'ZA_4', 'OR_2', 'DO_6', 'OK_1', 'ZA_3', 'DO_7', 'DO_8', 'DO_9'    ],
        'SE_3': [      'PO_2', 'OZ_2', 'OR_2120', 'PO_1', 'OR_4', 'ZA_2', 'DO_10', 'DO_11', 'HW_3', 'VO_1'    ],
        'SE_2': [      'PO_2', 'OR_2120', 'PO_1', 'HW_2', 'ZA_3', 'ZA_4', 'OR_2', 'DO_6', 'OK_1', 'ZA_3', 'DO_7', 'DO_8', 'DO_9'    ],
        'SE_1': [      'PO_2', 'OR_2120', 'PO_3', 'ZA_1', 'DO_1', 'OZ_1', 'DO_2', 'HW_2', 'PO_4', 'ZA_2', 'DO_3', 'DO_4', 'HW_3', 'DO_5'    ]
      },
      'ANSWERS-LIST': [    'Samochód pułapka robi samochód , w którym podłożono materiał wybuchowy w celu dokonania zamachu ',    'Samochód robi samochód , w którym podłożono materiał wybuchowy w celu dokonania zamachu ',    'Samochód sanitarny robi samochód przystosowany do przewożenia chorych lub rannych ',    'Samochód robi pojazd na kołach napędzany silnikiem , służący do przewozu osób lub ładunków ',    'Przegląd zerowy samochodu robi przegląd samochodu dokonywany w salonie przed wydaniem samochodu kupującemu '  ],
      'RANDOM-ANSWER': 'Samochód robi samochód , w którym podłożono materiał wybuchowy w celu dokonania zamachu ',
      'FOUND': True
    }
    
Funkcja zwraca zestaw danych zawierający listę symboli, operacje związków między symbolami, dane techniczne, listę odpowiedzi oraz wybraną odpowiedź losową.


(EN)

### The dicson_brain function is used to obtain a set of data about the given sentence. 

Here is an example of its use:

##### python
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    result = awareness.dicson_brain(base, 'what the car does')
    print(result)
    
Result example:

    {
       'ASK-LIST': ['ZA_19', 'OR_2120', 'DO_11952'],
       'OPERATION': {
         'SE_20270': [ ['PO_5344', 'OZ_1796', 'DO_4634'],
           ['OR_2120'],
           ['PO_4230', 'DO_4634', 'OZ_394', 'ZA_3', 'DO_11410', 'ZA_108', 'DO_11411', 'DO_4634', 'OZ_4220']
         ],
         'SE_8387': [ ['PO_2', 'DO_7007'],
           ['OR_2120'],
           ['PO_1', 'HW_2', 'ZA_3', 'ZA_4', 'OR_2', 'DO_6', 'OK_1', 'ZA_3', 'DO_7', 'DO_8', 'DO_9']
         ],
         'SE_3': [ ['PO_2', 'OZ_2'],
           ['OR_2120'],
           ['PO_1', 'OR_4', 'ZA_2', 'DO_10', 'DO_11', 'HW_3', 'VO_1']
         ],
         'SE_2': [ ['PO_2'],
           ['OR_2120'],
           ['PO_1', 'HW_2', 'ZA_3', 'ZA_4', 'OR_2', 'DO_6', 'OK_1', 'ZA_3', 'DO_7', 'DO_8', 'DO_9']
         ],
         'SE_1': [ ['PO_2'],
           ['OR_2120'],
           ['PO_3', 'ZA_1', 'DO_1', 'OZ_1', 'DO_2', 'HW_2', 'PO_4', 'ZA_2', 'DO_3', 'DO_4', 'HW_3', 'DO_5']
         ]
       },
       'TECHNICAL': {
         'SE_20270': [ 'PO_5344', 'OZ_1796', 'DO_4634', 'OR_2120', 'PO_4230', 'DO_4634', 'OZ_394', 'ZA_3', 'DO_11410', 'ZA_108', 'DO_11411', ' DO_4634', 'OZ_4220' ],
         'SE_8387': [ 'PO_2', 'DO_7007', 'OR_2120', 'PO_1', 'HW_2', 'ZA_3', 'ZA_4', 'OR_2', 'DO_6', 'OK_1', 'ZA_3', ' DO_7', 'DO_8', 'DO_9' ],
         'SE_3': [ 'PO_2', 'OZ_2', 'OR_2120', 'PO_1', 'OR_4', 'ZA_2', 'DO_10', 'DO_11', 'HW_3', 'VO_1' ],
         'SE_2': [ 'PO_2', 'OR_2120', 'PO_1', 'HW_2', 'ZA_3', 'ZA_4', 'OR_2', 'DO_6', 'OK_1', 'ZA_3', 'DO_7', ' DO_8', 'DO_9' ],
         'SE_1': [ 'PO_2', 'OR_2120', 'PO_3', 'ZA_1', 'DO_1', 'OZ_1', 'DO_2', 'HW_2', 'PO_4', 'ZA_2', 'DO_3', ' DO_4', 'HW_3', 'DO_5' ]
       },
       'ANSWERS-LIST': ['A car trap makes a car in which an explosive was planted in order to commit an attack', 'A car trap makes a car in which an explosive was planted in order to commit an attack', 'The sanitary car makes a car adapted to transport sick people or injured ', 'A car is a vehicle on wheels powered by an engine, used to transport people or loads', 'Zero car inspection is an inspection of the car carried out in the showroom before handing over the car to the buyer' ],
       'RANDOM-ANSWER': 'Car makes a car in which an explosive was planted to commit an attack',
       'FOUND': True
    }

The function returns a data set containing a list of symbols, symbol relationship operations, technical data, a list of responses, and a selected random response.
