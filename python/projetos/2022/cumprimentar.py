# coding: utf-8
from datetime import datetime

template_horario = u", agora são {0} horas"


def cumprimentar():
    agora = datetime.now()
    if (0 < agora.hour < 12):
        resposta = "Bom Dia"
    elif (12 <= agora.hour < 18):
        resposta = "Boa tarde"
    else:
        resposta = "Boa noite"
    resposta = resposta + template_horario.format(agora.strftime("%H:%M"))
 
    return resposta
print('-'*35)
print(cumprimentar())
print('-'*35)