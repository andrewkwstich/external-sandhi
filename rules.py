from sounds import *

# Each of the below three functions is called in at least one rule manipulating the input string.

def poa_assimilate(consonant_1, consonant_2):
  '''
  consonant_1 and consonant_2 are keys in the SOUNDS dictionary corresponding to consonant phonemes.
  Returns a consonant (string) with identical features to consonant_1 except with its Place of Articulation replaced by consonant_2's.
  '''
  for k, v in SOUNDS.items():
    consonant_1_features = SOUNDS[consonant_1]
    consonant_2_features = SOUNDS[consonant_2]

    for feature in consonant_1_features:
      if feature in CPLACE:
        new_consonant_1_features = consonant_1_features[:]
        new_consonant_1_features.remove(feature)

        for feature in consonant_2_features:
          if feature in CPLACE:
            new_consonant_1_features.append(feature)

            for k, v in SOUNDS.items():
              if sorted(v) == sorted(new_consonant_1_features):
                return k

  raise Exception('Unable to find consonant with equivalent Place of Articulation')

def vowel_lengthen(vowel):
  '''
  vowel is a key in the SOUNDS dictionary corresponding to a vowel phoneme.
  If vowel is short (i.e. its feature list does not contain 'long'), returns a vowel (string) with identical features to
  consonant_1 except that it is long. If vowel is long, returns vowel.
  '''
  vowel_features = SOUNDS[vowel]
  new_vowel_features = vowel_features[:]

  if LONG not in new_vowel_features:
    new_vowel_features.append(LONG)

  for k, v in SOUNDS.items():
    if sorted(v) == sorted(new_vowel_features):
	    return k

  raise Exception('Unable to find equivalent long vowel')

def same_vplace(vowel_1, vowel_2):
  '''Returns True iff vowel_1 and vowel_2 are vowels in the SOUNDS dictionary with the same Place of Articulation
  '''
  vowel_1_features = SOUNDS[vowel_1]
  vowel_2_features = SOUNDS[vowel_2]

  if vowel_1 in VOWELS and vowel_2 in VOWELS:
    return set(vowel_1_features).intersection(VPLACE) == set(vowel_2_features).intersection(VPLACE)

'''
Each of the below classes describes a sound change and contains two functions:
A function specifying in what cases the rule applies, and a function specifying the transformation it effects.
Each rule takes as input a string of two words separated by a space.
'''

class Rule:
  
  def apply(self, pair):
    if not self.applies_to(pair):
      raise Exception('Expected `pair` to satisfy applies_to condition. Did you call applies_to beforehand?')
    return pair


class Prazlista(Rule):
  '''
  If the first word ends with a vowel and the second starts with a vowel with the same Place of Articulation,
  merges the two words together with the first vowel lengthened and the second deleted.
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False
  
    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    return same_vplace(first_phoneme, second_phoneme) and first_phoneme not in ['e', 'o', '@', '$']

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    first_phoneme = tokens[0][-1]

    return tokens[0][:-1] + vowel_lengthen(first_phoneme) + tokens[1][1:]

class Gliding(Rule):
  '''
  If the first word ends with a high vowel or vocalic 'R' and the second word starts with a vowel with a different
  Place of Articulation, replaces the last sound of the first word with its consonant equivalent.
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    if first_phoneme in HIGH_VOWELS or first_phoneme == 'R':
      return second_phoneme in VOWELS and not same_vplace(first_phoneme, second_phoneme)

    return False

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')
    first_phoneme = tokens[0][-1]

    assert first_phoneme in HIGH_VOWELS or first_phoneme == 'R', 'Last phoneme of first word should be i, I, u, U, or vocalic R'

    if first_phoneme.lower() == 'i':
      return tokens[0][:-1] + 'y ' + tokens[1]  # A space is conventionally left in Sanskrit romanizations

    if first_phoneme == 'R':
      return tokens[0][:-1] + 'r ' + tokens[1]

    if first_phoneme.lower() == 'u':
      return tokens[0][:-1] + 'v ' + tokens[1]

