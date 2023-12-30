| Type of coupling    | Example                                                                                      | Mitigation pattern                                            |
|---------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| Domain coupling     | Order Processor depends on Warehouse and Payment microservices for reserving stock and taking payment | Reduce the number of downstream dependencies, use asynchronous communication, apply back pressure |
| Temporal coupling   | Order Processor makes a synchronous HTTP call to Warehouse, which needs to be available at the same time | Use asynchronous communication, implement retries and circuit breakers, use sagas for distributed transactions |
| Common coupling     | Multiple microservices access shared static reference data from the same database              | Avoid sharing mutable data, use data replication or caching, use event sourcing |
| Content coupling    | Warehouse service directly updates the order table in the Order service’s database, bypassing its logic and exposing its internal structure | Encapsulate the internal data and logic of a microservice, use well-defined interfaces, respect the boundaries of microservices |
| External coupling   | Order Processor relies on an external service that is outside its control, such as a payment gateway or a shipping API | Use adapters or gateways to isolate the external dependency, use feature toggles to switch between different providers, use stubs or mocks for testing |







