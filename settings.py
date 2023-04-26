from os import environ


SESSION_CONFIGS = [
    dict(
        name='guess_two_thirds',
        display_name="Guess 2/3 of the Average",
        app_sequence=['guess_two_thirds', 'payment_info'],
        num_demo_participants=3
    ),
    dict(
        name='survey', app_sequence=['survey', 'payment_info'], num_demo_participants=1
    ),
    dict(
        name='ravens_test',
        display_name="Raven's Test",
        app_sequence=['ravens_test', 'payment_info'],
        num_demo_participants=2
    ),
    dict(
        name='trust_tutorial',
        display_name="Trust Tutorial",
        app_sequence=['trust_tutorial', 'payment_info'],
        num_demo_participants=2
    ),
    dict(
        name='IQ_and_rational_behavior',
        display_name="IQ and Rational Behavior",
        app_sequence=['IQ_and_rational_behavior_part1', 'ravens_test', 'IQ_and_rational_behavior_part2', 'centipede_game', 'IQ_and_rational_behavior_part3', 'payment_info'],
        num_demo_participants=2
    ),
    dict(
        name='IQ_and_rational_behavior_3',
        display_name="IQ and Rational Behavior (just part 3)",
        app_sequence=['IQ_and_rational_behavior_part3'],
        num_demo_participants=2
    ),
    dict(
        name='centipede_game',
        display_name="Centipede Game",
        app_sequence=['centipede_game'],
        num_demo_participants=2
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.01, participation_fee=5.00, doc=""
)

PARTICIPANT_FIELDS = ['unique_id', 'control', 'game1', 'game2', 'game3', 'raven_results', 'raven_score', 'raven_percentile',
                      'lottery_choice', 'dictator_choice', 'dictator_from_others', 'BI_choice', 'expiry']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '2108994663617'

INSTALLED_APPS = ['otree']
