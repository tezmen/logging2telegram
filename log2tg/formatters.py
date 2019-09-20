# -*- coding: utf-8 -*-
import logging
import html
from typing import Optional


class HtmlFormatter(logging.Formatter):
	fmt: str = '📢<b>%(levelname)s</b> > <code>%(filename)s:%(name)s:%(funcName)s</code> (line:%(lineno)s)' \
	           '<pre>%(message)s</pre><code>%(exc_text)s</code>\n_________________________\n🕐<i>%(asctime)s</i>'
	style: str = '%'
	parse_mode: str = 'HTML'

	def __init__(self, fmt: Optional[str] = None, *args, **kwargs):
		super().__init__(fmt or self.fmt, *args, **kwargs)

	def format(self, record: logging.LogRecord) -> str:
		record.funcName: str = html.escape(record.funcName)
		record.name: str = html.escape(record.name)
		record.msg: str = html.escape(str(record.msg))
		record.message = record.getMessage()
		if self.usesTime():
			record.asctime = self.formatTime(record, self.datefmt)
		record.exc_text = str()
		if record.exc_info:
			record.exc_text = self.formatException(record.exc_info)

		return self.formatMessage(record)
