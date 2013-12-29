#!/usr/local/bin/python
print('Weight (g): ',end='')
precipInGrams = input()
amount = (int(precipInGrams) - 462) / 197
print('%(amount).02f' % {'amount': amount})
