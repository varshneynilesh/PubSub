import json
import csv
from google.cloud import pubsub

project_name = '<PROJECT-NAME>'
topic_name = 'purchases'
file = 'data/customers_data.csv'

publisher = pubsub.PublisherClient()
topic_path = publisher.topic_path(project_name, topic_name)

with open(file) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    for row in rd:
        data = json.dumps(dict(row))
        publisher.publish(topic_path, data=data.encode('utf-8'))

