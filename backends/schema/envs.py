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
    'items': {
        type: 'list',
        'schema': {
            'type': 'string',
            'data_relation': {
                'resource': 'item',
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

