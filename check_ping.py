from pythonping import ping


def get_ip_from_file(file):

    ip_list = []

    with open(file) as file_pings:
        for str in file_pings.readlines():
            index_colon = str.find(':')
            if index_colon != -1:
                ip_list.append((str[:index_colon], str[index_colon+1:].strip()))

    return ip_list

def get_ms_from_ip_list(ip_list):
    ms_list = []
    # not_work_ip = []

    for ip in ip_list:
        response = ping(ip[0], timeout=0.5)
        if response.rtt_avg_ms >= 500:
            # not_work_ip.append(ip)
            continue
        ms_list.append((ip, response.rtt_min_ms, response.rtt_max_ms, response.rtt_avg_ms))

    return ms_list

def converter_ip_list_to_str(ip_list):
    r = []
    for ip in ip_list:
        temp = '{0}:{1} min={2}, max={3}, avg={4}'.format(ip[0][0], ip[0][1], ip[1], ip[2], ip[3])
        r.append(temp)
    return r

def main(file):
    # file = 'file_pings.txt'
    ip_list = get_ip_from_file(file)
    work_ip =  get_ms_from_ip_list(ip_list)
    work_ip.sort(key=lambda tup: tup[3])

    return converter_ip_list_to_str(work_ip)

# print(main(file='file_pings.txt'))