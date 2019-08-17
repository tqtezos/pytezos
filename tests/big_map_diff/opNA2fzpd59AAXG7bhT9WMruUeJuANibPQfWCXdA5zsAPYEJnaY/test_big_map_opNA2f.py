from unittest import TestCase

from tests import get_data
from pytezos.michelson.contract import ContractStorage


class BigMapCodingTestopNA2f(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_opNA2f(self):    
        section = get_data(
            path='big_map_diff/opNA2fzpd59AAXG7bhT9WMruUeJuANibPQfWCXdA5zsAPYEJnaY/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/opNA2fzpd59AAXG7bhT9WMruUeJuANibPQfWCXdA5zsAPYEJnaY/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
