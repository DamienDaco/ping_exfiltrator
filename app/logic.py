from app.multithreading import *
from app.network_functions import *

class Logic:

    def __init__(self, selected_interface):
        super().__init__()
        print("Logic has been initialized")
        self.threads = []                   # List for storing multiple threads
        self.identities = 0                # List of workers identities (numbers)
        self.interfaces = get_interfaces()
        self.selected_interface = selected_interface

    def start_thread(self):

        thread = MultiThreading(self.identities, self.selected_interface)
        thread.start_thread()
        self.threads.append(thread)
        self.identities += 1

    def stop_thread(self):

        if len(self.threads) > 0:               # Check if there's something in the list
            for thread in self.threads:         # Let's go through the list of threads
                thread.stop_thread()            # And send the stop signal to each thread

        self.threads = []                       # When done, reset list
        self.identities = 0
