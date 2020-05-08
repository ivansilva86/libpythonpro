from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'ivan.paulosilva@gmail.com',
        'anacristinaacm@yahoo.com.br',
        'Test Curso Python-Pro',
        'Validando Testes Automáticos'
    )
    assert 'ivan.paulosilva@gmail.com' in resultado
