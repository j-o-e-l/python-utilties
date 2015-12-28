#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
#============================================================================
Filename   : genpw_sha512.py
Author     : <joel (a t) jacean (d o t) com>
Date       : 27 December 2015
Version    : 0.1
Copyright  : Copyright © 2015 JACEAN LLC
             All rights reserved. See LICENSE file.

             This project is licensed under the BSD 2-Clause license, it is 
             made possible by the PyMOTW, Passlib, Python open source 
             project(s) and other open source software.
 
             Copyright © 2008 Doug Hellmann
             Copyright © 2008-2015 Assurance Technologies, LLC.
             Copyright © 2001-2015 Python Software Foundation. 

Description: Usage 1: Prompt the user for a password, without echoing what 
                      they type to the console, then SHA-512 hash the input.

             Usage 2: From stdin (ex. echo "password" | python genpw_sha512.py)
                      SHA-512 the input.

             These are suitable for a Linux password to be stored in the 
             /etc/shadow file.

Credits    : https://pymotw.com/2/getpass/
             http://www.doughellmann.com/PyMOTW/
             https://bitbucket.org/ecollins/passlib/wiki/Home
             https://www.python.org/

Warning    : This code does NO 'real' error checking, use at your own risk!
#============================================================================
"""
from passlib.hash import sha512_crypt
import getpass
import sys

def main():  
    if sys.stdin.isatty():
        print('[.] TTY detected.')
        plain_text_password = getpass.getpass('[.] Enter your password to be SHA-512 hashed: ')
    else:
        plain_text_password = sys.stdin.readline().rstrip()
        
    if plain_text_password == "":
        print("[!] WARNING: Detected blank password.")

    hashed_pw = sha512_crypt.encrypt( plain_text_password )

    print(hashed_pw)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print('Usage 1: echo "password" | python {0}').format( sys.argv[0] )
        print('Usage 2: python {0}').format( sys.argv[0] )
        sys.exit()
    else:
        main()
