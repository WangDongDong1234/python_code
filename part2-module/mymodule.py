import sys
__all__ = ["login", "name"]
name = "alex"


def login():
    print("我饿了%s" % (name))
my_module=sys.modules["__main__"]

getattr(my_module,"login")()
import imaplib
imaplib.reload(aaa)


