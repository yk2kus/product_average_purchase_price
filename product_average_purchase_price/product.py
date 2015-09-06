# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

from openerp.osv import osv, fields

class product_template(osv.osv):
    _inherit = 'product.template'
    
    def _get_average_purchase_price(self, cr, uid, ids, name, arg, context=None):
        pol_obj = self.pool.get('purchase.order.line')
        res = {}
        for template in self.browse(cr, uid, ids, context=context):
            #get all purchase order lines with current product template
            res[template.id] = qty = subtot = 0.0
            product_id = self.pool.get('product.product').search(cr, uid, [('product_tmpl_id','=',template.id)])
            if len(product_id):
                line_ids = pol_obj.search(cr, uid, [('product_id', '=', product_id[0])], context=context)
                for line in pol_obj.browse(cr, uid, line_ids, context):
                    qty += line.product_qty
                    subtot += line.price_subtotal
                    try:
                        res[template.id] = subtot/qty
                    except:
                        pass #there might be case when qty is 0 it would give you error devision by zero
        return res 
    
    _columns = {
                'average_purchaes_price' : fields.function(_get_average_purchase_price, string= 'Average Purchase Price', type ='float')
                }
    
    
    
   