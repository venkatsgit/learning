| Type                    | Description                                                             | Pros                                             | Cons                                                | Example                                       |
|-------------------------|-------------------------------------------------------------------------|--------------------------------------------------|-----------------------------------------------------|-----------------------------------------------|
| Synchronous blocking    | A microservice makes a call to another microservice and waits for the response | Simple and familiar, suitable for situations where the result is needed before further processing | Temporal coupling, increased latency, long call chains | HTTP request/response with REST API             |
| Asynchronous nonblocking | A microservice sends a call to another microservice and does not wait for the response | Temporal decoupling, suitable for long-running processes or parallel calls | Increased complexity, requires message brokers or common data sources, potential message loss or duplication | AMQP, Kafka, or file-based communication      |
| Request-response         | A microservice sends a request to another microservice asking for something to be done and expects a response | Explicit and direct, suitable for data retrieval or commands | Coupling between requester and responder, requires error handling and retries | REST, gRPC, or message queues                  |
| Event-driven            | A microservice emits events that other microservices can consume and react to | Loose coupling, suitable for broadcasting facts or state changes | Implicit and indirect, requires event sourcing and tracking, eventual consistency | Pub/sub, event streams, or webhooks            |
|Asynchronous nonblocking|	The client does not wait for a response from the service. The service sends a response when it is ready.	|Scalable and resilient. Avoids blocking threads and resources.|	More complex and requires coordination.	|HTTP/HTTPS with callbacks or promises.|




