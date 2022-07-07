# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup

class FeedCollector(object):    
    def __init__(self, url):
        self.url = url
    def download_raw_files(self, path):
        os.system("wget "+self.url+" -P "+path)

class DantorCollector(FeedCollector):    
    def download_raw_files(self, path):
        for url in self.url:
            os.system("wget "+url+" -P "+path)

class DomainCollector(FeedCollector):
    def download_raw_files(self, path):
        os.system("wget "+self.url+" -P "+path)

class FeodoCollector(FeedCollector): 
    def download_raw_files(self, path):
        for url in self.url:            
            os.system("wget "+url+" -P "+path)

class FireholCollector(FeedCollector):
    def download_rep(self, url):
        os.system("git clone "+url+" temp/")
 
    def download_raw_files(self, path):
        cwd = os.getcwd()
        self.download_rep(self.url)
        self.move_lists(path, cwd+"/temp")
        os.system("rm -r "+cwd+"/temp/")

    def download_raw_files(self, path):
        cwd = os.getcwd()
        self.download_rep(self.url)
        self.move_lists(path, cwd+"/temp")
        os.system("rm -r "+cwd+"/temp/")

    def move(self, copy_location, paste_location):
        os.system("cp "+copy_location+" "+paste_location)

    def move_lists(self, folder_path, git_path):
        cues = "blocklist cleantalk dronebl firehol_abusers ipblocklist stopforspam sblam proxylists proxy ri_connect ri_web " \
           "socks_proxy ssl_proxy xroxy bi_any bi_apache bi_as bi_cms bi_default bi_dns bi_dov bi_ftp bi_htt bi_mail bi_ " \
           "blocklist_de blueliv dataplane dshield_ firehol_ normshield_ urandomusto".split(" ")
        files_list = os.listdir(git_path)
        
        for file_name in files_list:
            complete_path = git_path+"/"+file_name
            if os.path.isfile(complete_path):
                for cue in cues:
                    if cue in file_name and "bot" and "dos" and "tor" not in file_name:
                        self.move(complete_path, folder_path)
                        break
                    elif "bot" in file_name:
                        self.move(complete_path, folder_path)
                        break
                    elif "dos" in file_name:
                        self.move(complete_path, folder_path)
                        break
                    elif "tor" in file_name:
                        self.move(complete_path, folder_path)
                        break

class GreenSnowCollector(FeedCollector):
    def download_raw_files(self, path):
        for i in range(6,9):
            os.system("wget "+self.url.replace("<level>", str(i))+" -P "+path)
        self.url = url
    def download_raw_files(self, path):import os

class Collector(FeedCollector):    
    def download_raw_files(self, path):
        os.system("wget "+self.url+" -P "+path)
        os.system("wget "+self.url+" -P "+path)

class MalshareCollector(FeedCollector): 
    def download_raw_files(self, path):
        os.system("wget "+self.url+" -P "+path)

class MISPCollector(FeedCollector):  
    def download_raw_files(self, path):
        for i in range(6,9):
            os.system("wget "+self.url.replace("<level>", str(i))+" -P "+path)

class OpenphishCollector(FeedCollector):
    def download_raw_files(self, path):
        os.system("wget "+self.url+" -P "+path)

class SSLCollector(FeedCollector):
    def download_raw_files(self, path):
        os.system("wget "+self.url+" -P "+path)

class SuricataCollector(FeedCollector):
    def get_links(self, url, iptype):
        links_list = []
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        for hlink in soup.findAll('a'):
            url_link = hlink.get('href')
            if iptype in url_link:
                links_list.append(url+url_link[2:])
        return(links_list)

    def download_raw_files(self, path):
        self.URI = []
        IPTypes = ["bot", "tor"]
        for iptype in IPTypes:
            self.URI.append(self.get_links(self.url, iptype)[0])
        for uri in self.URI:
            os.system("wget "+uri+" -P " +path)

class ThreatFoxCollector(FeedCollector):
    def download_raw_files(self, path):
        os.system("wget "+self.url+" -P "+path)


