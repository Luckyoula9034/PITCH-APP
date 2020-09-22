import unittest
from models import pitch
Pitch = pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(122,'lucky')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


if __name__ == '__main__':
    unittest.main()