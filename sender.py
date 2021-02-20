from transport.pubsub_adapter import PubSubPublisher, PubSubSubcriber
import os
#os.environ['GRPC_SSL_CIPHER_SUITES'] = 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384'
PROJECT_ID = "total-array-286510"

publisher = PubSubPublisher(PROJECT_ID)
publisher.create()
publisher.publish("topic1", "abc")

subscriber = PubSubSubcriber(PROJECT_ID)
subscriber.create()

def callback(message):
    print(f"Received {message}.")
    message.ack()

streaming_pull_future = subscriber.subscriber.subscribe(subscriber.subscription_path, callback=callback)
print(f"Listening for messages on {subscriber.subscription_path}..\n")

# Wrap subscriber in a 'with' block to automatically call close() when done.
with subscriber.subscriber:
    try:
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        streaming_pull_future.result(timeout=10)
    except TimeoutError:
        streaming_pull_future.cancel()
