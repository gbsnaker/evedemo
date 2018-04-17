# -*- coding: utf-8 -*-

"""
    Eve Demo
    ~~~~~~~~
    A demostration of a simple API powered by Eve REST API.
    The live demo is available at eve-demo.herokuapp.com. Please keep in mind
    that the it is running on Heroku's free tier using a free MongoHQ
    sandbox, which means that the first request to the service will probably
    be slow. The database gets a reset every now and then.
    :copyright: (c) 2016 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""
import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

#sys.path.insert(0, "/path/to/your/package_or_module")

from flask_script import Manager
from eve import Eve
from eve_swagger import swagger, add_documentation




from backends.auths.auth import MyBasicAuth

# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'



#app = Flask(__name__)
#app = Eve(auth=MyBasicAuth)
app = Eve()
app.register_blueprint(swagger)
# required. See http://swagger.io/specification/#infoObject for details.
app.config['SWAGGER_INFO'] = {
    'title': 'My Supercool API',
    'version': '1.0',
    'description': 'an API description',
    'termsOfService': 'my terms of service',
    'contact': {
        'name': 'evedemo',
        'url': 'https://github.com/gbsnaker/evedemo'
    },
    'license': {
        'name': 'BSD',
        'url': 'https://github.com/pyeve/eve-swagger/blob/master/LICENSE',
    },
    'schemes': ['http', 'https'],
}

# optional. Will use flask.request.host if missing.
app.config['SWAGGER_HOST'] = '127.0.0.1'

# optional. Add/Update elements in the documentation at run-time without deleting subtrees.
add_documentation({'paths': {'/status': {'get': {'parameters': [
    {
        'in': 'query',
        'name': 'foobar',
        'required': False,
        'description': 'special query parameter',
        'type': 'string'
    }]
}}}})

# configure your app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()


