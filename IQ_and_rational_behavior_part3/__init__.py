from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'part3'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    lottery_choice = models.IntegerField(initial=0, widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6])
    dictator_choice = models.IntegerField(initial=0)
    BI_choice = models.IntegerField(initial=0, widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6])

    gender = models.StringField()


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
class Allocation(Page):
    form_model = 'player'
    form_fields = ['dictator_choice']

    def before_next_page(player: Player, timeout_happened):
        player.participant.dictator_choice=player.dictator_choice
        for opponent in player.get_others_in_group():
            opponent.participant.dictator_from_others = 100-player.dictator_choice


# PAGES
class BI(Page):
    form_model = 'player'
    form_fields = ['BI_choice']

    def before_next_page(player: Player, timeout_happened):
        player.participant.BI_choice=player.BI_choice


class ResultsWaitPage(WaitPage):
    pass

class Demographic(Page):
    form_model = 'player'
    form_fields = ['gender']


class Results(Page):
    def vars_for_template(player: Player):
        import random

        part1_earned = 0
        part1_correct = 0
        selected = random.choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], k=2)
        for question_index in selected:
            if player.participant.raven_results[question_index] == 1:
                part1_earned += 100
                part1_correct += 1
        part1_text = '{} LD = ${:.2f}'.format(part1_earned, part1_earned / 100.0)

        # Part 2
        part2_selected = random.randint(1,3)
        part2_earned = player.participant.game_payoffs[part2_selected-1]
        part2_turn = player.participant.game_ends[part2_selected-1]
        part2_text = '{} LD = ${:.2f}'.format(part2_earned, part2_earned / 100.0)


        lottery_earned = 0
        allocation_earned = 0
        bI_earned = 0

        lottery_result = random.randint(1,2)
        payoff_matrix = [[140,140], [120,180], [100,220], [80,260], [60,300], [10, 350]]
        lottery_earned += payoff_matrix[player.lottery_choice-1][lottery_result-1]
        if lottery_result == 1: lottery_extra = "Lottery result was A"
        else: lottery_extra = "Lottery result was B"

        allocation_earned += 100-player.participant.dictator_choice
        allocation_earned += player.participant.dictator_from_others
        allocation_extra = f"{player.participant.dictator_from_others} given to you by another player"

        if player.BI_choice == 1:
            bI_earned = 100
            bI_extra = "Your answer was Correct"
        else:
            bI_extra = "Your answer was Incorrect"

        lottery_text = '{} LD = ${:.2f}'.format(lottery_earned, lottery_earned / 100.0)
        allocation_text = '{} LD = ${:.2f}'.format(allocation_earned, allocation_earned / 100.0)
        bI_text = '{} LD = ${:.2f}'.format(bI_earned, bI_earned / 100.0)


        player.participant.payoff = part1_earned+part2_earned+lottery_earned+allocation_earned+bI_earned

        total_text = '${:.2f}'.format((500+part1_earned+part2_earned+part3_earned) / 100.0)

        return dict(
            part1_correct = part1_correct,
            part1_text=part1_text,
            part1_earned = part1_earned,
            part2_selected=part2_selected,
            part2_turn=part2_turn,
            part2_text=part2_text,
            lottery_extra=lottery_extra,
            allocation_extra=allocation_extra,
            bI_extra=bI_extra,
            lottery_text = lottery_text,
            allocation_text=allocation_text,
            bI_text=bI_text,
            total_text=total_text
        )


page_sequence = [Introduction, Lottery, Allocation, BI, Demographic, ResultsWaitPage, Results]
