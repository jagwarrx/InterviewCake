import unittestdef reverse_char(message, front_pointer, back_pointer):    while front_pointer <= back_pointer:        message[front_pointer], message[back_pointer] = message[back_pointer], message[front_pointer]        front_pointer += 1        back_pointer -= 1    return message    passdef reverse_words(message):    reverse_char(message, 0 , len(message)-1)    current_word_start = 0    for i in xrange(len(message)+1):        if(i == len(message) or message[i] == ' '):            print(i)            print(reverse_char(message, current_word_start, i-1))            print(message)            current_word_start = i+1    print(message)    pass    # Testsclass Test(unittest.TestCase):    def test_one_word(self):        message = list('vault')        reverse_words(message)        expected = list('vault')        self.assertEqual(message, expected)    def test_two_words(self):        message = list('thief cake')        reverse_words(message)        expected = list('cake thief')        self.assertEqual(message, expected)    def test_three_words(self):        message = list('one another get')        reverse_words(message)        expected = list('get another one')        self.assertEqual(message, expected)    def test_multiple_words_same_length(self):        message = list('rat the ate cat the')        reverse_words(message)        expected = list('the cat ate the rat')        self.assertEqual(message, expected)    def test_multiple_words_different_lengths(self):        message = list('yummy is cake bundt chocolate')        reverse_words(message)        expected = list('chocolate bundt cake is yummy')        self.assertEqual(message, expected)    def test_empty_string(self):        message = list('')        reverse_words(message)        expected = list('')        self.assertEqual(message, expected)unittest.main(verbosity=2)
