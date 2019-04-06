import unittest


def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    # see if two numbers add up to third number


    # O(n)
    movie_dict = set()
    
    for i in range(len(movie_lengths)):
        second_movie_length = flight_length - movie_lengths[i]
        if second_movie_length in movie_dict:
            retur n True
        movie_dict.add(movie_lengths[i])
    return False
        

'''O(nlogn)
   movie_lengths.sort()
   front_pointer = 0
   back_pointer = len(movie_lengths) - 1
   while(front_pointer < back_pointer):
        sum_lengths = movie_lengths[front_pointer] + movie_lengths[back_pointer]
        if(sum_lengths == flight_length):
           return True
        elif(sum_lengths > flight_length):
            back_pointer = back_pointer - 1
        elif(sum_lengths < flight_length):
            front_pointer = front_pointer + 1
   return False
'''
   
      
    
''' O(n^2)
    no_of_movies = len(movie_lengths)
    for i in range(no_of_movies):
        for j in range(no_of_movies):
            if((movie_lengths[j] == flight_length - movie_lengths[i]) && (i != j)):
                return True

    return False
'''




# Tests

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_movie(self):
        result = can_two_movies_fill_flight([4, 3, 2], 5)
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)
