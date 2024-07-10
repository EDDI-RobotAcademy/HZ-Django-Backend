from drinkcart.repository.drinkcart_item_repository_impl import DrinkcartItemRepositoryImpl
from drinkorders.entity.drinkorders_status import DrinkorderStatus
from drinkorders.repository.drinkorders_item_repository_impl import DrinkordersItemRepositoryImpl
from drinkorders.repository.drinkorders_repository_impl import DrinkordersRepositoryImpl
from drinkorders.service.drinkorders_service import DrinkordersService


class DrinkordersServiceImpl(DrinkordersService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__drinkordersRepository = DrinkordersRepositoryImpl.getInstance()
            cls.__instance.__drinkordersItemRepository = DrinkordersItemRepositoryImpl.getInstance()
            cls.__instance.__drinkcartItemRepository = DrinkcartItemRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createDrinkorder(self, accountId, drinkorderItemList):
        try:
            drinkorders = self.__drinkordersRepository.create(accountId, DrinkorderStatus.PENDING)

            for item in drinkorderItemList:
                drinkcartItem = self.__drinkcartItemRepository.findById(item['drinkcartItemId'])
                self.__drinkordersItemRepository.create(
                    drinkorders,
                    drinkcartItem.drink,
                    item['drinkorderPrice'],
                    item['drinkquantity']
                )

            return drinkorders.id

        except Exception as e:
            print('Error creating drinkorder:', e)
            raise e

    # def createOrder(self, account_id, order_items):
    #     try:
    #         # Example: Create orders in database
    #         order_ids = []
    #         for item in order_items:
    #             cart_item_id = item['cartItemId']
    #             quantity = item['quantity']
    #             order_price = item['orderPrice']
    #
    #             # Create Order object and save it to database
    #             order = Orders.objects.create(
    #                 account_id=account_id,
    #                 cart_item_id=cart_item_id,
    #                 quantity=quantity,
    #                 order_price=order_price,
    #             )
    #             order_ids.append(order.id)  # Collecting created order ids
    #
    #         # Return list of order ids (assuming multiple orders can be created at once)
    #         return order_ids
    #
    #     except Exception as e:
    #         # Handle exceptions
    #         print('Error creating order:', e)
    #         raise e
