import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido

destinatario = 'ivan.paulosilva@gmail.com'


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['ivan.paulosilva@gmail.com', 'foo@bar.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'anacristinaacm@yahoo.com.br',
        'Test Curso Python-Pro',
        'Validando Testes Automáticos'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'foo']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'anacristinaacm@yahoo.com.br',
            'Test Curso Python-Pro',
            'Validando Testes Automáticos'
        )
