from rules import *

'''Sounds represented by two letters in the input string are replaced by a single letter to make the string easier to operate on.
The replacement letters are not used in Sanskrit romanization. After sandhi rules have been applied, the placeholder letters are
reverted to the originals.
'''

transliteration = [
  ('kh', 'f'),
  ('gh', 'q'),
  ('ch', 'w'),
  ('jh', 'x'),
  ('Th', 'F'),
  ('Dh', 'Q'),
  ('th', 'W'),
  ('dh', 'X'),
  ('ph', '&'),
  ('bh', '^'),
  ('RR', '#'),
  ('ai', '@'),
  ('au', '$'),
]

def decode_user_input(string):
  for t in transliteration:
    string = string.replace(t[0], t[1])
  
  return string

def encode_user_input(string):
  for t in transliteration:
    string = string.replace(t[1], t[0])
  
  return string

def do_external_sandhi(string):
  string = decode_user_input(string)

  tokens = string.split(' ')
  if len(tokens) > 1:
    accumulator = ''  # Accumulator stores "output so far"
    for i in range(1, len(tokens)):
      accumulator_tokens = accumulator.split(' ')
      if not accumulator:
        first_word = tokens[0]
      else:
        first_word = accumulator_tokens[-1]
      
      pair = first_word + ' ' + tokens[i]
      for rule in Rules:
        if rule.applies_to(pair):
          pair = rule.apply(pair)
      
      accumulator = ' '.join(accumulator_tokens[:-1])
      if accumulator:
        accumulator += ' '
      accumulator += pair

    string = accumulator

  string_end_rule = RAndSBecomeVisarga()
  if string and string_end_rule.applies_to(string):
    string = string_end_rule.apply(string)

  return encode_user_input(string)


if __name__ == '__main__':
  while True:
    string = input('Please enter some Sanskrit text: ')
    print(do_external_sandhi(string))