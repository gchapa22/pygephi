# -*- coding: utf-8 -*-

def cambia_caracteres_utf(palabra):
    accents = { 'a': 'á',
    			'A': 'Á',
    			'e': 'é',
    			'E': 'É',
    			'i': 'í',
    			'I': 'Í',
    			'o': 'ó',
    			'O': 'Ó',
    			'u': 'ú',
    			'U': 'Ú',
                'ñ': 'n',
                'Ñ': 'N' }
    for (char, accented_char) in accents.iteritems():
        palabra = palabra.replace(accented_char, char)
    return palabra
