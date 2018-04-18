




item = {
    #apps-manage-service
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 120,
        'required': True,
        'unique': True,
    },
    #create version
    'version': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 120,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
    },
    'jvmruntime': {
        'type': 'dict',
        'schema': {
            'mainclass': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 120,
                'required': True
            },
            'jvm_port': {
                'type': 'integer',
                'required': True
                },
            'service_port': {
                'type': 'list',
                'required': True
            },
            'java_version': {
                'type':'string',
                'allowed': ["jdk1.8", "jdk1.7"]
            },
            'java_options': {
                'type':'string',
                'minlength': 1,
                'maxlength': 300
            },
        },
    },
    'maven_env': {
        'type' : 'string',
        'allowed': ["mvn3.3-jdk7", "mvn2.2-jdk7","mvn3.3-jdk8"]
    },
    "wirte_service_started": {
        'type': 'boolean',
        'default': False,
    },
    'gulp': {
        'type': 'boolean',
        'default': False,
    },
    "have_gray_nginx": {
        'type': 'boolean',
        'default': True,
    },
    "logs": {
        "type": "list",
        "schema": {
            "log_name": {
                "type": "string"
            },
            "log_path": {
                "type": "string"
            }
        }
    },
    "required_dns": {
        "type": "list",
        "schema": {
            "name": {
                "type": "string"
            },
        },
    },
    "required_middlewares": {
        "type": "list",
        "schema": {
            "name": {
                "type": "string"
            },
            "decrpitions": {
                "type": "string"
            },
            "ports_list": {
                "type": "list",
                "schema": {
                    "name": {
                        "type": "string"
                    },
                    "port": {
                        "type": "string"
                    }
                }
            },
        },
    },
    "others": {
        "type": "list",
        "schema": {
            "name": {
                "type": "string"
            },
            "decrpitions": {
                "type": "string"
            }
        }
    },
    #item creater
    # 'author': {
    #      'type': 'dict',
    #      'schema': {
    #          '_id': {'type': 'objectid'},
    #          '_version': {'type': 'integer'}
    #      },
    #      'data_relation': {
    #          'resource': 'users',
    #          'field': '_id',
    #          'embeddable': True,
    #          'version': True,
    #      },
    #  },
}

envs = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 120,
        'required': True,
        'unique': True,
    },
    'version': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 120,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    # 'role': {
    #     'type': 'list',
    #     'allowed': ["author", "contributor", "copy"],
    # },
    # An embedded 'strongly-typed' dictionary.
    'creater': {
        'type': 'list',
        'schema': {
            'type': 'objectid',
                        'data_relation': {
                'resource': 'people',
                'field': '_id',
                'embeddable': True
            }
        }
    },
    'items': {
        'type': 'list',
        'schema': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'items',
                'field': '_id',
                'embeddable': True
            }
        }
    } ,
    # 'item': {
    #     'type': 'dict',
    #     'schema': {
    #         'name': {'type': 'string'},
    #         'version': {'type': 'string'}
    #     },
    # },
    'stroy': {
        'type': 'boolean',
        'default': False,
    },
}

