from otree.api import *


doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'ravens_test'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 12
    QUESTION_ORDER = ["03", "10", "12", "15", "16", "18", "21", "22", "28", "30", "31", "34"]
    IMAGE_NAMES = [
        'a1.png',
        'a2.png',
        'a3.png',
        'a4.png',
        'a5.png',
        'a6.png',
        'a7.png',
        'a8.png'
    ]


def make_image_data(question_number):
    return [dict(name=name, path='ravens_test/apm{}/{}'.format(C.QUESTION_ORDER[question_number], name)) for name in C.IMAGE_NAMES]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    img_choice = models.StringField()


# PAGES
class RavensQuestions(Page):
    form_model = 'player'
    form_fields = ['img_choice']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(image_data=make_image_data(player.round_number-1),
                    question_data=dict(name='q', path='ravens_test/apm{}/q.png'.format(C.QUESTION_ORDER[player.round_number-1])))



page_sequence = [RavensQuestions]
