phrase = input()
letter_list = []
prints = []
FROM=0  # Индексы в массиве animations
TO=1
ANIMATION=2
animations = [
	#      FROM                     TO                 ANIMATION
	["злой_открытый рот.svg", 'нейтрзакр.svg', "злой-открытый-закрытый.svg"],
	['нейтрзакр.svg', 'нейтральный1(полуоткрытый_рот).svg', 'нейтрзакр-нейтрполуоткр.svg'],
	['нейтральный1(полуоткрытый_рот).svg', 'нейтрзакр.svg', 'нейтрполуоткр-нейтрзакр.svg']
	#      FROM                     TO                 ANIMATION
]
LETTERS=0  # Индекс в массиве mouth
SVG=1  # Индекс в массивах mouth и prints
mouth = [
	#  LETTERS            SVG
	["бмпую ", 'нейтрзакр.svg'],
	["агкядтэн", "злой_открытый рот.svg"],
	['еийывфохчцжшщёзс', 'нейтральный1(полуоткрытый_рот).svg']
	#  LETTERS            SVG
]
ONLY_MATCH=0  # нулевой (единственный) элемент
LAST=-1  # Индекс последнего элемента любого массива
TIME=0  # Индекс в массиве prints
for c in phrase:
    letter_list.append(c)
# Добавление закрытого рта перед словом:
prints.append([41, 'нейтрзакр.svg'])
# Добавление закрытого рта после слова с помощью добавления символа "пробел", которому в массиве mouth соответствует 'нейтрзакр.svg':
letter_list.append(" ")
for l in letter_list:
	mouth_matches = [line for line in mouth if l in line[LETTERS]]  # Взять какие-то из строк mouth, у которых нулевой элемент (строка) - LETTERS - содержит букву из l
	match = mouth_matches[ONLY_MATCH][SVG]  # Взять нулевое единственное совпадение и в нем взять имя файла
	if prints[LAST][SVG] == match:
		prints[LAST][TIME] += 41
	else:
		anim_matches = [line for line in animations if line[FROM]==prints[LAST][SVG] and line[TO]==match]  # Взять какие-то из строк animations, у которых нулевой элемент - FROM -(из какого положения рта перейти) совпадает с текущим (prints[-1]), а первый элемент - TO - (в какое положение рта перейти) совпадает с требуемым
		if len(anim_matches) == 0:
		    raise Exception("В animations не найдена запись FROM='%s' TO='%s'" % (prints[LAST][SVG], match))
		anim = anim_matches[ONLY_MATCH][ANIMATION]  # Взять нулевое единственное совпадение и в нем взять имя файла анимации
		prints.append([14, anim])
		prints.append([27, match])
# Печать итогового списка таймингов и SVG-файлов:
for x in prints:
	print(x)
