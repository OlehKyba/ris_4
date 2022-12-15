import logging

from aiokafka import AIOKafkaConsumer
from kafka.consumer.fetcher import ConsumerRecord

from ris_4.settings import KAFKA_BOOTSTRAP_SERVER, KAFKA_GROUP_ID, KAFKA_TOPIC
from ris_4.bl import decrease_by_one_letter
from ris_4.server.client import send_message_to_grpc_server

log = logging.getLogger(__name__)


async def handle_msg(msg: ConsumerRecord) -> None:
    log.info(f'[RIS-4] Kafka consumer get: {msg=}')
    word = msg.value.decode()

    new_word = decrease_by_one_letter(word)
    log.info(f'[RIS-4] Decrease "{word}" by one letter: {new_word=}')

    if new_word:
        await send_message_to_grpc_server(new_word)
    else:
        log.info(f'[RIS-4] Finish! {new_word=}')


async def serve() -> None:
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id=KAFKA_GROUP_ID,
        auto_offset_reset="earliest",
        # session_timeout_ms=100000,
        # request_timeout_ms=3000000,
        # max_poll_interval_ms=60000000,
        # retry_backoff_ms=300000,
    )

    try:
        await consumer.start()
        log.info(
            f'[RIS-4] Consumer for kafka on {KAFKA_BOOTSTRAP_SERVER} starts.'
        )

        async for msg in consumer:
            await handle_msg(msg)
    finally:
        log.info('[RIS-4] Shutdown kafka consumer')
        await consumer.stop()
