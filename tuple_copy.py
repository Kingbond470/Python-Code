'''
OddTuple: copy the tuple which are present at odd position
returns:tuple,every other element of a tuple
'''
def oddTuples(tup):
	copy=()
	i=0
	while i<len(tup):
		copy+=(tup[i],)
		i+=2
	return copy

tuple_eg=('L','what','loves','am','to','for','live','where','with','a','humanity' )
print(oddTuples(tuple_eg))