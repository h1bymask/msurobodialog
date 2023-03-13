from articulation import click_face, speak_and_articulate, click_eyes


await click_eyes("eyes/глаза_улыбающийся1.svg")
await speak_and_articulate("привет, ты видел, что вчера написали в группу")

await click_eyes("eyes/глаза_улыбающийся1.svg")
await speak_and_articulate("зачета завтра не будет, его перенесли на субботу!")
 
await click_eyes("eyes/глаза_злой.svg")
await speak_and_articulate("ты всегда так говоришь и сдаешь на тройку, может пора начинать учить")

await click_eyes("eyes/глаза_грустный.svg")
await speak_and_articulate("хорошо, извини. Больше не буду")

await click_eyes("eyes/глаза_улыбающийся1.svg")
await speak_and_articulate("ну раз ты платишь, то я согласна!")