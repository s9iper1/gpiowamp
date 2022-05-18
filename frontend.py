from os import environ
import txaio
import aioconsole

from helper import constants

txaio.use_asyncio()
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


class Component(ApplicationSession):
    async def onJoin(self, details):
        # listening for the corresponding message from the "backend"
        # (any session that .publish()es to this topic).
        def onevent(msg):
            print("Got event: {}".format(msg))
        await self.subscribe(onevent, constants.status_command)
        while True:
            command = await aioconsole.ainput(">>> ")
            if command.lower() == "status":
                res = await self.call(constants.status_command)
            elif command.lower() == "on":
                res = await self.call(constants.on_command)
            elif command.lower() == "off":
                res = await self.call(constants.off_command)
            else:
                print("command not found")
            # call a remote procedure.
            print("command {}".format(res))



if __name__ == '__main__':
    runner = ApplicationRunner(
        environ.get("AUTOBAHN_DEMO_ROUTER", "ws://localhost:8080/ws"),
        "realm1",
    )
    runner.run(Component)
