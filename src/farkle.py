import random


class FarkleError(Exception):
    pass


class EmptyHandError(FarkleError):
    pass

class InvalidDieFace(FarkleError):
    pass


class SixSidedDie(object):
    def __init__(self, value=None) -> None:
        self._value = None
        if value is not None:
            self.set(value)
        else:
            self.roll()

    @property
    def value(self):
        return self._value

    def roll(self):
        self._value = random.randint(1, 6)
        return self._value

    def set(self, value):
        if value < 1 or value > 6:
            raise InvalidDieFace("Invalid die value")
        else:
            self._value = value

    def get(self):
        return self._value

    def __eq__(self, other):
        if isinstance(other, SixSidedDie):
            other = other.value
        return self.value == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, SixSidedDie):
            other = other.value
        return self.value > other

    def __ge__(self, other):
        if isinstance(other, SixSidedDie):
            other = other.value
        return self.value >= other

    def __lt__(self, other):
        if isinstance(other, SixSidedDie):
            other = other.value
        return self.value < other

    def __le__(self, other):
        if isinstance(other, SixSidedDie):
            other = other.value
        return self.value <= other

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self._value)


class FarkleHand(object):

    def __init__(self, scored=None, current=None) -> None:
        self._farkle = False
        self._scored_dice = list()
        self._current_dice = list()
        self._score = 0
        self._roll_count = 0

        if scored is not None:
            for d in scored:
                if isinstance(d, SixSidedDie):
                    self._scored_dice.append(d)
                else:
                    self._scored_dice.append(SixSidedDie(d))
        if current is not None:
            for d in current:
                if isinstance(d, SixSidedDie):
                    self._current_dice.append(d)
                else:
                    self._current_dice.append(SixSidedDie(d))
        else:
            self._current_dice = self._new_hand()

    def __repr__(self) -> str:
        parms = list()
        if self._scored_dice:
            parms.append("scored=[")
            for d in self._scored_dice:
                parms.append(d.__repr__())
            parms.append("]")
        if self._current_dice:
            parms.append("current=[")
            for d in self._current_dice:
                parms.append(d.__repr__())
            parms.append("]")
        return "{}({})".format(self.__class__.__name__, "".join(parms))

    def _new_hand(self):
        return [SixSidedDie() for i in range(6)]

    def get_scored_dice(self):
        return list(self._scored_dice)

    def get_current_dice(self):
        return list(self._current_dice)

    def roll(self):
        for d in self._current_dice:
            d.roll()

    def score(self, dice):
        scored_dice = list()
        scored_dice_i = list()
        for die in dice:
            if isinstance(die, int):
                scored_die = self._current_dice[die]
                scored_dice_i.append(die)
            else:
                index = self._current_dice.index(die)
                scored_die = self._current_dice[index]
                scored_dice_i.append(index)
            scored_dice.append(scored_die)
        self._scored_dice.append(tuple(scored_dice))
        self._current_dice = [d
                              for i, d
                              in enumerate(self._current_dice)
                              if i not in scored_dice_i]


if __name__ == '__main__':
    f = FarkleHand()

    print (f.get_current_dice())
    f.roll()
    print (f.get_current_dice())
    f.score([0, 1, 2])

    print (f.get_scored_dice())
    print (f.get_current_dice())
