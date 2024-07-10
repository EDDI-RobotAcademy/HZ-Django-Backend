from foodcart.repository.foodcart_item_repository_impl import FoodcartItemRepositoryImpl
from foodorders.entity.foodorders_status import FoodorderStatus
from foodorders.repository.foodorders_item_repository_impl import FoodordersItemRepositoryImpl
from foodorders.repository.foodorders_repository_impl import FoodordersRepositoryImpl
from foodorders.service.foodorders_service import FoodordersService


class FoodordersServiceImpl(FoodordersService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__foodordersRepository = FoodordersRepositoryImpl.getInstance()
            cls.__instance.__foodordersItemRepository = FoodordersItemRepositoryImpl.getInstance()
            cls.__instance.__foodcartItemRepository = FoodcartItemRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createFoodorder(self, accountId, foodorderItemList):
        try:
            foodorders = self.__foodordersRepository.create(accountId, FoodorderStatus.PENDING)

            for item in foodorderItemList:
                foodcartItem = self.__foodcartItemRepository.findById(item['foodcartItemId'])
                self.__foodordersItemRepository.create(
                    foodorders,
                    foodcartItem.food,
                    item['foodorderPrice'],
                    item['foodquantity']
                )

            return foodorders.id

        except Exception as e:
            print('Error creating foodorder:', e)
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
