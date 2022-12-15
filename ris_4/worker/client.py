import logging

from aiokafka import AIOKafkaProducer

from ris_4.settings import KAFKA_BOOTSTRAP_SERVER, KAFKA_TOPIC

log = logging.getLogger(__name__)


async def send_message_to_kafka_worker(word: str) -> None:
    log.info(f'[RIS-4] Sending "{word}" to kafka worker')
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER
    )
    await producer.start()
    try:
        await producer.send_and_wait(KAFKA_TOPIC, word.encode())
    finally:
        await producer.stop()
