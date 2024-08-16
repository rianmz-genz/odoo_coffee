# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

from ..helpers.response import response_json, base_format
from ..services.user_service import UserService
from ..repositories.user_repository import UserRepository
from . import middlewares
import logging
logger = logging.getLogger(__name__)

class UserController(http.Controller):
    
    @http.route('/api/auth/login', auth='none', methods=['POST'], csrf=False)
    def login(self, **kw):
        """
        Retrieves token user.

        Returns:
            string: token

        Raises:
            ValueError: If user is not found.
            ValidationError: If expected field is not same.
        """
        try:
            kw_login = kw.get('login')
            logger.info(f"loginngk {kw_login}")
            if not kw_login: 
                return response_json(request=request, raw=base_format({}, "login field is required"))

            product_repository = UserRepository(request.env)
            product_service = UserService(product_repository)
            
            res = product_service.authenticate(login=kw_login)
            return response_json(request=request, raw=base_format(res.__dict__, "Success to login"))
        except Exception as e:
            return response_json(request=request, raw=base_format({}, f"{e}"))
