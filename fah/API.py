#!/usr/bin/env python3

class API:
    def __init__(self):
        conn = Connection()
        text = conn.read_data()
        conn.write_data(b'auth putzfuck\n')
        text = conn.read_data()
        conn.write_data(b'slot-info\n')
        text = conn.read_data()
        slots = conn.parse_pyon(text)
        print(slots)
        conn.close()
        
if __name__ == '__main__':
    API()
