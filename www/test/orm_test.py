import asyncio
import orm
from models import User, Blog, Comment

async def test(loop):
	await orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')

	u = User(name='zzgbird', email='zzgbird@example.com', passwd='1234567890', image='about:blank')

	await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()

for x in test():
	pass


# Traceback (most recent call last):
#   File "orm_test.py", line 13, in <module>
#     loop.run_until_complete(test(loop))
#   File "/home/guobird/anaconda3/lib/python3.7/asyncio/base_events.py", line 584, in run_until_complete
#     return future.result()
#   File "orm_test.py", line 6, in test
#     await orm.create_pool(loop=loop,user='www-data', password='www-data', database='awesome')
#   File "/home/guobird/awesome-python3-webapp/www/orm.py", line 21, in create_pool
#     db=kw['db'],
# KeyError: 'db'



# import orm
# import asyncio
# from models import User, Blog, Comment


# async def test(loop):
#     await orm.create_pool(loop=loop, user='root', password='root', db='awesome')

#     u = User(name='Test', email='test1@example.com',
#              passwd='1234567890', image='about:blank')
#     await u.save()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.run_forever()

# for x in test(loop):
#     pass
