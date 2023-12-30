## SOA

Service-oriented architecture (SOA) is a design approach where multiple services collaborate as separate operating system processes, communicating across a network. Originating to address challenges in large, monolithic applications, SOA aims to enhance software reusability and facilitate maintenance or rewriting by replacing services without changing semantics significantly. Despite its sensible core idea, there's a lack of consensus on effective SOA implementation. 
**Issues arise from communication protocols, vendor middleware, and unclear guidance on service granularity.** **The microservices approach evolved from real-world use, offering a specific and improved approach within the broader context of SOA**. Unlike some SOA implementations, microservices emphasize avoiding coupling to databases and enable independent service deployment.

## Microservices 

### Principles

##### Independent deployability
- having the ability to make changes to a microservice, deploy those changes, and release them to users without needing to deploy any other microservices simultaneously
-  To achieve this, microservices must be loosely coupled, requiring explicit, well-defined, and stable contracts between them.

##### Modeled Around a Business Domain
 - Modeling microservices around business domains, like product catalogue or user authentication, makes it easier to introduce new features. To achieve this, microservices should own their data, avoiding shared databases. Keeping services as end-to-end slices of business functionality, rather than layered technical structures, promotes efficient changes.
 - layered technical architecture
   - Presentation Layer: The user interface and user interaction components are in this layer. It deals with the presentation and display of information.
   -  Application Layer: Also known as the business logic layer, it contains the core logic and processing rules of the application. It handles the business-specific functionality.
   -  Data Layer: This layer involves data storage, retrieval, and management. It includes databases or other data storage systems
  - In a layered technical structure, these layers are often owned by different teams, each specializing in a particular layer. While this design provides a clear separation of concerns, it can lead to challenges when changes in functionality span multiple layers, requiring coordination across different teams for even minor updates. This can result in increased complexity, slower development cycles, and challenges in adapting to changing business needs.

##### Flexibility and Autonomy
  - Microservices aim to provide flexibility and autonomy to development teams. Owning their data allows microservices to make independent decisions about how data is stored, queried, and manipulated without impacting other services. Teams can choose databases and storage mechanisms that best suit their specific requirements.
   
