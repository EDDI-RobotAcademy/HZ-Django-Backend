from account.repository.account_repository_impl import AccountRepositoryImpl
from drinkcart.repository.drinkcart_item_repository_impl import DrinkcartItemRepositoryImpl
from drinkcart.repository.drinkcart_repository_impl import DrinkcartRepositoryImpl
from drinkcart.service.drinkcart_service import DrinkcartService
from drink.repository.drink_repository_impl import DrinkRepositoryImpl


class DrinkcartServiceImpl(DrinkcartService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__drinkcartRepository = DrinkcartRepositoryImpl.getInstance()
            cls.__instance.__drinkRepository = DrinkRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__drinkcartItemRepository = DrinkcartItemRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def drinkcartRegister(self, drinkcartData, accountId):
        account = self.__accountRepository.findById(accountId)
        drinkcart = self.__drinkcartRepository.findByAccount(account)
        if drinkcart is None:
            print("장바구니 새롭게 생성")
            drinkcart = self.__drinkcartRepository.register(account)

        print("기존 장바구니 사용")

        drinkId = drinkcartData.get('drinkId')
        drinkcartItemList = self.__drinkcartItemRepository.findAllByDrinkId(drinkId)

        drinkcartItem = None
        for item in drinkcartItemList:
            drinkcartFromDrinkcartItem = item.drinkcart
            accountFromDrinkcart = drinkcartFromDrinkcartItem.account
            if accountFromDrinkcart.id == account.id:
                drinkcartItem = item
                break

        if drinkcartItem is None:
            print("신규 음식 추가")
            drink = self.__drinkRepository.findByDrinkId(drinkId)
            self.__drinkcartItemRepository.register(drinkcartData, drinkcart, drink)
        else:
            print("기존 음식 추가")

            drinkcartItem.drinkquantity += 1
            self.__drinkcartItemRepository.update(drinkcartItem)

    def drinkcartList(self, accountId):
        account = self.__accountRepository.findById(accountId)
        drinkcart = self.__drinkcartRepository.findByAccount(account)
        print(f"drinkcartList -> drinkcart: {drinkcart}")
        drinkcartItemList = self.__drinkcartItemRepository.findByDrinkcart(drinkcart)
        print(f"drinkcartList -> drinkcartItemList: {drinkcartItemList}")
        drinkcartItemListResponseForm = []

        for drinkcartItem in drinkcartItemList:
            drinkcartItemResponseForm = {
                'drinkcartItemId': drinkcartItem.drinkcartItemId,
                'drinkId': drinkcartItem.drink.drinkId,
                'drinkName': drinkcartItem.drink.drinkName,
                'drinkType': drinkcartItem.drink.drinkType,
                'drinkDescription': drinkcartItem.drink.drinkDescription,
                'drinkPrice': drinkcartItem.drink.drinkPrice,
                'drinkquantity': drinkcartItem.drinkquantity,
            }
            drinkcartItemListResponseForm.append(drinkcartItemResponseForm)

        return drinkcartItemListResponseForm

    def removeDrinkcartItem(self, accountId):
        print(f"accountId: {accountId}")
        drinkcartId = self.__drinkcartRepository.findDrinkcartIdByAccountId(accountId)
        print(f"drinkcartId: {drinkcartId}")
        return self.__drinkcartItemRepository.deleteByDrinkcartId(drinkcartId)


    # def cartList(self, accountId):
    #     return self.cartRepository.findByAccount(accountId)

    # def cartList(self, accountId):
    #     account = self.__accountRepository.findById(accountId)
    #     print(f"cartList -> account:", account)
    #     if account:
    #         drinkcart = self.__cartRepository.findByAccount(account)
    #         print(f"cartList -> drinkcart:", drinkcart)
    #         if drinkcart:
    #             return drinkcart.items.all()
    #     return []


