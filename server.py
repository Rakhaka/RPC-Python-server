# import library simpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# import xmlrpc bagian client 
import xmlrpc.client

# buat server pada ip dan port yang telah ditentukan 
ip_address = "localhost"
port = 12354
server = SimpleXMLRPCServer((ip_address,port))

# buatlah fungsi bernama file_download
def file_download ():
    # buka file bernama file_download.txt
    with open("file_didownload.txt", "rb") as handle:
        # kirimkan file tersebut dalam bentuk xml dengan cara memanggil xmlrpc.client.Binary ()
        return xmlrpc.client.Binary(handle.read())
    
 # print bahwa "server mendengarkan port xxx"
print ("listening on port", port)

# register fungsi download pada server 
server.register_function(file_download, "download")

# jalankan servernya
server.serve_forever()
    
