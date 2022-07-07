# -*- coding: utf-8 -*-
import yaml
from time import sleep
import os
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

import logging 
import traceback

from . import feeds
from .utils import ensure_current_date_folder

class Collector():
    def parse_args(self):
        with open("/usr/local/etc/intelCollectorConfig.yaml") as config_params:
            self.config = yaml.full_load(config_params)
        self.frequency = self.config.get("update_every") 
        self.raw_files_location = self.config.get("raw_files_location")
        self.intel_list_path = self.config.get("intel_list")
        self.log_file_location = self.config.get("log_file_location")
        with open(self.intel_list_path) as url_file:   
            self.urls = yaml.full_load(url_file)
        self.collectors.append(feeds.SuricataCollector(self.urls.get("suricata"), "suricata"))
        self.collectors.append(feeds.FireholCollector(self.urls.get("firehol"), "firehol"))
        self.collectors.append(feeds.DomainCollector(self.urls.get("domains"), "domains"))
        self.collectors.append(feeds.SSLCollector(self.urls.get("fingerprint"), "fingerprint"))
        self.collectors.append(feeds.GreenSnowCollector(self.urls.get("greensnow"), "greensnow"))
        self.collectors.append(feeds.OpenphishCollector(self.urls.get("openphish"), "openphish"))
        self.collectors.append(feeds.MalshareCollector(self.urls.get("malshare"), "malshare"))
        self.collectors.append(feeds.ThreatFoxCollector(self.urls.get("threatfox"), "threatfox"))
        self.collectors.append(feeds.DantorCollector(self.urls.get("dan_tor"), "dan_tor"))
        self.collectors.append(feeds.FeodoCollector(self.urls.get("feodo_tracker"), "feodo_tracker"))
        self.collectors.append(feeds.MISPCollector(self.urls.get("misp_level"), "misp_level"))

    def __init__(self):        
        self.cwd = str(os.getcwd())
        self.collectors = []
        self.parse_args()
        self.scheduler = BackgroundScheduler()
        logging.basicConfig(filename=self.log_file_location, format='%(asctime)s %(message)s', filemode='a')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    def download_raw_files(self):
        self.raw_folder = ensure_current_date_folder(self)
        for collector in self.collectors:
            try:
                collector.download_raw_files(self.raw_folder)
                self.logger.info("Downloaded "+str(collector.url))
            except Exception as e:
                self.logger.error(e)
                self.logger.error(traceback.print_exc())
            
            collector.mold_files(self.raw_folder)
    def start(self):
        self.scheduler.add_job(self.download_raw_files, 'interval', minutes=1)
        self.scheduler.start()     

def main():
    collector = Collector()
    #collector.mold_files(collector.name)
    collector.download_raw_files()
    '''
    collector.start()
    while True:
        sleep(1)
    '''
if __name__ == '__main__':
    main()
