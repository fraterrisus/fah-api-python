#!/usr/bin/env python3

class Slot:
    def __init__(self, obj):
        self.id = obj['id']
        self.status = obj['status']
        self.description = obj['description']
        self.options = obj['options']
        self.reason = obj['reason']
        self.idle = obj['idle']

    def to_dict(self):
        return { 
            'id': self.id,
            'status': self.status,
            'description': self.description,
            'options': self.options,
            'reason': self.reason,
            'idle': self.idle,
        }

    def __repr__(self):
        return self.to_dict().__str__()
