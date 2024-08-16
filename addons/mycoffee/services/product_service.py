from abc import ABC, abstractmethod

from ..models.models import Models
from ..repositories.product_repository import IProductRepository
from typing import List
from dataclasses import dataclass
from ..helpers.encode_decode import bin_to_base64
@dataclass
class ProductDTO:
    id: int
    name: str
    price: float
    image: str
    
class IProductService(ABC):
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def get_by_id(self, id):
        pass
    
    
class ProductService(IProductService):
    def __init__(self, product_repository: IProductRepository):
        self.product_repository = product_repository

    def get_all(self) -> List[ProductDTO]:
        products = self.product_repository.search([
            ('detailed_type', '=', 'product')
        ])
        
        if len(products) == 0:
            raise Exception("Product not found")
        
        # Convert product models to DTOs
        res = [
            ProductDTO(
                id=product.id,
                name=product.name,
                price=product.list_price,
                image=bin_to_base64(product.image_1920)
            )
            for product in products
        ]
        
        return res

    def get_by_id(self, id) -> ProductDTO:
        try:
            product = self.product_repository.search([
                ('id', '=', int(id))
            ], limit=1)
        except Exception as e:
            raise e

        if not product:
            raise Exception("Product not found")

        # Convert the product model to a DTO
        return ProductDTO(
            id=product.id,
            name=product.name,
            price=product.list_price,
            image=bin_to_base64(product.image_1920)
        )