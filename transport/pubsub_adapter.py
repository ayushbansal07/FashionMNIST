from .transport_adapter import IPublisherAdapter, ISubscriberAdapter
from google.cloud import pubsub

import os
os.environ['GRPC_SSL_CIPHER_SUITES'] = 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384'

class PubSubPublisher(IPublisherAdapter):
    def __init__(self, project):
        self.publisher = None
        self.project = project

    def _getTopicString(self, topic):
        return "projects/"+self.project+"/topics/"+topic

    def create(self):
        self.publisher = pubsub.PublisherClient()

    def publish(self, topic, msg):
        self.publisher.publish(self._getTopicString(topic), msg.encode())

class PubSubSubcriber(ISubscriberAdapter):
    def __init__(self, project):
        self.subscriber = None
        self.project = project
        self.subscription_path = ""

    def _getTopicString(self, topic):
        return "projects/"+self.project+"/topics/"+topic

    def create(self):
        self.subscriber = pubsub.SubscriberClient()
        self.subscription_path = self.subscriber.subscription_path(self.project, "subscrip")

    
