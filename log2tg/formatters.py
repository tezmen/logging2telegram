# -*- coding: utf-8 -*-
import logging
import html
from typing import Optional


class HtmlFormatter(logging.Formatter):
	fmt: str = '📢<b>%(levelname)s</b> > <code>%(filename)s:%(name)s:%(funcName)s</code> (line:%(lineno)s)' \
	           '<pre>%(message)s</pre>\n_________________________\n🕐<i>%(asctime)s</i>'
	style: str = '%'
	parse_mode: str = 'HTML'

	def __init__(self, fmt: Optional[str] = None, *args, **kwargs):
		super().__init__(fmt or self.fmt, *args, **kwargs)

	def format(self, record) -> str:
		record.msg: str = html.escape(record.getMessage())
		record.funcName: str = html.escape(record.funcName)
		record.name: str = html.escape(record.name)
		return super().format(record)
