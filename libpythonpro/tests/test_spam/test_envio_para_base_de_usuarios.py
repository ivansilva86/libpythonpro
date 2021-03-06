from unittest.mock import Mock

import pytest

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
            Usuario(nome='Ivan', email='ivan.paulosilva@gmail.com')
        ]
    ]
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ivan.paulosilva@gmail.com',
        'Curso Python-Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Ivan', email='ivan.paulosilva@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@gmail.com',
        'Curso Python-Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'luciano@gmail.com',
        'ivan.paulosilva@gmail.com',
        'Curso Python-Pro',
        'Confira os módulos fantásticos'
    )
