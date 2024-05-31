# import xmlrpc bagian client 
import xmlrpc.client

# buat proxy untuk mengakses server
# gunakan parameter URL server yang akan diakses berupa ip dan port
# bentuk http://IP:Port 
proxy = xmlrpc.client.ServerProxy("http://localhost:12354")

with open("hasil_download.txt","wb") as handle:
    handle.write(proxy.download().data)
    