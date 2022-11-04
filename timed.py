import time
def timeme(function):
    def wrapper():
        before = time.time()
        function()
        after = time.time()
        total = after - before
        print("Total Time is: %f" % total)
    return wrapper