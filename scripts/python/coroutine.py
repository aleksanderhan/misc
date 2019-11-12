# from typing import List, Coroutine
# c = None # type: Coroutine[List[str], str, int]

# x = c.send('hi') # type: List[str]
# async def bar() -> None:
#     x = await c # type: int

from functools import wraps

# Decorator function
def coroutine(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		cr = func(*args, **kwargs)
		next(cr)
		return cr
	return wrapper


@coroutine
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


search = grep('ass')
search.send('jabadabadooo')
search.send('ass n titties')


# @coroutine
# def 