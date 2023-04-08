from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'IQ_and_rational_behavior_part2'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    part1_intro_q1 = models.BooleanField(choices=[ [True, 'True'], [False, 'False'] ])
    part1_intro_q2 = models.BooleanField(choices=[ [True, 'True'], [False, 'False'] ])
    part1_intro_q3 = models.BooleanField(choices=[ [True, 'True'], [False, 'False'] ])
    part1_intro_q4 = models.BooleanField(choices=[ [True, 'True'], [False, 'False'] ])
    pass



# PAGES

class IntroAndPayment(Page):
    form_model = 'player'
    form_fields = ['part1_intro_q1', 'part1_intro_q2', 'part1_intro_q3', 'part1_intro_q4']


    def vars_for_template(player: Player):
        return dict(
            raven_score=player.participant.raven_score,
            unique_id=player.participant.unique_id,
            participant=player.participant,
            control=player.participant.control,
        )


class Game1Explanation(Page):
    form_model = 'player'
    form_fields = ['part1_intro_q1', 'part1_intro_q2', 'part1_intro_q3', 'part1_intro_q4']


    def vars_for_template(player: Player):
        return dict(
            raven_score=player.participant.raven_score,
        )


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [IntroAndPayment, ResultsWaitPage, Results]

