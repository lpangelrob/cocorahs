#!/usr/local/bin/python

import argparse

parser = argparse.ArgumentParser(description='Calculate water value for provided weight.')
parser.add_argument("weight", help='Weight (in grams) of the CoCoRaHS canister.', type=float)
args = parser.parse_args()

amount = (int(args.weight) - 462) / 197
print('Precip: %(amount).02f' % {'amount': amount})
