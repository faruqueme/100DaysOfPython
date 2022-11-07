### underconstruction ###

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
letter_list=[]
def cearsar(direction, text, shift):
	if direction=='decode':
		alphabet.reverse()
	for n in text:
		find_letter=alphabet.index(n)
		x=find_letter+shift
		search_letter=alphabet[x]
		letter_list.extend(search_letter)
		join_items="".join(letter_list)
	if direction=='decode':
		print(f"Here's {direction}d result is {join_items}.")
	elif direction=='encode':
		print(f"Here's {direction}d result is {join_items}.")




cearsar(direction, text, shift)

