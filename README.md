# logging2telegram

Fastest and simple handler for stream logging output to telegram chats. 

[![N|Solid](https://img.shields.io/pypi/pyversions/logging2telegram.svg)](https://pypi.python.org/pypi/logging2telegram)

### Installation
You can install or upgrade package with PIP:
```
$ pip install logging2telegram --upgrade
```
Or you can install from source with:
```
$ git clone https://github.com/tezmen/logging2telegram
$ cd logging2telegram
$ python setup.py install
```
...or install from source buth with pip
```
$ pip install git+https://github.com/tezmen/logging2telegram.git
```

### Example
```python
import logging.config
import logging

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'tg_full': {
            'class': 'log2tg.HtmlFormatter',
        }
    },
    'handlers': {
        'telegram': {
            'level':     'DEBUG',
            'class':     'log2tg.TelegramHandler',
            'formatter': 'tg_full',
            'disable_web_page_preview': True,
            'token':     'BOT:TOKEN',
            'ids':       [123,132,321],
        },
    },
    'loggers': {
        'myapp': {
            'handlers': ['telegram']
        }
    },
})

def show():
	logger = logging.getLogger('myapp')
	logger.warning('we have <b>a</b> warning')

if __name__ == '__main__':
	show()

```
For custom formating:

```python
'formatters': {
    'tg_full': {
        'class': 'log2tg.HtmlFormatter',
        'format': '%(message)s'
    }
}
```
