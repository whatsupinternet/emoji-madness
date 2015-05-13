import random
from random import shuffle

values = open('emoji.txt').read().split()
shuffle(values) #shuffle

# print len(values) #1369 emoji

def getRandomEmoji():
	return random.choice(values)

# print getRandomEmoji()
