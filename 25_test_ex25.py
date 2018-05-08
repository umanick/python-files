#25_test_ex25.py

import ex25
sentence = "All good things come to those who wait."
words = ex25.break_em(sentence)
print words
#words = ex25.sort_em(words)
#print words
#words = ex25.sort_sentence(sentence)
#print words
print 'Printing first words from "words"'
ex25.print_first_word(words)
print 'Printing last words from "words"'
ex25.print_last_word(words)
print 'Printing first and last words from "words"'
ex25.print_first_and_last(sentence)
words = ex25.sort_sentence(sentence)
print words
print 'Printing first words from "words" after sorting'
ex25.print_first_word(words)
print 'Printing last words from "words" after sorting'
ex25.print_last_word(words)
print 'Printing first and last words from "words" after sorting'
ex25.print_first_last_sorted(sentence)