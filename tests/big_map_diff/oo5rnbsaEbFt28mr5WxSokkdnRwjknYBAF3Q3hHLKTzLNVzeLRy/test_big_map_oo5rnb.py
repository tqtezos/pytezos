from unittest import TestCase

from tests import get_data
from pytezos.michelson.contract import ContractStorage


class BigMapCodingTestoo5rnb(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_oo5rnb(self):    
        section = get_data(
            path='big_map_diff/oo5rnbsaEbFt28mr5WxSokkdnRwjknYBAF3Q3hHLKTzLNVzeLRy/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/oo5rnbsaEbFt28mr5WxSokkdnRwjknYBAF3Q3hHLKTzLNVzeLRy/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
