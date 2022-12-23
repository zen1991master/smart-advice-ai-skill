from mycroft import MycroftSkill, intent_handler


class SmartAdviceAi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('ai.advice.smart.intent')
    def handle_ai_advice_smart(self, message):
        self.speak_dialog('ai.advice.smart')


def create_skill():
    return SmartAdviceAi()

