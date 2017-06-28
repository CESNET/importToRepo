# Automatický import dát
Import dát prebieha z Open Enventory.

Implementácia samostatného skriptu, ktorý sa stara o automatický
import dát do repozitára, s napojením priamo na databázu. V samotnom
Open Enventory je v tomto prípade potrebné umiestnit tlacidlo, ktoré
spustí tento skript a odovzdá mu parametre potrebné pre import (teda
id reakcie alebo laboratórneho denníka, ktorý chce užívatel importovat
do repozitára).

## Nastavenie pripojenia k DB
V settings.py je potrebne nastavit pristupove udaje k databazi Open Enventory a pripojenie k repozitaru.

## Volanie
Zavolanim manage.py tasku importToRepo s parametrom id reakcie.

Samotny import obsluhuje metoda
```python
class ImportReaction:
    def import_reaction(self, reaction_id, user):
```