import random
import nltk
from nltk.corpus import words

# Initialize data set
if not nltk.data.find('corpora/words.zip'):
	nltk.download("words")
word_list = words.words()

# Choose only words that are all lowercase
word_list_lowers_only = [word for word in word_list if word == word.lower()]
answer = random.choice(word_list_lowers_only)

guess = ""
lower = ""
upper = ""
guesses = 0
while guess != answer:
	guess = input("Guess the word! ")
	guesses += 1
	if guess == answer:
		break
	if answer < guess and (guess < upper or not upper):
			upper = guess
	elif guess > lower or not lower:
		lower = guess
	if upper and lower:
		order = f'between "{lower}" and "{upper}"'
	elif upper:
		order = f'before "{upper}"'
	else:
		order = f'after "{lower}"'
	print(f'Nope! The correct answer comes {order} alphabetically.')
print(f"Yep that's it! You got it in {guesses} guesses!")