# -*- encoding: utf-8 -*-
##############################################################################
#
#    edit_payment_term: Allows editing payment term once invoice 
#                       has been validated
#    Copyright (c) 2013 Codeback Software S.L. (http://codeback.es)    
#    @author: Miguel García <miguel@codeback.es>
#    @author: Javier Fuentes <javier@codeback.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

from osv import fields, osv

class account_invoice(osv.osv):
    
    name = "account.invoice"
    _inherit = "account.invoice"  

    """modificamos las propiedades del campo para permitir su edición"""    

    _columns = {        
        'date_due': fields.date('Due Date', readonly=False, select=True,
            help="If you use payment terms, the due date will be computed automatically at the generation "\
                "of accounting entries. The payment term may compute several due dates, for example 50% now and 50% in one month, but if you want to force a due date, make sure that the payment term is not set on the invoice. If you keep the payment term and the due date empty, it means direct payment."),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: