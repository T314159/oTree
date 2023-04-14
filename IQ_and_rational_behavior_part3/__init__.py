from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'IQ_and_rational_behavior_part3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    lottery_choice = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6])
    dictator_choice = models.IntegerField()

# PAGES
class Introduction(Page):
    pass

# PAGES
class Lottery(Page):
    form_model = 'player'
    form_fields = ['lottery_choice']

# PAGES
class Dictator(Page):
    pass

# PAGES
class BackwardsInduction(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Introduction, Lottery, Dictator, BackwardsInduction, ResultsWaitPage, Results]
