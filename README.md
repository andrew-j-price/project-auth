# Project-Auth
I made this repo for me, but if you happen to stumble across it then please enjoy!

### Notes
I needed a development environment to test various LDAP and SSO configurations
  - Since this is a throw away development environment, I take several liberties like running a GUI and logging in as root
  - Some sample code included in this repo are from other projects I have configured, which may or may not appear relevant

### Note WSGI ways to import Python apps
Take a look at "__ init__.py" and "wsgi.py" in the directories below:
  - www_apps/hello_flask
  - www_apps/host
  - www_apps/rps

### LDAP authentication examples
```
curl --user andrpric:Password123 http://127.0.0.1:5000
curl --user andrpric:Password123 http://127.0.0.1/389ds/
curl --user andrpric:Password123 http://127.0.0.1/openldap/
```

### Clean-up files (be very very careful)
```
for i in `find . -name *.pyc`; do echo $i; done
for i in `find . -name *.pyc`; do rm -f $i; done
```
