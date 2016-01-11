import requests
import logging
from bs4 import BeautifulSoup
import socket
import socks
from fake_useragent import UserAgent
from helpers.read_config import ReadConfig
import os
import time
from random import randint
from multiprocessing.dummy import Pool as ThreadPool

logging.basicConfig(level=logging.ERROR, filename='error.log')

base_path = os.path.dirname(os.path.abspath("__file__"))
cfg = ReadConfig(os.path.join(base_path, 'config.yaml'))

tor_port_range = cfg.config['tor_port_range']
ua = UserAgent()

def crawler(url):
    try:
        headers = {'User-Agent': ua.random}
        random_port = lambda l, r: randint(l, r)
        l_port = tor_port_range[0]
        r_port = tor_port_range[1]
        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", random_port(l_port, r_port))
        socket.socket = socks.socksocket
        print('scraping')
        r = requests.get(url, verify=False, headers=headers)
        make_soup(r)
        time.sleep(20)
    except Exception, e:
        logging.exception("error message")

def make_soup(response):
    soup = BeautifulSoup(response.text, "lxml")

if __name__ == '__main__':
    urls = []

    pool = ThreadPool(10)
    pool.map(crawler, urls)
    pool.close()
    pool.join()
