from iconservice import *


class post_module(IconScoreBase):

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
    def transaction_start(self) -> str:
        if self.__token[str(self.msg.sender)] % 2 == 0:
            self.__token[str(self.msg.sender)] += 1
            # DB가 필요하다
        else:
            return 0

    @external(readonly=True)
    def transaction_end(self) -> str:
        self.__token[str(self.msg.sender)] += 1

    @external(readonly=True)
    def usetoken_money(self, usetoken) -> str:
        self.__token[str(self.msg.sender)] -= usetoken * 2

    @external(readonly=True)
    def usetoken_voltime(self, usetoken) -> str:
        self.__token[str(self.msg.sender)] -= usetoken * 2

    @external(readonly=True)
    def token_check(self) -> str:
        return self.__token[str(self.msg.sender)] / 2


def fallback(self) -> None:
    """SCORE 배포를 위한 형식을 위해 존재하는 함수

    이 SCORE는 실제 icx코인을 사용하지 않기 때문에 이 함수는 실제 기능하지않는다.
    """
    pass
