import socket
from bs4 import BeautifulSoup

HOST = "localhost"
PORT = 8080
PATHS = [""]
VISITED_PATHS = set()
GRAPH_REPORT = set()

print("🕷️ Iniciando o Crawler...")

while PATHS:
    
    path = PATHS.pop(0)

    # print(f"\n🔗 Visitando: http://{HOST}:{PORT}/{path}")
    request = f"GET /{path} HTTP/1.1\r\nConnection: close\r\nHost: localhost\r\n\r\n"
    
    VISITED_PATHS.add(path)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(request.encode())

        response = b""

        while True:
            data = s.recv(1024)
            if not data:
                break
            response += data

    html_content = response.decode('utf-8', errors='ignore')
    html_content_list = html_content.splitlines()
    
    header = html_content_list[0]
    header_splited = header.split()
    status_code = header_splited[1]

    if status_code == "301":
        for content in html_content_list:
            if content.startswith("Location:"):
                line = content.split(" ")
                redirect_url = line[1]
                clean_path = redirect_url.removeprefix("http://localhost/")

                GRAPH_REPORT.add((path, clean_path))
                
                if clean_path not in VISITED_PATHS and clean_path not in PATHS:   
                    PATHS.append(clean_path)
    elif status_code == "404":
        continue
    elif status_code == "501":
        continue
    else:      
        soup = BeautifulSoup(html_content, 'html.parser')

        for link in soup.find_all('a'):
            href = link.get('href')
            
            if href.startswith("/"):
                href = href[1:]

            GRAPH_REPORT.add((path, href))
            if href not in VISITED_PATHS and href not in PATHS:   
                PATHS.append(href)

