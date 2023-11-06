{
    "name": "connect user",  # The name that will appear in the App list
    "version": "16.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        'data/connect.partner.csv',
        'views/connect_property_views.xml',
        'views/connect_menus.xml',
        'security/ir.model.access.csv',
        'views/connect_tree.xml',
        'view/connect_form.xml'
    ],
    "installable": True,
    'license': 'LGPL-3',
}
