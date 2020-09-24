import unittest
from app.model import Pitch  
Pitch = Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(133,'killed by excelence')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))
