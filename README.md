# 🎉 DEMO Python Rabbitmq
RabbitMQ is a message broker software that facilitates communication between applications by sending and receiving messages. It supports AMQP and is open-source, reliable, scalable, and portable.

![version](https://img.shields.io/badge/version-1.0-blue)
![rating](https://img.shields.io/badge/rating-★★★★★-yellow)
![uptime](https://img.shields.io/badge/uptime-100%25-brightgreen)

### ⚓ Developer Tool

- [RabbitMQ](https://github.com/natthasath/docker-rabbitmq)

### 🐋 Hello World
___

- _shell 1_ - `Start Consumer`

```shell
# python receive.py
[*] Waiting for messages. To exit press CTRL+C
```

- _shell 2_ - `Start Producer`

```shell
# python send.py
[x] Sent 'Hello World!'
```

- _shell 1_ - `Consumer Receive Message`

```shell
[x] Received 'Hello World!'
```

### 🐇 Work Queues
___

`Round Robin Dispatching` is a basic **_load balancing technique_** in which messages are evenly distributed across multiple consumers. In RabbitMQ, this can be achieved by declaring a queue as a "Work Queue" with **_multiple consumers_** listening to the same queue. Each time a message is sent to the queue, RabbitMQ will deliver it to the next available consumer. This way, messages are dispatched to the consumers in a round-robin fashion, ensuring a balanced distribution of the workload.

`Message acknowledgment` is the process of confirming that a message has been successfully processed and can be safely removed from the queue. Acknowledge mode can be either manual or automatic. In manual acknowledge mode, the consumer must explicitly acknowledge each message after processing it. In automatic acknowledge mode, messages are automatically acknowledged as soon as they are delivered to the consumer. The choice of acknowledge mode depends on the specific requirements of your application.

- _shell 1_ - `Start Worker`

```shell
# python worker.py
[*] Waiting for messages. To exit press CTRL+C
```

- _shell 2_ - `Start Worker`

```shell
# python worker.py
[*] Waiting for messages. To exit press CTRL+C
```

- _shell 3_ - `Start Task`

```shell
# python task.py First message
# python task.py Second message
# python task.py Third message
# python task.py Fourth message
# python task.py Fifth message
```

- _shell 1_ - `Worker Receive Message`

```shell
# python worker.py
[*] Waiting for messages. To exit press CTRL+C
[x] Received 'First message'
[x] Received 'Third message'
[x] Received 'Fifth message'
```

- _shell 2_ - `Worker Receive Message`

```shell
# python worker.py
[*] Waiting for messages. To exit press CTRL+C
[x] Received 'Second message'
[x] Received 'Fourth message'
```

### 🐽 Publish/Subscribe
___

`Exchanges` is the component responsible for routing messages to queues. When a message is published to RabbitMQ, it is sent to an exchange, which then routes the message to one or more queues based on rules defined by bindings.

- _`Direct exchange`_ : routes messages to queues based on an exact match between the routing key and the binding key.
- _`Fanout exchange`_ : broadcasts all messages it receives to all queues bound to it, ignoring routing keys.
- _`Topic exchange`_ : routes messages to queues based on a pattern matching between the routing key and binding key.
- _`Headers exchange`_ : routes messages to queues based on header attributes instead of routing keys.

`Bindings` are the connections between exchanges and queues. A binding specifies the rules for how messages are routed from the exchange to the queues. When a message is published to an exchange, RabbitMQ will evaluate the bindings and route the message to one or more queues based on the routing key and binding rules.

- _shell 1_ - `Start Consumer`

```shell
# python receive_logs.py > log/exchange.log
[*] Waiting for logs. To exit press CTRL+C
```

- _shell 2_ - `Start Producer`

```shell
# python send_log.py
[x] Sent 'info: Hello World!'
```

### 🕸️ Routing
___

- _shell 1_ - `Start Consumer`

```shell
# python receive_logs_direct.py info warning error > log/exchange_direct.log
[*] Waiting for logs. To exit press CTRL+C
```

- _shell 2_ - `Start Producer`

```shell
# python send_log_direct.py error "Run. Run. Or it will explode."
[x] Sent 'error':'Run. Run. Or it will explode.
```

### 🐼 Topic
___

- _shell 1_ - `Start Consumer (Receive all logs)`

```shell
# python receive_logs_topic.py "#"
[*] Waiting for logs. To exit press CTRL+C
```

- _shell 1_ - `Start Consumer (Receive all logs from facility)`

```shell
# python receive_logs_topic.py "kern.*"
[*] Waiting for logs. To exit press CTRL+C
```

- _shell 1_ - `Start Consumer (Receive all logs only critical)`

```shell
# python receive_logs_topic.py "*.critical"
[*] Waiting for logs. To exit press CTRL+C
```

- _shell 2_ - `Start Producer`

```shell
# python send_log_topic.py "kern.critical" "A critical kernel error"
[x] Sent 'kern.critical':'A critical kernel error'
```

### 🐬 RPC
___

- _shell 1_ - `Start RPC Server`

```shell
# python rpc_server.py
[x] Awaiting RPC requests
```

- _shell 2_ - `Start RPC Client`

```shell
# python rpc_client.py
[x] Requesting fib(30)
```