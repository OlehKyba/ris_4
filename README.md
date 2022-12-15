# РІС. Практична робота №4.

## Завдання
Два завдання:

* Зробити клієнт серверне застосування, що обмінюється інформацією за допомогою `gRPC`;
* Зробити два сервера, що обмінюються інформацією з використанням черги повідомлень.


## Описання проєкту
Цей проєкт містить у собі два сервери, що обмінюються даними між собою
за допомогою `gRPC` та `Apache Kafka`. 

Обидва сервери виконують одну і ту саму логіку: вони отримують стрічку,
зменшують її на один символ та передають її далі до іншого сервера по `gRPC` чи 
чергу повідомлень (`Apache Kafka`) поки слово не перетвориться у пусту стрічку.
   

## Як запустити проєкт?
1. Виконати команду для збору `docker image` з кодом `python`:
```bash
make build
```
2. Запускаємо сервери:
```bash
make run
```
3. Передаємо слово:
```bash
make send word=<слово>
```

## Приклад роботи
1. Запускаємо сервера:
```bash
(venv) ➜  ris_4 git:(master) ✗ make run
docker-compose up --scale ris-image=0
Starting ris_4_zookeeper_1 ... done
Starting ris_4_kafka_1     ... done
Recreating ris_4_grpc_1    ... done
Recreating ris_4_worker_1  ... done
Attaching to ris_4_worker_1, ris_4_grpc_1``
grpc_1       | INFO:ris_4.server.service:Starting async gRPC server on [::]:50051
worker_1     | INFO:aiokafka.consumer.subscription_state:Updating subscribed topics to: frozenset({'decrease-by-one-letter'})
worker_1     | INFO:aiokafka.consumer.group_coordinator:Discovered coordinator 1001 for group test-group
worker_1     | INFO:aiokafka.consumer.group_coordinator:Revoking previously assigned partitions set() for group test-group
worker_1     | INFO:aiokafka.consumer.group_coordinator:(Re-)joining group test-group
worker_1     | INFO:aiokafka.consumer.group_coordinator:Joined group 'test-group' (generation 2) with member_id aiokafka-0.8.0-028ddf32-7c85-40b1-bc79-ed78fb49e304
worker_1     | INFO:aiokafka.consumer.group_coordinator:Elected group leader -- performing partition assignments using roundrobin
worker_1     | INFO:aiokafka.consumer.group_coordinator:Successfully synced group test-group with generation 2
worker_1     | INFO:aiokafka.consumer.group_coordinator:Setting newly assigned partitions {TopicPartition(topic='decrease-by-one-letter', partition=0)} for group test-group
worker_1     | INFO:ris_4.worker.service:[RIS-4] Consumer for kafka on kafka:9092 starts.
```
2. У сусідньому терміналі передаємо початкове слово (скріпт надсилає його через `Apache Kafka`):
```bash
(venv) ➜  ris_4 git:(master) ✗ make send word=hello_world
docker-compose run ris-image python -m ris_4.scripts.send_word hello_world
Creating ris_4_ris-image_run ... done
INFO:ris_4.worker.client:[RIS-4] Sending "hello_world" to kafka worker
```
3. Дивимося на результат взаємодії двох серверів через `gRPC` та `Apache Kafka`:
```bash
worker_1     | INFO:ris_4.worker.service:[RIS-4] Kafka consumer get: msg=ConsumerRecord(topic='decrease-by-one-letter', partition=0, offset=6, timestamp=1671062631536, timestamp_type=0, key=None, value=b'hello_world', checksum=None, serialized_key_size=-1, serialized_value_size=11, headers=())
worker_1     | INFO:ris_4.worker.service:[RIS-4] Decrease "hello_world" by one letter: new_word='hello_worl'
worker_1     | INFO:ris_4.server.client:[RIS-4] Sending "hello_worl" to gRPC server
grpc_1       | INFO:ris_4.server.service:[RIS-4] Get gRPC request: request.word='hello_worl'
grpc_1       | INFO:ris_4.server.service:[RIS-4] Decrease "hello_worl" by one letter: new_word='hello_wor'
grpc_1       | INFO:ris_4.worker.client:[RIS-4] Sending "hello_wor" to kafka worker
worker_1     | INFO:ris_4.worker.service:[RIS-4] Kafka consumer get: msg=ConsumerRecord(topic='decrease-by-one-letter', partition=0, offset=7, timestamp=1671062631559, timestamp_type=0, key=None, value=b'hello_wor', checksum=None, serialized_key_size=-1, serialized_value_size=9, headers=())
worker_1     | INFO:ris_4.worker.service:[RIS-4] Decrease "hello_wor" by one letter: new_word='hello_wo'
worker_1     | INFO:ris_4.server.client:[RIS-4] Sending "hello_wo" to gRPC server
grpc_1       | INFO:ris_4.server.service:[RIS-4] Get gRPC request: request.word='hello_wo'
grpc_1       | INFO:ris_4.server.service:[RIS-4] Decrease "hello_wo" by one letter: new_word='hello_w'
grpc_1       | INFO:ris_4.worker.client:[RIS-4] Sending "hello_w" to kafka worker
worker_1     | INFO:ris_4.worker.service:[RIS-4] Kafka consumer get: msg=ConsumerRecord(topic='decrease-by-one-letter', partition=0, offset=8, timestamp=1671062631579, timestamp_type=0, key=None, value=b'hello_w', checksum=None, serialized_key_size=-1, serialized_value_size=7, headers=())
worker_1     | INFO:ris_4.worker.service:[RIS-4] Decrease "hello_w" by one letter: new_word='hello_'
worker_1     | INFO:ris_4.server.client:[RIS-4] Sending "hello_" to gRPC server
grpc_1       | INFO:ris_4.server.service:[RIS-4] Get gRPC request: request.word='hello_'
grpc_1       | INFO:ris_4.server.service:[RIS-4] Decrease "hello_" by one letter: new_word='hello'
grpc_1       | INFO:ris_4.worker.client:[RIS-4] Sending "hello" to kafka worker
worker_1     | INFO:ris_4.worker.service:[RIS-4] Kafka consumer get: msg=ConsumerRecord(topic='decrease-by-one-letter', partition=0, offset=9, timestamp=1671062631593, timestamp_type=0, key=None, value=b'hello', checksum=None, serialized_key_size=-1, serialized_value_size=5, headers=())
worker_1     | INFO:ris_4.worker.service:[RIS-4] Decrease "hello" by one letter: new_word='hell'
worker_1     | INFO:ris_4.server.client:[RIS-4] Sending "hell" to gRPC server
grpc_1       | INFO:ris_4.server.service:[RIS-4] Get gRPC request: request.word='hell'
grpc_1       | INFO:ris_4.server.service:[RIS-4] Decrease "hell" by one letter: new_word='hel'
grpc_1       | INFO:ris_4.worker.client:[RIS-4] Sending "hel" to kafka worker
worker_1     | INFO:ris_4.worker.service:[RIS-4] Kafka consumer get: msg=ConsumerRecord(topic='decrease-by-one-letter', partition=0, offset=10, timestamp=1671062631609, timestamp_type=0, key=None, value=b'hel', checksum=None, serialized_key_size=-1, serialized_value_size=3, headers=())
worker_1     | INFO:ris_4.worker.service:[RIS-4] Decrease "hel" by one letter: new_word='he'
worker_1     | INFO:ris_4.server.client:[RIS-4] Sending "he" to gRPC server
grpc_1       | INFO:ris_4.server.service:[RIS-4] Get gRPC request: request.word='he'
grpc_1       | INFO:ris_4.server.service:[RIS-4] Decrease "he" by one letter: new_word='h'
grpc_1       | INFO:ris_4.worker.client:[RIS-4] Sending "h" to kafka worker
worker_1     | INFO:ris_4.worker.service:[RIS-4] Kafka consumer get: msg=ConsumerRecord(topic='decrease-by-one-letter', partition=0, offset=11, timestamp=1671062631622, timestamp_type=0, key=None, value=b'h', checksum=None, serialized_key_size=-1, serialized_value_size=1, headers=())
worker_1     | INFO:ris_4.worker.service:[RIS-4] Decrease "h" by one letter: new_word=''
worker_1     | INFO:ris_4.worker.service:[RIS-4] Finish! new_word=''
```
