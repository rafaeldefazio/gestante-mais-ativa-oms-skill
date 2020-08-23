from mycroft import MycroftSkill, intent_file_handler


class GestanteMaisAtivaOms(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('oms.ativa.mais.gestante.intent')
    def handle_oms_ativa_mais_gestante(self, message):
        self.speak_dialog('oms.ativa.mais.gestante')


def create_skill():
    return GestanteMaisAtivaOms()

