class Usuario:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def realizar_login(self, login, password):
        if self.login != login:
            raise ValueError("Login inválido!")
        if self.password != password:
            raise ValueError("Password inválido!")
