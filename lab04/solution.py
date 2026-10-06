def winner(names, scores):
	max_score = scores[0]	
	
	for i in range(len(scores)):
		if scores[i]>max_score:
			max_score = scores[i]
			winner = names[i]
	return winner
	
def average(scores):
	avg = 0
	return round(sum(scores)/len(scores),1)
	
def ranking(names, scores):
	pairs = []
	for i in range(len(scores)):
		pairs.append([scores[i],-i, names[i]])
	pairs.sort(reverse=True)
	
	result = []
	for pair in pairs:
		result.append(pair[2])
	
	return result

def above_average(names, scores):
	above_avg = [names[i] for i in range(len(scores)) if scores[i] > average(scores)]
	return above_avg

names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

print('Победитель:',winner(names,scores))
print('Среднее значение баллов:',average(scores))
print('Имена по убыванию результата:',ranking(names,scores))
print('Имена тех, чей результат строго выше среднего:',above_average(names, scores))
