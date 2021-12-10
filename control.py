from ppadb.client import Client as AdbClient

import time
import logging
import requests

logging.basicConfig(
    filename='reg.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')

logging.getLogger().addHandler(logging.StreamHandler())
client = AdbClient(host="127.0.0.1", port=5037)
device = client.devices()[0]

# Tipo de rede
# 0 5G
# 1 2G

def get_click(id):
    x, y = [[80,1363], [161,583], [161,1147]][id]
    return "input tap {} {}".format(x,y)

def restart():
    logging.info("Iniciando restart")
    device.shell(get_click(0))
    time.sleep(1)
    device.shell(get_click(2))
    time.sleep(1)
    device.shell(get_click(0))
    device.shell(get_click(1))
    logging.info("Finalizando restart")
    return 0

def verify():
    try:
        url = "https://fast.com/"
        r = requests.get(url,timeout=10)
        if len(r.history) == 0:
            logging.info("Internet OK")
            return 2
        else:
            return restart()
    except:
        return restart()

while 1:
    verify()
    time.sleep(10)