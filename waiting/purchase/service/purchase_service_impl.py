# from cart.repository.cart_item_repository_impl import CartItemRepositoryImpl
from drinkorders.repository.drinkorders_repository_impl import DrinkordersRepositoryImpl
from foodorders.repository.foodorders_repository_impl import FoodordersRepositoryImpl
from purchase.repository.purchase_repository_impl import PurchaseRepositoryImpl
from purchase.service.purchase_service import PurchaseService


class PurchaseServiceImpl(PurchaseService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__purchaseRepository = PurchaseRepositoryImpl.getInstance()
            cls.__instance.__foodordersRepository = FoodordersRepositoryImpl.getInstance()
            cls.__instance.__drinkordersRepository = DrinkordersRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createPurchase(self, accountId, foodorderId=None, drinkorderId=None):
        try:
            purchase = self.__purchaseRepository.create(accountId, foodorderId, drinkorderId)
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


