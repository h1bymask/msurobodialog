from articulation import click_face, speak_and_articulate, click_eyes
 
await click_eyes("eyes/глаза_нейтральный1.svg")
await speak_and_articulate("привет. Нет, а что случилось")

await click_eyes("eyes/глаза_нейтральный1.svg")
await speak_and_articulate("и это все Я и так не собирался готовиться, там же все элементарно")

await click_eyes("eyes/глаза_злой.svg")
await speak_and_articulate("не повышай на меня голос!")

await click_eyes("eyes/глаза_улыбающийся1.svg")
await speak_and_articulate("пойдем лучше в столовую, я угощаю!")