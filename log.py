import time
def timestamp(func):
    def timestampWrap(*args, **kwargs):
        print(time.ctime())
        func(*args, **kwargs)
    return timestampWrap