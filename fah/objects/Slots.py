#!/usr/bin/env python3

from .Slot import Slot

class Slots:
    def __init__(self, slots):
        self.slots = [Slot(s) for s in slots]

    def __repr__(self):
        return [s.to_dict() for s in self.slots].__str__()
