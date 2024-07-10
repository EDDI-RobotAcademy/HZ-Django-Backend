# from cart.repository.cart_item_repository_impl import CartItemRepositoryImpl
from drink.repository.drink_repository_impl import DrinkRepositoryImpl
from drinkcart.repository.drinkcart_item_repository_impl import DrinkcartItemRepositoryImpl
from drinkcart.repository.drinkcart_repository_impl import DrinkcartRepositoryImpl
from drinkorders.repository.drinkorders_repository_impl import DrinkordersRepositoryImpl
from food.repository.food_repository_impl import FoodRepositoryImpl
from foodcart.repository.foodcart_item_repository_impl import FoodcartItemRepositoryImpl
from foodcart.repository.foodcart_repository_impl import FoodcartRepositoryImpl
from foodorders.repository.foodorders_repository_impl import FoodordersRepositoryImpl
from purchase.repository.purchase_item_repository_impl import PurchaseItemRepositoryImpl
from purchase.repository.purchase_repository_impl import PurchaseRepositoryImpl
from purchase.service.purchase_service import PurchaseService


class PurchaseServiceImpl(PurchaseService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__purchaseRepository = PurchaseRepositoryImpl.getInstance()
            cls.__instance.__purchaseItemRepository = PurchaseItemRepositoryImpl.getInstance()
            cls.__instance.__foodordersRepository = FoodordersRepositoryImpl.getInstance()
            cls.__instance.__drinkordersRepository = DrinkordersRepositoryImpl.getInstance()
            cls.__instance.__foodcartItemRepository = FoodcartItemRepositoryImpl.getInstance()
            cls.__instance.__drinkcartItemRepository = DrinkcartItemRepositoryImpl.getInstance()
            cls.__instance.__foodRepository = FoodRepositoryImpl.getInstance()
            cls.__instance.__drinkRepository = DrinkRepositoryImpl.getInstance()


        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createPurchase(self, accountId, purchaseItemList):
        try:
            purchase = self.__purchaseRepository.create(accountId)

            for item in purchaseItemList:
                print(f"purchaseItem: {item}")

                foodcartItem = None
                if 'foodcartItemId' in item:
                    print(f"Searching for foodcartItemId: {item['foodcartItemId']}")
                    foodcartItem = self.__foodcartItemRepository.findById(item['foodcartItemId'])
                    print(f"foodcartItem: {foodcartItem}")

                # Check if 'drinkcartItemId' is present in the item
                drinkcartItem = None
                if 'drinkcartItemId' in item:
                    print(f"Searching for drinkcartItemId: {item['drinkcartItemId']}")
                    drinkcartItem = self.__drinkcartItemRepository.findById(item['drinkcartItemId'])
                    print(f"drinkcartItem: {drinkcartItem}")

                self.__purchaseItemRepository.create(
                    purchase,
                    foodcartItem.food,
                    item['foodorderPrice'],
                    item['foodquantity'],
                    drinkcartItem.drink,
                    item['drinkorderPrice'],
                    item['drinkquantity']
                )

            return purchase.id

        except Exception as e:
            print('Error creating purchase:', e)
            raise e

    def readPurchaseDetails(self, purchaseId, accountId):
        try:
            purchase = self.__purchaseRepository.findById(purchaseId)

            if not purchase:
                raise ValueError('Purchase not found')

            if purchase.account.id != int(accountId):
                raise ValueError('Invalid accountId for this purchase')

            account = purchase.account

            account_login_type = account.loginType.name if hasattr(account.loginType, 'name') \
                else str(account.loginType)
            account_role_type = account.roleType.name if hasattr(account.roleType, 'name') \
                else str(account.roleType)

            purchaseItemList = self.__purchaseItemRepository.findAllByPurchase(purchase)

            totalPrice = sum(purchaseItem.total_price() for purchaseItem in purchaseItemList)

            purchase_details = {
                'purchase': {
                    'id': purchase.id,
                    'purchase_date': purchase.purchase_date.isoformat(),
                    'account': {
                        'id': account.id,
                        'loginType': account_login_type,
                        'roleType': account_role_type
                    }
                },
                'purchase_items': [
                    {
                        'food_id': item.food_id,
                        'food_name': self.__foodRepository.findByFoodId(item.food_id).foodName,
                        'foodquantity': item.foodquantity,
                        'foodprice': item.foodprice,
                        'drink_id': item.drink_id,
                        'drink_name': self.__drinkRepository.findByDrinkId(item.drink_id).drinkName,
                        'drinkquantity': item.drinkquantity,
                        'drinkprice': item.drinkprice,
                        'total_price': item.total_price(),
                    }
                    for item in purchaseItemList
                ],
                'foodorder': None,
                'drinkorder': None
            }

            if purchase.foodorder:
                foodorder = purchase.foodorder
                purchase_details['foodorder'] = {
                    'id': foodorder.id,
                    'status': foodorder.status,
                    'created_date': foodorder.created_date.isoformat()
                }

            if purchase.drinkorder:
                drinkorder = purchase.drinkorder
                purchase_details['drinkorder'] = {
                    'id': drinkorder.id,
                    'status': drinkorder.status,
                    'created_date': drinkorder.created_date.isoformat()
                }

            # print(f"purchase_details: {purchase_details}")

            return purchase_details

        except Exception as e:
            print('Error reading purchase details:', e)
            raise e



