#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'  # copy by zzgbird 20190420

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
	summary =  'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
	blogs = [
		Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
		Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
		Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200),
		Blog(id='4', name='Learn cs and hard working for ten years or more', summary='失败只有一种,那就是半途而废^^', created_at=time.time()-86400)
	]
	return {
		'__template__': 'blogs.html',
		'blogs': blogs
	}

@get('/api/users')
async def api_get_users():
	users = await User.findAll(orderBy='created_at desc')
	for u in users:
		u.passwd = '******'
	return dict(users=users)

