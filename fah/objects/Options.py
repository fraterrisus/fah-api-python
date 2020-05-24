#!/usr/bin/env/python3

# Several parameters are excluded for security
class Options:
    def __init__(self, obj):
        # self.allow = obj['allow']
        self.child = bool(obj['child'])
        self.daemon = bool(obj['daemon'])
        # self.deny = obj['deny']
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
        # self.web_allow = obj['web-allow']

    def to_dict(self):
        return { 
            # 'allow': self.allow,
            'child': self.child,
            'daemon': self.daemon,
            # 'deny' : self.deny,
            'fold_anon': self.fold_anon,
            'log_date': self.log_date,
            # 'password': self.password,
            'password_set': self.password_set,
            'power': self.power,
            'team': self.team,
            'user': self.user,
            # 'web_allow': self.web_allow,
        }

    def __repr__(self):
        return self.to_dict().__str__()
