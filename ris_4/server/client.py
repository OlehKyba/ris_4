import logging

from grpc.aio import insecure_channel

from ris_4.settings import GRPC_HOST, GRPC_PORT
from ris_4.server.grpc.ris_4_pb2 import DecreaseByOneLetterRequest
from ris_4.server.grpc.ris_4_pb2_grpc import RIS4ServiceStub

log = logging.getLogger(__name__)


async def send_message_to_grpc_server(word: str) -> None:
    log.info(f'[RIS-4] Sending "{word}" to gRPC server')
    async with insecure_channel(f'{GRPC_HOST}:{GRPC_PORT}') as channel:
        stub = RIS4ServiceStub(channel)
        await stub.DecreaseByOneLetter(
            DecreaseByOneLetterRequest(word=word)
        )
