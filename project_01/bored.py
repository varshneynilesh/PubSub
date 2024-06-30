from google.cloud import pubsub
import requests
import time

project_name = "<GCP-Project-ID"
topic_name = "<Pubsub Topic>"
api = 'https://www.boredapi.com/api/activity/'

publisher = pubsub.PublisherClient()
topic_path = publisher.topic_path(project=project_name, topic=topic_name)

while True:
    response = requests.get(api).text
    print
    publisher.publish(topic_path, data=response.encode('utf-8'))
    time.sleep(5)
