from setuptools import setup
from io import open


def read(filename):
	with open(filename, encoding='utf-8') as file:
		return file.read()


setup(
	name='pyQiwiP2P',
	version='1.0a5',
	packages=['pyqiwip2p', 'pyqiwip2p.types', 'pyqiwip2p.notify'],
	url='https://github.com/WhiteApfel/pyQiwiP2P',
	license='Mozilla Public License 2.0',
	author='WhiteApfel pfel.cc',
	author_email='white@pfel.ru',
	description='pyQiwiP2P',
	install_requires=['cherrypy', 'phonenumbers', 'email_validator'],
	project_urls={
		"Документальное чтиво": "https://pyqiwip2p.readthedocs.io/ru/latest/",
		"На морожешку и кофеёк": "https://rocketbank.ru/whiteapfel",
		"Оставить пару ласковых": "https://saythanks.io/to/white%40pfel.ru",
		"Это сделано из этого": "https://github.com/pypa/sampleproject/",
		"А поговорить можно тут": "https://t.me/apfel"
	},
	long_description=read('README.md'),
	long_description_content_type="text/markdown",
	keywords='qiwip2p api p2p bill tools sdk python'
)
