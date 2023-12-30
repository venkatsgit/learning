**Pitfalls of Monoliths**

    1. Scalability Challenges:
    Monoliths can be challenging to scale as a whole, often requiring duplication of the entire application.
    2. Technology Homogeneity:
    Limited flexibility in choosing technologies, as the entire monolith must adhere to a single tech stack.
    3. Difficulty in Deployment:
    Updating a monolith may necessitate redeploying the entire application, leading to downtime.
    
**Advantages of Microservices	Pain Points of Microservices**

| Technology Heterogeneity   | Developer Experience Challenges        |
|---------------------------|----------------------------------------|
| Resilience                 | Technology Overload                    |
| Scalability               | Increased Costs in the Short-Term       |
| Continuous Delivery       | Reporting Complexity                   |
| Ease of Deployment         | Monitoring and Troubleshooting          |
| Organizational Alignment   | Security Concerns                       |
| Composability              | Testing Complexity                     |
| Latency in Distributed Operations                                        |
| Data Consistency Challenges 


**Pain points**

**Developer Experience:**

Challenge: An increased number of microservices may impact developer experience, especially with resource-intensive runtimes like JVM.
Consideration: "Developing in the cloud" is an extreme solution; limiting the scope of developer work or providing a collective ownership model can be more practical.

**Technology Overload:**

Challenge: The abundance of new technologies labelled as "microservice-friendly" can lead to complexity and a potential technology overload.
Balancing Act: Balancing technology diversity against the associated costs is crucial; gradual adoption allows for better understanding and management.

**Cost:**

Challenge: Short-term cost increase due to additional processes, computers, network, and supporting software.
Consideration: Microservices may not be cost-effective for organizations solely focused on cost reduction; benefits lie in reaching more customers or parallel development.

**Reporting:**

Challenge: Microservices break up a monolithic database, complicating reporting across scattered data.
Adaptation: Modern reporting approaches, such as streaming or centralized reporting databases, can address challenges but may require new technology adoption.

**Monitoring and Troubleshooting:**

Challenge: Microservices introduce complexity in monitoring individual service instances and understanding failure impact.
Solutions: Explore concepts of observability; consider distributed systems observability for detailed insights.

**Security:**

Challenge: Increased data flow between services over networks raises security concerns.
Mitigation: Implement robust measures to protect data in transit and secure microservice endpoints; address challenges discussed in Chapter 11.

**Testing:**

Challenge: End-to-end testing in microservices becomes complex, resource-intensive, and yields diminishing returns.
Adaptation: Explore new testing approaches like contract-driven testing, testing in production, and progressive delivery techniques discussed in Chapter 8.

**Latency:**

Challenge: Microservices, with distributed processing, may result in increased latency due to serialization, transmission, and deserialization.
Incremental Measurement: Undertake microservice migration incrementally, measure the impact on latency, and ensure acceptable performance.

**Data Consistency:**

Challenge: Transition from a monolithic system to distributed microservices raises issues of data consistency.
Adoption Approach: Gradually decompose the application, adopting concepts like sagas and eventual consistency; assess impact incrementally in production.
