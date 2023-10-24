import pandas as pd
import load_utility as ut
import file_tokenize as tk
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import requests
import time
import os

def authenticate_rpi(unique_id):
    url = "https://api.wmipnu.store/checkRpi"
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    data = '{"code":' + '"' + unique_id + '"}'
    # 이런식으로 아이디와 고유 코드를 전송해서 서버에서 유효성을 검증한다.

    try:
        requests.post(url=url, data=data, headers=headers)
        if(requests.Response == "OK"):
            print("성공적으로 인증 되었습니다.")
            time.sleep(10)
        else:
            assert "유효한 고유 코드가 아닙니다."
    except:
        print("Cannot connect to server!!")

if __name__ == "__main__":
    fp = open("uniqueCode.txt", 'r')
    unique_id = fp.readline()
    # authenticate_rpi(unique_id) # 여기서 기기인증 시도

    sys.path.append("../")
    RSS_directory = "RSS-1-realtime"  # txt 파일을 저장할 directory

    out_filename = RSS_directory + "/" + "RSS-realtime"
    scan_command = "sudo iwlist wlan0 scan | grep -E 'level|Address' | sed 's/level=//' | awk '{ if ( $1 == \"Cell\" ) { print $5 } if ( $2 == \"Signal\" ) { print $3 } }'"
    predict_counter = 1

    ap_list = ut.load_ap_list()
    url = "https://api.wmipnu.store/ap"
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    while predict_counter <= 3:
        client_rss_store = [0 for _ in range(107)]
        data_for_request = ""

        #curr_out_filename = "hello" + str(predict_counter) + ".txt"
        curr_out_filename = out_filename + "#" + str(predict_counter) + ".txt"
        curr_scan_command = scan_command + " > " + curr_out_filename
        os.system(curr_scan_command)

        data_for_parse = tk.parse_for_calculate(curr_out_filename)
        splitted_data = data_for_parse.split(",")
        idx = 0

        while idx < len(splitted_data):
            try:
                client_rss_store[ap_list[splitted_data[idx]]] = int(splitted_data[idx + 1])
            except:
                pass

            idx += 2

        for num in client_rss_store:
            data_for_request = data_for_request + str(num) + ','

        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data_for_request = '{"client_rss_store": "' + data_for_request[:-1] + '"}'
        response = requests.post("http://3.35.229.16:8000/predict/", headers=headers, data=data_for_request)
        
        response_for_spring = response.text[2:len(response.text)-2]
        response_for_spring = response_for_spring.split(',')

        data_for_spring = tk.coordinate_to_json(response_for_spring[0], response_for_spring[1]) # response를 잘 만져보자
        data_for_spring = tk.add_unique_id(unique_id, data_for_spring)
        print(data_for_spring)
        predict_counter += 1