class NucleusTensing(Rule):
  '''
  If the first word ends with the sound 'ai' (encoded as '@') and the second begins with a vowel,
  replaces '@' with 'A' (IAST 'ā').
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    return first_phoneme == '@' and second_phoneme in VOWELS

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    first_phoneme = tokens[0][-1]

    assert first_phoneme == '@', 'Last phoneme of first word should be ai (encoded as @)'

    return tokens[0][:-1] + 'A ' + tokens[1]


class LongMidMonophthongs(Rule):
  '''
  If the first word ends with 'e' or 'o' and the second word starts with a vowel, then if that vowel is 'a', 'a' is deleted and
  replaced with an apostrophe; otherwise, 'e' or 'o' is replaced with 'a'.
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')
    
    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    if first_phoneme == 'e' or first_phoneme == 'o':
      return second_phoneme in VOWELS

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    assert first_phoneme == 'e' or first_phoneme == 'o', 'Last phoneme of first word should be e or o'

    if second_phoneme == 'a':
      return tokens[0] + ' \'' + tokens[1][1:]  # An apostrophe is conventionally inserted in romanization

    return tokens[0][:-1] + 'a ' + tokens[1]

class DiphthongGliding(Rule):
  '''
  Given the first word ends with 'au' (encoded as '$') and the second word starts with a vowel, merges the two words together
  such that the vowel sequence is replaced with 'Av' + the first sound of the second word.
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    return first_phoneme == '$' and second_phoneme in VOWELS

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    first_phoneme = tokens[0][-1]

    assert first_phoneme == '$', 'Last phoneme of first word should be au (encoded as $)'

    return tokens[0][:-1] + 'Av' + tokens[1]

class Diphthongization(Rule):
  '''
  If the first word ends with a low vowel and the second word starts with a front or back vowel,
  merges the two words together; if the second word starts with a high vowel, the vowel sequence is replaced with 'e' or 'o',
  whichever shares the high vowel's frontness/backness; otherwise, it is replaced with 'ai' (encoded as '@') or 'au' (encoded as '$').
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    if first_phoneme in LOW_VOWELS:
      return second_phoneme in FRONT_VOWELS or second_phoneme in BACK_VOWELS

    return False
  
  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    second_phoneme = tokens[1][0]

    assert second_phoneme in FRONT_VOWELS or second_phoneme in BACK_VOWELS, 'Phoneme should be a front vowel or a back vowel'

    if second_phoneme.lower() == 'i':
      return tokens[0][:-1] + 'e' + tokens[1][1:]

    if second_phoneme.lower() == 'u':
      return tokens[0][:-1] + 'o' + tokens[1][1:]

    if second_phoneme in FRONT_VOWELS:
      return tokens[0][:-1] + '@' + tokens[1][1:]
      
    if second_phoneme in BACK_VOWELS:
      return tokens[0][:-1] + '$' + tokens[1][1:]
    
class RAndSBecomeVisarga(Rule):
  '''Most Sanskrit dictionaries arbitrarily spell some words ending in the sound called 'visarga', H (IAST 'ḥ'), with a final 's' or 'r',
  depending on the grammatical properties of the word. There are no other Sanskrit words ending in 's' or 'r'. This rule replaces 's'
  and 'r' with 'H', and must be applied before all other rules relating to visarga.
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]

    return first_phoneme == 's' or first_phoneme == 'r'

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    return tokens[0][:-1] + 'H ' + tokens[1]

class LowVowelBeforeVisarga(Rule):
  '''
  Applies when the first word ends with 'a' or 'A' (IAST ā) followed by the sound called 'visarga', H (IAST 'ḥ'), and the second word
  starts with a voiced sound (consonant or vowel). If that voiced sound is a vowel other than 'a', the 'H' is deleted. Otherwise,
  'AH' becomes 'A' or 'aH' becomes 'o'; additionally, in the latter case, the voiced sound is replaced with an apostrophe if it is 'a'.
  This rule must apply before ConsonantVoicing and after RAndSBecomeVisarga.
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-2]
    second_phoneme = tokens[0][-1]
    third_phoneme = tokens[1][0]

    if second_phoneme == 'H':
      return first_phoneme in LOW_VOWELS and third_phoneme in VOICED

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    first_phoneme = tokens[0][-2]
    third_phoneme = tokens[1][0]

    assert first_phoneme.lower() == 'a', 'The second last phoneme of the first word should be A or a'

    if first_phoneme == 'A':
      return tokens[0][:-1] + ' ' + tokens[1]

    if first_phoneme == 'a':
      if third_phoneme in VOWELS:
        if third_phoneme != 'a':
          return tokens[0][:-1] + ' ' + tokens[1]

        else:
          return tokens[0][:-2] + 'o \'' + tokens[1][1:]

      else:
        return tokens[0][:-2] + 'o ' + tokens[1]
    
