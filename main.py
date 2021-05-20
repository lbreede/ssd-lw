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
	# dic = "english.txt"

	with open(dic, "r") as f:
		words = f.read().split("\n")

	words = [w.lower() for w in words]

	bad_letters = "[gkmqvwxzäüöß]"
	# bad_letters = "[gkmqvwxzäüößio]" # added i and o to bad letters

	longest_possible_word = ""

	for w in words:
		if (len(w) >= len(longest_possible_word) and
			not re.search(bad_letters, w)):
			longest_possible_word = w

	print(longest_possible_word)

if __name__ == '__main__':
	main()