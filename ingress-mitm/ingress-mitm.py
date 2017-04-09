import time,json

from mitmproxy.script import concurrent
#from mitmproxy.net.http import message
#from mitmproxy.protocol.http import decoded


@concurrent  # 
def request(flow):
    #print("start  request: %s%s" % (flow.request.host, flow.request.path))
    if flow.request.host == "m-dot-betaspike.appspot.com":
       print("handle request: %s%s" % (flow.request.host, flow.request.path))
       if flow.request.path == '/rpc/player/say' :
          print("say")
       if flow.request.path == '/rpc/gameplay/getPaginatedPlexts' :
          print("plext req")

@concurrent
def response(flow):
    #print("start  response: %s%s" % (flow.request.host, flow.request.path))
    if flow.request.host == "m-dot-betaspike.appspot.com":
       print("handle response: %s%s" % (flow.request.host, flow.request.path))
       if flow.request.path == '/handshake' :
          print("handshake!")
       if flow.request.path == '/rpc/gameplay/getPaginatedPlexts' :
          print("plext resp")
       if flow.request.path == '/rpc/gameplay/getObjectsInCells' :
          print("goic resp")

       #request_headers = [{"name": k, "value": v} for k, v in flow.request.headers]
       #response_headers = [{"name": k, "value": v} for k, v in flow.response.headers]
       print ("################################")
       print ("FOR: " + flow.request.url)
       print (flow.request.method + " " + flow.request.path + " " + flow.request.http_version)
       #print ("HTTP REQUEST HEADERS")
       #print (flow.request.headers)
       print ("HTTP RESPONSE CONTENT")
       #print (flow.response.content)
       req = json.loads(flow.response.text)
       print (req)
       print ("")
       
