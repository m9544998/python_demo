
'''
score=[72,73,33]
average=sum(score)/len(score)
print(f"average: {average}")
'''
from cs50 import get_int
scores = []
for i in range(3):
    score=(get_int("Score: "))
    scores+=[score]
average = sum(scores) / len(scores)
print(f"average: {average}")

