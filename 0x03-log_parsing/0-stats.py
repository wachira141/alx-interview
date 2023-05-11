#!/usr/bin/env python3
'''
function to check logs from NGINX
'''
import re


def get_log_input():
    '''
    get inputs from stin
    '''
    status_code_list = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }
    file_size = 0
    incrementer = 1
    try:
        while True:
            log_input = input()
            regex_data = regex_parser(log_input)
            count_codes = counter(regex_data['status'])
            file_size += regex_data['file_size']

            if count_codes in status_code_list.keys():
                status_code_list[count_codes] += 1

            if incrementer % 10 == 0:
                print_result(status_code_list, file_size)
            incrementer += 1
    except (KeyboardInterrupt, EOFError):
        print_result(status_code_list, file_size)


def counter(status_code):
    '''get the number of replied status code
    '''
    status_list = [
        '200',
        '301',
        '400',
        '401',
        '403',
        '404',
        '405',
        '500'
        ]
    if status_code in status_list:
        return status_code


def print_result(status_code_list, file_size):
    '''
    print the status code list
    '''
    for k, v in status_code_list.items():
        print('{}: {}'.format(k, v))
    print('File size: {}'.format(file_size))


def regex_parser(log_input):
    '''
    check if the line of log parsed
    '''
    reg_format = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<method>[^"]*)"\s*',
        r'\s*(?P<status_code>\d+)',
        r'\s*(?P<file_size>\d+)')

    formated_log = '{} - {}{}{}{}\\s*'\
        .format(reg_format[0], reg_format[1], reg_format[2], reg_format[3], reg_format[4])
    resp_match = re.fullmatch(formated_log, log_input)

    data = {
        'status': 0,
        'file_size': 0
     }
    if resp_match is not None:
        status = resp_match.group('status_code')
        file_size = resp_match.group('file_size')
        data['status'] = status
        data['file_size'] = int(file_size)

    return data


if __name__ == '__main__':
    get_log_input()
