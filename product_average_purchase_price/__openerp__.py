# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Product Purchase Average Price',
    'version': '7.0',
    'author': 'Yogesh kushwaha',
    'website': 'http://www.openerp.com',
    'sequence':130,
    'category': 'Project Management',
    'images': ['image/price.jpg'],
    'depends': [
                'product',
                'purchase',
                ],
    'description': """
        This module adds purchase average price on product template form and tree view
        
        Features:
        It computes average price by searching prices in purchaes order lines in all states
    """,
    'demo': [],
    'test': [
    ],
    'data': [
       'product_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
