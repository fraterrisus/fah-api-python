#!/usr/bin/env python3

from dateutil.parser import isoparse

class Unit:
    def __init__(self, obj):
        self.id = int(obj['id'])
        self.assigned = isoparse(obj['assigned'])
        self.attempts = obj['attempts']
        self.base_credit = int(obj['basecredit'])
        self.clone = obj['clone'] #int
        self.core = obj['core'] #hex?
        self.credit_estimate = int(obj['creditestimate'])
        self.cs = obj['cs']
        self.deadline = isoparse(obj['deadline'])
        self.error = obj['error'] #str
        self.eta = obj['eta'] #str
        self.frames_done = int(obj['framesdone'])
        self.gen = obj['gen'] #int
        self.next_attempt = obj['nextattempt']
        self.percent_done = float(obj['percentdone'][:-1]) / 100
        self.project = obj['project'] #int
        self.run = obj['run'] #int
        self.slot = int(obj['slot'])
        self.state = obj['state'] #str
        self.timeout = isoparse(obj['timeout'])
        self.time_remaining = obj['timeremaining']
        self.total_frames = int(obj['totalframes'])
        self.tpf = obj['tpf']
        self.unit = obj['unit'] #hex?
        self.waiting_on = obj['waitingon']
        self.ws = obj['ws']


    def to_dict(self):
        return {
            'id': self.id,
            'assigned': self.assigned,
            'attempts': self.attempts,
            'base_credit': self.base_credit,
            'clone': self.clone,
            'core': self.core,
            'credit_estimate': self.credit_estimate,
            'cs': self.cs,
            'deadline': self.deadline,
            'error': self.error,
            'eta': self.eta,
            'frames_done': self.frames_done,
            'gen': self.gen,
            'next_attempt': self.next_attempt,
            'percent_done': self.percent_done,
            'project': self.project,
            'run': self.run,
            'slot': self.slot,
            'state': self.state,
            'timeout': self.timeout,
            'time_remaining': self.time_remaining,
            'total_frames': self.total_frames,
            'tpf': self.tpf,
            'unit': self.unit,
            'waiting_on': self.waiting_on,
            'ws': self.ws,
        }


    def __repr__(self):
        return self.to_dict().__str__()
