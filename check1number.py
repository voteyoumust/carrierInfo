#!/usr/bin/env python

# code based on twilio example here:
# https://www.twilio.com/docs/lookup/tutorials/carrier-and-caller-name#identify-a-phone-numbers-carrier-and-type

from twilio.rest import Client

import argparse
import json

argp = argparse.ArgumentParser(description='test program to get carrier info via twilio')
argp.add_argument('--credential', '-c', help='twilio credential specified as json with keys "account_sid" and "auth_token"', required=True)
argp.add_argument('--debug', '-d', help='enable debug print', action='store_true')
argp.add_argument('--phone_number', '-n', help='US telephone number', type=str, required=True)
args=vars(argp.parse_args())

with open(args['credential'], 'r') as json_input:
    tcr = json.load(json_input)

if args['debug']:
    print(tcr)

client = Client(tcr['account_sid'], tcr['auth_token'])

phone_number = client.lookups \
                     .phone_numbers(args['phone_number']) \
                     .fetch(type=['carrier'])

if args['debug']:
    print(phone_number.carrier)
else:
    print(phone_number.carrier['name'])
