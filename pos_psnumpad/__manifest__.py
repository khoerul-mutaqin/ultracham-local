# encoding: utf-8
# Part of Odoo - CLuedoo Edition. Ask Falinwa / CLuedoo representative for full copyright And licensing details.
{
    "name": "POS Custom Numpad",
    "version": "18.0.0.0.0",
    "license": "OPL-1",
    "summary": "POS Customization",
    "category": "Inventory",    
    "author": "Falinwa",
    "website": "https://www.cluedoo.com",
    "description": """
        POS Customization
    """,
    "depends": ["point_of_sale", "base", "web"],
    "images": [],
    "init_xml": [],
    "data": [
        # 'views/pos_order_views.xml',
    ],
    "assets": {
        'point_of_sale._assets_pos': [
            'pos_nk_specific/static/src/numpad/numpad.js', 
            # 'pos_nk_specific/static/src/numpad/numpad.scss',
            # 'pos_nk_specific/static/src/numpad/numpad.xml',
        ]
    },
    "installable": True,
}
