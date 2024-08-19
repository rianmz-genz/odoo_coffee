# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

from ..helpers.response import response_json, base_format
from ..services.product_service import ProductService
from ..repositories.product_repository import ProductRepository
from . import middlewares
import logging

logger = logging.getLogger(__name__)

class ProductController(http.Controller):

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
            # Instantiate the repository and service within the request scope
            product_repository = ProductRepository(request.env)
            product_service = ProductService(product_repository)

            # Use the service to get all products
            products = product_service.get_all()
            # Convert DTOs to dictionaries for JSON serialization
            products_list = [product.__dict__ for product in products]
            return response_json(request=request, raw=base_format(products_list, "Success get all products"))
        except Exception as e:
            # Convert the exception to a string for error reporting
            error_message = str(e)
            return response_json(request=request, raw=base_format({}, error_message))
    
    
    @http.route('/api/products/<int:id>', auth='none', methods=['GET'], csrf=False)
    @middlewares.custom_auth_required
    def by_id(self, id, **kw):
        """
        Retrieve product storable by id.

        Returns:
            object: productData.
            string: message

        Raises:
            ValueError: If the product is not found.
        """
        try:
            # Instantiate the repository and service within the request scope
            product_repository = ProductRepository(request.env)
            product_service = ProductService(product_repository)

            # Use the service to get the product by id
            product = product_service.get_by_id(id)
            # Convert the DTO to a dictionary for JSON serialization
            product_data = product.__dict__
            raw = base_format(product_data, "Success get product by ID")
            return response_json(request=request, raw=raw)
        except Exception as e:
            # Convert the exception to a string for error reporting
            error_message = str(e)
            raw = base_format({}, f"Error {error_message}")
            return response_json(request=request, raw=raw)
