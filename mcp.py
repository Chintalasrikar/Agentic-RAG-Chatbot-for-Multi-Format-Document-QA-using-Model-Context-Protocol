import queue
import uuid
import logging

# MCP message queue
mcp_queue = queue.Queue()

# Send MCP message
def send_mcp_message(sender, receiver, msg_type, payload):
    message = {
        "sender": sender,
        "receiver": receiver,
        "type": msg_type,
        "trace_id": str(uuid.uuid4()),
        "payload": payload
    }
    mcp_queue.put(message)
    logging.info(f"MCP Message Sent: {message}")
    return message

# Receive MCP message
def receive_mcp_message(receiver):
    while not mcp_queue.empty():
        message = mcp_queue.get()
        if message["receiver"] == receiver:
            logging.info(f"MCP Message Received: {message}")
            return message
    return None