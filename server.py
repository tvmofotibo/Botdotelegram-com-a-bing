# gpt bot telegram

#importação
import requests
import telebot
import time
import os
#Declaração das variáveis 
outputai=""
inputuser=""
#chave da api do telegram
api_chave_bot=os.environ.get("API_KEY_BOT")
api_chave_bing=os.environ.get("API_KEY_BING")
#Função para fazer a requisição para uma api da Bing AI gpt4
def aigetapi():
	global inputuser
	url = "https://chatgpt-bing-ai-chat-api.p.rapidapi.com/ask"
	payload = {
	"question": inputuser,"bing_u_cookie": "Please replace this string with a string representing your Bing _U cookie. You can obtain your _U cookie by accessing the Developer Console and searching for the _U cookie name. Please follow this link for guidance: https://i.ibb.co/94YWpQD/1676391128.png"
	}
	headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": api_chave_bing,
	"X-RapidAPI-Host": "chatgpt-bing-ai-chat-api.p.rapidapi.com"
}
	response = requests.post(url, json=payload, headers=headers)
	resposta=response.json()
	return resposta.get("text_response")
#configurações na bing
#inputuser="Responda todas minhas perguntas em português por favor"
#time.sleep(0.5)
#print(aigetapi())
#inputuser=" "

#Iniciando bot no telegram 

bot=telebot.TeleBot(api_chave_bot)

#função que chama a função aigetapi()
def funveri(mensagem):
	global outputai
	global inputuser
	inputuser=mensagem.text
	print(" "*5+"Input user: "+inputuser)
	print("\n")
	if(inputuser!="start"):
		outputai=aigetapi()
		print(" "*5+"Output AI: "+outputai)
		print("\n")
		return True
	return False

@bot.message_handler(commands=["opensource"])
def opensource(mensagem):
	bot.send_message(mensagem.chat.id,"codigo feito por Alvino Gabriel")
	bot.send_message(mensagem.chat.id,"depois coloco o link para o GitHub, flw")
	time.sleep(0.3)
	bot.send_message(mensagem.chat.id,"meu instagram: ")
	time.sleep(0.3)
	bot.send_message(mensagem.chat.id,"https://instagram.com/alvino_gabriel_santana?igshid=ZDc4ODBmNjlmNQ==")

@bot.message_handler(commands=["start"])
def start(mensagem):
    nome1=" "
    nome2=" "
    if (str(mensagem.from_user.last_name)=="None"):
    	nome2=""
    else:
    	nome2=str(mensagem.from_user.last_name)+", "
    if (str(mensagem.from_user.first_name)=="None"):
    	nome1=""
    else:
    	
    	
    	nome1="Olá "+str(mensagem.from_user.first_name)+" "
    bot.send_message(mensagem.chat.id, "%s%sEu sou sr bunda cagada, o Rick colocou em min a Bing AI para eu ficar mais inteligente."%(nome1,nome2))
    bot.send_message(mensagem.chat.id,"faça-me qual quer pergunta")
    
@bot.message_handler(func=funveri)
def respon(mensagem):
   
    bot.send_message(mensagem.chat.id, outputai)
    

    
bot.polling()