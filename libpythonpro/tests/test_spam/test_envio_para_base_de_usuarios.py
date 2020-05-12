import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Ivan', email='ivan.paulosilva@gmail.com'),
            Usuario(nome='Luciano', email='luciano@gmail.com')
        ],
        [
            Usuario(nome='Luciano', email='luciano@gmail.com')
        ]
    ]
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ivan.paulosilva@gmail.com',
        'Curso Python-Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_de_emails_enviados
