# coding:utf-8


class User(object):
    def __init__(self, uid, name, email, encrypted_password):
        self.uid = uid
        self.name = name
        self.email = email
        self.encrypted_password = encrypted_password
