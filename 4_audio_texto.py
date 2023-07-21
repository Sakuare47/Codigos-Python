import speech_recognition as sr 
import pyaudio


r = sr.Recognizer()


# Inicializa o microfone

with sr.Microphone() as source:

	print('Diga alguma coisa: ')
	audio = r.listen(source)


try:

	# Tenta reconhecer o áudio usando o Google Speech Recognition
	text = r.recognize_google(audio, language='pt-BR')

	print(f'Você disse: {text}')

except sr.UnknownValueError:

	print('Não entendi o que você disse')

except sr.RequestError as e:

	print('Erro de requisição; {0}'.format(e))

