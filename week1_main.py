import os
from dotenv import load_dotenv
from src.kafka.kafka_client import KafkaClient
from src.kafka.message import Message
from src.utils.logger import get_logger

# Load environment variables
load_dotenv()

# Configure logger
logger = get_logger(__name__, level=os.getenv('LOG_LEVEL', 'INFO'))


def main():
    """
    Main function to demonstrate Kafka producer and consumer.
    """
    # Load configuration from environment variables
    bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
    client_id = os.getenv('KAFKA_CLIENT_ID', 'test-client')
    topic = os.getenv('KAFKA_TOPIC', 'orders')
    consumer_group_id = os.getenv('KAFKA_CONSUMER_GROUP_ID', 'order-processor')

    logger.info("Starting Kafka application")
    logger.info(f"Connecting to Kafka at: {bootstrap_servers}")

    try:
        # Initialize Kafka client
        client = KafkaClient(bootstrap_servers, client_id)

        # Produce a message
        msg = Message('order-1', {'amount': 100, 'status': 'pending'})
        logger.info(f"Producing message to topic: {topic}")
        client.produce_message(topic, msg)

        # Consume messages - iterate over the generator
        logger.info(f"Starting to consume from topic: {topic}")
        for consume_msg in client.consume_messages(topic, consumer_group_id):
            logger.info(f"Processing order: {consume_msg.value}")
            break  # Exit after processing one message for demo purposes

    except KeyboardInterrupt:
        logger.warning("Application interrupted by user")
    except Exception as e:
        logger.error(f"Application error: {e}")
        raise
    finally:
        logger.info("Closing Kafka client")
        client.close()
        logger.info("Application shutdown complete")


if __name__ == '__main__':
    main()
