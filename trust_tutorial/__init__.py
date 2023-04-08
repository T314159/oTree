from otree.api import *


doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'trust_tutorial'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    ENDOWMENT = cu(10)
    MULTIPLICATION_FACTOR = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        labels = "How much money would you like to give to participant B?",
        min = cu(0),
        max = C.ENDOWMENT
    )
    sent_back_amount = models.CurrencyField(
        labels="How much money would you like to return?",
    )

def sent_back_amount_choice(group):
    return currency_range(
        cu(0),
        C.MULTIPLICATION_FACTOR*group.sent_amount,
        cu(1)
    )

def set_payoffs(group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
    p2.payoff = group.sent_amount*C.MULTIPLICATION_FACTOR - group.sent_back_amount

class Player(BasePlayer):
    pass


# PAGES
class Send(Page):
    form_model = "group"
    form_fields = ["sent_amount"]

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

class WaitForP1(WaitPage):
    pass

class SendBack(Page):
    form_model = "group"
    form_fields = ["sent_back_amount"]

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        return dict(
            tripled_amount=group.sent_amount*C.MULTIPLICATION_FACTOR
        )


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [Send, WaitForP1, SendBack, ResultsWaitPage, Results]
