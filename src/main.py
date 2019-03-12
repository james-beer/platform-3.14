from controller import *
from server import *
import os

port = int(os.environ['PLATFORM_3_14_PORT'] or '80')

# Sample layout inspired by Zwift.
controller = Controller([
  ('Watopia Central', ['Volcano', 'Alpe du Zwift']),
  ('Volcano', ['Watopia Central', 'Scenic Loop'])
])

server = Server(controller)

if __name__ == '__main__':
    server.run(port)