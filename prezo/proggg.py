phrase = input()
letter_list = []
prints = []
articulation = [
	["злой_открытый рот.svg", "нейтрзакр.svg", "злой-открытый-закрытый.svg"],
	['нейтрзакр.svg', 'нейтральный1(полуоткрытый_рот).svg', 'нейтрзакр-нейтрполуоткр.svg']
]
mouth = [
	["бмпую ", "нейтрзакр.svg"],
	["агкядтэн", "злой_открытый рот.svg"],
	['еийывфохчцжшщёзс', 'нейтральный1(полуоткрытый_рот).svg']
]
for c in phrase:
    letter_list.append(c)
letter_list.append(" ")
prints.append({"svg": "нейтрзакр.svg", "time": 41})
for l in letter_list:
	mouth_matches = [line for line in mouth if l in line[0]]  # взять какие-то из строк mouth, у которых нулевой элемент (строка) содержит букву из l
	match = mouth_matches[0][1]  # взять нулевое совпадение и в нем взять имя файла
	if prints[-1]["svg"] == match:
		prints[-1]["time"] += 41
	else:
		anim_matches = [line for line in articulation if line[0]==prints[-1]["svg"] and line[1]==match]  # взять какие-то из строк articulation, у которых нулевой элемент (из какого положения рта перейти) совпадает с текущим (prints[-1]), а первый элемент (в какое положение рта перейти) совпадает с требуемым
		anim = anim_matches[0][2]  # взять нулевое совпадение и в нем взять имя файла анимации
		prints.append({"svg": anim, "time":14})
		prints.append({"svg": match, "time":27})		
for x in prints:
	print(x)