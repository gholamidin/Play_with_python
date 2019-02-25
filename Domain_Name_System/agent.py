import threading
import socket
import socketserver


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        request_data = self.request[0]
        # 将请求转发到 114 DNS
        redirect_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        redirect_socket.sendto(request_data, ('114.114.114.114', 53))
        response_data, address = redirect_socket.recvfrom(1024)
    
        # 将114响应响应给客户
        client_socket = self.request[1]
        client_socket.sendto(response_data, self.client_address)


class Server(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass


if __name__ == "__main__":
    # 一下ip需换成自己电脑的ip
    server = Server(('192.168.100.12', 53), Handler)
    with server:
        server_thread = threading.Thread(target=server.serve_forever) #创建现成
        server_thread.daemon = True 				      #将线程放入后台处理
        server_thread.start() 					      #执行线程
        print('The DNS server is running at 172.16.42.254...')
        server_thread.join()        				      #防并发，一个线程结束后再执行下一个
