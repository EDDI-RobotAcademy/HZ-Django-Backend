from view.repository.view_repository_impl import ViewRepositoryImpl
from view.service.view_service import ViewService


class ViewServiceImpl(ViewService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__viewRepository = ViewRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createView(self, accountId, viewedMovie):
        try:
            view = self.__viewRepository.create(accountId, viewedMovie)

            return view.id
        except Exception as e:
            print('Error creating view:', e)
            raise e

