from trame.app import get_server
from modules import ui, pipeline

server = get_server()
state = server.state

# Load layout and pipeline logic
ui.initialize(server)
pipeline.initialize(server)

if __name__ == "__main__":
    server.start()
