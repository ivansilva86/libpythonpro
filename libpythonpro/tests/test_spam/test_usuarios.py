from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Ivan', email='ivan.paulosilva@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Ivan', email='ivan.paulosilva@gmail.com'),
        Usuario(nome='Luciano', email='luciano@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

