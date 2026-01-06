class AuthService:
    def login(self, username, password):
        if username == 'elek' and password == 'alma':
            return 'TOKEN123'
        raise ValueError('Nem jó a username vagy a jelszo')
