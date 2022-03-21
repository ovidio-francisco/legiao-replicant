#!/usr/bin/python3

import sys 
from LyricsAnswerer import LyricsAnswerer

la = LyricsAnswerer()


def print_answer(quest):

	if not la.containsVerse(quest):
		print("Não encontrado")
		return

	ans = la.format_answer(quest)
	if (len(ans) > 0):
		print("\n"+ans+"\n")




if __name__ == "__main__":

	if(len(sys.argv) > 1):
		trecho = sys.argv[1]
	else:
		print("Trecho: ", end='')
		trecho = input()


	print_answer(trecho)


















#  keys = qa.keys()
#  for k in keys:
	#  print("Q: '" + k +"'")



#  question = input()
#  question = "Esquecer que acreditei "
#  question = "Ai que eu quis o perigo e deu nisso"

# Teste

#  question = "Explicar o que ninguém consegue"


#  print("Question: " + question)


#  la = LyricsAnswerer()


#  la.print_answer(question)
# Teste

















#  keys = qa.keys()

#  for k in keys:
	#  print("Q: " + k)
	#  #  a = answer(k, qa)
	#  a = qa[k]
	
	#  for i in a:
		#  print("A: " + i )
		#  print()
