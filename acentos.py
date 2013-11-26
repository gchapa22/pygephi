# -*- coding: utf-8 -*-

def cambia_caracteres_utf(palabra):
    accents = { 'a': [u'á', u'\xe1'],
    			'A': [u'Á', u'\xc1'],
    			'e': [u'é', u'\xe9'],
    			'E': [u'É'],
    			'i': [u'í', u'\xed'],
    			'I': [u'Í'],
    			'o': [u'ó', u'\xf3'],
    			'O': [u'Ó', u'\xd3'],
    			'u': [u'ú', u'\xfa'],
    			'U': [u'Ú'],
                'n': [u'ñ', u'\xf1'],
                'N': [u'Ñ'] }
    if not isinstance(palabra,int):
        for (char, accented_chars) in accents.iteritems():
            for accented_char in accented_chars:
                palabra = palabra.replace(accented_char, char)
    # for letra in palabra:
    #     if letra not in abc:
    #         palabra.replace(letra,' ')
    return palabra

def quita_letras(word):
    nums = [1,2,3,4,5,6,7,8,9,0,'/','.','-','+']
    if not isinstance(word,int):
        for char in word:
            if char not in nums:
                word.replace(char, '')
    return word
