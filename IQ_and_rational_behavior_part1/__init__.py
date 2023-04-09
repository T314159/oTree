from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'IQ_and_rational_behavior_part1' #TODO: Change
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

# PAGES
class Introduction(Page):
    pass

class SetGroups(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        import random
        permutation = [['standard', 'constant', 'linear'],
                      ['standard', 'linear', 'constant'],
                      ['constant', 'standard', 'linear'],
                      ['constant', 'linear', 'standard'],
                      ['linear', 'standard', 'constant'],
                      ['linear', 'constant', 'standard']]
        random.shuffle(permutation)

        for player in group.get_players():
            player.participant.unique_id = player.id_in_group
            if player.id_in_group <= 4:
                player.participant.control = True
                player.participant.game1 = permutation[0][0]
                player.participant.game2 = permutation[0][1]
                player.participant.game3 = permutation[0][2]
            elif player.id_in_group <= 8:
                player.participant.control = False
                player.participant.game1 = permutation[1][0]
                player.participant.game2 = permutation[1][1]
                player.participant.game3 = permutation[1][2]
            elif player.id_in_group <= 12:
                player.participant.control = True
                player.participant.game1 = permutation[2][0]
                player.participant.game2 = permutation[2][1]
                player.participant.game3 = permutation[2][2]
            elif player.id_in_group <= 16:
                player.participant.control = False
                player.participant.game1 = permutation[3][0]
                player.participant.game2 = permutation[3][1]
                player.participant.game3 = permutation[3][2]
            elif player.id_in_group <= 20:
                player.participant.control = True
                player.participant.game1 = permutation[4][0]
                player.participant.game2 = permutation[4][1]
                player.participant.game3 = permutation[4][2]
            else:
                player.participant.control = False
                player.participant.game1 = permutation[5][0]
                player.participant.game2 = permutation[5][1]
                player.participant.game3 = permutation[5][2]

class Overview(Page):
    pass



page_sequence = [Introduction, SetGroups, Overview]


