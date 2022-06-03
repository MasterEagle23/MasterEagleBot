import discord
from MyCustomLibraries import JsonAndDict, log

# inizialize and load the config file
global config
# noinspection PyRedeclaration
config = JsonAndDict.open_json('config.json')


async def message_recieved(client, message):
    log.add(f'Message recieved: {message.content}', 6)
    if message.content[:1] == config.get('prefix'):
        temp = message.content.replace(config.get('prefix'), '', 1)
        command = temp.split(' ')
        log.add(f'Command recieved: {command}', 5)

        # DEBUG Befehle
        if command[0] == 'ping':
            await message.channel.send('pong')
            log.add('Responded to Ping!', 5)
        if command[0] == 'shutdown':
            log.add('Shutting down!', 1)
            await client.close()

        #
        if command[0] == '':
            pass

    else:
        log.add('Recieved message is no command!', 6)


class MyClient(discord.Client):
    # do not touch this code
    async def on_ready(self):
        # when the connection to Discord is successfully establish, print and log it
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        await message_recieved(self, message)


def main():
    log.initialize(7)
    client = MyClient()
    client.run(config.get('token'))


if __name__ == '__main__':
    main()
