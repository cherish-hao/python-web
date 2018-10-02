#!/usr/bin/env python3
#coding:utf-8
"""
the url structure of website
"""
from handlers.index import IndexHandler
from handlers.index import ErrorHandler
from handlers.user import UserHandler
url = [
    (r'/',IndexHandler),
    (r'/user',UserHandler),
    (r'/error',ErrorHandler),
]
