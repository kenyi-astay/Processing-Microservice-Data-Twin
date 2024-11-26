from concurrent import futures
import logging
import asyncio
from grpc import ServerCredentials
from proto_files import hello_pb2_grpc
from proto_files import TopographyFile_pb2_grpc
import grpc
from services.HelloService import HelloService
from services.TopographyFileService import TopographyFileService


async def server() -> None:
    server = grpc.aio.server()
    hello_pb2_grpc.add_HelloServiceServicer_to_server(servicer=HelloService(),server=server)
    TopographyFile_pb2_grpc.add_TopographyFileServiceServicer_to_server(servicer=TopographyFileService(),server=server)
    # server.add_secure_port('[::]:50057', server_credentials=ServerCredentials())
    server.add_insecure_port('[::]:50057')
    await server.start()
    print("gRPC Server started. Listing on port 50057")
    await server.wait_for_termination()



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(server())

