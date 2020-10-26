'''
character: enter a single character from any alphabets
returns:  it will return true if a entered character is vowel otherwise false
'''
def vowelCheck(character):
	vowel='aeiouAEIOU'	
	counter=0
	count_vowel=len(vowel)
	while counter< count_vowel:
		check_character=vowel[counter:counter+1]
		counter+=1
		if check_character==character:
			return True
	return False
character=input('Enter the character: ')
print(vowelCheck(character))