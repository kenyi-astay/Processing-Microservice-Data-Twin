from proto_files import hello_pb2
from  proto_files import hello_pb2_grpc


class HelloService(hello_pb2_grpc.HelloServiceServicer):
    def SayHello(self,request,context):
        print(request)
        return hello_pb2.HelloResponse(greet="Hello "+request.name)

