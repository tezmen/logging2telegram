# -*- coding: utf-8 -*-
import logging
import logging.config
import requests
from dataclasses import dataclass
from typing import List

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.propagate = True


@dataclass(eq=False)
class TelegramHandler(logging.Handler):
	token: str
	ids: List[int]
	disable_notification: bool = False
	disable_web_page_preview: bool = True
	timeout: float = 2.0
	level: str = logging.NOTSET

	def __post_init__(self):
		super().__init__(level=self.level)

	def emit(self, record: logging.LogRecord) -> None:
		try:
			requests_handler: logging.Logger = logging.getLogger('requests')
			requests_handler.propagate = False
			url: str = 'https://api.telegram.org/bot{}/sendMessage'.format(self.token)
			for chat_id in self.ids:
				payload = {
					'chat_id':                  chat_id,
					'text':                     self.format(record),
					'disable_web_page_preview': self.disable_web_page_preview,
					'disable_notification':     self.disable_notification,
					'parse_mode':               getattr(self.formatter, 'parse_mode', None),
				}
				requests.post(url, data=payload, timeout=self.timeout)
				logger.debug(f'Send  logging-message to {chat_id} tg chat')
			requests_handler.propagate = True
		except:
			self.handleError(record)
