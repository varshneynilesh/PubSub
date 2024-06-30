# create topic and Subscription
# -----------------------------
$ gcloud pubsub topics create MyTopic
$ gcloud pubsub topics list
$ gcloud pubsub subscriptions create --topic MyTopic MySub

$ sudo apt-get update
$ sudo apt-get install virtualenv
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install --upgrade google-cloud-pubsub

$ git clone <Git Location>
$ python bored.py


# Read the message
------------------
$ gcloud pubsub subscriptions pull MySub --auto-ack --limit 3


# Delete topic and subscription
# -------------------------------
$ gcloud pubsub subscriptions delete MySub
$ gcloud pubsub topic delete MyTopic


# more examples - https://github.com/GoogleCloudPlatform/python-docs-samples.git
