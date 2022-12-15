import asyncio
import argparse
import logging

from ris_4.worker.client import send_message_to_kafka_worker

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(description='Send initial word to services.')
parser.add_argument('word', help='initial word', type=str)

args = parser.parse_args()


async def main() -> None:
    await send_message_to_kafka_worker(args.word)

asyncio.run(main())
