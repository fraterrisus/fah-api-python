#!/usr/bin/env python3

import objects

class Slots:
    def __init__(self, slots):
        self.slots = [objects.Slot(s) for s in slots]

    def __repr__(self):
        return [s.to_dict() for s in self.slots].__str__()
