import txaio

from helper import constants

txaio.use_asyncio()
from os import environ
from helper.gpio_control import set_out_low, set_out_high, get_state
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


class Component(ApplicationSession):
    async def onJoin(self, details):
        # a remote procedure; see frontend.py for a Python front-end
        # that calls this. Any language with WAMP bindings can now call
        # this procedure if its connected to the same router and realm.

        def status():
            return get_state(21).get('value_verbose')

        def on():
            print('Turn on the button')
            result = set_out_high(21)
            print(result)
            return status()

        def off():
            print('Turn off the button')
            result = set_out_low(21)
            print(result)
            return status()

        state = await self.register(status, constants.status_command)
        on = await self.register(on, constants.on_command)
        off = await self.register(off, constants.off_command)

        # print(f"registered 'com.myapp.add2' with id {registration.id}")

        # publish an event every second. The event payloads can be
        # anything JSON- and msgpack- serializable
        # while True:
        #     self.publish('com.myapp.hello', 'Hello, world!')
        #     await asyncio.sleep(1)
        #


if __name__ == '__main__':
    runner = ApplicationRunner(
        environ.get("AUTOBAHN_DEMO_ROUTER", "ws://localhost:8080/ws"),
        "realm1",
    )
    runner.run(Component)
