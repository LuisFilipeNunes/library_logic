class Book():
    
    def __init__(self, title, book_code, path, coverpage):
        self.title = title
        self.id = book_code
        self.path = path
        self.coverpage = coverpage 
    
    def get_att(self, att):
        '''
        This must receive att string as title, id, path or coverpage\n
        
        It will return the value of the attribute, or 15 if it fails
        '''
        try :
            return getattr(self, att)
        except:
            return 15
