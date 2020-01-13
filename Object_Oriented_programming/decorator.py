import time


class LogTime:

    def __init__(self, use_int=False):
        self.use_int = use_int

    def __call__(self, func):
        def _log(*args, **kwargs):
            beg = time.time()
            result = func(*args, **kwargs)
            if not self.use_int:
                print('use time (float) : {}'.format(time.time() - beg))
            else:
                print('use time (int) : {}'.format(int(time.time() - beg)))
            return result
        return _log


@LogTime(True)
def my_sleep():
    time.sleep(1)


my_sleep()
