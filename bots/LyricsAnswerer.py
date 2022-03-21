#!/usr/bin/python3

import csv
import unidecode
import random


#  meu pai perguntou se eu quero colocar um ouro no dente
#  |quero colo| 



class LyricsAnswerer:

	def __init__(self):

		self.emojis = "🎶🎵"
		self.ending = "\n\n#Legiãoreplicant"
		#  self.ending =+ "\nOuça Legião Urbana"


		self.qa = {}
		self.readLyrics("../letras/indios.csv")
		self.readLyrics("../letras/tempo-perdido.csv")
		self.readLyrics("../letras/ha-tempos.csv")
		self.readLyrics("../letras/quase-sem-querer.csv")
		self.readLyrics("../letras/sera.csv")
		self.readLyrics("../letras/que-pais-e-esse.csv")
		self.readLyrics("../letras/eu-sei.csv")
		self.readLyrics("../letras/pais-e-filhos.csv")
		self.readLyrics("../letras/perfeicao.csv")

		print(f"{len(self.qa)} QAs read")


		#  for q in self.qa:
			#  if (len(q) <2):
				#  print(f"----------------------Ans: '{self.qa[q]}'")

			#  print(f"Question: '{q}'")



		#  s = self.norm("Ando distraída")
		#  print("Norm = " + s)


	def norm(self, text):
		result = [ unidecode.unidecode(c.lower()) for c in text if (c == ' ' or c.isalpha()) ]
		return ''.join(result)


	def readLyrics(self, file):
		print("Reading " + file + " ...", end='')

		q_count = 0
		a_count = 0

		with open(file) as csvfile:
			reader = csv.reader(csvfile, skipinitialspace=True)
			l = [row for row in reader if row]

			for row in l:

				# get and normalize the question
				q = self.norm(row[0])
				q = q.strip()

				if(q==''):
					continue

				#  get and clean the answer
				a = row[1].strip()

				if (q in self.qa.keys()):
					self.qa[q].append(a)
				else:
					self.qa[q] = [a]
					q_count += 1        # if q not in keys, it's a new question
				
				# new answer
				a_count += 1

		print(f"[{q_count} questions & {a_count} anwers]")

			#  return qa



	#  def containsVerse(self, text): 
		#  text = self.norm(text)
		#  keys = [ k for k in self.qa.keys() if k in text ] 
		#  return len(keys) > 0



	#  def containsVerse(self, verse): 
		#  v = self.norm(verse)

		#  return v in self.qa.keys()


	#  def answer(self, quest):

		#  ans_list = self.qa[self.norm(quest)]
		#  ans = random.choice(ans_list)

		#  return ans

	def answer(self, quest):

		quest = self.norm(quest)

		# get the keys that are in then quest
		keys = [ k for k in self.qa.keys() if k in quest ] 

		if (len(keys) == 0):
			return ""

		print("\nkey: " + str(keys))

		#  choose a key
		key = random.choice(keys)

		#  choose an answer
		ans_list = self.qa[self.norm(key)]
		ans = random.choice(ans_list)

		return ans



	def format_answer(self, ans):

		#  ans = self.answer(quest)
		
		#  if (len(ans) == 0):
			#  return ""
		ans = '“'+ans+'…'+ self.emojis + '”'
		ans = ans + self.ending

		return ans



#  🎶🎼
#  “”
