
import bcrypt
from werkzeug.security import check_password_hash
from hashlib import sha1
import hmac

from eve.auth import TokenAuth
from eve.auth import HMACAuth
from flask import current_app as app
from eve.auth import BasicAuth

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        return True
        #return username == 'admin' and password == 'secret'



#Basic Authentication with bcrypt
class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        account = accounts.find_one({'username': username})
        return account and \
            bcrypt.hashpw(password, account['password']) == account['password']


#Basic Authentication with SHA1/HMAC
class Sha1Auth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        account = accounts.find_one({'username': username})
        return account and \
            check_password_hash(account['password'], password)

#Token-Based Authentication
class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        """For the purpose of this example the implementation is as simple as
        possible. A 'real' token should probably contain a hash of the
        username/password combo, which sould then validated against the account
        data stored on the DB.
        """
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        return accounts.find_one({'token': token})

#HMAC Example
class HMACAuth(HMACAuth):
    def check_auth(self, userid, hmac_hash, headers, data, allowed_roles,
                   resource, method):
        # use Eve's own db driver; no additional connections/resources are
        # used
        accounts = app.data.driver.db['accounts']
        user = accounts.find_one({'userid': userid})
        if user:
            secret_key = user['secret_key']
        # in this implementation we only hash request data, ignoring the
        # headers.
        return user and \
            hmac.new(str(secret_key), str(data), sha1).hexdigest() == \
                hmac_hash


#base role setting  ALLOWED_ROLES = ['admin']
class RolesAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        lookup = {'username': username}
        if allowed_roles:
            # only retrieve a user if his roles match ``allowed_roles``
            lookup['roles'] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        return account and check_password_hash(account['password'], password)



#User-Restricted Resource Access
class BCryptAuth(BasicAuth):
     def check_auth(self, username, password, allowed_roles, resource, method):
         # use Eve's own db driver; no additional connections/resources are used
         accounts = app.data.driver.db['accounts']
         account = accounts.find_one({'username': username})
         # set 'auth_field' value to the account's ObjectId
         # (instead of _id, you might want to use ID_FIELD)
         if account and '_id' in account:
             self.set_request_auth_value(account['_id'])
         return account and \
             bcrypt.hashpw(password, account['password']) == account['password']


#Auth-driven Database Access
class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        if username == 'user1':
            self.set_mongo_prefix('MONGO1')
        elif username == 'user2':
            self.set_mongo_prefix('MONGO2')
        else:
            # serve all other users from the default db.
            self.set_mongo_prefix(None)
        return username is not None and password == 'secret'


#OAuth2 Integration
