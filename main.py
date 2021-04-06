from rules import *
from transliteration import *

def do_external_sandhi(string, transliteration=NON_STANDARD):
  '''
  Applies external sandhi on a string.
  '''
  string = transliteration.decode(string)

  tokens = string.split(' ')
  if len(tokens) > 1:
    accumulator = ''  # accumulator stores "output so far"
    for i in range(1, len(tokens)):
      accumulator_tokens = accumulator.split(' ')
      if not accumulator:
        first_word = tokens[0]
      else:
        first_word = accumulator_tokens[-1]
      
      pair = first_word + ' ' + tokens[i]
      for rule in RULES:
        if rule.applies_to(pair):
          pair = rule.apply(pair)
      
      accumulator = ' '.join(accumulator_tokens[:-1])
      if accumulator:
        accumulator += ' '
      accumulator += pair

    string = accumulator

  string_end_rule = FinalRAndSBecomeVisarga()
  '''
  This rule is the only one to apply to the whole string.
  '''
  if string and string_end_rule.applies_to(string):
    string = string_end_rule.apply(string)

  return transliteration.encode(string)

if __name__ == '__main__':
  use_iast = input('Use IAST (y/n)? ')
  transliteration = {
    'y': IAST,
    'n': NON_STANDARD
  }[use_iast]

  while True:
    string = input('Please enter some Sanskrit text: ')
    print(do_external_sandhi(string, transliteration))