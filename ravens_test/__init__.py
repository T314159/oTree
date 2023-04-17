from otree.api import *


doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'ravens_test'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2
    QUESTION_ORDER = ["03", "10", "12", "15", "16", "18", "21", "22", "28", "30", "31", "34"]
    CORRECT_ANSWERS = [7, 4, 6, 2, 4, 7, 8, 7, 5, 5, 4, 1]
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
class PatternExplanation(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.participant.expiry = time.time() + 8 * 60


class RavensQuestions(Page):
    form_model = 'player'
    form_fields = ['img_choice']

    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()

    @staticmethod
    def vars_for_template(player: Player):
        return dict(image_data=make_image_data(player.round_number-1),
                    question_data=dict(name='q', path='ravens_test/apm{}/q.png'.format(C.QUESTION_ORDER[player.round_number-1])))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.round_number == 1:
            player.participant.raven_results = [0]*C.NUM_ROUNDS
        if int(player.img_choice[1]) == C.CORRECT_ANSWERS[player.round_number-1]:
            player.participant.raven_results[player.round_number-1] = 1
        if player.round_number == C.NUM_ROUNDS:
            player.participant.raven_score = sum(player.participant.raven_results)


class End(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    def vars_for_template(player: Player):
        return dict(raven_results=player.participant.raven_results,
                    raven_score=player.participant.raven_score)

class ResultsWaitPage(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def after_all_players_arrive(group: Group):
        for player in group.get_players():
            less_than = -0.5 # To account for the fact we will be adding our own score in
            for other_player in group.get_players():
                if other_player.participant.raven_score < player.participant.raven_score:
                    less_than += 1
                elif other_player.participant.raven_score == player.participant.raven_score:
                    less_than += 0.5
            player.participant.raven_percentile = round(100 * less_than / (len(group.get_players())-1))


page_sequence = [PatternExplanation, RavensQuestions, End, ResultsWaitPage]
