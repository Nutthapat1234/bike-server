from config import ENABLE_DEBUG

ppppp = print
def print(*v):
    global ppppp
    if ENABLE_DEBUG:
        ppppp(*v)
