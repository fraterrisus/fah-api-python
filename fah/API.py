#!/usr/bin/env python3

from .Connection import Connection

__connection = None
__password = None


def set_password(new_pass):
    global __password
    __password = new_pass


def heartbeat():
    return __send_command_and_parse('heartbeat')

#def info():
#    return __send_command_and_parse('info')

def options():
    return __send_command_and_parse('options -d')

def slot_info():
    return __send_command_and_parse('slot-info')
    

def __authorize():
    global __password
    conn = __get_connection()
    if __password is not None:
        conn.write_data(b'auth %s\n' % (__password.encode('utf-8')))
        return conn.read_data()
    else:
        return None


def __get_connection():
    global __connection
    if __connection is None:
        __connection = Connection()

    return __connection


def __send_command_and_parse(chars):
    conn = __get_connection()
    conn.read_data()
    _authorize()
    conn.write_data(b'%s\n' % (chars.encode('utf-8')))
    text = conn.read_data()
    obj = conn.parse_pyon(text)
    conn.close()
    return obj
