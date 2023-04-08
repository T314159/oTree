from otree.api import *


doc = """
Your app description
"""

def make_image_data(image_names):
    return [dict(name=name, path='ravens_test/apm03/{}'.format(name)) for name in image_names]


class C(BaseConstants):
    NAME_IN_URL = 'ravens_test'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 12


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
        image_names = [
            'a1.png',
            'a2.png',
            'a3.png',
            'a4.png',
            'a5.png',
            'a6.png',
            'a7.png',
            'a8.png'
        ]
        return dict(image_data=make_image_data(image_names), question_data=dict(name='q', path='ravens_test/apm03/q.png'))



class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

page_sequence = [RavensQuestions, ResultsWaitPage, Results]
