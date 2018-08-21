from config import ENABLE_DEBUG

forcePrint = print
def print(*v):
    global forcePrint
    if ENABLE_DEBUG:
        forcePrint(*v)
