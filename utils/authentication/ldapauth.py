#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import ldap

class AuthLDAP(object):
    """
    AuthLDAP: Authenticate a user against a ldap server
    """

    def __init__(self, ldapserver="127.0.0.1", domain="WORKSHOP", ssl=True, groups=[]):
        self.ldapserver = ldapserver
        self.domain = domain
        self.ssl = ssl
        self.groups = groups

    def authenticate(self, username, password):
        self.server = ldap.open(self.ldapserver)
        try:
            self.server.simple_bind_s(username, password)
        except Exception:
            return False
        else:
            return True
