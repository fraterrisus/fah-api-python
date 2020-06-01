#!/usr/bin/env/python3

class Options:
    def __init__(self, obj):
        self.child = bool(obj['child'])
        self.daemon = bool(obj['daemon'])
        self.fold_anon = bool(obj['fold-anon'])
        self.log_date = bool(obj['log-date'])
        # self.password = obj['password']
        if obj['password'] is not None:
            self.password_set = True
        else:
            self.password_set = False

        self.power = obj['power'] # LIGHT
        self.team = obj['team']
        self.user = obj['user']

    def to_dict(self):
        return { 
            'child': self.child,
            'daemon': self.daemon,
            'fold_anon': self.fold_anon,
            'log_date': self.log_date,
            # 'password': self.password,
            'password_set': self.password_set,
            'power': self.power,
            'team': self.team,
            'user': self.user,
        }

    def __repr__(self):
        return self.to_dict().__str__()
