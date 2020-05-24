#!/usr/bin/env python3

class Error:
    def __init__(self, message=None):
        self.message = message

    def message(self):
        return self.message

    def __repr__(self):
        if self.message is None:
            return '<Error object message=None>'
        else:
            return '<Error object message=%s>' % self.message
