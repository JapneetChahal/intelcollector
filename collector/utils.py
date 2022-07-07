# -*- coding: utf-8 -*-
import yaml
import os
from datetime import datetime

def ensure_current_date_folder(self):
    currentDateTime = "".join(str(datetime.now()).replace(' ', 'T').split('.')[:-1])
    test_folder = self.raw_files_location+"/"+currentDateTime
    if not os.path.isdir(test_folder):
        os.mkdir(test_folder)
    return test_folder
