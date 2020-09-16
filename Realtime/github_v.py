import pandas as pd
import matplotlib.pyplot as plt
import json
import requests
import csv
from collections import Counter
from matplotlib.ticker import MaxNLocator
import datetime
import dateutil.parser


def fetch_data():
    print('olleh')
    res = requests.get('https://api.github.com/users/sjlouji/repos')
    data = json.loads(res.text)
    df = pd.json_normalize(data)
    df.to_csv('test.csv', index=False, encoding='utf-8')

def plot_data_as_bar():
    print('hello')
    data_counter  = Counter()
    repo_name = []
    created = []
    with open('test.csv') as github_stats:
        data = csv.DictReader(github_stats, delimiter=',')
        for row in data:
            yourdate = dateutil.parser.parse(row['created_at'])
            repo_name.append(row['name'])
            created.append(yourdate.strftime('%A, %d. %B %Y'))
    plt.plot_date(created,repo_name)
    plt.xticks(rotation=60)
    plt.tight_layout()
    # plt.savefig('test.png')
    plt.show()

if __name__ == "__main__":
    plot_data_as_bar()