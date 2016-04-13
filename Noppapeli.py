# -*- coding: utf-8 -*-
import random

while True:
	user = input('Arvaa kahden nopan yhteenlaskettu silmäluku (2-12) tai lopeta peli (x): ')

	if user.strip() == 'x':
		break
	try:
		arvaus = int(user.strip())
		if arvaus < 2 or arvaus > 12:
			continue
	except ValueError:
		continue

	noppa1 = random.randint(1,6)
	noppa2 = random.randint(1,6)
	summa = noppa1 + noppa2

	print('Ensimmäisen nopan tulos: {}'.format(noppa1))
	print('Toisen nopan tulos: {}'.format(noppa2))
	print('Yhteenlaskettu summa: {}'.format(summa))

	if arvaus == summa:
		print('Arvasit oikein, onneksi olkoon!')
	else:
		print('Arvasit väärin, parempi onni toisella kerralla.')
	