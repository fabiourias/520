#!/bin/ptyhon3

from ldap3 import Server, Connection
from hashlib import md5
from binascii import b2a_base64
from pprint import pprint 

username = 'admin'
password = '4linux'

try:
  server = Server('ldap://127.0.0.1:389')
  con = Connection(
    server,
    "cn={},dc=dexter,dc=com,dc=br".format(username),password
  )
  con.bind()
  
  md5json = md5('senhapadrao'.encode('utf-8')).digest()
  user = {
    'cn': 'joao',
    'sn':'hummel',
    'mail':'joao.hummel@jkl.com',
    'uidNumber': '123',
    'gidNumber': '123',
    'homeDirectory': 'home/joao',
    'uid': 'joao',
    'userPassword':"{}"+b2a_base64(md5json).decode('utf-8')

  }
  objectClass = ['top', 'person', 'organizationalPerson', 'inetOrgPerson', 'posixAccount']
  cn = 'uid={},dc=dexter,dc=com,dc=br'.format(user['mail'])
  print(con.add(cn, objectClass, user))
  #dn = "udi=daniel.prata,dc=dexter,dc=com,dc=br"
 # con.search(
 #   dn, '(objectclass=person)',
  #  attributes=['sn', 'userPassword']

 # print(con.entries)

except Exception as e:
    pprint('Error: {}'.format(e))
    exit()
