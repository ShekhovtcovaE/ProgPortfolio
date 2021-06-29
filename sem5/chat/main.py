import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.locks import Condition
import asyncio
import functools

def singleton(class_):
    instances = {}
    @functools.wraps(class_)
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        
class MessageBuffer():
    def __init__(self, messages):
        self.__messages = []
        self.__messages_size = 50
        self.cond = tornado.locks.Condition()
        
    def add_message(self, message):
        self.__messages.append(message)
        if len(self.__messages) > self.__messages_size:
            self.__messages = self.__messages[-self.__messages_size:]
        self.cond.notify_all()
        
    def get_message(self):
        return self.__messages 
    
    def get_message_since(self, cursor):
        results = []
        for msg in reversed(self.__messages):
            if msg['id'] = cursor:
                break
            results.append(msg)
        results.reverse()
        
        return results
        
globalmessagebuffer = MessageBuffer()
globalmessagebuffer.add_message({"id": "0", "message":"The chat was started."}) 
globalmessagebuffer.add_message({"id": "0", "message": "Say hello to everybody!"})

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", messages = globalmessagebuffer.get_message())


class EchoWebSocketHandler(tornado.websocket.WebSocketHandler):    

    messages = {}
    
    def onopen(self):
        print("websocket is opened")
        
    def on_message(self, message):
        """import time
        key = time.strftime("%Y%m%d%H%M%S")
        new_message = {'message': message}
        globalmessagebuffer.add_message(new_message)
        EchoWebSocketHandler.messages[key] = message
        self.write_message(f" Message was sent: {message}")"""
        import uuid

        id = uuid.uuid4()
        new_message = {'id': id.hex,  'message': message}
        
        globalmessagebuffer.add_message(new_message)
        print(f"{ new_message.get('id', 'Unknown ID') } write {new_message.get('message', 'Empty message')}")
        self.write_message(f" Message was sent: {message} ")
    
    def on_close(self):
        print("websocket is opened")


class MessageUpdatesHandler(tornado.web.RequestHandler):
    async def post(self):
        cursor = self.get_argument('cursor', None)
        
        print(f'cursor{cursor}')
        messages = globalmessagebuffer.get_message_since(cursor)
        print(messages)
    
    def on_connection_close(self):
        self.wait_future.cancel()

    
def make_app():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/index", IndexHandler),
        (r"/echo", EchoWebSocketHandler),
        (r"/message/update", MessageUpdatesHandler),
    ], debug = True)
    
if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
 