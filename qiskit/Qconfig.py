# Before you can use the jobs API, you need to set up an access token.
# Log in to the IBM Q experience. Under "Account", generate a personal
# access token. Replace 'PUT_YOUR_API_TOKEN_HERE' below with the quoted
# token string. Uncomment the APItoken variable, and you will be ready to go.

APItoken = '8c59ea067e5408b44148e8ee035e5ef44edddfb2f00e52cc4d97993100bee472e3e65b14925856c1e426cbfe76899dde4c428d225960992fe9b203c7b05c5951+'

config = {
    'url': 'https://quantumexperience.ng.bluemix.net/api',

    # If you have access to IBM Q features, you also need to fill the "hub",
    # "group", and "project" details. Replace "None" on the lines below
    # with your details from Quantum Experience, quoting the strings, for
    # example: 'hub': 'my_hub'
    # You will also need to update the 'url' above, pointing it to your custom
    # URL for IBM Q.
    'hub': None,
    'group': None,
    'project': None
}

if 'APItoken' not in locals():
    raise Exception('Please set up your access token. See Qconfig.py.')
