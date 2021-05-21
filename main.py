# ====================================================================
#
# "What's The Longest Word You Can Write With Seven-Segment Displays?"
# 	- Tom Scott (https://youtu.be/zp4BMR88260)
# 
# Python solution by Lennart Breede
#
# ====================================================================

import re

def main():

	dic = "german.dic"
	dic = "english.dic"

	with open(dic, "r") as f:
		words = f.read().split("\n")

	words = [w.lower() for w in words]

	bad_letters = "[gkmqvwxzäüöß]"
	bad_letters = "[gkmqvwxzäüößio]" # added i and o to bad letters
	bad_letters = "[gkmqvwxzäüößio-]" # added - after getting "three-and-a-halfpenny"

	longest_possible_word = ""

	for w in words:
		if (len(w) >= len(longest_possible_word) and
			not re.search(bad_letters, w)):
			longest_possible_word = w
	print(longest_possible_word)
	draw_word(longest_possible_word)

def convert_letter(char):
	chars = {
			"0": [" _ ", "| |", "|_|"],
			"1": ["   ", "  |", "  |"],
			"2": [" _ ", " _|", "|_ "],
			"3": [" _ ", " _|", " _|"],
			"4": ["   ", "|_|", "  |"],
			"5": [" _ ", "|_ ", " _|"],
			"6": [" _ ", "|_ ", "|_|"],
			"7": [" _ ", "| |", "  |"],
			"8": [" _ ", "|_|", "|_|"],
			"9": [" _ ", "|_|", " _|"],
			"a": [" _ ", "|_|", "| |"],
			"b": ["   ", "|_ ", "|_|"],
			"c": [" _ ", "|  ", "|_ "],
			"d": ["   ", " _|", "|_|"],
			"e": [" _ ", "|_ ", "|_ "],
			"f": [" _ ", "|_ ", "|  "],
			"h": ["   ", "|_|", "| |"],
			"i": ["   ", "  |", "  |"],
			"j": ["   ", "  |", " _|"],
			"l": ["   ", "|  ", "|_ "],
			"n": [" _ ", "| |", "| |"],
			"o": ["   ", " _ ", "|_|"],
			"p": [" _ ", "|_|", "|  "],
			"r": ["   ", " _ ", "|  "],
			"s": [" _ ", "|_ ", " _|"],
			"t": ["   ", "|_ ", "|_ "],
			"u": ["   ", "| |", "|_|"],
			"y": ["   ", "|_|", " _|"]
		}

	if char in chars:
		return chars[char]
	else:
		return ["   ", "   ", " {0} ".format(char)]

def draw_word(word):
	word = word.lower()
	line1 = ""
	line2 = ""
	line3 = ""
	for char in word:
		l1, l2, l3 = convert_letter(char)
		line1 += l1
		line2 += l2
		line3 += l3

	print("{0}\n{1}\n{2}".format(line1, line2, line3))


if __name__ == '__main__':
	main()