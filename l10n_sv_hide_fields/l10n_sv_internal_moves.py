# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning

class internalmoves(models.Model):
    _inherit = ['stock.picking']
    
    location_orig_id = fields.Many2one('stock.location', string='Location origin')
    location_desti_id = fields.Many2one('stock.location', string='Location destination')

    def create(self, cr, uid, vals, context=None):
        id = super(internalmoves, self).create(cr, uid, vals, context=context)
        stock_obj = self.pool.get('stock.picking')
        move_obj = self.pool.get('stock.move')
        browse = stock_obj.browse(cr, uid, [id], context=context)[0]
        loc_id = browse.location_orig_id.id
        loc_dest_id = browse.location_desti_id.id
        res = {
            'location_id': loc_id,
            'location_dest_id': loc_dest_id
        }
        move_search = move_obj.search(cr, uid, [('picking_id', '=', id)])
        move_browse = move_obj.browse(cr, uid, move_search, context=context)
        for item in move_browse:
            move_obj.write(cr, uid, [item.id], res, context=context)

        return id
        #raise except_orm(_('Limit'), _("valor del vals %s" %res))
  
internalmoves()