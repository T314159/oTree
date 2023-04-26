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

        part1_correct = 0
        selected = random.choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], k=2)
        for question_index in selected:
            if player.participant.ravens_results[question_index] == 1:
                part1_earned += 100
                part1_correct += 1
        part1_text = '{}LD = ${:.2f}'.format(part1_earned, part1_earned / 100.0)

        # Part 2
        part2_selected = random.randint(1,3)
        part2_earned = player.participant.game_payoffs[part2_selected-1]
        part2_turn = player.participant.game_ends[part2_selected-1]
        part2_text = '{}LD = ${:.2f}'.format(part2_earned, part2_earned / 100.0)

        part3_selected = random.choice(["Lottery", "Allocation", "Reasoning"])
        if selected == "Lottery":
            lottery_result = random.randint(1,2)
            payoff_matrix = [[140,140], [120,180], [100,220], [80,260], [60,300], [10, 350]]
            part3_earned += payoff_matrix[player.lottery_choice-1][lottery_result-1]
            if lottery_result == 1: part3_extra = "Lottery result was A"
            else: part3_extra = "Lottery result was B"

        elif selected == "Allocation":
            pass
            part3_earned += 100-player.participant.dictator_choice
            part3_earned += player.participant.dictator_from_others
            part3_extra = f"{player.participant.dictator_from_others} given to you by another player"
        else:
            if player.BI_choice == 1:
                part3_earned = 100
                part3_extra = "Answer was correct"
            else:
                part3_extra = "Answer was incorrect"

        part3_text = '{}LD = ${:.2f}'.format(part3_earned, part3_earned / 100.0)


        total_text = '${:.2f}'.format((500+part1_earned+part2_earned+part3_earned) / 100.0)

        return dict(
            part1_correct = part1_correct,
            part1_text=part1_text,
            part1_earned = part1_earned,
            part2_selected=part2_selected,
            part2_turn=part2_turn,
            part2_text=part2_text,
            part3_selected=part3_selected,
            part3_extra=part3_extra,
            part3_text = part3_text,
            total_text=total_text
        )


page_sequence = [Introduction, Lottery, Dictator, BackwardsInduction, ResultsWaitPage, Results]
