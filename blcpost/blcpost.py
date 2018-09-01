from iconservice import *


class postmodule(IconScoreBase):

    __STORAGE = "storage"
    __WORKERS = "workers"
    __TOKEN = "token"

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

        self.__storage = VarDB(self.__STORAGE, db, valuetype=Address)
        self.__workers = ArrayDB(self.__WORKERS, db, valuetype=str)
        self.__token = DictDB(self.__TOKEN, db, valuetype=int,)


    def on_install(self, workers) -> None:
        super().on_install()

        self.__storage.set(self.msg.sender)
        self.__workers = workers

        for worker in list(self.__workers.values()):
            self.__token[str(worker)] = 0


    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def transaction_start(self, wid: str) -> int:
        if self.__token[str(wid)] % 2 == 0:
            self.__token[str(wid)] += 1
            return 1
        else:
            return 0

    @external(readonly=True)
    def transaction_end(self, wid: str) -> None:
        self.__token[str(wid)] += 1


    def fallback(self) -> None:
        pass
