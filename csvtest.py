import os
import csv
import random


# '/home/jasonkirk/Dropbox/@project_files/python/workcvs/20131105_computrace_dump.csv'
csvfile_name = '20131105_computrace_dump.csv'

def get_file_path(filename):
        currentdirpath = os.getcwd()
        file_path = os.path.join(os.getcwd(),filename)
        return file_path

def proc_csv_lastcall(row):
        if row[0]:
                lc_date, lc_time = row[0].split(' ')
        else:
                lc_date = "\t"
                lc_time = "\t"
        return lc_date, lc_time

def proc_csv_username(row):
        if row[1]:
                if "@" in row[1]:
                        username, domane = row[1].split('@')

                elif "\\" in row[1]:
                        domane, username = row[1].split('\\')

                elif row[1]:
                        username = row[1]
                else:
                        username = "\t"
                return username

def proc_csv_devicename(row):
        if row[2]:
                if "_" in row[2]:
                        location_code, barcode = row[2].split('_')

                else:
                        location_code = "\t"
                        barcode = "\t"
                return location_code, barcode

def read_csv():
        with open(get_file_path(csvfile_name), newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter='\t')
                for row in reader:
                        if not row: break
                        if not "Username" in row:

                                lc_date, lc_time = proc_csv_lastcall(row)
                                ct_list_date.append(lc_date)
                                ct_list_time.append(lc_time)                               

                                username = proc_csv_username(row)
                                location_code, barcode = proc_csv_devicename(row)
                                print(lc_date,"\t",lc_time,"\t",username,"\t",location_code,"\t",barcode)
                                    
ct_list_date=[]
ct_list_time=[]
read_csv()
print(len(ct_list_time))
print(ct_list_time[1:800])
#test