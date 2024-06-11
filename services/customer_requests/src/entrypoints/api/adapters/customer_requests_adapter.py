class CustomerRequestsAdapter:
    def process_request(self, topic: str, description: str):
        # Create a customer request object
        if topic == "Sales":
            return {"topic": topic, "description": description, "channel": "Slack"}
        elif topic == "Pricing":
            return {"topic": topic, "description": description, "channel": "Email"}
        else:
            return { "error": "Unknown topic. Try again."}