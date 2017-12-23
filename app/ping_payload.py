

class PingPayload:

    def __init__(self):
        super().__init__()

    def ping_exfiltrate(self, binary_ip, identity, selected_interface):

        print("Sending ping payload %d on interface %s" % (identity, selected_interface))
