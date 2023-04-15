from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'IQ_and_rational_behavior_part3'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    lottery_choice = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6])
    dictator_choice = models.IntegerField()
    BI_choice = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6])

# PAGES
class Introduction(Page):
    pass

# PAGES
class Lottery(Page):
    form_model = 'player'
    form_fields = ['lottery_choice']

    def before_next_page(player: Player, timeout_happened):
        player.participant.lottery_choice=player.lottery_choice

# PAGES
class Dictator(Page):
    form_model = 'player'
    form_fields = ['dictator_choice']

    def before_next_page(player: Player, timeout_happened):
        player.participant.dictator_choice=player.dictator_choice
        for opponent in player.get_others_in_group():
            opponent.participant.dictator_from_others = 100-player.dictator_choice

# PAGES
class BackwardsInduction(Page):
    form_model = 'player'
    form_fields = ['BI_choice']

    def before_next_page(player: Player, timeout_happened):
        player.participant.BI_choice=player.BI_choice

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Introduction, Lottery, Dictator, BackwardsInduction, ResultsWaitPage, Results]
