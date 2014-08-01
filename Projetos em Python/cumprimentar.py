# coding: utf-8
from datetime import datetime
 
template_horario = u", são {0} horas"
 
def cumprimentar():
    agora = datetime.now()
    if (0 < agora.hour < 12):
        reposta = "bom dia"
    elif (12 <= agora.hour < 18):
        resposta = "boa tarde"
    else:
        resposta = "boa noite"
    #resposta = resposta + template_horario.format(hora)
    #resposta = resposta + u" são " + str(hora) + " horas"
    resposta = resposta + template_horario.format(agora.strftime("%H:%M"))
 
    return resposta
 
print(cumprimentar())