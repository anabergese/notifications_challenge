*Notification System Architecture*
The product department requires a system to notify them when a customer requests assistance from a bot. The bot will send an HTTP request containing the topic (either "sales" or "pricing") and a description of the problem. The system needs to expose an API endpoint to receive this request and forward it to the appropriate channel (Slack or Email). The architecture must support future expansion to include more topics and channels.


*How to run the app* 
    Go to the main folder of the project.
    Run: `docker compose up`.
