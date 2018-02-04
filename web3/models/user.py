from models import Model

class User(Model):
    def __init__(self,form):
        self.username = form.get('username','')
        self.password = form.get('password','')
