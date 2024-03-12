import logging
from pathlib import Path

import pandas as pd
from kafka import KafkaConsumer
from kafka.errors import KafkaError

logger = logging.getLogger()

def main():
    messages = []
    maxlen = 4
    column_name = "test_event_data"
    try:
        consumer = KafkaConsumer(
            "topic1",
            group_id="g1",
            bootstrap_servers=["enter_the_ip_address_of_the_kafka_producer:9092"],
            enable_auto_commit=True
        )
    except KafkaError as e:
        logger.exception(e, exc_info=True)
    else:
        while(True):
            try:
                for message in consumer:
                    if len(messages) >= maxlen:
                        logger.info(f"converting {maxlen} messages to dataframe")
                        df = pd.DataFrame({column_name: messages})
                        print(f"DataFrame : {df}")
                        messages.clear()
                        messages.append(message.value.decode("utf-8"))
                    else:
                        msg = message.value.decode("utf-8")
                        print(f"message : {msg}")
                        messages.append(message.value.decode("utf-8"))
                        print(f"messages : {messages}")
            except KafkaError as e:
                logger.exception(e, exc_info=True)
            finally:
                consumer.close()
    finally:
        consumer.close()