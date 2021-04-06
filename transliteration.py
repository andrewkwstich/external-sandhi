class Transliteration:
    def __init__(self, schema):
        self.schema = schema
        
        
    def decode(self, string):
        for c in self.schema:
            string = string.replace(c[0], c[1])

        return string
    
    def encode(self, string):
        for c in self.schema:
            string = string.replace(c[1], c[0])
        
        return string

'''
Single sounds represented by two letters in the input string are replaced by a single character to make the string easier to operate on.
The replacement characters are not used in Sanskrit romanization.
There is no ambiguity in the digraphs: e.g., 'kh' always represents the single sound 'kh' and not the sounds 'k' + 'h'.
After sandhi rules have been applied, the placeholder characters are reverted to the original digraphs.
'''

NON_STANDARD = Transliteration([
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
    ('au', '$')
])

IAST = Transliteration([
    ('ā', 'A'),
    ('ḍ', 'D'),
    ('ḥ', 'H'),
    ('ī', 'I'),
    ('ṃ', 'M'),
    ('ṇ', 'N'),
    ('ñ', 'J'),
    ('ṅ', 'G'),
    ('ṛ', 'R'),
    ('ṝ', '#'),
    ('ṣ', 'S'),
    ('ś', 'z'),
    ('ṭ', 'T'),
    ('ū', 'U'),
    ('kh', 'f'),
    ('gh', 'q'),
    ('ch', 'w'),
    ('jh', 'x'),
    ('ṭh', 'F'),
    ('ḍh', 'Q'),
    ('th', 'W'),
    ('dh', 'X'),
    ('ph', '&'),
    ('bh', '^'),
    ('ai', '@'),
    ('au', '$')
])