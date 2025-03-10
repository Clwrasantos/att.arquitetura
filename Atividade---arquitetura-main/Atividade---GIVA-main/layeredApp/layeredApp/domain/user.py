class User:
    id:int
    Name:str
    Descricao:str 
    Preco_de_compra:float
    login:str
    password:str

    def __init__(self, id = 0, login="",password=""):
        self.id = id
        self.login = login
        self.password = password