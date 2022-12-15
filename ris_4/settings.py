import os

GRPC_HOST = os.getenv('GRPC_HOST', 'grpc')
GRPC_PORT = os.getenv('GRPC_PORT', 50051)

KAFKA_BOOTSTRAP_SERVER = os.getenv('KAFKA_BOOTSTRAP_SERVER', 'kafka:9092')
KAFKA_GROUP_ID = os.getenv('KAFKA_GROUP_ID', 'test-group')
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'decrease-by-one-letter')