class ConsonantVoicing(Rule):
  '''
  If the last sound of a word is voiceless and the first sound of the second word is voiced, the voiceless sound is replaced with its
  voiced equivalent. For 'H' this eqiuvalent is 'r'; for other sounds it is the key in the SOUNDS dictionary whose value is identical
  except that it contains 'voiced'. The apply condition ensures the rule does not conflict with LowVowelBeforeVisarga.
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    if first_phoneme == 'H' and tokens[0][-2] in LOW_VOWELS:
      return False

    return second_phoneme in VOICED and first_phoneme not in VOICED

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    first_phoneme = tokens[0][-1]

    if first_phoneme == 'H':
      return tokens[0][:-1] + 'r '+ tokens[1]

    voiced_equivalent_features = SOUNDS[first_phoneme] + [VOI]

    for k, v in SOUNDS.items():
      if sorted(v) == sorted(voiced_equivalent_features):
        return tokens[0][:-1] + k + ' ' + tokens[1]
    
    raise Exception('Couldn\'t find H or a stop with voiced equivalent')

class CompensatoryLengthening(Rule):
  '''If the second last letter of the first word ends in 'i' or 'u', the last letter is 'H' or 'r', and the first letter of the 
  second word is 'r', the last letter of the first word is deleted and the preceding vowel is lengthened.
  Rule must apply before ConsonantVoicing and after NasalGemination.
  '''

  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-2]
    second_phoneme = tokens[0][-1]
    third_phoneme = tokens[1][0]

    if second_phoneme == 'H':
      # The rule given in the source contradicts itself about what happens to 'aH r'; other sources give that it returns 'o r'
      return first_phoneme in SHORT_VOWELS and first_phoneme != 'a' and third_phoneme == 'r'
    return False

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    return tokens[0][:-2] + vowel_lengthen(tokens[0][-2]) + ' ' + tokens[1]

class Nasalization(Rule):
  '''If the last sound of the first word is a stop and the first sound of the second word is a nasal, the former is replaced with its
  nasal equivalent. No Sanskrit word starts with the sound called anusvara, 'M' (IAST 'ṃ'). This rule must apply after ConsonantVoicing.
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    return first_phoneme in STOPS and second_phoneme in NASALS

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    first_phoneme = tokens[0][-1]
    first_phoneme_plus_nasalization = SOUNDS[first_phoneme] + [NAS]

    for k, v in SOUNDS.items():
      if sorted(v) == sorted(first_phoneme_plus_nasalization):
        return tokens[0][:-1] + k + ' ' + tokens[1]
   
    raise Exception('Couldn\'t find nasalized equivalent')

class NasalGemination(Rule):
  '''
  If the second last sound of the first word is a short vowel, the last sound is 'n' or 'G' (IAST 'ṅ'), and the first sound of the
  second word is a vowel, the 'n' or 'G' is geminated (doubled).
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-2]
    second_phoneme = tokens[0][-1]
    third_phoneme = tokens[1][0]

    return first_phoneme in SHORT_VOWELS and second_phoneme in ['n', 'G'] and third_phoneme in VOWELS

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    second_phoneme = tokens[0][-1]
    
    return tokens[0] + second_phoneme + ' ' + tokens[1]

class Anusvara(Rule):
  '''
  If the first word ends in 'm' and the second word begins with a consonant, 'm' becomes the anusvara 'M' (IAST ṃ).
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    return first_phoneme == 'm' and second_phoneme in CONSONANTS

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    return tokens[0][:-1] + 'M ' + tokens[1]

