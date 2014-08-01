import copa
def calcula_numero_jogos(grupo):
	total_jogos = 0
	for time, dados_time in grupo.items(): 
		jogos = int(dados_time['jogos'])
		total_jogos += jogos
	return total_jogos / 2

print calcula_numero_jogos(copa.grupo_a)


