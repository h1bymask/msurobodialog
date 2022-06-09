from browser import document, window, aio

LONG_SOUNDS=".-"

def on_press_key(key):  # key.code: PageUp, Enter, q, w, e, r, t, y, " ", ...
	if key.code == "PageUp":
		window.slide("slides/злой.svg")
	elif key.code == "PageDown":
		window.slide("slides/грустный.svg")
document.bind("keydown", on_press_key)

async def enter_face():
	await window.wait_key("Enter")
	window.slide("slides/нейтральный1.svg")

def get_articulations(phrase):
	letter_list = []
	articulations = []
	FROM=0  # Индексы в массиве animations
	TO=1
	ANIMATION=2
	animations = [
		#      FROM                     TO                 ANIMATION
		['злой_открытый рот.svg', 'нейтрзакр.svg', 'злой-открытый-закрытый.svg'],
		['нейтрзакр.svg', 'нейтральный1(полуоткрытый_рот).svg', 'нейтрзакр-нейтрполуоткр.svg'],
		['нейтрзакр.svg', 'злой_открытый рот.svg', 'злой-открытый-закрытый.svg'],  ## Исправить название файла анимации
		['нейтральный1(полуоткрытый_рот).svg', 'нейтрзакр.svg', 'нейтр-полуоткрытый-закрытый.svg'],
		['нейтральный1(полуоткрытый_рот).svg', 'злой_открытый рот.svg', 'нейтрполуоткр-злойоткр.svg'],
		['злой_открытый рот.svg', 'нейтральный1(полуоткрытый_рот).svg', 'злойоткр-нейрполуоткр.svg']
		#      FROM                     TO                 ANIMATION
	]
	LETTERS=0  # Индекс в массиве mouth
	SVG=1  # Индекс в массивах mouth и articulations
	LETTER=0  # Индекс в массиве articulations
	mouth = [
		#  LETTERS            SVG
		["бмлпую ", 'нейтрзакр.svg'],
		["агкядтэн", "злой_открытый рот.svg"],
		['еийывфохчцжшщёзс', 'нейтральный1(полуоткрытый_рот).svg']
		#  LETTERS            SVG
	]
	ONLY_MATCH=0  # нулевой (единственный) элемент
	LAST=-1  # Индекс последнего элемента любого массива
	TIME=2  # Индекс в массиве articulations
	for c in phrase.lower().translate(str.maketrans("","","ьъыр,?!@#$%^&*()[]{}№=+_`'~\\/0123456789")):
		letter_list.append(c)
	## Добавление закрытого рта перед словом:
	articulations.append([" ", 'нейтрзакр.svg', 0])
	# Добавление закрытого рта после слова с помощью добавления символа "пробел", которому в массиве mouth соответствует 'нейтрзакр.svg':
	letter_list.append(" ")
	for l in letter_list:
		if l in LONG_SOUNDS:
			if len(articulations) == 0:
				articulations.append([" ", 'нейтрзакр.svg', 5*(14+27)])
			else:
				articulations[LAST][TIME] += 5*(14+27)
		else:
			mouth_matches = [line for line in mouth if l in line[LETTERS]]  # Взять какие-то из строк mouth, у которых нулевой элемент (строка) - LETTERS - содержит букву из l
			match = mouth_matches[ONLY_MATCH][SVG]  # Взять нулевое единственное совпадение и в нем взять имя файла
			if articulations[LAST][SVG] == match:
				articulations[LAST][TIME] += 14+27
				articulations[LAST][LETTER] += l
			else:
				anim_matches = [line for line in animations if line[FROM]==articulations[LAST][SVG] and line[TO]==match]  # Взять какие-то из строк animations, у которых нулевой элемент - FROM -(из какого положения рта перейти) совпадает с текущим (articulations[-1]), а первый элемент - TO - (в какое положение рта перейти) совпадает с требуемым
				if len(anim_matches) == 0:
					raise Exception("В animations не найдена запись FROM='%s' TO='%s'" % (articulations[LAST][SVG], match))
				anim = anim_matches[ONLY_MATCH][ANIMATION]  # Взять нулевое единственное совпадение и в нем взять имя файла анимации
				articulations.append([" ", anim, 14])
				articulations.append([l, match, 27])
	articulations.append([" ", 'нейтрзакр.svg', 14+27])
	# Печать итогового списка таймингов и SVG-файлов:
	#print("SVG-файлы и тайминги для фразы '" + phrase + "':")
	totaltime = 0
	for x in articulations:
		#print(x)
		totaltime = totaltime + x[TIME]
	print("Фраза " + phrase + ": продолжительность артикуляции %d мс" % totaltime)
	return articulations
	
async def speak_and_articulate(phrase):
	window.play("speech/" + phrase.translate(str.maketrans("","",LONG_SOUNDS)) + ".wav")
	for (letter, file, time) in get_articulations(phrase):
		await window.articulation(time, "articulation/" + file)
	# TODO: Too long articulation even if audio is twice as fast. Too long SVG loading?
	await window.wait_audio()
