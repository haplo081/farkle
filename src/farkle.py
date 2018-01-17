import random

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
            raise Exception("Invalid die value")
        else:
            self._value = value

    def get(self):
        return self._value

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

    def get_scored_values(self):
        return [d.value for d in self._scored_dice]

    def get_current_values(self):
        return [d.value for d in self._current_dice]

    def roll(self):
        for d in self._current_dice:
            d.roll()

if __name__ == '__main__':
    f = FarkleHand()

    print (sorted(f.get_current_values()))
    f.roll()
    print (sorted(f.get_current_values()))
