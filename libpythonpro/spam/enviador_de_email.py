class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de rementente Invalido {remetente}')
        return remetente


class EmailInvalido(Exception):
    pass