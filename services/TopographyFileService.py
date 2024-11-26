from proto_files import TopographyFile_pb2
from  proto_files import TopographyFile_pb2_grpc


class TopographyFileService(TopographyFile_pb2_grpc.TopographyFileServiceServicer):
    def UploadFile(self,request,context):
        print(request)
        return TopographyFile_pb2.UploadStatus(success=True,message = "File uploaded")

