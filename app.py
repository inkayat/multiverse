from argparse import ArgumentParser
import csv
import json
from pprint import pprint
import requests


def get_mean_values():
   url = 'http://localhost:8000/api/compute/mean'
   response = requests.get(url)
   pprint(response.json())
   return response.json()

def get_best_n_feature(n:str=''):
    if n=='all':
        url='http://localhost:8000/api/compute/feature-importance'
    else:
        url = 'http://localhost:8000/api/compute/feature-importance/'+str(n)+'/'
    response = requests.get(url)
    print(response.json())
    return response.json()


def preview(n):
    if n==1:
        pprint(get_mean_values())
    else:
        pprint(get_best_n_feature())

def save(data):
   with open('product_data.csv', 'w') as f:
       field_names = ['']
       writer = csv.DictWriter(f, fieldnames=field_names)

       writer.writeheader()
       for row in data.json():
           writer.writerow(row)


if __name__ == '__main__':
    parser = ArgumentParser(description='A command line tool for interacting with our API')
    parser.add_argument('-cm', '--mean', action='store_true', help='Sends a GET request to the API to calculate mean of data values.')
    parser.add_argument('-f', '--feature', action='store', type=str, help='Sends a GET request to API to find most important features.')
    parser.add_argument('-p', '--preview', action='store', type=int, help='Shows us a preview of the data.')

    args = parser.parse_args()

    if args.mean:
        get_mean_values()
    elif args.feature :
        get_best_n_feature(args.feature)
    elif args.preview:
        preview(args.preview)
    else:
        print('Use the -h or --help flags for help')
