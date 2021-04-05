VOI = 'voiced'
VEL = 'velar'
PAL = 'palatal'
RET = 'retroflex'
DEN = 'dental'
LAB = 'labial'
GLOT = 'glottal'
NAS = 'nasal'
ASP = 'aspirated'
SON = 'sonorant'
FRIC = 'fricative'
HIGH = 'high'
LONG = 'long'
LOW = 'low'
BACK = 'back'
FRONT = 'front'
DIPH = 'diphthong'
SOUNDS = {
'k':[VEL],
'f':[VEL, ASP],
'g':[VEL, VOI],
'q':[VEL, VOI, ASP],
'c':[PAL],
'w':[PAL, ASP],
'j':[PAL, VOI],
'x':[PAL, VOI, ASP],
'T':[RET],
'F':[RET, ASP],
'D':[RET, VOI],
'Q':[RET, VOI, ASP],
't':[DEN],
'W':[DEN, ASP],
'd':[DEN, VOI],
'X':[DEN, VOI, ASP],
'p':[LAB],
'&':[LAB, ASP],
'b':[LAB, VOI],
'^':[LAB, VOI, ASP],
'G':[VEL, NAS, VOI],
'J':[PAL, NAS, VOI],
'N':[RET, NAS, VOI],
'n':[DEN, NAS, VOI],
'm':[LAB, NAS, VOI],
'M':[NAS, VOI],
'y':[PAL, SON, VOI],
'r':[RET, SON, VOI],
'l':[DEN, SON, VOI],
'v':[LAB, SON, VOI],
'H':[GLOT, FRIC],
'z':[FRIC, PAL],
'S':[FRIC, RET],
's':[FRIC, DEN],
'h':[GLOT, FRIC, VOI],
'i':[HIGH, FRONT, VOI],
'I':[HIGH, FRONT, LONG, VOI],
'u':[HIGH, BACK, VOI],
'U':[HIGH, BACK, LONG, VOI],
'a':[LOW, VOI],
'A':[LOW, LONG, VOI],
'e':[FRONT, LONG, VOI],
'o':[BACK, LONG, VOI],
'@':[FRONT, LONG, DIPH, VOI],
'$':[BACK, LONG, DIPH, VOI],
'R':[RET, VOI],
'#': [RET, VOI, LONG]
}
CONSONANTS = ['k', 'f', 'g', 'q', 'c', 'w', 'j', 'x', 'T', 'F', 'D', 'Q', 't', 'W', 'd', 'X', 'p', '&', 'b', '^', 'G', 'J', 'N', 'n', 'm', 'M', 'y', 'r', 'l', 'v', 'H', 'z', 'S', 's', 'h']

VOWELS = ['i', 'I', 'u', 'U', 'a', 'A', 'e', 'o', '@', '$', 'R', '#']

VOICED = []
for k, v in SOUNDS.items():
	if VOI in v:
		VOICED.append(k)
			
FRICATIVES = []
for k, v in SOUNDS.items():
	if FRIC in v:
		FRICATIVES.append(k)

DENTALS = []
for k, v in SOUNDS.items():
  if DEN in v:
    DENTALS.append(k)
			
CORONALS = []
for k, v in SOUNDS.items():
	if PAL in v or RET in v or DEN in v:
		CORONALS.append(k)

CONTINUANTS = []
for k, v in SOUNDS.items():
	if FRIC in v or SON in v or NAS in v or k in VOWELS:
		CONTINUANTS.append(k)

NASALS = []
for k, v in SOUNDS.items():
	if NAS in v:
		NASALS.append(k)

STOPS = ['k', 'f', 'g', 'q', 'c', 'w', 'j', 'x', 'T', 'F', 'D', 'Q', 't', 'W', 'd', 'X', 'p', '&', 'b', '^']
			
HIGH_VOWELS = []
for k, v in SOUNDS.items():
	if HIGH in v:
		HIGH_VOWELS.append(k)
			
LOW_VOWELS = []
for k, v in SOUNDS.items():
	if LOW in v:
	    LOW_VOWELS.append(k)
			
FRONT_VOWELS = []
for k, v in SOUNDS.items():
	if FRONT in v:
		FRONT_VOWELS.append(k)
		
BACK_VOWELS = []		
for k, v in SOUNDS.items():
	if BACK in v:
		BACK_VOWELS.append(k)

RETRO_VOWELS = ['R', '#']

LONG_VOWELS = []
for k, v in SOUNDS.items():
	if LONG in v:
		LONG_VOWELS.append(k)

SHORT_VOWELS = ['a', 'i', 'u']

DIPHTHONGS = ['@', '$']

CPLACE = [VEL, PAL, RET, DEN, LAB, GLOT]
VPLACE = [HIGH, LOW, BACK, FRONT, RET]