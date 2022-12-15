import asyncio
import logging

from ris_4.worker.service import serve

logging.basicConfig(level=logging.INFO)
asyncio.run(serve())
