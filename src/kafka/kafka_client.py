import os

from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError, KafkaTimeoutError
from typing import Optional, Generator
import json
from .message import Message
from ..utils.logger import get_logger

logger = get_logger(__name__, level=os.getenv('LOG_LEVEL', 'INFO'))


class KafkaClient:
    """
    KafkaClient wrapper for Kafka producer and consumer functionalities.

    Provides methods to produce and consume messages from Kafka topics
    with built-in serialization and error handling.
    """

    def __init__(self, bootstrap_servers: str, client_id: str) -> None:
        """
        Initialize the KafkaClient.

        Args:
            bootstrap_servers: Comma-separated list of Kafka broker addresses
            client_id: Unique identifier for this client instance
        """
        self.bootstrap_servers = bootstrap_servers
        self.client_id = client_id
        self._producer: Optional[KafkaProducer] = None
        self._consumer: Optional[KafkaConsumer] = None
        logger.info(f"KafkaClient initialized with client_id: {client_id}")

    def get_producer(self) -> KafkaProducer:
        """
        Get or create a KafkaProducer instance.

        Returns:
            Configured Kafka producer

        Raises:
            KafkaError: If producer creation fails
        """
        if not self._producer:
            try:
                self._producer = KafkaProducer(
                    bootstrap_servers=self.bootstrap_servers,
                    client_id=self.client_id,
                    value_serializer=lambda v: json.dumps(v).encode('utf-8')
                )
                logger.info("Producer created successfully")
            except KafkaError as e:
                logger.error(f"Failed to create producer: {e}")
                raise
        return self._producer

    def get_consumer(self, topic: str, group_id: str) -> KafkaConsumer:
        """
        Get or create a KafkaConsumer instance.

        Args:
            topic: Kafka topic to subscribe to
            group_id: Consumer group identifier

        Returns:
            Configured Kafka consumer

        Raises:
            KafkaError: If consumer creation fails
        """
        if not self._consumer:
            try:
                self._consumer = KafkaConsumer(
                    topic,
                    bootstrap_servers=self.bootstrap_servers,
                    client_id=self.client_id,
                    group_id=group_id,
                    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
                )
                logger.info(f"Consumer created for topic: {topic}, group: {group_id}")
            except KafkaError as e:
                logger.error(f"Failed to create consumer: {e}")
                raise
        return self._consumer

    def produce_message(self, topic: str, message: Message) -> None:
        """
        Produce a message to a Kafka topic.

        Args:
            topic: Target Kafka topic
            message: Message object to send

        Raises:
            KafkaTimeoutError: If message delivery times out
            KafkaError: If message production fails
        """
        try:
            producer = self.get_producer()
            future = producer.send(topic, value=message.to_dict())
            future.get(timeout=10)
            logger.info(f"Message sent to topic '{topic}': {message.key}")
        except KafkaTimeoutError as e:
            logger.error(f"Timeout sending message to '{topic}': {e}")
            raise
        except KafkaError as e:
            logger.error(f"Failed to send message to '{topic}': {e}")
            raise
        except Exception as e:
            logger.critical(f"Unexpected error sending message: {e}")
            raise

    def consume_messages(self, topic: str, group_id: str) -> Generator[Message, None, None]:
        """
        Consume messages from a Kafka topic.

        Args:
            topic: Kafka topic to consume from
            group_id: Consumer group identifier

        Yields:
            Deserialized message objects

        Raises:
            KafkaError: If consumer fails
        """
        try:
            consumer = self.get_consumer(topic, group_id)
            logger.info(f"Starting to consume from topic: {topic}")

            for kafka_message in consumer:
                try:
                    message = Message.from_dict(kafka_message.value)
                    logger.debug(f"Received message: {message.key}")
                    yield message
                except Exception as e:
                    logger.warning(f"Failed to deserialize message: {e}")
                    continue

        except KafkaError as e:
            logger.error(f"Consumer error on topic '{topic}': {e}")
            raise
        except Exception as e:
            logger.critical(f"Unexpected error consuming messages: {e}")
            raise

    def close(self) -> None:
        """
        Close producer and consumer connections.
        """
        try:
            if self._producer:
                self._producer.close()
                logger.info("Producer closed")
            if self._consumer:
                self._consumer.close()
                logger.info("Consumer closed")
        except Exception as e:
            logger.warning(f"Error closing connections: {e}")