class PalatalizationBeforeZ(Rule):
  '''If the first word ends with a dental and the second word begins with the palatal fricative 'z' (IAST 'ś'), the dental is replaced
  with its palatal equivalent and the 'z' with 'ch' (coded as 'w').
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    return first_phoneme in DENTALS and  second_phoneme == 'z'

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    first_phoneme = tokens[0][-1]

    if first_phoneme != 'n':
      return tokens[0][:-1] + poa_assimilate(first_phoneme, 'z') + ' w' + tokens[1][1:]

    else:
      return tokens[0][:-1] + 'J z' + tokens[1][1:]

class DentalLateralization(Rule):
  '''If the first word ends with a dental and the second word starts with 'l', the dental is replaced with 'l'.
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    return first_phoneme in DENTALS and second_phoneme == 'l'

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    return tokens[0][:-1] + 'l ' + tokens[1]

class DentalPOAAssimilation(Rule):
  '''
  If the first word ends with a dental other than 'n' and the second word starts with a coronal stop, the Place of Articulation
  of the dental assimilates to that of the stop. If the dental is 'n', it is replaced with 'M' + the fricative with the same
  Place of Articulation as the following coronal stop.
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    if first_phoneme == 'n':
      return first_phoneme in DENTALS and second_phoneme in CORONALS and second_phoneme in STOPS and second_phoneme not in VOICED

    return first_phoneme in DENTALS and second_phoneme in CORONALS and second_phoneme in STOPS

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    if first_phoneme != 'n':
      return tokens[0][:-1] + poa_assimilate(first_phoneme, second_phoneme) + ' ' + tokens[1]

    else:
      first_phoneme_assimilated = None

      for k, v in SOUNDS.items():
        if FRIC in v and len(set(v).intersection(SOUNDS[second_phoneme])) == 1:
          first_phoneme_assimilated = k
          break
      
      if first_phoneme_assimilated is None:
        raise Exception('Couldn\'t find a fricative to which to assimilate n')
      return tokens[0][:-1] + 'M' + first_phoneme_assimilated + ' ' + tokens[1]
    

class VisargaPOAAssimilation(Rule):
  '''
  If the first word ends with 'H' (IAST ḥ) and the second word starts with a coronal stop, the Place of Articulation of 'H'
  changes to that of the following stop.
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    return first_phoneme == 'H' and second_phoneme in CORONALS and second_phoneme in STOPS and second_phoneme not in VOICED

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    second_phoneme = tokens[1][0]

    return tokens[0][:-1] + poa_assimilate('H', second_phoneme) + ' ' + tokens[1]

class Buccalization(Rule):
  '''
  If the first word ends with a stop and the second word begins with 'h', the 'h' becomes the aspirated equivalent of the stop.
  '''
  def applies_to(self, pair):
    tokens = pair.split(' ')

    if len(tokens) == 1:
      return False

    first_phoneme = tokens[0][-1]
    second_phoneme = tokens[1][0]

    return first_phoneme in STOPS and second_phoneme == 'h'

  def apply(self, pair):
    pair = super().apply(pair)
    tokens = pair.split(' ')

    first_phoneme = tokens[0][-1]

    if first_phoneme in VOICED:
      first_phoneme_features = SOUNDS[first_phoneme] + [ASP]
    else:
      first_phoneme_features = SOUNDS[first_phoneme] + [VOI, ASP]

    second_phoneme = None

    for k, v in SOUNDS.items():
      if sorted(v) == sorted(first_phoneme_features):
        second_phoneme = k
    
    if second_phoneme is None:
        raise Exception('Couldn\'t find an aspirated equivalent to the last phoneme of the first word')  

    return tokens[0] + ' ' + second_phoneme + tokens[1][1:]

RULES = [
  Prazlista(),
  DiphthongGliding(),
  Diphthongization(),
  LongMidMonophthongs(),
  NucleusTensing(),
  Gliding(),
  RAndSBecomeVisarga(),
  LowVowelBeforeVisarga(),
  NasalGemination(),
  Anusvara(),
  PalatalizationBeforeZ(),
  DentalLateralization(),
  CompensatoryLengthening(),
  ConsonantVoicing(),
  DentalPOAAssimilation(),
  Nasalization(),
  VisargaPOAAssimilation(),
  Buccalization(),
]

class FinalRAndSBecomeVisarga:
  '''
  A final R or S at the end of a string becomes visarga.
  '''
  def applies_to(self, string):
    return string[-1] == 'r' or string[-1] == 's'
  
  def apply(self, string):
    return string[:-1] + 'H'