from flask import Flask, g
from flask_simpleldap import LDAP

app = Flask(__name__)
app.secret_key = 'dev key'
app.debug = True

app.config['LDAP_HOST'] = '127.0.0.1'
app.config['LDAP_PORT'] = '1389'
app.config['LDAP_USERNAME'] = 'cn=admin,dc=example,dc=com'
app.config['LDAP_PASSWORD'] = 'Password123'
app.config['LDAP_BASE_DN'] = 'ou=users,dc=example,dc=com'
app.config['LDAP_OBJECTS_DN'] = 'uid'
app.config['LDAP_USER_OBJECT_FILTER'] = '(&(objectclass=person)(uid=%s))'
app.config['LDAP_OPENLDAP'] = True

ldap = LDAP(app)


@app.route('/')
@app.route("/openldap", strict_slashes=False)
@ldap.basic_auth_required
def index():
    return 'Welcome, {0}!'.format(g.ldap_username)
