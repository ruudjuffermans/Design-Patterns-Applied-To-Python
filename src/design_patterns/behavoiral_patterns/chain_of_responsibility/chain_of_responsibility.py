from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass

class BaseHandler(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler
    
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None
    
class ConcreteHandlerA(BaseHandler):
    def handle(self, request):
        if request == "A":
            return f"ConcreateHandlerA: Handled: {request}"
        else:
            return super().handle(request)

class ConcreteHandlerB(BaseHandler):
    def handle(self, request):
        if request == "B":
            return f"ConcreateHandlerB: Handled: {request}"
        else:
            return super().handle(request)

class ConcreteHandlerC(BaseHandler):
    def handle(self, request):
        if request == "C":
            return f"ConcreateHandlerC Handled: {request}"
        else:
            return super().handle(request)


if __name__ == "__main__":
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_c = ConcreteHandlerC()

    handler_a.set_next(handler_b).set_next(handler_c)

    requests = ["A", "B", "C", "D"]

    for request in requests:
        result = handler_a.handle(request)
        if result:
            print(result)
        else:
            print(f"{request} was not handled")