from mycroft import MycroftSkill, intent_file_handler
import requests

class GestanteMaisAtivaOms(MycroftSkill):
	def __init__(self):
		MycroftSkill.__init__(self)

	@intent_file_handler('oms.ativa.mais.gestante.intent')
	def handle_oms_ativa_mais_gestante(self, message):

		ipAPI = 'http://177.21.53.138:3000'


		payload = {'user':'publico','password':'123'}
		getToken = requests.post(ipAPI + "/login", data=payload)


		myToken = getToken.content;
		headers = {'x-access-token': myToken}

		r = requests.get(ipAPI + '/oms/mais-ativa', headers=headers)

		if r.status_code != 200 or len(r.json()) == 0:
			self.speak('Ocorreu algum problema ao me conectar ao servidor de dados. Pode ser, também, que as gestantes não tenham registrado atividades na semana atual. Por favor, verifique as credenciais e tente novamente.')

		else:
			result = r.json()[0]
			result['cpf_gestante'] = " ".join(result['cpf_gestante'])

			result['cpf_gestante'] = result['cpf_gestante'].replace(".", ", ponto, ")
			result['cpf_gestante'] = result['cpf_gestante'].replace("-", ", traço, ")

			if result['atingiu_recomendacao'] == 0:
				result['atingiu_recomendacao'] = 'não'
			else:
				result['atingiu_recomendacao'] = ''

			self.speak_dialog('oms.ativa.mais.gestante', data=result)

def create_skill():
	return GestanteMaisAtivaOms()

