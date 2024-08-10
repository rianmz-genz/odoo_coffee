# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

from ..helpers.response import response_json, base_format
from ..services.product_services import ProductService
from . import middlewares
import logging
logger = logging.getLogger(__name__)
class Products(http.Controller):
    @http.route('/api/docs', auth='public', website=True)
    def swagger_ui(self, **kw):
        return request.render('mycoffee.swagger_ui')
    
    @http.route('/api/products', auth='none', methods=['GET'], csrf=False)
    @middlewares.custom_auth_required
    def index(self, **kw):
        """
        Retrieves all product storable.

        Returns:
            list: list product.
            string: message

        Raises:
            ValueError: If the product is not found.
        """
        try:
            res = ProductService.get_all(request)
            return response_json(request=request, raw=base_format(res, "Success get all products"))
        except Exception as e:
            return response_json(request=request, raw=base_format(None, e))
    
    
    @http.route('/api/products/<int:id>', auth='none', methods=['GET'], csrf=False)
    @middlewares.custom_auth_required
    def by_id(self, id,**kw):
        """
        Retrieves product storable by id.

        Returns:
            object: data product.
            string: message

        Raises:
            ValueError: If the product is not found.
        """
        try:
            res = ProductService.get_by_id(request, id)
            raw = base_format(res, "Success get all products")
            return response_json(request=request, raw=raw)
        except Exception as e:
            raw = base_format("", f"Error {str(e)}")
            return response_json(request=request, raw=raw)
