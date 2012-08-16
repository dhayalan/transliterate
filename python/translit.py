import sys,re
from itertools import product
from lang.ta_IN import charmap

#regex for vowels & consonants
vowels = r'(A(hh)?)|(E)|(H)|(I)|(O)|(U)|(a((a)|(e)|(i)|(u))?)|(e(e)?)|(i)|(o((a)|(o))?)|(u)' 
consonants = r'(L)|(N)|(R)|(b(h)?)|(c(h)?)|(d(h)?)|(f)|(g)|(h)|(j)|(k(h)?)|(l)|(m)|(n((G)|(N)|(Y))?)|(p)|(r)|(s(h)?)|(t(h)?)|(v)|(w)|(y)|(z(h)?)' 


words = []
result_buffer=[]


def to_syllables (word):
    syllables =[]
    charmapping = []
    vowel_start = True
    while word:
        vow_re = re.compile (vowels)
        match_vow = vow_re.match(word)
        if match_vow:
            matched =  match_vow.group(0) 
            if vowel_start:
                syllables.append('~'+matched)
            else:
                syllables.append(matched)
            vowel_start = True
            word = word[len(matched):]
        else:
            cons_re = re.compile(consonants)
            match_cons = cons_re.match(word)
            if match_cons:
                matched = match_cons.group(0)
                syllables.append(matched)
                vowel_start = False
                word = word[len(matched):]
                next_char = vow_re.match(word)
                if not next_char or len(word) == 0:
                    syllables.append('*') #handle Otru character
            else:
                syllables.append(word[:1])
                word = word[1:]
    for i in syllables:
        if i in charmap:
            charmapping.append(charmap[i])
        else:
            charmapping.append(i)
    return ''.join(charmapping)


    
def test():
    """ Print all the vowels & consonants """    
    uyir_chars= ['a','A','i','I','u','U','e','E','ai','o','O','au']
    mei_chars = ['k','nG','ch','nY','t','nN','th','N','p','m','y','r','l','v','z','L','R','n']
    for i in product(mei_chars,uyir_chars):
        x,y=i
        word = to_syllables(x+y)
        print  "u'%s'" % (word)

try: 
    text = sys.argv[1]
    if text:    
        for word in text.split():
            words.append(word)

        for word in words:
            result_buffer.append(to_syllables(word))
    print ' '.join(result_buffer)
except:
    print 'No text to transliterate....Running tests'
    test()
