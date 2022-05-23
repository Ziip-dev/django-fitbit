# Your Fitbit access credentials, which must be requested from Fitbit.
# You must provide these in your project's settings.
FITAPP_CONSUMER_KEY = None
FITAPP_CONSUMER_SECRET = None


# The verification code for verifying subscriber endpoints (default to None)
FITAPP_VERIFICATION_CODE = '452b4b45628977dcce960f240fdc857fa70193308204d8735b3c162eb42ff450'

# By default, don't subscribe to user data. Set this to true to subscribe (False)
FITAPP_SUBSCRIBE = True

# Only retrieve data for resources in FITAPP_SUBSCRIPTIONS.
# The default value of None results in all subscriptions being retrieved.
# Override it to be an OrderedDict of just the items you want retrieved in the order.
# The default ordering is ['category', 'resource'] when a subscriptions dict is
# not specified.
from collections import OrderedDict
FITAPP_SUBSCRIPTIONS = OrderedDict([
    # ('foods', ['log/caloriesIn', 'log/water']),
    ('activities', ['steps',
                    'minutesSedentary',
                    'minutesLightlyActive',
                    'minutesFairlyActive',
                    'minutesVeryActive',
                    ]),
    ])


# The initial delay (in seconds) when doing the historical data import
FITAPP_HISTORICAL_INIT_DELAY = 10
# The delay (in seconds) between items when doing requests
FITAPP_BETWEEN_DELAY = 5

# The template to use when an unavoidable error occurs during Fitbit
# integration.
FITAPP_ERROR_TEMPLATE = 'fitapp/error.html'

# The default message used by the fitbit_integration_warning decorator to
# inform the user about Fitbit integration. If a callable is given, it is
# called with the request as the only parameter to get the final value for the
# message.
FITAPP_DECORATOR_MESSAGE = 'This page requires Fitbit integration.'

# Where to redirect to after Fitbit authentication is successfully completed.
FITAPP_LOGIN_REDIRECT = '/'

# Where to redirect to after Fitbit authentication credentials have been
# removed.
FITAPP_LOGOUT_REDIRECT = '/'
