# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from ..models.models import Models
from . import middlewares
class Products(http.Controller):
    
    @http.route('/api/products', auth='none')
    @middlewares.custom_auth_required
    def index(self, **kw):
        """
        Retrieves all product.

        Returns:
            list: list product.

        Raises:
            ValueError: If the product is not found.
        """
        products = Models.Product(request.env).search([])
        res = []
        for product in products:
            res.append({
                'id': product.id,
                'name': product.name,
                'price': product.list_price,
                'canBeSold': product.sale_ok,
                'canBePurchased': product.purchase_ok,
                'type': product.detailed_type,
                'hpp': product.standard_price
            })
        return request.make_response(json.dumps(res))

