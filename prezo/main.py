def face(key):  # PageUp, Enter, q, w, e, r, t, y, " ", ...
	if key== "PageUp":
		slide("slides/злой.svg")
	elif key =="PageDown":
		slide("slides/нейтральный1.svg")
	else:
		slide("slides/грустный.svg")
		
def get_articulations(phrase):
	letter_list = []
	articulations = []
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
	SVG=1  # Индекс в массивах mouth и articulations
	mouth = [
		#  LETTERS            SVG
		["бмпую ", 'нейтрзакр.svg'],
		["агкядтэн", "злой_открытый рот.svg"],
		['еийывфохчцжшщёзс', 'нейтральный1(полуоткрытый_рот).svg']
		#  LETTERS            SVG
	]
	ONLY_MATCH=0  # нулевой (единственный) элемент
	LAST=-1  # Индекс последнего элемента любого массива
	TIME=0  # Индекс в массиве articulations
	for c in phrase:
		letter_list.append(c)
	# Добавление закрытого рта перед словом:
	articulations.append([41, 'нейтрзакр.svg'])
	# Добавление закрытого рта после слова с помощью добавления символа "пробел", которому в массиве mouth соответствует 'нейтрзакр.svg':
	letter_list.append(" ")
	for l in letter_list:
		mouth_matches = [line for line in mouth if l in line[LETTERS]]  # Взять какие-то из строк mouth, у которых нулевой элемент (строка) - LETTERS - содержит букву из l
		match = mouth_matches[ONLY_MATCH][SVG]  # Взять нулевое единственное совпадение и в нем взять имя файла
		if articulations[LAST][SVG] == match:
			articulations[LAST][TIME] += 41
		else:
			anim_matches = [line for line in animations if line[FROM]==articulations[LAST][SVG] and line[TO]==match]  # Взять какие-то из строк animations, у которых нулевой элемент - FROM -(из какого положения рта перейти) совпадает с текущим (articulations[-1]), а первый элемент - TO - (в какое положение рта перейти) совпадает с требуемым
			if len(anim_matches) == 0:
				raise Exception("В animations не найдена запись FROM='%s' TO='%s'" % (articulations[LAST][SVG], match))
			anim = anim_matches[ONLY_MATCH][ANIMATION]  # Взять нулевое единственное совпадение и в нем взять имя файла анимации
			articulations.append([14, anim])
			articulations.append([27, match])
	# Печать итогового списка таймингов и SVG-файлов:
	for x in articulations:
		print(x)
	return articulations
	
def speak_and_articulate(phrase):
	play("speech/" + phrase + ".wav")
	for (time, file) in get_articulations():
		articulation(time, "articulation/" + file)
	wait_audio()

slide("лого_персиковый.svg")
face(read_key())
speak_and_articulate("можете забрать завтрак, приятного аппетита")

articulation(82, "articulation/нейтрзакр.svg")
articulation(14, "articulation/нейтрзакр-нейрполуоткр.svg")
articulation(68, "articulation/нейтральный1(полуоткрытый_рот).svg")
articulation(14, "articulation/нейтрполуоткр-злойоткр.svg")
articulation(27, "articulation/нейтральный2(открытый_рот).svg")
articulation(14, "articulation/злойоткр-нейрполуоткр.svg")
articulation(27, "articulation/нейтральный1(полуоткрытый_рот).svg")
articulation(14, "articulation/нейтр-полуоткрытый-закрытый.svg")
articulation(27, "articulation/нейтрзакр.svg")
articulation(82, "articulation/нейтрзакр.svg")
articulation(14, "articulation/нейтрзакр-нейрполуоткр.svg")
articulation(68, "articulation/нейтральный1(полуоткрытый_рот).svg")
articulation(14, "articulation/нейтрполуоткр-злойоткр.svg")
articulation(27, "articulation/нейтральный2(открытый_рот).svg")
articulation(14, "articulation/злойоткр-нейрполуоткр.svg")
articulation(27, "articulation/нейтральный1(полуоткрытый_рот).svg")
articulation(14, "articulation/нейтр-полуоткрытый-закрытый.svg")
articulation(27, "articulation/нейтрзакр.svg")

read_key()

slide("slides/слайд1.svg")


