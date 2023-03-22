import ldap3
import os

LDAP_URI = "ldap://ldap:389"
LDAP_USER = "cn=admin,dc=example,dc=com"
LDAP_PASSWORD = "abc123456"
KDC = "kerberos"
KRB5_REALM = "EXAMPLE.COM"

os.system(f"echo -e '{LDAP_PASSWORD}\n{LDAP_PASSWORD}' | kinit -V -r 7d -f {LDAP_USER}@{KRB5_REALM}")

server = ldap3.Server(LDAP_URI, get_info=ldap3.ALL)
conn = ldap3.Connection(server, user=LDAP_USER, password=LDAP_PASSWORD, auto_bind=True)

if conn.bind():
    print("Success")
else:
    print("Failed")

