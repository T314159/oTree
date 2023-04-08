from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'IQ_and_rational_behavior'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    part1_intro_q1 = models.BooleanField()
    part1_intro_q2 = models.BooleanField()
    part1_intro_q3 = models.BooleanField()
    part1_intro_q4 = models.BooleanField()
    pass


# PAGES
class Introduction(Page):
    pass

class Overview(Page):
    pass

class PatternExplanation(Page):
    pass

class RavenTest(Page):
    pass

class Part1End(Page):
    pass

class Part2IntroAndPayment(Page):
    '''
    1. I will be paired with the same person for all of the games: True or False
    2. I will be randomly assigned to a new person for each game: True or False
    3. I will receive payment for every game I complete: True or False
    4. One of the 3 games will be chosen at random for my payment: True or False
    '''
    form_model = 'player'

    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Introduction, Overview, PatternExplanation, RavenTest, Part1End,
                 Part2IntroAndPayment,
                 ResultsWaitPage, Results]

"Introduction, Overview, PatternExplanation, RavenTest, Part1End"

