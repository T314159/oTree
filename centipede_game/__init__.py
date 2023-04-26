from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'centipede_game'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 3

    payoffs = {
        'standard': [[40, 10], [20, 80], [160, 40], [80, 320], [640, 160], [320, 1280], [2560, 640]],
        'constant': [[800, 800], [700, 900], [1000, 600], [500, 1100], [1200, 400], [300, 1300], [1400, 200]],
        'linear': [[600, 300], [400, 700], [800, 500], [600, 900], [1000, 700], [800, 1100], [1200, 900]]
    }


class Subsession(BaseSubsession):
    variant = models.StringField()

def creating_session(subsession: Subsession):
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
    ans7 = models.IntegerField()
    if not False:
        ans5 = models.LongStringField()
        ans6 = models.LongStringField()


# PAGES
class Game1Introduction1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    def before_next_page(player: Player, timeout_happened):
        if player.round_number == 1:
            player.participant.game_payoffs = [0, 0, 0]
            player.participant.game_ends = [0, 0, 0]

class Game1Introduction2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class Game1Introduction3(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class Game1Introduction4(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Game2Introduction1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 2

class Game2Introduction2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 2

class Game3Introduction1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 3

class Game3Introduction2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 3


class WaitForBoth(WaitPage):
    pass


def current_game(player, round_number):
    if round_number == 1: return player.participant.game1
    elif round_number == 2: return player.participant.game2
    elif round_number == 3: return player.participant.game3


class CentipedeGameStandard(Page):
    form_model = 'group'
    form_fields = ['end_turn']

    @staticmethod
    def is_displayed(player: Player):
        return current_game(player, player.round_number) == 'standard'

    @staticmethod
    def js_vars(player: Player):
        return dict(my_id=player.id_in_group)

    def live_method(player: Player, data):
        if player.id_in_group == 1:
            return {2: {'choice' : data['choice'], 'time-left' : data['time-left']}}
        else:
            return {1: {'choice' : data['choice'], 'time-left' : data['time-left']}}

    def before_next_page(player: Player, timeout_happened):
        if player.round_number == 1: payoff = C.payoffs[player.participant.game1]
        elif player.round_number == 2: payoff = C.payoffs[player.participant.game2]
        elif player.round_number == 3: payoff = C.payoffs[player.participant.game3]

        player.payoff = payoff[player.group.end_turn-1][player.id_in_group-1]
        player.participant.game_payoffs[player.round_number-1] = player.payoff
        player.participant.game_ends[player.round_number-1] = player.group.end_turn

        player.participant.control = False


class CentipedeGameLinear(Page):
    form_model = 'group'
    form_fields = ['end_turn']

    @staticmethod
    def is_displayed(player: Player):
        return current_game(player, player.round_number) == 'linear'

    @staticmethod
    def js_vars(player: Player):
        return dict(my_id=player.id_in_group)

    def live_method(player: Player, data):
        if player.id_in_group == 1:
            return {2: {'choice' : data['choice'], 'time-left' : data['time-left']}}
        else:
            return {1: {'choice' : data['choice'], 'time-left' : data['time-left']}}

    def before_next_page(player: Player, timeout_happened):
        if player.round_number == 1: payoff = C.payoffs[player.participant.game1]
        elif player.round_number == 2: payoff = C.payoffs[player.participant.game2]
        elif player.round_number == 3: payoff = C.payoffs[player.participant.game3]

        player.payoff = payoff[player.group.end_turn-1][player.id_in_group-1]
        player.participant.game_payoffs[player.round_number-1] = player.payoff
        player.participant.game_ends[player.round_number-1] = player.group.end_turn

        player.participant.control = False


class CentipedeGameConstant(Page):
    form_model = 'group'
    form_fields = ['end_turn']

    @staticmethod
    def is_displayed(player: Player):
        return current_game(player, player.round_number) == 'constant'

    @staticmethod
    def js_vars(player: Player):
        return dict(my_id=player.id_in_group)

    def live_method(player: Player, data):
        if player.id_in_group == 1:
            return {2: {'choice' : data['choice'], 'time-left' : data['time-left']}}
        else:
            return {1: {'choice' : data['choice'], 'time-left' : data['time-left']}}

    def before_next_page(player: Player, timeout_happened):
        if player.round_number == 1: payoff = C.payoffs[player.participant.game1]
        elif player.round_number == 2: payoff = C.payoffs[player.participant.game2]
        elif player.round_number == 3: payoff = C.payoffs[player.participant.game3]

        player.payoff = payoff[player.group.end_turn-1][player.id_in_group-1]
        player.participant.game_payoffs[player.round_number-1] = player.payoff
        player.participant.game_ends[player.round_number-1] = player.group.end_turn

        player.participant.control = False


class Questionnaire(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player): #Change
        if player.participant.control:
            if player.round_number != 3:
                return ['ans1', 'ans2a', 'ans2b', 'ans2c', 'ans3', 'ans4']
            else:
                return ['ans1', 'ans2a', 'ans2b', 'ans2c', 'ans3', 'ans4', 'ans7']
        else:
            if player.round_number != 3:
                return ['ans1', 'ans2a', 'ans2b', 'ans2c', 'ans3', 'ans4', 'ans5', 'ans6']
            else:
                return ['ans1', 'ans2a', 'ans2b', 'ans2c', 'ans3', 'ans4', 'ans5', 'ans6', 'ans7']


    @staticmethod
    def error_message(player, values):
        if len(values['ans1']) < 60:
            return 'Please expand a little more for Question 1'
        if len(values['ans3']) < 40:
            return 'Please expand a little more for Question 3'
        if not player.participant.control:
            if len(values['ans6']) < 40:
                return 'Please expand a little more for Question 6'

class Game1Rules(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Game2Rules(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 2

class Game3Rules(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 3

class Assignment(Page):

    def vars_for_template(player: Player):
        for other in player.get_others_in_group():
            if other.participant.raven_percentile <= 25:
                other_quartile = "1st"
                quartile_range = "0% and 25%"
            elif other.participant.raven_percentile <= 50:
                other_quartile = "2nd"
                quartile_range = "25% and 50%"
            elif other.participant.raven_percentile <= 75:
                other_quartile = "3rd"
                quartile_range = "50% and 75%"
            else:
                other_quartile = "4th"
                quartile_range = "75% and 100%"
        if player.id_in_group == 1:
            your_color = "RED"
            other_color = "BLUE"
        else:
            your_color = "BLUE"
            other_color = "RED"
        return dict(
            other_quartile = other_quartile,
            quartile_range = quartile_range,
            image_path='centipede_game/quartile' + str( round((other.participant.raven_percentile+12.5)/25.0) ) + '.png',
            your_color=your_color,
            other_color=other_color
        )


class ResultsWaitPage(WaitPage):
    pass



page_sequence = [Game1Introduction1, Game1Introduction2, Game1Introduction3, Game1Introduction4,
                 Game2Introduction1, Game2Introduction2, Game3Introduction1, Game3Introduction2,
                 Game1Rules, Game2Rules, Game3Rules,Assignment, WaitForBoth, CentipedeGameStandard,
                 CentipedeGameLinear, CentipedeGameConstant, Questionnaire, ResultsWaitPage]
