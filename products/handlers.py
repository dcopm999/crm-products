import logging
from django.contrib.auth import get_user_model

from products import models
from telegrambots.handlers import HandlerCommandBase


logger = logging.getLogger(__name__)


class CatalogMixin:
    def __init__(self):
        self.catalog_model = models.Catalog
        self.product_model = models.Product
        self.order_model = models.Order
        self.user_model = get_user_model()
        super(CatalogMixin, self).__init__()

    def get_product_by_categoty(self, category: str):
        try:
            products = self.catalog_model.objects.get(name=category).product_set.all()
        except self.catalog_model.DoesNotExist:
            products = None
        return products

    def set_product_order(self, chat_id: int, product_id: int):
        logger.debug(f'{self.__class__}: set_product_order(chat={chat_id}, product_id={product_id})')
        user = self.user_model.objects.get(telegram_id=chat_id)
        if not user.phone_number:
            logger.debug(f'{user.username}: phone number not set')
            
        product = self.product_model.objects.get(id=product_id)
        order = self.order_model(user=user, product=product)
        order.save()


class HandlerProductList(CatalogMixin, HandlerCommandBase):
    command = '__all__'

    def run(self, request):
        logger.debug('%s: run()', self.__class__)
        if request.get('message'):
            chat_id = request.get('message').get('chat').get('id')
            category = request.get('message').get('text')
            products = self.get_product_by_categoty(category)
            if products is None:
                pass
            else:
                for product in products:
                    buy_btn = self.bot.get_kb_inline_buy(product)
                    self.bot.send_photo(chat_id, product.image.path, product.caption, buy_btn)


class HandlerProductOrder(CatalogMixin, HandlerCommandBase):
    command = '__all__'

    def run(self, request):
        logger.debug(f'{self.__class__}: run() {request}')
        if request.get('callback_query'):
            callback_id = request.get('callback_query').get('id')
            chat_id = request.get('callback_query').get('message').get('chat').get('id')
            product_id = request.get('callback_query').get('data')
            self.set_product_order(chat_id=chat_id, product_id=product_id)

