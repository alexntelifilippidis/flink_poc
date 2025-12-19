"""
Kafka Configuration
"""

# Kafka Broker Configuration
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"

# Topic Configuration
DEFAULT_TOPIC = "test-topic"

# Producer Configuration
PRODUCER_CONFIG = {
    "acks": "all",  # Wait for all replicas to acknowledge
    "retries": 3,
    "max_in_flight_requests_per_connection": 1,
    "compression_type": None,  # Options: 'gzip', 'snappy', 'lz4', 'zstd'
}

# Consumer Configuration
CONSUMER_CONFIG = {
    "group_id": "test-consumer-group",
    "auto_offset_reset": "earliest",  # Start from beginning if no offset
    "enable_auto_commit": True,
    "auto_commit_interval_ms": 1000,
}

