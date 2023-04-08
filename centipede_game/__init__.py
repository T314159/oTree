from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'centipede_game'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 3

    import random
    matrix = [i for i in range(1, 12)]
    random.shuffle(matrix)
    variant_order = ['standard', 'constant', 'linear']
    random.shuffle(variant_order)

    payoffs = {
        'standard': [[40, 10], [20, 80], [160, 40], [80, 320], [640, 160], [320, 1280], [2560, 640]],
        'constant': [[800, 800], [700, 900], [1000, 600], [500, 1100], [1200, 400], [300, 1300], [1400, 200]],
        'linear': [[600, 300], [400, 700], [800, 500], [600, 900], [1000, 700], [800, 1100], [1200, 900]]
    }


class Subsession(BaseSubsession):
    variant = models.StringField()

def creating_session(subsession: Subsession):
      subsession.variant = C.variant_order[subsession.round_number-1]
      matrix = subsession.get_group_matrix()

      if subsession.round_number == 1:
         matrix = [[1, 3], [2, 4], [5, 6]]
         #subsession.set_group_matrix(matrix)
      elif subsession.round_number == 2:
          matrix = [[3,2],[1,4],[6,5]]
          #subsession.set_group_matrix(matrix)
#         matrix = [ [C.matrix[0][0], C.matrix[1][1]],
#                    [C.matrix[1][0], C.matrix[2][1]],
#                    [C.matrix[2][0], C.matrix[0][1]],
#                    [C.matrix[3][0], C.matrix[4][1]],
#                    [C.matrix[4][0], C.matrix[5][1]],
#                    [C.matrix[5][0], C.matrix[3][1]] ]
#         subsession.set_group_matrix(matrix)
#     elif subsession.round_number == 3:
#         matrix = [ [C.matrix[0][0], C.matrix[2][1]],
#                    [C.matrix[1][0], C.matrix[0][1]],
#                    [C.matrix[2][0], C.matrix[1][1]],
#                    [C.matrix[3][0], C.matrix[5][1]],
#                    [C.matrix[4][0], C.matrix[3][1]],
#                    [C.matrix[5][0], C.matrix[4][1]] ]
#         subsession.set_group_matrix(matrix)
#
#     print(subsession.get_group_matrix())


class Group(BaseGroup):
    end_turn = models.IntegerField()

class Player(BasePlayer):
    ans1 = models.LongStringField()
    ans2a = models.IntegerField()
    ans2b = models.IntegerField()
    ans2c = models.IntegerField()
    ans3 = models.LongStringField()
    ans4 = models.IntegerField()
    if not False:
        ans5 = models.LongStringField()
        ans6 = models.LongStringField()


# PAGES
class Game1Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Game2Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 2

class Game3Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 3


class CentipedeGame(Page):
    form_model = 'group'
    form_fields = ['end_turn']

    @staticmethod
    def js_vars(player: Player):
        return dict(my_id=player.id_in_group)

    def live_method(player: Player, data):
        if player.id_in_group == 1:
            return {2: {'choice' : data['choice']}}
        else:
            return {1: {'choice' : data['choice']}}

    def before_next_page(player: Player, timeout_happened):
        payoff = C.payoffs[C.variant_order[player.round_number-1]]
        player.payoff = payoff[player.group.end_turn-1][player.id_in_group-1]
        player.participant.control = False

class Questionnaire(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player): #Change
        if player.participant.control:
            return ['ans1', 'ans2a', 'ans2b', 'ans2c', 'ans3', 'ans4']
        else:
            return ['ans1', 'ans2a', 'ans2b', 'ans2c', 'ans3', 'ans4', 'ans5', 'ans6']


    @staticmethod
    def error_message(player, values):
        if values['ans2a'] + values['ans2b'] + values['ans2c'] != 100:
            return 'The sum of the percentages in Question 2 must add up to 100%'
        if len(values['ans1']) < 60:
            return 'Please expand a little more for Question 1'
        if len(values['ans3']) < 50:
            return 'Please expand a little more for Question 3'

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass



page_sequence = [Game1Introduction, Game2Introduction, Game3Introduction, CentipedeGame, Questionnaire, ResultsWaitPage, Results]
