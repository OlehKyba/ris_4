import logging

from grpc import ServicerContext
from grpc.aio import server

from ris_4.server.grpc.ris_4_pb2_grpc import RIS4ServiceServicer, add_RIS4ServiceServicer_to_server
from ris_4.server.grpc.ris_4_pb2 import (
    DecreaseByOneLetterRequest,
    DecreaseByOneLetterResponse,
)
from ris_4.bl import decrease_by_one_letter
from ris_4.settings import GRPC_PORT
from ris_4.worker.client import send_message_to_kafka_worker

log = logging.getLogger(__name__)


class RIS4GrpcServer(RIS4ServiceServicer):
    async def DecreaseByOneLetter(
        self,
        request: DecreaseByOneLetterRequest,
        context: ServicerContext,
    ) -> DecreaseByOneLetterResponse:
        log.info(f'[RIS-4] Get gRPC request: {request.word=}')

        new_word = decrease_by_one_letter(request.word)
        log.info(f'[RIS-4] Decrease "{request.word}" by one letter: {new_word=}')

        if new_word:
            await send_message_to_kafka_worker(new_word)
        else:
            log.info(f'[RIS-4] Finish! {new_word=}')

        return DecreaseByOneLetterResponse(is_decreased=bool(new_word))


async def serve():
    app = server()
    add_RIS4ServiceServicer_to_server(RIS4GrpcServer(), app)

    listen_addr = f"[::]:{GRPC_PORT}"
    app.add_insecure_port(listen_addr)

    log.info(f'Starting async gRPC server on {listen_addr}')
    await app.start()
    await app.wait_for_termination()
