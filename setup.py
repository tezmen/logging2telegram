# -*- coding: utf-8 -*-
from os import path
from setuptools import setup


def long_description():
	this_dir = path.abspath(path.dirname(__file__))
	with open(path.join(this_dir, 'README.md'), encoding='utf-8') as f:
		return f.read()


def requirements():
	requirements_list = list()
	with open('requirements.txt') as pc_requirements:
		for install in pc_requirements:
			requirements_list.append(install.strip())
	return requirements_list


setup(
	name='logging2telegram',
	version='1.0.2',
	packages=['log2tg'],
	url='https://github.com/tezmen/loging2telegram',
	author='tezmen',
	license='Apache License, Version 2.0, see LICENSE file',
	description='Telegram logging handler',
	long_description=long_description(),
	long_description_content_type='text/markdown',
	install_requires=requirements(),
	classifiers=[
		'License :: OSI Approved :: Apache Software License',
		'Operating System :: OS Independent',
		'Environment :: Console',
		'Development Status :: 3 - Alpha',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: Implementation :: PyPy',
	]
)
