{
    "name": "connect user",  # The name that will appear in the App list
    "version": "16.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        'data/connect.partner.csv',
    ],
    "installable": True,
    'license': 'LGPL-3',
}
