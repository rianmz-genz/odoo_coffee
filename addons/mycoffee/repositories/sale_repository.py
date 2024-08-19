from abc import ABC, abstractmethod
from ..models.models import Models
from dataclasses import dataclass
from ..helpers.encode_decode import encode_object
import logging

logger = logging.getLogger(__name__)

@dataclass
class DSaleOrderLine:
    orderId: int
    product: str
    name: str
    qty: float

@dataclass
class DSaleOrder:
    id: int
    partnerId: int
    validityDate: str
    quotationDate: str    
    
class ISaleRepository(ABC):
    @abstractmethod
    def create_sale_order(self, partner_id, validity_date, quotation_date,) ->DSaleOrder:
        pass
    
    @abstractmethod
    def create_sale_order_line(self, order_id, product_template_id, name,product_uom_qty) -> DSaleOrderLine:
        pass
    
class SaleRepository(ISaleRepository):
    def __init__(self, env):
        self.env = env
        
    def create_sale_order(self, partner_id, validity_date, quotation_date,):
        try:
            new_sale_order = Models.SaleOrder(self.env).create({
                'partner_id': partner_id,
                'validity_date': validity_date,
                'quotation_date': quotation_date,
            })
            return DSaleOrder(
                    id=new_sale_order.id,
                    partner_id=new_sale_order.partner_id, 
                    validity_date=new_sale_order.validity_date, 
                    quotation_date=new_sale_order.quotation_date, 
                )
        except Exception as e:
            logger.info(f"errorr saleorder create repo {e}")
            raise Exception("Error in repo create saleorder")
    
    def create_sale_order_line(self, order_id, product_template_id, name,product_uom_qty) -> DSaleOrder:
        try:
            new_sale_order_line = Models.SaleOrderLine(self.env).create({
                'order_id': order_id,
                'product_template_id': product_template_id,
                'name': name,
                'product_uom_qty': product_uom_qty,
            })
            return DSaleOrderLine(
                    name=new_sale_order_line.name, 
                    orderId=new_sale_order_line.orderId, 
                    product=new_sale_order_line.product, 
                    qty=new_sale_order_line.qty, 
                )
        except Exception as e:
            logger.info(f"errorr saleorderline create repo {e}")
            raise Exception("Error in repo create saleorderline")
         