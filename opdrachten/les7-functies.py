# In de vorige opdrachten heb je een stuk code geschreven dat telt hoeveel klinkers er in een stuk tekst staan
# > Herschrijf dit nu naar een functie die het aantal teruggeeft
# > Voorbeeld:
# >>> print(tel_klinkers('Dit is een string'))
# >>> 5

# > Pas deze functie aan zodat je zelf mee kan geven naar welke letters er gezocht moet worden, en dat de functie teruggeeft hoe vaak deze letters (totaal) in de string staan (dus niet per letter).
# > Voorbeeld:
# >>> print(tel_letters('Dit is een string', 's'))
# >>> 2
# OF
# >>> print(tel_letters('Dit is een string', 'is'))
# >>> 1

# > Schrijf een functie die als argument een lijst meekrijgt en een lijst teruggeeft met alle even getallen uit de originele lijst
# Voorbeeld:
# >>> print(alleen_even_getallen([1,2,3,4,5,6,7,8]))
# >>> [2,4,6,8]

# Een pangram is een stuk tekst dat alle letters uit het alfabet bevat: 'The quick brown fox jumps over the lazy dog' is er één, en 'Sphinx of Black Quartz, judge my vow!' ook. In het Nederlands 'Pa's wijze lynx bezag vroom het fikse aquaduct' of 'Doch vlakbij zwerft 'n exquis gympje'.
# > Schrijf een functie die als argument een string meekrijgt en checkt of deze een pangram is. Let op hoofdlettergevoeligheid!
# > Voorbeeld:
# >>> print(check_pangram('Dit is een string'))
# >>> False
# >>> print(check_pangram('Doch vlakbij zwerft 'n exquis gympje'))
# >>> True

# > Maak een functie die checkt of een lijst gesorteerd is.
# > Voorbeeld:
# >>> print(is_gesorteerd([1,5,4]))
# >>> False
# >>> print(is_gesorteerd([1,4,5]))
# >>> True

# > Maak een functie die een lijst met random nummers genereert. Deze functie krijgt mee hoe veel getallen in de lijst moeten komen, en tussen welke waardes
# Gebruik hiervoor de volgende functie: randint
# Deze kan je importeren uit de random library
# met de volgende regel code:
from random import randint
# > Je kunt nu de randint(..) functie gebruiken
# > Dit doe je door randint(min, max)
# LET OP: de max is inclusief, dus randint(0,10) kan ook 10 teruggeven


def genereer_lijst(aantal_getallen, min, max):
	lijst = []
	# Vul hier je eigen code in
	# Je mag de code die er al staat ook aanpassen
	return lijst


# > Gebruik deze twee laatste functies om net zolang lijsten van 10 nummers tussen de 0 en 5 te genereren tot er een gesorteerde lijst uit komt. Print deze lijst, en tel eventueel hoeveel lijsten er gegenereerd moesten worden voordat je een gesorteerde lijst had.
