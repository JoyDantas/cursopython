from eletronicos import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} não está ligado!'
            print(error)
            self.log_error(error)
            return

        if self._conectado:
            info = f'{self._nome} Já está conectado!'
            print(info)
            self.log_info(info)

        info = f'{self._nome} Está Conectado. '
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} Não está Conectado.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} Foi desligado com sucesso.'
        print(info)
        self.log_info(info)
        self._conectado = False
