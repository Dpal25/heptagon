import time
import json
import multiprocessing


def add(json_data):
    s = 0
    for item in json_data['inputs']:
        s += item

    return {'input' : json_data['inputs'], 'response' : s}


if __name__ == '__main__':
    jsons = json.load(open('input.json'))
    responses = []
    print('Number of entries = {}'.format(len(jsons['data'])))
    with multiprocessing.Pool() as pool:
        responses = pool.map(add, [item for item in jsons['data']])

    for response in responses:
        print(response)

