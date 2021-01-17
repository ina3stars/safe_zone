
import random
answer = ['I','slept','bad']
# 'answer' is the list that contains the user's answer to the surveys
goodwords = ['great','awesome','good','10','ten','nine','9','8','eight','amazing','excellent']
# I made a list of positive words that the program will recognise in the answer
badwords = ['bad','very bad','1','one','2','two','3','three','4','four','five','5','six','6','seven','7','horrible','stressful','stress','stressed']
# I made a list of negative words that the program will recognise in the answer
points = 0
# points will gain a point every time the user gives a positive answer and loose a point if the user gives a negative answer
activities = ['doodling','drawing','dancing','singing','coding','reading','knitting','going for a walk','listening to music','taking care of plants','meeting friends','calling a family member',]
for word in answer:
    for elt in goodwords:
        if elt == word:
            points = points + 1
for word in answer:
    for elt in badwords:
        if elt == word:
            points = points - 1
if points > 0:
    print('great! I see you are feeling good today !')
elif points < 0:
    print("I'm sorry you are not feeling very well :( . " + random.choice(activities) +" helps deal with stress !")



