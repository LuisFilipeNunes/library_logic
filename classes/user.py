from user_bookstand import UserBookstand
class User():
    def __init__(self, name, id, email, password):
        self.name = name
        self.id = id
        self.email = email
        self.password = password
        self.bookstand = UserBookstand()

    def adquire_book(self, book):
        self.bookstand.add_book(book)
        
    def get_att(self, att):
        '''
        This must receive att string as name, email, password or bookstand\n

        It will return the value of the attribute, or 15 if it fails
        '''
        try :
            return getattr(self, att)
        except:
            return 15