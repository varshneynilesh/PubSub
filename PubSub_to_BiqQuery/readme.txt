# data generation source: https://www.mockaroo.com/


# Steps
# -----
# create temp storage bucket for dataflow
$ gcloud storage buckets create gs://sfo-pubsub-bq-tmp

# create topic
$ gcloud pubsub topics create purchases

# create subscriptions
$ gcloud pubsub subscriptions create --topic purchases trends

# install pubsub python api
$ sudo pip3 install google-cloud-pubsub

# create big query dataset trends and purchase table to match the table schema from csv ffile


# create dataflow job from tempalte to stream data from pubsub to bigquery

# clone the git
$ git clone https://github.com/varshneynilesh/PubSub.git
$ cd /PubSub/PubSub_to_BiqQuery

# change the project name in main.py and run
$ python main.py


# Validate data in Big Query table


# Delete all the resouces created
--------------------------------
# stop and delete dataflow job
# delete subscription and topics
# delete big query dataset
# delete cloud storage cucket
