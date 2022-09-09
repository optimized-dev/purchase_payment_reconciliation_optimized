{
    'name': 'Purchase Payment Reconciliation',
    'version': '15.1',
    'sequence': 185,
    'category': 'Invoicing',
    'website': 'https://amis.lk/',
    'author': "Sachitha Perera",
    'summary': 'Manage Purchase Payments with pre payments',
    'depends': [
        'base',
        'mail',
        'account'
    ],
    'data': [
        'views/account_account_inherit_view.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
