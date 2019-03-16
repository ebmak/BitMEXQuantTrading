import logging
import sys
from market_maker.ws.ws_thread import BitMEXWebsocket
from time import sleep

i = "XBTUSD"


if __name__ == '__main__':
    # create console handler and set level to debug
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    ws = BitMEXWebsocket()

    ws.logger = logger
    # ws.connect("https://testnet.bitmex.com/api/v1")
    ws.connect("https://www.bitmex.com/api/v1/", i, False)

    # print(ws.get_instrument(i))
    while ws.ws.sock.connected:
        # print(ws.get_ticker(i))
        # print(json.dumps(ws.data.get('trade'), indent=2))
        # print(str(len(ws.data.get('trade')))+","+str(sys.getsizeof(ws.data)))
        sleep(10)
