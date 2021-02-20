from .transport_adapter import IPublisherAdapter, ISubscriberAdapter
from confluent_kafka import Producer

class KafkaPublisher(IPublisherAdapter):
    def __init__(self, port=9002):
        self.port = port
        self.conf = {'bootstrap.servers': "localhost:"+str(port)}
        self.publisher = None

    def create(self):
        self.publisher = Producer(self.conf)

    def publish(self, topic, msg):
        self.publisher.produce(topic, value=msg)
