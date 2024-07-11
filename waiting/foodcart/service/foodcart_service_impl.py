from account.repository.account_repository_impl import AccountRepositoryImpl
from foodcart.repository.foodcart_item_repository_impl import FoodcartItemRepositoryImpl
from foodcart.repository.foodcart_repository_impl import FoodcartRepositoryImpl
from foodcart.service.foodcart_service import FoodcartService
from food.repository.food_repository_impl import FoodRepositoryImpl


class FoodcartServiceImpl(FoodcartService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__foodcartRepository = FoodcartRepositoryImpl.getInstance()
            cls.__instance.__foodRepository = FoodRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__foodcartItemRepository = FoodcartItemRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def foodcartRegister(self, foodcartData, accountId):
        account = self.__accountRepository.findById(accountId)
        foodcart = self.__foodcartRepository.findByAccount(account)
        if foodcart is None:
            print("장바구니 새롭게 생성")
            foodcart = self.__foodcartRepository.register(account)

        print("기존 장바구니 사용")

        foodId = foodcartData.get('foodId')
        foodcartItemList = self.__foodcartItemRepository.findAllByFoodId(foodId)

        foodcartItem = None
        for item in foodcartItemList:
            foodcartFromFoodcartItem = item.foodcart
            accountFromFoodcart = foodcartFromFoodcartItem.account
            if accountFromFoodcart.id == account.id:
                foodcartItem = item
                break

        if foodcartItem is None:
            print("신규 음식 추가")
            food = self.__foodRepository.findByFoodId(foodId)
            self.__foodcartItemRepository.register(foodcartData, foodcart, food)
        else:
            print("기존 음식 추가")

            foodcartItem.foodquantity += 1
            self.__foodcartItemRepository.update(foodcartItem)

    def foodcartList(self, accountId):
        account = self.__accountRepository.findById(accountId)
        foodcart = self.__foodcartRepository.findByAccount(account)
        print(f"foodcartList -> foodcart: {foodcart}")
        foodcartItemList = self.__foodcartItemRepository.findByFoodcart(foodcart)
        print(f"foodcartList -> foodcartItemList: {foodcartItemList}")
        foodcartItemListResponseForm = []

        for foodcartItem in foodcartItemList:
            foodcartItemResponseForm = {
                'foodcartItemId': foodcartItem.foodcartItemId,
                'foodId': foodcartItem.food.foodId,
                'foodName': foodcartItem.food.foodName,
                'foodType': foodcartItem.food.foodType,
                'foodDescription': foodcartItem.food.foodDescription,
                'foodPrice': foodcartItem.food.foodPrice,
                'foodquantity': foodcartItem.foodquantity,
            }
            foodcartItemListResponseForm.append(foodcartItemResponseForm)

        return foodcartItemListResponseForm

    def removeFoodcartItem(self, accountId):
        print(f"accountId: {accountId}")
        foodcartId = self.__foodcartRepository.findFoodcartIdByAccountId(accountId)
        print(f"foodcartId: {foodcartId}")
        return self.__foodcartItemRepository.deleteByFoodcartId(foodcartId)

    # def cartList(self, accountId):
    #     return self.cartRepository.findByAccount(accountId)

    # def cartList(self, accountId):
    #     account = self.__accountRepository.findById(accountId)
    #     print(f"cartList -> account:", account)
    #     if account:
    #         foodcart = self.__cartRepository.findByAccount(account)
    #         print(f"cartList -> foodcart:", foodcart)
    #         if foodcart:
    #             return foodcart.items.all()
    #     return []


