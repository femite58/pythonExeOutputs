import os
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer 
from pyftpdlib.authorizers import DummyAuthorizer

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('OLORUNFEMI', "JHVH6828", os.getcwd(), perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())
    handler = FTPHandler 
    handler.authorizer = authorizer 
    server = FTPServer(("", 21), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
    