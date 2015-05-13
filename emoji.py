import random
from random import shuffle

emoji = open('emoji.txt').read().split()
# emoji = open('less').read().split()
weapons = open('weapons').read().split()

output = open('output.txt', 'w')

# print weapons
leftwins = weapons[0:3]
rightwins = weapons[3:6]

input = emoji
shuffle(input) #shuffle

# print len(emoji) #1024 emoji

def getRandomEmoji():
	return random.choice(values)

round_1 = input

def increment(input_array, i):
	tmp_array = input_array
	new_array = []
	while len(input_array) > 0:
		match = [tmp_array.pop(0), tmp_array.pop(0)]
		victor = random.choice(['left','right'])
		if victor == 'left':
			# print match[0] + " " + random.choice(leftwins) + " " + match[1] + " #EmojiMadness #Round" + str(i) + "  #LeftWins"
			output.write( match[0] + " " + random.choice(leftwins) + " " + match[1] + " #EmojiMadness #Round" + str(i) + "\n" )
			winner = match[0]
		if victor == 'right':
			# print match[0] + " " + random.choice(rightwins) + " " + match[1] + " #EmojiMadness #Round" + str(i) + " #RightWins"
			output.write( match[0] + " " + random.choice(rightwins) + " " + match[1] + " #EmojiMadness #Round" + str(i) + "\n" )
			winner = match[1]
		new_array.append(winner)
	return new_array 

def iterate(input_round, i):
	if len(input_round) > 1:
		output.write( 'Round ' + str(i) + " Begins Now! #EmojiMadness #Round" + str(i) + "\n" ) 
	else:
		# print 'America\'s Next Top Emoji: ',
		output.write( 'America\'s Next Top Emoji: ', )
		for item in input_round:
			# print item, 
			output.write( item, ) 
	next_round = []
	while len(input_round) > 1:
		next_round = increment(input_round, i)
		iterate(next_round, i+1)
	return next_round
i = 1
iterate(round_1, i)