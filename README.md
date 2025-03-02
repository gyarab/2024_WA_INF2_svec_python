# 2024_WA_INF2_svec_python

Repozitář obsahuje jednoduchý CMS vytvořený v Django

Na webu se nachází informace o 10 významných bitvách z 19. století a dá se jednoduše proklikávat a vybírat si témata podle názvů bitev nebo válek v kterých se bitvy odehráli. Při výběru názvu bitvy je uživateli ukázán obrázek (např. dobový obraz bitvy) se základními informacemi a jednoduchým popisem. V seznamu těchto základních informací se nachází rok, kdy se bitva odehrála, název regionu a státu, který tento region vlastnil, jednoduchý popis, počet obětí, <ins>název války</ins> a <ins> odkaz na obsáhlejší text o taktice a průběhu bitvy </ins>.

Obě poslední položky umožňují se uživateli prokliknout dále. Při kliknutí na název války je uživatel přesměrován na obecné znalosti o válce a mapu zobrazující jednotlivé strany války. Obecné znalosti o válce jsou dostupné už z homepage, kde pod názvem bitvy je menším písmem uveden název války. Odkaz na obsáhlejší text o taktikách a průběhu bitvy je dostupný pod názvem "Taktiky bitvy u '_____'. Při kliknutí je uživatel přesměrován k mapě bojiště a jednotek, které bojovali a pod mapou se nachází text.

Web je postaven pomocí templatů, které slouží k snížení repetetivnosti kódu a lepšímu třídění jednotlivých částí webu. Všechny údaje jsou obsaženy v souboru articles.json, kde jsou kategorie "context" a "tactics" vygenerované AI a zbytek textů jsou mé vlastní.

Seznam potřebných knihoven se nachází v souboru "requirements.txt".

**Autor** Marek Švec 3.E

