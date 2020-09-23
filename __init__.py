from mycroft import MycroftSkill, intent_file_handler


class Seconlambon(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('seconlambon.intent')
    def handle_seconlambon(self, message):
        self.speak_dialog('seconlambon')


def create_skill():
    return Seconlambon()

