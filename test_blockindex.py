# test_blockindex.py
"""
Tests for BlockIndex module.
"""

import unittest
from blockindex import BlockIndex

class TestBlockIndex(unittest.TestCase):
    """Test cases for BlockIndex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockIndex()
        self.assertIsInstance(instance, BlockIndex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockIndex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
