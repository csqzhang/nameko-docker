from nameko.rpc import rpc
import random

n = random.randint(0,100)


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}! I am {}".format(name, n)