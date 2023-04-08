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
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.unique_id = player.id_in_group
        if player.id_in_group <= 4:
            player.participant.control = True
        elif player.id_in_group <= 8:
            player.participant.control = False
        elif player.id_in_group <= 12:
            player.participant.control = True
        elif player.id_in_group <= 16:
            player.participant.control = False
        elif player.id_in_group <= 20:
            player.participant.control = True
        else:
            player.participant.control = False

class Overview(Page):
    pass


page_sequence = [Introduction, Overview]


