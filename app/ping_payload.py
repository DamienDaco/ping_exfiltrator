import time


class PingPayload:

    def __init__(self):
        super().__init__()

    def ping_exfiltrate(self, binary_ip, identity, index, rate,  selected_interface):

        print("Worker %d is sending ping payload %d at rate %d on interface %s" % (identity, index, rate, selected_interface))
        time.sleep(rate)