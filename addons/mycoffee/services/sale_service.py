from abc import ABC, abstractmethod

from ..models.models import Models
from ..repositories.sale_repository import ISaleRepository
from ..repositories.product_repository import IProductRepository
from typing import List
from dataclasses import dataclass
from ..helpers.encode_decode import bin_to_base64
    
class ISaleService(ABC):
    @abstractmethod
    def create_order(self, partner_id,quotation_date,validity_date):
        pass
    
    
class SaleService(ISaleService):
    def __init__(self, sale_repository: ISaleRepository, product_repository: IProductRepository):
        self.sale_repository = sale_repository
        self.product_repository = product_repository

    def create_order(self, partner_id,quotation_date,validity_date, order_lines):
        try:
            
            new_sale_order = self.sale_repository.create_sale_order(
                    partner_id=partner_id,
                    quotation_date=quotation_date,
                    validity_date=validity_date
                )
            for line in order_lines:
                new_sale_order_line = self.sale_repository.create_sale_order_line(
                    name=line.name,
                    order_id=new_sale_order.id,
                    product_template_id=line.product_template_id,
                    product_uom_qty=line.product_uom_qty,
                )
                
        except Exception as e:
            raise e

        # Convert the sale model to a DTO
        return 