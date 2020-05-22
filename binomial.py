from scipy.stats import binom

#Jogar uma moeda 5x, qual a probabilidade de dar certo 3x
prob = binom.pmf(3, 5, 0.5)
print(prob)

#Passar por 4 sinais 4 tempos, qual probabilidade de pegar sinal verde
print(binom.pmf(0, 4, 0.25))
#Passar em 1 sinal
print(binom.pmf(1, 4, 0.25))
#Passar em 2 sinais
print(binom.pmf(2, 4, 0.25))
#Passar em 3 sinais
print(binom.pmf(3, 4, 0.25))
#Passar em todos os sinais
print(binom.pmf(4, 4, 0.25))

#Probabilidade acumulativa
print(binom.cdf(4, 4, 0.25))

#Probabilidade acerto concurso com 12 questões, acertar 7 considerando 4 alternativas em cada
total = binom.pmf(7, 12, 0.25)
#Exibir em Percentual %
total *= 100
print(total)