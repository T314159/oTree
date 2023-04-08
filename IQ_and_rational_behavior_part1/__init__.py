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
        permutation = random.shuffle([['standard', 'constant', 'linear'],
                                      ['standard', 'linear', 'constant'],
                                      ['constant', 'standard', 'linear'],
                                      ['constant', 'linear', 'standard'],
                                      ['linear', 'standard', 'constant'],
                                      ['linear', 'constant', 'standard']])

        for player in group.get_players():
            player.participant.unique_id = player.id_in_group
            if player.id_in_group <= 4:
                player.participant.control = True
                player.participant.variant_order = permutation[0]
            elif player.id_in_group <= 8:
                player.participant.control = False
                player.participant.variant_order = permutation[1]
            elif player.id_in_group <= 12:
                player.participant.control = True
                player.participant.variant_order = permutation[2]
            elif player.id_in_group <= 16:
                player.participant.control = False
                player.participant.variant_order = permutation[3]
            elif player.id_in_group <= 20:
                player.participant.control = True
                player.participant.variant_order = permutation[4]
            else:
                player.participant.control = False
                player.participant.variant_order = permutation[5]

class Overview(Page):
    pass



page_sequence = [Introduction, SetGroups, Overview]


