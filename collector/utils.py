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

def deduplicate_files(self, folder_path, priority_list):
    final_files = []
    initial_file = open(folder_path+"/"+priority_list[0], "r")
    initial_arr = initial_file.readlines()
    
    final_files.append(initial_file.readlines())
    for file_name in priority_list[1:]:
        file_path = folder_path+"/"+file_name
        file_ = open(file_path, "r")
        file_lines = file_.readlines()
        temp = file_lines
        for ioc_file in final_files:
            temp = list(set(temp) - set(ioc_file))
        final_files.append(temp)
    for i in range(len(priority_list)):
        temp_file = open(folder_path+"/"+priority_list[i], "w")
        temp_file.writelines(final_files[i])
        temp_file.close()

def is_valid_ioc(self, ioc_value, ioc_type):  
    return True

def validate_file(self, file_path):
    ioc_type = file_path.split("/")[-1].split(".")[0]
    file_ = open(file_path, "r")
    file_lines = file_.readlines()
    file_.close()
    new_lines = []
    for ioc in file_lines:
        if is_valid_ioc(self, ioc, ioc_type):
            new_lines.append(ioc)
    file_ = open(file_path, "w")
    file_.writelines(new_lines)
    file_.close()

def validate_folder(self, folder_path):
    for file_name in os.listdir(folder_path):
        validate_file(self, folder_path+"/"+file_name)