face(read_key())
play("speech/выберите, что вам нужно сделать.wav")
articulation(500, "articulation/нейтрзакр-нейтрполуоткр.svg")
articulation(500, "articulation/нейтр-полуоткрытый-закрытый.svg")
 
read_key()

articulation(0, "пусто.svg")
slide("slides/слайд3.svg")
 
read_key()

slide("slides/слайд5.svg")
play("speech/приложите палец.wav")
wait_audio()


face(read_key())
play("speech/можете забрать лекарства.wav")
articulation(500, "articulation/нейтрзакр-нейтрполуоткр.svg")
articulation(500, "articulation/нейтр-полуоткрытый-закрытый.svg")

read_key()

articulation(0, "пусто.svg")
slide("slides/слайд7.svg")
	
face(read_key())
play("speech/выберите, что вы хотите сделать.wav")
articulation(500, "articulation/нейтрзакр-нейтрполуоткр.svg")
articulation(500, "articulation/нейтр-полуоткрытый-закрытый.svg")
 
articulation(0, "пусто.svg")
slide("slides/слайд9.svg")


face(read_key())
play("speech/можете забрать завтрак, приятного аппетита.wav")
articulation(500, "articulation/нейтрзакр-нейтрполуоткр.svg")
articulation(500, "articulation/нейтр-полуоткрытый-закрытый.svg")

articulation(0, "пусто.svg")
slide("slides/слайд11.svg")


face(read_key())
play("speech/выберите, что вы хотите сделать.wav")
articulation(500, "articulation/нейтрзакр-нейтрполуоткр.svg")
articulation(500, "articulation/нейтр-полуоткрытый-закрытый.svg")

articulation(0, "пусто.svg")
slide("slides/слайд13.svg")


face(read_key())
play("speech/выберите, что вам нужно сделать.wav")
articulation(500, "articulation/нейтрзакр-нейтрполуоткр.svg")
articulation(500, "articulation/нейтр-полуоткрытый-закрытый.svg")
 
articulation(0, "пусто.svg")
slide("slides/слайд15.svg")

face(read_key())
play("speech/выберите, что вам нужно сделать.wav")
articulation(500, "articulation/нейтрзакр-нейтрполуоткр.svg")
articulation(500, "articulation/нейтр-полуоткрытый-закрытый.svg")


face(read_key())
play("speech/media8.wav")
articulation(500, "articulation/нейтрзакр-нейтрполуоткр.svg")
articulation(500, "articulation/злой-открытый-закрытый.svg")

articulation(0, "пусто.svg")
slide("slides/слайд19.svg")


face(read_key())
play("speech/media10.wav")
articulation(82, "articulation/нейтрзакр.svg")
articulation(14, "articulation/нейтрзакр-нейрполуоткр.svg")
articulation(68, "articulation/нейтральный1(полуоткрытый_рот).svg")
articulation(14, "articulation/нейтрполуоткр-злойоткр.svg")
articulation(27, "articulation/нейтральный2(открытый_рот).svg")
articulation(14, "articulation/злойоткр-нейрполуоткр.svg")
articulation(27, "articulation/нейтральный1(полуоткрытый_рот).svg")
articulation(14, "articulation/нейтр-полуоткрытый-закрытый.svg")
articulation(27, "articulation/нейтрзакр.svg")

read_key()

articulation(0, "пусто.svg")
slide("slides/слайд21.svg")

articulation(0, "пусто.svg")
slide("slides/слайд22.svg")

read_key()

articulation(0, "пусто.svg")
slide("slides/слайд23.svg")


face(read_key())
play("speech/изменения сохранены.wav")
articulation(500, "articulation/нейтрзакр-нейтрполуоткр.svg")
articulation(500, "articulation/нейтр-полуоткрытый-закрытый.svg")

articulation(0, "пусто.svg")
slide("slides/слайд25.svg")

read_key() 

# articulation(500, "нейтрзакр.svg")
# articulation(500, "злойоткр-нейрполуоткр.svg")
# read_key()
# articulation(500, "нейтрполуоткр-злойоткр.svg")
# read_key()
# articulation(500, "злой-открытый-закрытый.svg")
# read_key()
# articulation(500, "злойоткр-нейрполуоткр.svg")
# read_key()
# articulation(500, "нейтрзакр-нейтрполуоткр.svg")
# read_key()
# articulation(500, "нейтр-полуоткрытый-закрытый.svg")
