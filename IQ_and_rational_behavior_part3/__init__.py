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
    def vars_for_template(player: Player):
        import random
        part1_earned = 0
        part2_earned = 0
        part3_earned = 0

        selected = random.choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], k=2)
        for question_index in selected:
            if player.participant.ravens_results[question_index] == 1:
                part1_earned += 100

        part2_selected = random.randint(1,3)
        # Get info from past.

        part3_selected = random.choice(["Lottery", "Allocation", "Reasoning"])
        if selected == "Lottery":
            lottery_result = random.randint(1,2)
            payoff_matrix = [[140,140],[120,180],[100,220],[80,260],[60,300],[10, 350]]
            part3_earned += payoff_matrix[player.lottery_choice-1][lottery_result-1]
        elif selected == "Allocation":
            pass
            #get info on dictator
        else:
            if player.BI_choice == 1:
                part3_earned = 100

        return dict(
            part1_text = part1_text,
            part2_text=part2_text,
            part3_text = part3_text
        )


page_sequence = [Introduction, Lottery, Dictator, BackwardsInduction, ResultsWaitPage, Results]
