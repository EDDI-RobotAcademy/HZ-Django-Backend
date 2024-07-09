from view.repository.view_repository import ViewRepository
from view.entity.models import View

class ViewRepositoryImpl(ViewRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, accountId, viewedMovie):
        view = View(account_id=accountId, viewed_movie = viewedMovie)
        view.save()

        return view

    def findById(self, viewId):
        return View.object.get(id=viewId)




