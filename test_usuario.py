import unittest
from usuario import Usuario

class TestUsuario(unittest.TestCase):
    LOGIN_CORRETO = "usuario01"
    SENHA_CORRETA = "usuario01_password"

    def setUp(self):
        self.usuario = Usuario(self.LOGIN_CORRETO, self.SENHA_CORRETA)

    """
    Testa se a exceçãoi do tipo ValueError é lançada quando a senha passada para função realizar_login da classe Usuario está incorreta
    """
    def test_realizar_login_lanca_erro_com_senha_incorreta(self):
        self.assertRaises(ValueError,self.usuario.realizar_login,self.LOGIN_CORRETO,"senha_errada")

    """
    Testa se a exceçãoi do tipo ValueError é lançada quando o login passado para função realizar_login da classe Usuario está incorreta
    """
    def test_realizar_login_lanca_erro_com_login_incorreto(self):
        self.assertRaises(ValueError, self.usuario.realizar_login,"login_errado", self.SENHA_CORRETA)

"""Executa todos os métodos das classes derivadas da classe TestCase"""
if __name__ == '__main__':
    unittest.main()
