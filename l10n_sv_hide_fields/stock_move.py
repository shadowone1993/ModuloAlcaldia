# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
class StockMoveExtension(models.Model):
    _inherit = ['stock.move']


    #def onchange_product_id(self, cr, uid, ids, prod_id=False, loc_id=False, loc_dest_id=False, partner_id=False):
    #    loc_obj = self.pool.get('stock.location')
    #    loc_search = loc_obj.search(cr, uid, [('usage', '!=', 'view')], limit=1)
    #    loc_browse = loc_obj.browse(cr, uid, loc_search)[0]
    #    loc_id = loc_browse.id
    #    result = super(StockMoveExtension, self).onchange_product_id(cr, uid, ids, prod_id, loc_id, loc_dest_id, partner_id)
    #    result['location_id'] = loc_id
    #    result['location_dest_id'] = loc_id
    #    return result




StockMoveExtension()
