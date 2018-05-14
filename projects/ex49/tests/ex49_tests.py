from nose.tools import assert_equal
from nose.tools import assert_raises
from ex49 import parser
from ex49.parser import ParserError

def test_proper_sentence():
	word_list = [('noun', 'bear'), ('verb', 'open'), ('stop', 'the'), ('noun', 'door'), ('error', 'and'), ('error', 'smack'), ('stop', 'the'), ('stop', 'in'), ('stop', 'the'), ('error', 'nose')]
	sentence = parser.parse_sentence(word_list)
	assert_equal(sentence.sentence(), 'bear open door')

def test_player_sentence():
	word_list = [('verb', 'open'), ('stop', 'the'), ('noun', 'door'), ('error', 'and'), ('error', 'smack'), ('stop', 'the'), ('noun', 'bear'), ('stop', 'in'), ('stop', 'the'), ('error', 'nose')]
	sentence = parser.parse_sentence(word_list)
	assert_equal(sentence.sentence(), 'player open door')

def test_exception2():
	word_list = []
	assert_raises(ParserError, parser.parse_sentence, word_list)

def test_exception1():
	word_list = [('stop', 'the'), ('noun', 'door'), ('error', 'and'), ('error', 'smack')]
	assert_raises(ParserError, parser.parse_sentence, word_list)