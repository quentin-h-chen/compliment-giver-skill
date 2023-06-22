from mycroft import MycroftSkill, intent_file_handler


class ComplimentGiver(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('giver.compliment.intent')
    def handle_giver_compliment(self, message):
        self.speak_dialog('giver.compliment')


def create_skill():
    return ComplimentGiver()

