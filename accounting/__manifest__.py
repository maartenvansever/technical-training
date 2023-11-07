{
    "name": "mvaccount",  # The name that will appear in the App list
    "version": "17.0.0.0.1",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base", "account"],  # dependencies
    "data": [
        'views/account_inherit_form.xml'
    ],
    "installable": True,
    'license': 'LGPL-3',
}
