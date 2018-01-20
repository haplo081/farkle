from ..farkle import SixSidedDie, InvalidDieFace
from unittest import TestCase

DICE_RANGE = range(1, 7)

class TestSixSidedDie(TestCase):
    def test_eq(self):
        self.assertTrue(SixSidedDie(4) == SixSidedDie(4))
        self.assertFalse(SixSidedDie(4) == SixSidedDie(5))

    def test_ne(self):
        self.assertFalse(SixSidedDie(4) != SixSidedDie(4))
        self.assertTrue(SixSidedDie(4) != SixSidedDie(5))

    def test_gt(self):
        self.assertFalse(SixSidedDie(4) > SixSidedDie(4))
        self.assertFalse(SixSidedDie(4) > SixSidedDie(5))
        self.assertTrue(SixSidedDie(5) > SixSidedDie(4))

    def test_ge(self):
        self.assertTrue(SixSidedDie(4) >= SixSidedDie(4))
        self.assertFalse(SixSidedDie(4) >= SixSidedDie(5))
        self.assertTrue(SixSidedDie(5) >= SixSidedDie(4))

    def test_lt(self):
        self.assertFalse(SixSidedDie(4) < SixSidedDie(4))
        self.assertTrue(SixSidedDie(4) < SixSidedDie(5))
        self.assertFalse(SixSidedDie(5) < SixSidedDie(4))

    def test_le(self):
        self.assertTrue(SixSidedDie(4) <= SixSidedDie(4))
        self.assertTrue(SixSidedDie(4) <= SixSidedDie(5))
        self.assertFalse(SixSidedDie(5) <= SixSidedDie(4))

    def test_value(self):
        for i in DICE_RANGE:
            self.assertEqual(i, SixSidedDie(i).value)

    def test_get(self):
        for i in DICE_RANGE:
            self.assertEqual(i, SixSidedDie(i).value)

    def test_set(self):
        die = SixSidedDie()
        for i in DICE_RANGE:
            die.set(i)
            self.assertEqual(i, die.value)
        self.assertRaises(InvalidDieFace, die.set, 0)
        self.assertRaises(InvalidDieFace, die.set, 7)
