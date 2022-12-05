



AWS Certified Cloud Practitioner

AWS certified Solutions Architect - Associate 
AWS certified SysOps Administrator - Associate 
AWS Certified Developer - Associate

AWS Certified Solutions Architect - Professional 
AWS Certified DevOps Engineer - Professional

AWS Certified Advanced Networking - Specialty 
AWS Certified Data Analytics - Specialty 
AWS Certified Database - Specialty 
AWS Certified Machine Learning - Specialty
AWS Certified Security - Specialty 
AWS Certified SAP on AWS - Specialty 


* https://explore.skillbuilder.aws/learn/course/internal/view/elearning/12483/aws-certified-cloud-practitioner-official-practice-question-set-clf-c01-english
* https://www.koenig-solutions.com/AWS
* https://www.whizlabs.com/aws-certified-cloud-practitioner/
* https://portal.tutorialsdojo.com/courses/free-aws-certified-cloud-practitioner-practice-exams-sampler/
* https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/
* https://www.udemy.com/course/aws-certified-cloud-practitioner-practice-test/
* https://www.awsboy.com/aws-practice-exams/
* https://aws.amazon.com/fr/certification/certified-cloud-practitioner/
* https://aws.amazon.com/fr/training/ramp-up-guides/
* https://www.youtube.com/watch?v=lDEFXtpEhLY
* https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf



# 1. Intro

Amazon Web Services offers a broad set of global cloud-based products including compute, storage, databases, analytics, networking, mobile, developer tools, management tools, IoT, security, and enterprise applications: on-demand, available in seconds, with pay-as-you-go pricing. 

From data warehousing to deployment tools, directories to content delivery, over 200 AWS services are available. New services can be provisioned quickly, without the upfront capital expense. This allows enterprises, start-ups, small and medium-sized businesses, and customers in the public sector to access the building blocks they need to respond quickly to changing business requirements. 

AWS offers a massive range of services for every business, starting with basic elements, like compute, storage, and network security tools, through complex solutions like blockchain, machine learning, or artificial intelligence, and robot development platforms, all the way through very specialized tool sets, like video production management systems, and orbital satellites you can rent by the minute.

* client-server model
  - In computing, a client can be a web browser or desktop application that a person interacts with to make requests to computer servers. 
  - A server can be services such as Amazon Elastic Compute Cloud (Amazon EC2), a type of virtual server.

Cloud Computing
* Cloud computing is the on-demand delivery of compute power, database, storage, applications, and other IT resources through a cloud services platform via the Internet with pay-as-you-go pricing.
* Cloud Computing Models
  * (1) Infrastructure as a Service (IaaS)
    - basic building blocks for cloud IT (networking + computers + data storage)
  * (2) Platform as a Service (PaaS)
    - provide management of underlying infrastructure (hardware + operating systems)
    - you can focus on deployment and management of your applications
  * (3) Software as a Service (SaaS)
    - a completed product, end-user applications
* Deployment Model 
  - depends on required cloud application components, preferred resource, management tools, legacy IT infrastruture requirements
  * (1) cloud-based
    - fully deployed in the cloud and all parts of the application run in the cloud.
  * (2) on-premise (private cloud)
  * (3) hybrid
    - connect infrastructure and applications between cloud-based resources and existing resources that are not located in the cloud
    - between the cloud and existing on-premises infrastructure to extend, and grow, an organization's infrastructure into the cloud while connecting cloud resources to the internal system


Benefits of the AWS Cloud/6 advantages of cloud computing
* (1) Trade upfront/capital expense for variable expense.
  - Upfront expenses include data centers, physical servers, and other resources that you would need to invest in before using computing resources. 
  - Instead of investing heavily in data centers and servers before you know how you’re going to use them, you can pay only when you consume computing resources.
* (2) Benefit from massive economies of scale.
  - By using cloud computing, you can achieve a lower variable cost than you can get on your own. 
  - Because usage from hundreds of thousands of customers aggregates in the cloud, providers such as AWS can achieve higher economies of scale. Economies of scale translate into lower pay-as-you-go prices.
* (3) Stop guessing capacity.
  - With cloud computing, you don’t have to predict how much infrastructure capacity you will need before deploying an application. 
  - For example, you can launch Amazon Elastic Compute Cloud (Amazon EC2) instances when needed and pay only for the compute time you use. Instead of paying for resources that are unused or dealing with limited capacity, you can access only the capacity that you need, and scale in or out in response to demand. 
* (4) Increase speed and agility.
  - The flexibility of cloud computing makes it easier for you to develop and deploy applications.
  - This flexibility also provides your development teams with more time to experiment and innovate.
* (5) Stop spending money running and maintaining data centers.
  - Cloud computing in data centers often requires you to spend more money and time managing infrastructure and servers. 
  - A benefit of cloud computing is the ability to focus less on these tasks and more on your applications and customers.
* (6) Go global in minutes.
  - The AWS Cloud global footprint enables you to quickly deploy applications to customers around the world, while providing them with low latency.


# 2. Compute
Cloud Computing = on-demand delivery of IT resources (e.g. compute, networking, storage, analytics..) over the internet with pay-as-you-go pricing

Amazon Elastic Compute Cloud (EC2) provides secure, resizable compute capacity in the cloud as Amazon EC2 instances. 
- Multitenancy: sharing underlying hardware between virtual machines

Computer as a service (CaaS)

How Amazon EC2 works
* Launch: configuration (os, application server, applications, hardware), network security
* Connect
* Use

Instance Types
* General purpose
  - balance of compute, memory and networking resources 
  - e.g. web servers, code repositories, application servers, gaming servers, backend servers for enterprise applications, small and medium databases
  - an application in which the resource needs for compute, memory, and networking are roughly equivalent
* Compute Optimized 
  - e.g. gaming servers, HPC, scientific modeling
  - batch processing workloads
* Memory Optimized 
 - a high-performance database or a workload that involves performing real-time processing of a large amount of unstructured data
 - In computing, memory is a temporary storage area. It holds all the data and instructions that a central processing unit (CPU) needs to be able to complete actions. Before a computer program or application is able to run, it is loaded from storage into memory. This preloading process gives the CPU direct access to the computer program.
* Accelerated computing
  - e.g. floating point number calculations, graphics processing, data pattern matching
  - workloads such as graphics applications, game streaming, application streaming
  - utilize hardware accelerators or coprocessors
* Storage Optimized
  - high performance for locally stored data
  - workloads that require high, sequential read and write access to large datasets on local storage
  - workloads such as distributed file systems, data warehousing applications, and high-frequency online transaction processing (OLTP) systems
  - In computing, input/output operations per second (IOPS) is a metric that measures the performance of a storage device. Storage optimized instances are designed to deliver tens of thousands of low-latency, random IOPS to applications. 


Pricing
* (1) On-Demand 
  - pay for compute capacity by hour or second
  - ideal for short-term, spiky, irregular (unpredictable) workloads that cannot be interrupted. 
  - No upfront costs or minimum contracts apply (no long-term commitment). The instances run continuously until you stop them, and you pay for only the compute time you use.
  - ✔️ Sample use cases include developing and testing applications and running applications that have unpredictable usage patterns. 
  - ✗ not recommended for workloads that last a year or longer because these workloads can experience greater cost savings using Reserved Instances.
* (2) EC2 Savings Plans (66% discount compared to On-Demand)
  - Amazon EC2 Savings Plans enable you to reduce your compute costs by committing to a consistent amount of compute usage (measured in $/hour) for a 1-year or 3-year term.
  - Any usage up to the commitment is charged at the discounted plan rate. Any usage beyond the commitment is charged at regular On-Demand rates.
  - AWS Cost Explorer can analyze your Amazon EC2 usage over the past 7, 30, or 60 days. AWS Cost Explorer also provides customized recommendations for Savings Plans.
* (3) Reserved Instances (up to 72% discount)
  - Reserved Instances are a billing discount applied to the use of On-Demand Instances in your account. 
  - You can purchase Standard Reserved and Convertible Reserved Instances for a 1-year or 3-year term, and Scheduled Reserved Instances for a 1-year term.
  - Type:
    - 1) Standard RIs (72% discount) Customers have the flexibility to change the Availability Zone, the instance size, and networking type of their Standard Reserved Instances.
    - 2) Convertible RIs (66% discount) if you need additional flexibility, such as the ability to use different instance families, operating systems, or tenancies over the RI term
  - Payment Option:
    - 1) All Upfront: pay for the entire RI term with one upfront payment (largest discount)
    - 2) Partial Upfront: make a low upfront payment, then charged a discounted hourly rate
    - 3) No Upfront: no upfront payment and provides a discounted hourly rate
* (4) Spot Instances (90% discount)
  - ideal for workloads with flexible start and end times, or that can withstand interruptions. 
  - Spot Instances use unused Amazon EC2 computing capacity and offer you cost savings at up to 90% off of On-Demand prices.
  - Hourly price varies based upon the demand for the selected instance (not static).
  - Spot request is the price which customer is willing to pay for a specific Instance type in an Availability zone. When Spot Price exceeds the Spot request, Instance gets terminated.
  - ✔️ Applications that have flexible start and end times
  - ✔️ Applications that are only feasible at very low compute prices
  - ✔️ Users with urgent computing needs for large amounts of additional capacity
* (5) Dedicated Hosts (most expensive)
  - physical servers with Amazon EC2 instance capacity that is fully dedicated to your use
  - You can use your existing per-socket, per-core, or per-VM software licenses to help maintain license compliance. 
  - You can purchase On-Demand Dedicated Hosts and Dedicated Hosts Reservations. 


Scaling
- Scalability & Elasticity (how capacity can grow and shrink, based on business needs)
- peaking demand (max load) vs average utilization
- vertical scaling (resize the instance) horizontal scaling (launch new instances)
* Amazon EC2 Auto Scaling
    - (1) Dynamic scaling responds to changing demand. 
    - (2) Predictive scaling automatically schedules the right number of Amazon EC2 instances based on predicted demand.
* Auto Scaling group = minimum capacity -> desired capacity (+ scale as needed) = maximum EC2 instances
    -  desired capacity defaults to minimum capacity

Direct Traffic with Elastic Load Balancing ()
- the request comes in and goes to which EC2 instance, to ensure an even distribution of workload across EC2 instances? 
* ELB is the AWS service (load balancer) that automatically distributes incoming application traffic across multiple resources, such as Amazon EC2 instances. 

Messaging and Queuing (=placing messages into a buffer)
* tightly coupled architecture (monolithic application)
    - if a single component fails, other components fail, and possibly the entire application fails.
* loosely coupled architecture (microservices)
    - if a single component fails, the other components continue to work because they are communicating with each other. The loose coupling prevents the entire application from failing.
* Simple Queue Service: 
    - Using Amazon SQS, you can send, store, and receive messages between software components, at any volume, without losing messages or requiring other services to be available.
    - payload: date contained within a message
    - In Amazon SQS, an application sends messages into a queue. A user or service retrieves a message from the queue, processes it, and then deletes it from the queue.
* Simple Notification Service: a publish/subscribe service
    - Using Amazon SNS topics, a publisher publishes messages to subscribers (e.g. web servers, email addresses, AWS Lambda functions..)
    - Also, SNS can be used to fan out notifications to end users using mobile push, SMS, and email


EC2 = run virtual servers in the cloud
Serverless Compute Services 
  - code runs on servers, but no need to provision or manage these servers (focus on application than configuration..)
  - flexibility to scale serverless applications automatically
* AWS Lambda
    - upload code to Lambda function, configure a trigger, then the service waits for the trigger. Upon trigger detected, the code is automatically run in a managed environment.
    - application runtime < 15 minutes

* AWS Container Services 
    - Containers: a package of application's code and dependencies into a single object
    - Docker: a platform that uses operating system level virtualization to deliver software in containers
    - Containers run on top of EC2 instances
    - Container Orchestration Tools: manage your containers (ECS, EKS)
    * (1) Elastic Container Service (ECS)
        - a highly scalable, high-performance container management system that enables you to run and scale containerized applications on AWS
        - Amazon ECS supports Docker containers. Docker is a software platform that enables you to build, test, and deploy applications quickly. AWS supports the use of open-source Docker Community Edition and subscription-based Docker Enterprise Edition. With Amazon ECS, you can use API calls to launch and stop Docker-enabled applications.
    * (2) Elastic Kubernetes Service (Amazon EKS)
        - a fully managed service that you can use to run Kubernetes on AWS
        - Kubernetes is open-source software that enables you to deploy and manage containerized applications at scale. A large community of volunteers maintains Kubernetes, and AWS actively works together with the Kubernetes community. As new features and functionalities release for Kubernetes applications, you can easily apply these updates to your applications managed by Amazon EKS.
* AWS Fargate (alternative to EC2)
    - a serverless compute engine for containers. 
    - It works with both Amazon ECS and Amazon EKS. 

Summary
- host traditional applications, want full access to the underlying operating system --> EC2
- host short running functions, service-oriented or event driven applications and don't want to manage the underlying environment at all --> AWS Lambda. 
- run Docker container-based workloads on AWS,
    - 1.choose orchestration tool -> Amazon ECS or Amazon EKS
    - 2.choose platform -> run your containers on EC2 instances that you manage or in a serverless environment like AWS Fargate that is managed for you


# 3. Global Infrastrcture & Reliability

Global Infrastrcture
* to determine the right Region for your services, data, and applications:
  - (1) Compliance with data governance and legal requirements (location-specific data regulations)
  - (2) Proximity to your customers (get content to the customers faster)
  - (3) Available services within a Region (some new services require physical hardware build)
  - (4) Pricing

Region
* geographically isolated areas, a physical location
* Each AWS Region consists of multiple isolated and physically separate AZs within a geographic Region

Availability Zones (AZ)
* Availability Zone is one or more discrete data centers, each with redundant power, networking, and connectivity, housed in separate facilities.
* AZ is a fully isolated portion of the AWS global infrastructure.
* AZ is a single data center or a group of data centers within a Region, located tens of miles apart from each other        
  - (1) close enough to have low latency (the time between when content requested and received) between Availability Zones
  - (2) distant enough to reduce the chance that multiple AZs are affected, if a disaster occurs in one part of the Region
* AZs offer the ability to operate production applications and databases that are more highly available, fault tolerant, and scalable than would be possible from a single data center
* redundantly deploying your infrastructure in (at least) two different AZs in a Region
* Many of the AWS services run at the Region level.
e.g. Region: us-west-1, AZ: us-west-1a, us-west-1b, us-west-1c

Each Region is designed to be completely isolated from the other Regions. This achieves the greatest possible fault tolerance and stability. 
Each Availability Zone is isolated, but the AZs in a Region are connected through low-latency links. 
AWS provides you with the flexibility to place instances and store data within multiple geographic regions as well as across multiple AZs within each AWS Region. Each Availability Zone is designed as an independent failure zone. This means that AZs are physically separated within a typical metropolitan region and are located in lower risk flood plains (specific flood zone categorization varies by Region). In addition to discrete uninterruptible power supply (UPS) and onsite backup generation facilities, data centers located in different AZs are designed to be supplied by independent substations to reduce the risk of an event on the power grid impacting more than one AZ. AZs are all redundantly connected to multiple tier-1 transit providers.


Edge Location
- Caching copies of data closer to the customers all around the world uses the concept of Content Delivery Networks
* Amazon CloudFront
  - a content delivery service (CDN) that uses Edge Locations to help deliver data, video, applications, and APIs to customers around the world with low latency and high transfer speeds
  - It uses a network of edge locations to cache content and deliver content to customers all over the world. When content is cached, it is stored locally as a copy. (content: video files, photos, webpages..)
* Edge Location 
  - a site that Amazon CloudFront uses to store cached copies of your content closer to your customers for faster delivery
  - a data center that an AWS service uses to perform service-specific operations
  - AWS Edge locations run a Domain Name Service (DNS), Amazon Route 53, helping direct customers to the correct web locations with reliably low latency.
* AWS Outposts
  - A service that you can use to run AWS infrastructure within your own on-premises data center in a hybrid approach
  - AWS install a fully operational mini Region inside your own data center
  - owned and operated by AWS, using 100% of AWS functionality, but isolated within your own building

Origin: the server from which Amazon CloudFront gets your files


Provision AWS resources/Interact with services (via API calls)
* AWS Management Console
  - browser-based user interface
  - test environments, viewing AWS bills, viewing monitoring, working with other non technical resources
* AWS Command Line Interface (CLI) 
  - a unified tool to manage your AWS services
  - script/program the API calls, scriptable and repeatable
  - CLI allows you to make API calls using the terminal on your machine
  - CLI allows to automate the actions that your services and applications perform through scripts
* AWS Software Development Kits (SDK)
  - SDK allows you to interact with AWS resources through various programming languages
  - SKDs simplify using AWS services in your applications with an Application Program Interface (API) tailored to your programming language or platform
* other managed tools 
  - (1) AWS Elastic Beanstalk
    - provision Amazon EC2-based environments
    - provide code and configuration settings, and Elastic Beanstalk deploys the resources necessary to perform the following tasks: Adjust capacity, Load balancing, Automatic scaling, Application health monitoring.
  - (2) AWS CloudFormation
    - an infrastructure as code tool 
      - define a wide variety of AWS resources in a declarative way using CloudFormation templates (JSON or YAML text-based documents)
      - CloudFormation parses the template and provisions all the resources you defined in parallel
    - not limited to EC2-based solutions
    - AWS CloudFormation provisions your resources in a safe, repeatable manner, enabling you to frequently build your infrastructure and applications without having to perform manual actions. It determines the right operations to perform when managing your stack and rolls back changes automatically if it detects errors.


# 4. Networking
Virtual Private Cloud
* a networking service used to establish boundaries around your AWS resources
  - A VPC allows you to define your private IP range for your AWS resources, and you place things like EC2 instances and ELBs inside of your VPC
  - Amazon VPC enables you to provision an isolated section of the AWS Cloud. 
  - In this isolated section, you can launch resources in a virtual network that you define. 
  - Within a virtual private cloud (VPC), you can organize your resources into subnets.
* subnet
  - section of a VPC that can contain resources such as Amazon EC2 instances
  - chunks of IP addresses in your VPC that allow you to group resources together 

Connectivity
* Gateway
  * (1) Internet gateway (IGW)
    - a connection between a VPC and the internet, to allow public traffic from the internet to access your VPC
  * (2) Virtual private gateway
    - to access private resources in a VPC
    - virtual private network (VPN) connection encrypts/protects your internet traffic from all the other requests around it; (but still use a regular internet connection with bandwidth shared by many people using the internet)
* AWS Direct Connect
    - a dedicated private fiber connection between your data center and a VPC
    - reduce network costs, increase the amount of bandwidth

AWS has a wide range of tools that cover every layer of security: network hardening, application security, user identity, authentication and authorization, distributed denial-of-service or DDoS prevention, data integrity, encryption, etc.

Subnets
* In a VPC, subnets are separate areas that are used to group together resources.
* A subnet is a section of a VPC in which you can group resources based on security or operational needs. Subnets can be public or private. 

A packet is a unit of data sent over the internet or a network.
  - When a customer requests data from an application hosted in the AWS Cloud, this request is sent as a packet.


Network Access Control Lists (ACL)
* a virtual firewall that controls inbound and outbound traffic at the subnet level.
  - The VPC component that checks packet permissions, before a packet can enter into a subnet or exit from a subnet.
  - These permissions indicate who sent the packet and how the packet is trying to communicate with the resources in a subnet.
  - Default network ACL allows all inbound and outbound traffic.
* Stateless packet filtering
  - remember nothing and check packets that cross the subnet border each way: inbound and outbound

Security group
* a virtual firewall that controls inbound and outbound traffic for an Amazon EC2 instance
  - it checks packet permissions for an Amazon EC2 instance
  - By default, a security group denies all inbound traffic and allows all outbound traffic.
* Stateful packet filtering
  - remember previous decisions made for incoming packets


Global Networking
* Domain Name System (DNS) resolution 
  - it involves a customer DNS resolver communicating with a company DNS server
  - DNS resolution is the process of translating a domain name to an IP address
* Amazon Route 53: a DNS web service
  - It gives developers and businesses a reliable way to route end users to internet applications hosted in AWS.
  - (1) Amazon Route 53 connects user requests to infrastructure running in AWS (such as Amazon EC2 instances and load balancers). It can route users to infrastructure outside of AWS.
  - (2) Route 53 is able to manage the DNS records for domain names. You can register new domain names directly in Route 53. You can also transfer DNS records for existing domain names managed by other domain registrars. This enables you to manage all of your domain names within a single location.
  - Amazon Route 53 routing policy
    - 1) Simple routing policy: useful in case of single resource
    - 2) Geolocation: route traffic to the resources based upon user location
    - 3) Geoproximity: route traffic based upon location of resources 
    - 4) Failover routing policy: suitable for routing to a secondary resource only in case of failure in primary resource
    - 5) Latency routing policy: suitable for routing based upon lowest latency to the resources from user location
    - 6) Multivalue answer routing policy: suitable to respond with multiple (up to 8) records for any query made to Route 53
    - 7) Weighted routing policy: route traffic to multiple resources based upon weights defined


# 5. Storage & Databases

## 5.1. Storage
Storage: (1.)block (2.)object (3.)file

Instance Store
* block-level storage volumes (behave like physical hard drives)
* temporary block-level storage for an Amazon EC2 instance 
  - An instance store is disk storage that is physically attached to the host computer for an EC2 instance, and therefore has the same lifespan as the instance. 
  - When the instance is terminated, you lose any data in the instance store.

Amazon Elastic Block Store (EBS)
* a service that provides block-level storage volumes that you can use with Amazon EC2 instances
  - To create an EBS volume, you define the configuration (volume, size, type) and provision it. 
  - After you create an EBS volume, it can attach to an Amazon EC2 instance.
* You can take incremental backups of EBS volumes by creating Amazon EBS snapshots.
  - The first backup taken of a volume copies all the data. 
  - For subsequent backups, only the blocks of data that have changed since the most recent snapshot are saved. 


(1.) Block Storage
* delta update
  - Block storage breaks files down to small component parts. When you make an edit and save that change, the engine only updates the blocks where those bits live. 

(2.) Object Storage
* Each object consists of data, metadata, and a key.
  - Data might be an image, video, text document, or any other type of file. 
  - Metadata contains information about what the data is, how it is used, the object size, and so on. 
  - An object’s key is its unique identifier.
* When you modify a file in block storage, only the pieces that are changed are updated. When a file in object storage is modified, the entire object is updated.


Amazon Simple Storage Service (S3)
* Amazon S3 is a service that provides object-level storage. Amazon S3 stores data as objects in buckets.
  - Amazon S3 offers unlimited storage space. 
  - The maximum file size for an object is 5 TB.
  - When you upload a file to Amazon S3, you can set permissions to control visibility and access to it. 
  - You can also use the Amazon S3 versioning feature to track changes to your objects over time.
* Amazon S3 storage classes
  - When selecting an Amazon S3 storage class, consider these 2 factors:
    - How often you plan to retrieve your data
    - How available you need your data to be
* (1) Amazon S3 Standard
  - Designed for frequently accessed data
  - Stores data in a minimum of three Availability Zones
  - Amazon S3 Standard provides high availability for objects. This makes it a good choice for a wide range of use cases, such as websites, content distribution, and data analytics. Amazon S3 Standard has a higher cost than other storage classes intended for infrequently accessed data and archival storage.
* (2) Amazon S3 Standard-Infrequent Access (S3 Standard-IA)
  - Ideal for infrequently accessed but immediately available data
  - Similar to Amazon S3 Standard but has a lower storage price and higher retrieval price
  - Amazon S3 Standard-IA is ideal for data infrequently accessed but requires high availability when needed. Both Amazon S3 Standard and Amazon S3 Standard-IA store data in a minimum of three Availability Zones. Amazon S3 Standard-IA provides the same level of availability as Amazon S3 Standard but with a lower storage price and a higher retrieval price.
* (3) Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA)
  - Stores data in a single Availability Zone
  - Has a lower storage price than Amazon S3 Standard-IA
  - Compared to Amazon S3 Standard and Amazon S3 Standard-IA, which store data in a minimum of three Availability Zones, Amazon S3 One Zone-IA stores data in a single Availability Zone. This makes it a good storage class to consider if the following conditions apply: You want to save costs on storage; You can easily reproduce your data in the event of an Availability Zone failure.
* (4) Amazon S3 Intelligent-Tiering
  - Ideal for data with unknown or changing access patterns
  - Requires a small monthly monitoring and automation fee per object
  - In the Amazon S3 Intelligent-Tiering storage class, Amazon S3 monitors objects’ access patterns. If you haven’t accessed an object for 30 consecutive days, Amazon S3 automatically moves it to the infrequent access tier (Amazon S3 Standard-IA). If you access an object in the infrequent access tier, Amazon S3 automatically moves it to the frequent access tier (Amazon S3 Standard).
* (5) Amazon S3 Glacier Instant Retrieval
  - Works well for archived data that requires immediate access
  - Can retrieve objects within a few milliseconds
  - When you decide between the options for archival storage, consider how quickly you must retrieve the archived objects. You can retrieve objects stored in the Amazon S3 Glacier Instant Retrieval storage class within milliseconds, with the same performance as Amazon S3 Standard.
* (6) Amazon S3 Glacier Flexible Retrieval
  - Low-cost storage designed for data archiving
  - Able to retrieve objects within a few minutes to hours
  - Amazon S3 Glacier Flexible Retrieval is a low-cost storage class that is ideal for data archiving. For example, you might use this storage class to store archived customer records or older photos and video files.
* (7) Amazon S3 Glacier Deep Archive
  - Lowest-cost object storage class ideal for archiving
  - Able to retrieve objects within 12 hours
  - Amazon S3 Deep Archive supports long-term retention and digital preservation for data that might be accessed once or twice in a year. This storage class is the lowest-cost storage in the AWS Cloud, with data retrieval from 12 to 48 hours. All objects from this storage class are replicated and stored across at least three geographically dispersed Availability Zones.
* (8) Amazon S3 Outposts
  - Creates S3 buckets on Amazon S3 Outposts
  - Makes it easier to retrieve, store, and access data on AWS Outposts
  - Amazon S3 Outposts delivers object storage to your on-premises AWS Outposts environment. Amazon S3 Outposts is designed to store data durably and redundantly across multiple devices and servers on your Outposts. It works well for workloads with local data residency requirements that must satisfy demanding performance needs by keeping data close to on-premises applications.


Comparison between EBS and S3
* EBS
  - block storage
    - delta update (doing complex read, write, change functions)
  - sizes up to 16TB
  - survive termination of their EC2 instance
  - solid state by default, HDD options
* S3
  - object storage
    - write once/read many (using complete objects or only occasional changes)
  - unlimited storage, individual 5TB
  - web-enabled (each object has a URL for access control)
  - regionally distributed, 99.999 999 999% durable
  - no Amazon EC2 instances needed
  - cost efficient than EBS


(3.) File Storage
* Multiple clients (users, applications, servers..) can access data that is stored in shared file folders. In this approach, a storage server uses block storage with a local file system to organize files. Clients access data through file paths.
* File storage is ideal for use cases in which a large number of services and resources need to access the same data at the same time.

Amazon Elastic File System (EFS)
* a scalable file system used with AWS Cloud services and on-premises resources.
  - As you add and remove files, EFS grows and shrinks automatically. It can scale on demand to petabytes without disrupting applications. 


Comparing EBS and EFS
* EBS
  - An EBS volume stores data in a single Availability Zone. 
  - To attach an Amazon EC2 instance to an EBS volume, both the Amazon EC2 instance and the EBS volume must reside within the same Availability Zone.
  - block storage service for access by an EC2 instance but no capability of a share file access
* EFS 
  - EFS is a regional service. It stores data in and across multiple Availability Zones. 
  - The duplicate storage enables you to access data concurrently from all the Availability Zones in the Region where a file system is located. Additionally, on-premises servers can access Amazon EFS using AWS Direct Connect.
  - It is designed for shared file access and scaling to petabyte data store.



## 5.2. Database

Relational Databases
* data is stored in a way that relates it to other pieces of data.
* Relational databases use structured query language (SQL) to store and query data. 
  - This approach allows data to be stored in an easily understandable, consistent, and scalable way.

Nonrelational Databases (NoSQL databases)
* In a nonrelational database, you create tables. A table is a place where you can store and query data.
* Nonrelational databases use structures other than rows and columns to organize data. 
  - One type of structural approach for nonrelational databases is key-value pairs. With key-value pairs, data is organized into items (keys), and items have attributes (values, different features of your data). 
  - In a key-value database, you can add or remove attributes from items in the table at any time. Additionally, not every item in the table has to have the same attributes. 


Amazon Relational Database Service (RDS)
* a service that enables you to run relational databases in the AWS Cloud.
* Amazon RDS is a managed service that automates tasks such as hardware provisioning, database setup, patching, and backups. 
  - With these capabilities, you can spend less time completing administrative tasks and more time using data to innovate your applications. 
  - You can integrate Amazon RDS with other services to fulfill your business and operational needs, such as using AWS Lambda to query your database from a serverless application.
* Amazon RDS provides a number of different security options. 
  - Many Amazon RDS database engines offer encryption at rest (protecting data while it is stored) and encryption in transit (protecting data while it is being sent and received).
* Amazon RDS is available on six database engines: Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle Database, Microsoft SQL Server
* Amazon Aurora
  - Amazon Aurora is an enterprise-class relational database. It is compatible with MySQL and PostgreSQL relational databases. It is up to 5 times faster than standard MySQL databases and up to 3 times faster than standard PostgreSQL databases.
  - Amazon Aurora helps to reduce your database costs by reducing unnecessary input/output (I/O) operations, while ensuring that your database resources remain reliable and available. 
  - Consider Amazon Aurora if your workloads require high availability. It replicates 6 copies of your data across 3 Availability Zones and continuously backs up your data to Amazon S3.


Amazon DynamoDB
* a key-value database service. It delivers single-digit millisecond performance at any scale.
  - Serverless
    - You do not have to provision, patch, or manage servers. also do not have to install, maintain, or operate software.
  - Automatic Scaling
    - As the size of your database shrinks or grows, DynamoDB automatically scales to adjust for changes in capacity while maintaining consistent performance. This makes it a suitable choice for use cases that require high performance while scaling.

Comparing Amazon RDS and DynamoDS
* RDS
  - need server
  - automatic high availability; recovery provided
  - customer ownership of data, schema, network
  - need complex relational joins
* DynamoDS
  - use key-value pairs, requires no advanded schema
  - serverless
  - massive throughput capabilities (scaling up to 10 trillion requests per day)
  - PB size potential
  - Granular API access
  - good for look-up tables


Amazon Redshift
* a fully managed, petabyte-scale data warehousing service that you can use for big data analytics. 
  - solution for big data Business Intelligence
  - It offers the ability to collect data from many sources and helps you to understand relationships and trends across your data.


AWS Database Migration Service (DMS) 
* DMS enables you to migrate relational databases, nonrelational databases, and other types of data stores.
  - With AWS DMS, you move data between a source database and a target database. The source and target databases can be of the same type or different types. During the migration, your source database remains operational, reducing downtime for any applications that rely on the database. 
* Other usecases:
  - Development and test database migrations
    - Enabling developers to test applications against production data without affecting production users
  - Database consolidation
    - Combining several databases into a single database
  - Continuous replication
    - Sending ongoing copies of your data to other target sources instead of doing a one-time migration


Additional Database Services
* (1) Amazon DocumentDB
  - a document database service that supports MongoDB workloads. (MongoDB is a document database program.)
* (2) Amazon Neptune
  - a graph database service. 
  - use Neptune to build and run applications that work with highly connected datasets, such as recommendation engines, fraud detection, and knowledge graphs.
* (3) Amazon Quantum Ledger Database (QLDB)
  - a ledger database service. 
  - use QLDB to review a complete history of all the changes that have been made to your application data.
* (4) Amazon Managed Blockchain
  - a service that you can use to create and manage blockchain networks with open-source frameworks. 
  - Blockchain is a distributed ledger system that lets multiple parties run transactions and share data without a central authority.
* (5) Amazon ElastiCache
  - a service that adds caching layers on top of your databases to help improve the read times of common requests. 
  - It supports two types of data stores: Redis and Memcached.
* (6) Amazon DynamoDB Accelerator (DAX)
  - an in-memory cache for DynamoDB. 
  - It helps improve response times from single-digit milliseconds to microseconds.


# 6. Security

Shared Responsibility Model
* AWS controls security OF the cloud and customers control security IN the cloud.
* Customers are responsible for the security of everything that they create and put in the AWS Cloud.
  - customer data; platform, applications, identity and access management; operating systems, network and firewall configuration; client-side data encryption; server-side encryption; networking traffic protection
  - When using AWS services, the customer maintains complete control over your content. You are responsible for managing security requirements for your content, including which content you choose to store on AWS, which AWS services you use, and who has access to that content. You also control how access rights are granted, managed, and revoked.
  - The security steps that you take will depend on factors such as the services that you use, the complexity of your systems, and your company’s specific operational and security needs. Steps include selecting, configuring, and patching the operating systems that will run on Amazon EC2 instances, configuring security groups, and managing user accounts. 
* AWS is responsible for security of the cloud.
  - software; compute, storage, database, networking; hardware/AWS global infrastructure; regions, availability zones, edge locations
  - AWS operates, manages, and controls the components at all layers of infrastructure. This includes areas such as the host operating system, the virtualization layer, and even the physical security of the data centers from which services operate. 
  - AWS is responsible for protecting the global infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure includes AWS Regions, Availability Zones, and edge locations.
  - AWS manages the security of the cloud, specifically the physical infrastructure that hosts your resources, which include: 
    - Physical security of data centers
    - Hardware and software infrastructure
    - Network infrastructure
    - Virtualization infrastructure
  - Although you cannot visit AWS data centers to see this protection firsthand, AWS provides several reports from third-party auditors. These auditors have verified its compliance with a variety of computer security standards and regulations.


Penetration Testing
* An authorized simulated cyberattack on a computer system, performed to evaluate the security of the system
* AWS customers can carry out penetration tests against their AWS infrastructure without prior approval for the services: 
  1. Amazon EC2 instances, NAT Gateways, and Elastic Load Balancers
  2. Amazon RDS
  3. Amazon CloudFront
  4. Amazon Aurora
  5. Amazon API Gateways
  6. AWS Fargate
  7. AWS Lambda and Lambda Edge functions
  8. Amazon Lightsail resources
  9. Amazon Elastic Beanstalk environments


## 6.1. User Permissions and Access
AWS Identity and Access Management (IAM)
* IAM enables you to manage access to AWS services and resources securely.
* IAM gives you the flexibility to configure access based on your company’s specific operational and security needs by using a combination of IAM features: (1) IAM users, groups, and roles (2) IAM policies (3) Multi-factor authentication

AWS account Root User
* The root user is accessed by signing in with the email address and password that you used to create your AWS account.
* It has complete access to all the AWS services and resources in the account.
  - Create an AWS account (root user identity). Do not use the root user for everyday tasks. 
  - Use root user to create your first IAM user and assign it permissions to create other users.
  - Then, continue to create other IAM users, and access those identities for performing regular tasks throughout AWS. Only use the root user when you need to perform a limited number of tasks that are only available to the root user, e.g. changing your root user email address and changing your AWS support plan.


IAM Users
* An IAM user is an identity that you create in AWS. 
  - It represents the person or application that interacts with AWS services and resources. It consists of a name and credentials.
  - By default, when you create a new IAM user in AWS, it has no permissions associated with it.
- We recommend that you create individual IAM users for each person who needs to access AWS. Even if you have multiple employees who require the same level of access, you should create individual IAM users for each of them. This provides additional security by allowing each IAM user to have a unique set of security credentials.


IAM Policies
* An IAM policy is a document that allows or denies permissions to AWS services and resources.
* IAM policies enable you to customize users’ levels of access to resources.
* You can apply IAM policies to IAM users, groups, or roles, but not AWS account root user.
- Follow the security principle of least privilege when granting permissions. 
- Prevent users or roles from having more permissions than needed to perform their tasks. 


IAM Groups
* An IAM group is a collection of IAM users. 
* When you assign an IAM policy to a group, all users in the group are granted permissions specified by the policy.


IAM Roles
* An IAM role is an identity that you can assume to gain temporary access to permissions.  
* Before an IAM user, application, or service can assume an IAM role, they must be granted permissions to switch to the role. 
* When someone assumes an IAM role, they abandon all previous permissions that they had under a previous role and assume the permissions of the new role. 


Multi-Factor Authentication (MFA)
- First, when a user signs in to an AWS website, they enter their IAM user ID and password.
- Next, the user is prompted for an authentication response from their AWS MFA device. This device could be a hardware security key, a hardware device, or an MFA application on a device such as a smartphone.


## 6.2. AWS Organizations
* use AWS Organizations to consolidate and manage multiple AWS accounts within a central location.
* When you create an organization, AWS Organizations automatically creates a root, which is the parent container for all the accounts in your organization. 
* Service Control Policies (SCPs)
  - In AWS Organizations, you can centrally control permissions for the accounts in your organization by using SCPs. SCPs enable you to place restrictions on the AWS services, resources, and individual API actions that users and roles in each account can access.
  - You can apply SCPs to the organization root, an individual member account, or an OU. An SCP affects all IAM users, groups, and roles within an account, including the AWS account root user.
* Consolidated billing is another feature of AWS Organizations. 

Organizational units (OUs)
* In AWS Organizations, you can group accounts into OUs to make it easier to manage accounts with similar business or security requirements. 
  - When you apply a policy to an OU, all the accounts in the OU automatically inherit the permissions specified in the policy.  
* By organizing separate accounts into OUs, you can more easily isolate workloads or applications that have specific security requirements.
  

Describe security policies at a basic level.

## 6.3. Compliance
AWS Cloud Compliance enables you to understand the robust controls in place at AWS to maintain security and data protection in the cloud.

AWS Audit Manager
* used for auditing AWS usage and building audit reports for risk & compliance


AWS Artifact
* a service that provides on-demand access to AWS security and compliance reports and select online agreements. 
* AWS Artifact consists of two main sections:
  - (1) AWS Artifact Agreements
    - Suppose that your company needs to sign an agreement with AWS regarding your use of certain types of information throughout AWS services. You can do this through AWS Artifact Agreements. 
    - In AWS Artifact Agreements, you can review, accept, and manage agreements for an individual account and for all your accounts in AWS Organizations. Different types of agreements are offered to address the needs of customers who are subject to specific regulations, such as the Health Insurance Portability and Accountability Act (HIPAA).
  - (2) AWS Artifact Reports
    - Suppose that a member of your company’s development team is building an application and needs more information about their responsibility for complying with certain regulatory standards. You can advise them to access this information in AWS Artifact Reports.
    - AWS Artifact Reports provide compliance reports from third-party auditors. These auditors have tested and verified that AWS is compliant with a variety of global, regional, and industry-specific security standards and regulations. AWS Artifact Reports remains up to date with the latest reports released. You can provide the AWS audit artifacts to your auditors or regulators as evidence of AWS security controls.
    - Each report includes a description of its contents and the reporting period for which the document is valid. 


Customer Compliance Center
* Customer Compliance Center contains resources to help you learn more about AWS compliance. 
  - (1) In the Customer Compliance Center, you can read customer compliance stories to discover how companies in regulated industries have solved various compliance, governance, and audit challenges.
  - (2) You can also access compliance whitepapers and documentation on topics such as:
    - AWS answers to key compliance questions
    - An overview of AWS risk and compliance
    - An auditing security checklist
  - (3) Additionally, the Customer Compliance Center includes an auditor learning path. This learning path is designed for individuals in auditing, compliance, and legal roles who want to learn more about how their internal operations can demonstrate compliance using the AWS Cloud.


Denial-of-Service attacks (DoS)
* A DoS attack is a deliberate attempt to make a website or application unavailable to users.
Distributed Denial-of-Service attacks (DDoS)
* In a DDoS attack, multiple sources are used to start an attack that aims to make a website or application unavailable. 
  - This can come from a group of attackers, or even a single attacker. The single attacker can use multiple infected computers (bots) to send excessive traffic to a website or application.

AWS Shield
* a service that protects applications against DDoS attacks. 
* AWS Shield provides two levels of protection: 
  - (1) Standard 
    - AWS Shield Standard automatically protects all AWS customers at no cost. It protects your AWS resources from the most common, frequently occurring types of DDoS attacks. 
    - As network traffic comes into your applications, AWS Shield Standard uses a variety of analysis techniques to detect malicious traffic in real time and automatically mitigates it. 
  - (2) Advanced
    - AWS Shield Advanced is a paid service that provides detailed attack diagnostics and the ability to detect and mitigate sophisticated DDoS attacks. 
    - It also integrates with other services such as Amazon CloudFront, Amazon Route 53, and Elastic Load Balancing. Additionally, you can integrate AWS Shield with AWS WAF by writing custom rules to mitigate complex DDoS attacks.


Additional AWS security services
* (1) AWS Key Management Service (AWS KMS)
  * KMS enables to perform encryption operations through the use of cryptographic keys.
    - A cryptographic key is a random string of digits used for locking (encrypting) and unlocking (decrypting) data. 
    - With AWS KMS, you can choose the specific levels of access control that you need for your keys. For example, you can specify which IAM users and roles are able to manage keys. Alternatively, you can temporarily disable keys so that they are no longer in use by anyone.
* (2) AWS WAF
  * a web application firewall that lets you monitor network requests that come into your web applications
  * WAF works together with Amazon CloudFront and an Application Load Balancer.
  * WAF uses a web access control list (ACL) to protect your AWS resources
* (3) Amazon Inspector
  * Amazon Inspector helps to improve the security and compliance of applications by running automated security assessments.
    - It checks applications for security vulnerabilities and deviations from security best practices, such as open access to Amazon EC2 instances and installations of vulnerable software versions. 
    - After Amazon Inspector has performed an assessment, it provides you with a list of security findings. The list prioritizes by severity level, including a detailed description of each security issue and a recommendation for how to fix it. 
    - However, AWS does not guarantee that following the provided recommendations resolves every potential security issue. Under the shared responsibility model, customers are responsible for the security of their applications, processes, and tools that run on AWS services.
* (4) Amazon GuardDuty
  * a service that provides intelligent threat detection for your AWS infrastructure and resources
  * It identifies threats by continuously monitoring the network activity and account behavior within your AWS environment.
    - After GuardDuty enabled for your AWS account, GuardDuty begins monitoring your network and account activity. You do not have to deploy or manage any additional security software. GuardDuty then continuously analyzes data from multiple AWS sources, including VPC Flow Logs and DNS logs. 
    - If any threats detected, you can review detailed findings (recommended steps for remediation) from the AWS Management Console. You can also configure AWS Lambda functions to take remediation steps automatically in response to GuardDuty’s security findings.



# 7. Monitoring & Analytics
Monitoring: observing systems, collecting metrics, and then using data to make decisions

Amazon CloudWatch
* a web service that enables you to monitor and manage various metrics in real time, and configure alarm actions based on data from those metrics
  - CloudWatch uses metrics to represent the data points for your resources. 
  - AWS services send metrics to CloudWatch. 
  - CloudWatch then uses these metrics to create graphs automatically that show how performance has changed over time. 
* CloudWatch alarms
  - CloudWatch alarms automatically perform actions if the value of your metric has gone above or below a predefined threshold.
* CloudWatch Dashboard
  - CloudWatch dashboard feature enables you to access all the metrics for your resources from a single location
* Benefits:
  - access to all your metrics from a central location
  - gain visibility into your applications, infrastructure, and services
  - reduce mean time to resolution (MTTR), and improve total cost of ownership (TCO)
  - drive insights to optimize applications and operational resources


AWS CloudTrail
* AWS CloudTrail records API calls for your account, including identity of the API caller, the time of the API call, the source IP address of the API caller, etc.
* With CloudTrail, you can view a complete history of user activity and API calls for your applications and resources.
* Events are typically updated in CloudTrail within 15 minutes after an API call.
* CloudTrail Insights
   - An optional feature allows CloudTrail to automatically detect unusual API activities in your AWS account. 


AWS Trusted Advisor
* a web service that inspects your AWS environment and provides real-time recommendations in accordance with AWS best practices
* Trusted Advisor compares its findings to AWS best practices in 5 categories:
  - (1) Cost Optimization includes checks for unused or idle resources that could be eliminated and provide cost savings.
  - (2) Performance includes checks for high-utilization EC2 instances. (checks for service limits and overutilized instances)
  - (3) Security includes checks that help you to review your permissions and identify which AWS security features to enable.
  - (4) Fault Tolerance includes checks to help improve your applications’ availability and redundancy.
  - (5) Service Limits
* AWS Trusted Advisor dashboard
  - When you access the Trusted Advisor dashboard on the AWS Management Console, you can review completed checks for cost optimization, performance, security, fault tolerance, and service limits.
    - The green check indicates the number of items for which it detected no problems.
    - The orange triangle represents the number of recommended investigations.
    - The red circle represents the number of recommended actions.


# 8. Pricing & Support

AWS Free Tier
* AWS Free Tier enables you to begin using certain services without having to worry about incurring costs for the specified period. 
* Always Free
  - AWS Lambda allows 1 million free requests and up to 3.2 million seconds of compute time per month. 
  - Amazon DynamoDB allows 25 GB of free storage per month
* 12 Months Free (following the initial sign-up date to AWS)
  - specific amounts of Amazon S3 Standard Storage
  - thresholds for monthly hours of Amazon EC2 compute time
  - amounts of Amazon CloudFront data transfer out
* Trials (short-term free trial offers start from the date you activate a particular service)
  - Amazon Inspector offers a 90-day free trial. 
  - Amazon Lightsail (a service that enables you to run virtual private servers) offers 750 free hours of usage over a 30-day period.

AWS pricing
* AWS offers a range of cloud computing services with pay-as-you-go pricing
  - (1) Pay for what you use (without requiring long-term contracts or complex licensing)
  - (2) Pay less when you reserve
    - Some services offer reservation options that provide a significant discount compared to On-Demand Instance pricing.
  - (3) Pay less with volume-based discounts when you use more
    - Some services offer tiered pricing, so the per-unit cost is incrementally lower with increased usage.
* AWS Pricing Calculator
  - AWS Pricing Calculator explores AWS services and creates an estimate for the cost of your use cases on AWS.
  - group: You can organize your AWS estimates by groups that you define.
  - link: When you have created an estimate, you can save it and generate a link to share it with others.


AWS Billing & Cost Management dashboard
* pay your AWS bill, monitor your usage, and analyze and control your costs
  - Compare your current month-to-date balance with the previous month, and get a forecast of the next month based on current usage.
  - View month-to-date spend by service.
  - View Free Tier usage by service.
  - Access Cost Explorer and create budgets.
  - Purchase and manage Savings Plans.
  - Publish AWS Cost and Usage Reports.


Consolidated Billing
- AWS Organizations, a service that enables you to manage multiple AWS accounts from a central location. 
- AWS Organizations also provides the option for consolidated billing.
* The consolidated billing feature of AWS Organizations enables you to receive a single bill for all AWS accounts in your organization.
  - The default maximum number of accounts allowed for an organization is 4, but you can contact AWS Support to increase your quota, if needed.
* Benefits:
  - review itemized charges incurred by each account
  - share bulk/volume discount pricing, Savings Plans, and Reserved Instances across the accounts in your organization


AWS Budgets
* In AWS Budgets, you can create budgets to plan your service usage, service costs, and instance reservations.
  - The information in AWS Budgets updates 3 times a day.
  - This helps you to accurately determine how close your usage is to your budgeted amounts or to the AWS Free Tier limits.
  - You can also set custom alerts when your usage exceeds (or is forecasted to exceed) the budgeted amount.
* Budget Name, Budge Type (Cost/Usage), Current/Budgeted/Forecasted


AWS Cost Explorer
* AWS Cost Explorer is a tool that enables you to visualize, understand, and manage your AWS costs and usage over time.
  - AWS Cost Explorer includes a default report of the costs and usage for your top five cost-accruing AWS services. 
  - You can apply custom filters and groups to analyze your data.


Comparison
- AWS Cost Explorer helps users to view graph displays of cost of your billing data and analyze them & get a forecast for likely spends for the next 12 months. The scenario is more to do with clients getting a cost estimate of different AWS services before they move to AWS cloud
- AWS Budgets helps clients to plan their service usage, service costs and get informed alerts when the costs reach a certain threshold
- AWS pricing calculator can estimate costs that will incur for various AWS services that the client wishes to use. The pricing calculator guides the user through a set of well defined service parameters.


AWS Support
* AWS offers 4 different Support plans to help you troubleshoot issues, lower costs, and efficiently use AWS services. 
* (1) Basic
  - access to whitepapers, documentation, and support communities
  - contact AWS for billing questions and service limit increases
  - limited selection of AWS Trusted Advisor checks
  - you can use the AWS Personal Health Dashboard (a tool that provides alerts and remediation guidance when AWS is experiencing events that may affect you)
* (2/3/4) [Developer, Business, Enterprise](https://aws.amazon.com/premiumsupport/plans/)
  - unrestricted number of technical support cases
  - pay-by-the-month pricing, no long-term contracts
  * (2) Developer
    - Best practice guidance
    - Client-side diagnostic tools
    - Building-block architecture support, which consists of guidance for how to use AWS offerings, features, and services together
  * (3) Business
    - Use-case guidance to identify AWS offerings, features, and services that can best support your specific needs
    - All AWS Trusted Advisor checks
    - Limited support for third-party software, such as common operating systems and application stack components
  * (4) Enterprise
    - Application architecture guidance, which is a consultative relationship to support your company’s specific use cases and applications
    - Infrastructure event management: A short-term engagement with AWS Support that helps your company gain a better understanding of your use cases. This also provides your company with architectural and scaling guidance.
    - Technical Account Manager (TAM)
      - Enterprise Support plan
      - TAM provide guidance, architectural reviews, and ongoing communication with your company as you plan, deploy, and optimize your applications


AWS Marketplace
* a digital catalog that includes thousands of software listings from independent software vendors. 
  - You can use AWS Marketplace to find, test, and buy software that runs on AWS. 
  - For each listing in AWS Marketplace, you can access detailed information on pricing options, available support, and reviews from other AWS customers. You can also explore software solutions by industry and use case.
* Categories
  - Business Applications, Data & Analytics, DevOps, Infrasturecture Software, Internet of Things, Machine Learning, Migration, Security


# 9. Migration & Innovation

AWS Cloud Adoption Framework (CAF)
- CAF organizes guidance into six areas of focus (Perspectives). Each Perspective addresses distinct responsibilities.
- Business, People, and Governance Perspectives focus on business capabilities; Platform, Security, and Operations Perspectives focus on technical capabilities.
* AWS CAF Action Plan: helps guide your organization for cloud migration
* (1) Business Perspective ensures that IT aligns with business needs and that IT investments link to key business results.
  - Use the Business Perspective to create a strong business case for cloud adoption and prioritize cloud adoption initiatives. Ensure that your business strategies and goals align with your IT strategies and goals.
  - Common roles: Business managers, Finance managers, Budget owners, Strategy stakeholders
* (2) People Perspective supports development of an organization-wide change management strategy for successful cloud adoption.
  - Use the People Perspective to evaluate organizational structures and roles, new skill and process requirements, and identify gaps. This helps prioritize training, staffing, and organizational changes.
  - Common roles: Human resources, Staffing, People managers
* (3) Governance Perspective focuses on the skills and processes to align IT strategy with business strategy. This ensures that you maximize the business value and minimize risks.
  - Use the Governance Perspective to understand how to update the staff skills and processes necessary to ensure business governance in the cloud. Manage and measure cloud investments to evaluate business outcomes.
  - Common roles: Chief Information Officer (CIO), Program managers, Enterprise architects, Business analysts, Portfolio managers
* (4) Platform Perspective includes principles and patterns for implementing new solutions on the cloud, and migrating on-premises workloads to the cloud.
  - Use a variety of architectural models to understand and communicate the structure of IT systems and their relationships. Describe the architecture of the target state environment in detail.
  - Common roles in the Platform Perspective include: Chief Technology Officer (CTO), IT managers, Solutions architects
* (5) Security Perspective ensures that the organization meets security objectives for visibility, auditability, control, and agility. 
  - Use the AWS CAF to structure the selection and implementation of security controls that meet the organization’s needs.
  - Common roles: Chief Information Security Officer (CISO), IT security managers, IT security analysts
* (6) Operations Perspective helps you to enable, run, use, operate, and recover IT workloads to the level agreed upon with your business stakeholders.
  - Define how day-to-day, quarter-to-quarter, and year-to-year business is conducted. Align with and support the operations of the business. The AWS CAF helps these stakeholders define current operating procedures and identify the process changes and training needed to implement successful cloud adoption.
  - Common roles: IT operations managers, IT support managers

- Security Perspective also helps you to identify areas on non-compliance and plan ongoing security initiatives.
- Governance Perspective helps you to identify and implement best practices for IT governance and support business processes with technology.
- Operations Perspective focuses on operating and recovering IT workloads to meet the requirements of your business stakeholders.
- Business Perspective helps you to move from a model that separates business and IT strategies into a business model that integrates IT strategy.


Migration Strategies
* (1) Rehosting/lift-and-shift
  - moving applications without changes
  - In the scenario of a large legacy migration, in which the company is looking to implement its migration and scale quickly to meet a business case, the majority of applications are rehosted.  
* (2) Replatforming/lift, tinker, and shift
  - making a few cloud optimizations to realize a tangible benefit. 
  - Optimization is achieved without changing the core architecture of the application.
* (3) Refactoring/re-architecting
  - reimagining how an application is architected and developed by using cloud-native features. 
  - Refactoring is driven by a strong business need to add features, scale, or performance that would otherwise be difficult to achieve in the application’s existing environment.
* (4) Repurchasing
  - moving from a traditional license to a software-as-a-service model. (moving to a different product)
  - A business might choose to implement the repurchasing strategy by migrating from a customer relationship management (CRM) system to Salesforce.com.
* (5) Retaining
  - keeping applications that are critical for the business in the source environment. 
  - This might include applications that require major refactoring before they can be migrated, or, work that can be postponed until a later time.
* (6) Retiring
  - removing applications that are no longer needed.


AWS Snow Family
* a collection of physical devices that help to physically transport up to exabytes of data into and out of AWS
* AWS Snow Family is composed of AWS Snowcone, AWS Snowball, and AWS Snowmobile. 
  - These devices offer different capacity points, and most include built-in computing capabilities. AWS owns and manages the Snow Family devices and integrates with AWS security, monitoring, storage management, and computing capabilities. 
* (1) AWS Snowcone is a small, rugged, and secure edge computing and data transfer device. 
  - It features 2 CPUs, 4 GB of memory, and 8 TB of usable storage.
* (2) AWS Snowball
  - Snowball Edge Storage Optimized devices are well suited for large-scale data migrations and recurring transfer workflows, in addition to local computing with higher capacity needs. 
    - Storage: 80 TB of hard disk drive (HDD) capacity for block volumes and Amazon S3 compatible object storage, and 1 TB of SATA solid state drive (SSD) for block volumes. 
    - Compute: 40 vCPUs, and 80 GiB of memory to support Amazon EC2 sbe1 instances (equivalent to C5).
  - Snowball Edge Compute Optimized provides powerful computing resources for use cases such as machine learning, full motion video analysis, analytics, and local computing stacks. 
    - Storage: 42-TB usable HDD capacity for Amazon S3 compatible object storage or Amazon EBS compatible block volumes and 7.68 TB of usable NVMe SSD capacity for Amazon EBS compatible block volumes. 
    - Compute: 52 vCPUs, 208 GiB of memory, and an optional NVIDIA Tesla V100 GPU. Devices run Amazon EC2 sbe-c and sbe-g instances, which are equivalent to C5, M5a, G3, and P3 instances.
* (3) AWS Snowmobile
  - an exabyte-scale data transfer service used to move large amounts of data to AWS. 
  - You can transfer up to 100 petabytes of data per Snowmobile, a 45-foot long ruggedized shipping container, pulled by a semi trailer truck.


Innovation with AWS
* When examining how to use AWS services, it is important to focus on the desired outcomes. You are properly equipped to drive innovation in the cloud if you can clearly articulate the following conditions: 
  - The current state
  - The desired state
  - The problems you are trying to solve
* Serverless applications
  - With AWS, serverless refers to applications that don’t require you to provision, maintain, or administer servers. You don’t need to worry about fault tolerance or availability. AWS handles these capabilities for you.
    - AWS Lambda is an example of a service that you can use to run serverless applications. If you design your architecture to trigger Lambda functions to run your code, you can bypass the need to manage a fleet of servers.
  - Building your architecture with serverless applications enables your developers to focus on their core product instead of managing and operating servers.
* Artificial intelligence
  - AWS offers a variety of services powered by artificial intelligence (AI). 
    - Convert speech to text with Amazon Transcribe.
    - Discover patterns in text with Amazon Comprehend.
    - Identify potentially fraudulent online activities with Amazon Fraud Detector.
    - Build voice and text chatbots (conversational interfaces) with Amazon Lex.
* Machine learning
  - Traditional machine learning (ML) development is complex, expensive, time consuming, and error prone. 
    - AWS offers Amazon SageMaker to remove the difficult work from the process and empower you to build, train, and deploy ML models quickly. 
  - You can use ML to analyze data, solve complex problems, and predict outcomes before they happen.


Amazon Textract is a machine learning service that automatically extracts text and data from scanned documents.

AWS DeepRacer is an autonomous 1/18 scale race car that you can use to test reinforcement learning models.

Amazon Augmented AI (A2I) provides built-in human review workflows for common machine learning use cases, such as content moderation and text extraction from documents. With Amazon A2I, you can also create your own workflows for machine learning models built on Amazon SageMaker or any other tools.
  Amazon Augmented AI enables you to build the workflows that are required for human review of machine learning predictions.

# 10. The Cloud Journey

AWS Well-Architected Framework
* AWS Well-Architected Framework helps you understand how to design and operate reliable, secure, efficient, and cost-effective systems in the AWS Cloud. It provides a way for you to consistently measure your architecture against best practices and design principles and identify areas for improvement.
* Well-Architected Framework is based on five pillars: 
* (1) Operational excellence
  - Operational excellence is the ability to run and monitor systems (gain insights into their operations) to deliver business value and to continually improve supporting processes and procedures.
  - Design principles for operational excellence in the cloud include performing operations as code, annotating documentation, anticipating failure, and frequently making small, reversible changes.
* (2) Security
  - Security is the ability to protect data/information, systems, and assets while delivering business value through risk assessments and mitigation strategies; and using cloud technologies to improve the security of your workloads.
  - When considering the security of your architecture, apply these best practices:
    - Automate security best practices when possible.
    - Apply security at all layers.
    - Protect data in transit and at rest.
* (3) Reliability
  - Reliability is the ability of a system to do the following:
    - Perform its intended functions consistently and correctly
    - Recover from infrastructure or service disruptions
    - Dynamically acquire computing resources to meet demand
    - Mitigate disruptions such as misconfigurations or transient network issues
  - Reliability includes testing recovery procedures, scaling horizontally to increase aggregate system availability, and automatically recovering from failure.
* (4) Performance efficiency
  - Performance efficiency is the ability to use computing resources efficiently to meet system requirements and to maintain that efficiency as demand changes and technologies evolve. 
  - Evaluating the performance efficiency of your architecture includes experimenting more often, using serverless architectures, and designing systems to be able to go global in minutes.
* (5) Cost optimization
  - Cost optimization is the ability to run systems to deliver business value at the lowest price point. 
  - Cost optimization includes adopting a consumption model, analyzing and attributing expenditure, and using managed services to reduce the cost of ownership.




# 11. Whizlabs Practice Test

- AWS Config is used to audit and monitor configuration changes. AWS Config is used for evaluating configuration on the resources deployed in AWS cloud.
- AWS License Manager provisions & tracks license usage across multiple AWS accounts & also on-premises environment. It helps to send an alert to an Administrator when license usage exceeds the limit.
- AWS Service Catalog can be used to create & deploy portfolio of products within AWS infrastructure.


Amazon Elastic Compute Cloud (Amazon EC2) SpotFleet



- AWS Certificate Manager can be used to store & provision SSL/TLS certificates. It is integrated with AWS resources like Amazon Elastic Load Balancer. SSL/TLS certificate can be directly imported from AWS certificate manager to Amazon Elastic Load Balancer.
- AWS CloudHSM is a managed hardware security model for generating and managing encryption keys on the AWS cloud. AWS CloudHSM can be used for offloading SSL processing for web servers. In this case, SSL processing is done on AWS CloudHSM instead of web servers which reduces load on web servers.
- AWS Secrets Manager can be used to implement secrets keys (password) rotation policy for secrets stored. It can also be used to manage & retrieve credentials/secrets which an application can use during its lifecycle.
- AWS Systems Manager Parameter Store can be used to store configuration data and passwords in encrypted or plain text.
- AWS KMS is a managed service for encrypting data.



Networking & Autherication
- Amazon Cognito User Pools is a managed service which can be used to manage user authentication to mobile applications. It can scale up to millions of users. It supports direct user sign-in as well as federated users using social and enterprise identity providers.
- Amazon Cognito Identity Pools are used to provide privilege credentials for accessing AWS services. Amazon Cognito User pools are used for authenticating users while identity pools will provide authorization for accessing AWS resources.
- AWS Single Sign-On is best suited for authenticating employees for accessing AWS services.
- AWS IAM is used to control access to AWS services or resources.


Detect anormalty
- AWS Detective is a persistent machine learning-driven service that automatically collates log data from all AWS resources. This log data is then applied into machine learning algorithms to derive data patterns between AWS services and resources, graph theory and statistical analysis. This information allows the user to proactively visualize their AWS environment from a security standpoint, thereby allowing them to quickly and efficiently conduct security investigations when they occur. (keep track of data behaviors between AWS services to detect anomalies)
- AWS Macie primarily matches and discovers sensitive data such as personally identifiable information (PII). 
- AWS Shield is a Distributed Denial of Service (DDoS) protection service that applies to applications running in the AWS environment.
- Amazon CloudWatch Anomaly Detection is a machine learning feature limited to Amazon CloudWatch metrics.


Amazon Dev Pay


Security
- Network ACL can be additionally configured on subnet level to control traffic in & out of the VPC.
- VPC Flow Logs will capture information about IP traffic in & out of VPC. This will not be used for controlling purposes.
- Web Application Firewall (WAF) can be configured to protect web applications from common security threats. It can be deployed on devices such as Amazon CloudFront, Application Load Balancer and Amazon API Gateway.
- Security Groups are attached at instance level & not at the subnet level.


Code
- AWS CodeCommit is a managed source control service. It can be used as a data store to store source code, binaries, scripts, HTML pages and images which are accessible over the internet. CodeCommit encrypts files in transit and at rest, which fulfills the additional client requirement (high confidentiality & security) mentioned in the question. Also, CodeCommit works well with Git tools and other existing CI/CD tools.
- AWS CodeDeploy is a deployment service that automates application deployments to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services.
- AWS CodeStar provides a unified user interface, enabling you to manage your software development activities in one place easily. With AWS CodeStar, you can set up your entire continuous delivery toolchain in minutes, allowing you to start releasing code faster. AWS CodeStar makes it easy for your whole team to work together securely, allowing you to manage access and add owners, contributors, and viewers to your projects easily. However, this question asks for the service to store the source code. AWS CodeStar is improper because it is a software development management tool rather than a source control service.
- AWS CodePipeline is a managed service for automation of delivery pipeline for application updates.


- Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. It does not guarantee the quality of connectivity between the organizations on-premise infrastructure and the AWS cloud build. The data KDS collects is available in milliseconds to enable real-time analytics use cases such as real-time dashboards, real-time anomaly detection, dynamic pricing, and more.
- Amazon Kinesis makes it easy to collect, process, and analyze real-time, streaming data to get timely insights and react quickly to new information.
- Amazon Kinesis Data Firehose is used to load streaming data into various destinations like data lakes, data stores and analytics tools. However, the service does not guarantee link quality between the organization’s on-premise infrastructure and the AWS cloud.


- Amazon QuickSight is a fully-managed service that allows for insightful business intelligence reporting with creative data delivery methods, including graphical and interactive dashboards. QuickSight includes machine learning that allows users to discover inconspicuous trends and patterns on their datasets.
- Amazon Redshift service is a data warehouse and will not meet the requirements of interactive dashboards and dynamic means of delivering reports.
- Amazon CloudWatch dashboards are used to monitor AWS system resources and infrastructure services, though they are customizable and present information graphically.
- Amazon Athena is a serverless query service that allows for easy data analysis (BigData) in Amazon S3 by using standard SQL.


Amazon S3 Transfer Acceleration enables fast, easy and secure transfers of files over long distances between your client and your Amazon S3 bucket.



# 12. AWS Services (Whitepaper)


**Analytics**
Amazon Athena
* analyze data in S3 using SQL
* no need for ETL (extract, transform, load) jobs

Amazon Kinesis
* collect, process and analyze real-time streaming data
* Data Firehouse
  - load streaming data into data stores (S3, Redshift, Elaticsearch, Splunk) and analytics tools
* Data Analytics
  - analyze streaming data, gain actionable insights and respond to your business and customer needs in real time (using SQL, Java)
* Data Streams
  - capture gigabytes of data per second from sources (e.g. website clickstreams, database event streams, finanicial transcations, social media feed, IT logs, location-tracking events)
* Video Steams
  - stream video from connected devices

Amazon Redshift
* cloud data warehouse
* fast, simple, cost-effective to analyze petabyte data using SQL or BI (biz intelligence) tools

Amazon QuickSight
* a fast, cloud-powered business intelligence (BI) service to deliver insights
* dashboard (browser, mobile devices)

Amazon Data Pipeline
* a web service to process and move data between different AWS compute and storage services, and on-premises data sources, at specified intervals.

Amazon Glue
* a extract, transform, and load service

AWS Lake Formation
* a secure data lake service
Data Lake: a centralized, curated, and secured repository that stores all the data, in its original form and prepared for analysis.


**Financial Management**
AWS Cost Explorer
* an interface to visualize, understand and manage AWS costs and usage over time
* create customer reports

AWS Budgets
* set custome budges that alert when costs or usage exceed (forcasted to exceed)
* set RI utilization or coverage targets and alert when utilization drops below threshold


**Compute**
Amazon Lightsail
* easiest way to launch and manage a virtual private server with AWS. 
* Lightsail plans include everything you need to jumpstart your project – a virtual machine, SSD- based storage, data transfer, DNS management, and a static IP address – for a low, predictable price.

Amazon Elastic Compute Cloud (EC2)
* a web service to provide secure, resizable compute capacity

Amazon Elastic Beanstalk
* deploy and scale web applications and services developed with Java, .NET, PHP, Python, Node.js, Ruby, Go, Docker on servers such as Apache, Nginx, Passenger and Internet Information Services (IIS).

AWS Fargate
* a compute engine to run containers without managing servers or clusters
* two modes: (1) Fargate launch type (2) EC2 launch type

AWS Lambda
* run code withpuy provisioning or managing servers

AWS Outposts
* bring native AWS services, infrastructure and operating models to virtually any data center, co-location space or on-premises facility.

**Container**
Amazon Elastic Container Registry
* a fully-managed Docker container registry
* integrate with ECS

Amazon Elastic Container Service (ECS)
* container orchestration service (Docker)

Amazon Elastic Kubernetes Service (EKS)
* deploy, manage, and scale containerized applications using Kubernetes

**Database**
Amazon Aurora
* a rational database engine
  
Amazon DynamoDB
* a key-value and document database

Amazon ElastiCache
* a web service tp deploy, operate, and scale an in-memory cache
* support 2 open-source in-memory caching engines: Redis, Memcached

Amazon Relational Database

**Developer Tool**
AWS CodeArtifact: a artifact repository service to store, publish and share software packages
AWS CodeBuild: a build service to compile source code, run tests, and produces software packages
AWS CodeCommit: a source control service to host private Git repositories
AWS CodeDeploy: automate code deployments to any instance (EC2, and instances running on premises)
AWS CodePipeline: a continuous delivery service that automates build, test and deploy phases of the release process
AWS CodeStar
* enable to quickly develop, build, and deploy application on AWS
* a unified user interface (set up CD toolchain), project management dashboard (JIRA)

AWS Fault Injection Simulator
* run fault injection experiments to improve application's performance, observability and resiliency
Fault Injection experiments: used in chaos engineering, stressing an application in testing or production environments by creating disruptive events (e.g. sudden increase in CPU or memory consumption), observe how the system responds, and implement improvements. 


**Front-End Web & Mobile Services**
AWS Amplify: a mobile backend that can be integrated with iOS, Andriod, web, React Native frontends


**Machine Learning**
Amazon CodeGuru: recommendations to improve code quality, idetify most expesive line of code
Amazon Comprehend: NLP
Amazon Fraud Detector: identify potentially (online) fraudulent activity
Amazon Kendra: search
Amazon Lex: conversational interfaces (~ Alexa)
Amazon Rekognition: image and video analysis
Amazon SageMaker: AutoML
Amazon Textract: OCR + table understanding (text and data from scanned doc)
Amazon Trascribe: speech recognition
Amazon Translate: neural machine translation


**Management and Governance**
Amazon CloudWatch
* monitor and manage operational health
* provide logs, metrics and events
* set alarms

AWS CloudFormation
* create and manage a collection of related AWS resources, provision and update them with templates

AWS CloudTrail
* web service to record API calls and deliver log files

AWS Config
* provide an AWS resource inventory, config history and config change notifications

AWS Service Catalog
* ceate and centrally manage catalogs of IT services that approved for use on AWS
* consistent governance and meet compliance requirements (enable users to deploy only the approved IT services thet need)

AWS System Manager
* give visibility and control of infrastructure on AWS
* view operational data from multiple AWS services
* group resources

AWS Trusted Advisor
* online resource to help you reduce cost, increase performance and improve security
* real-time guidance to help you provision your resources following AWS best practices

AWS Personal Health Dashboard
* provide alerts and remediation guidance when AWS is experiencing events that might affect you

AWS Managed Services
* ongoing management of AWS infrastructure reduce operational overhead and risk 
* automate actibities (change requests, monitoring, patch management, security, backup services and ...)

AWS License Manager
* manage license

**Migration and Transfer**
AWS Snow Family
* snowcone
* snowball
* snowmobile
* data transfer service, edge computing, edge storage, data migration/transfer

AWS Transfer Family
* file transfers directly into and out Amazon S3 or Amazon EFS

**Network and Content Delivery**
Amazon CloudFront
* a content delivery network service
* deliver data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment

Amazon Route 53
* a cloud Domain Name System (DNS) web service
* route end users to Internet applications by translating human readable names into numeric IP addresses(IPv4, IPv6)

Amazon VPC
* provision a logically isolated section of AWS Cloud where you can launch AWS resources in a virtual network that you define
- you have complete control over the virtual networking environment (selection of IP address, creation of subnets, configuration of route tables and network gateways)
- customize the network configuration for your VPC
  - You can create a public- facing subnet for your web servers that has access to the Internet, and place your backend systems, such as databases or application servers, in a private-facing subnet with no Internet access.
  - You can leverage multiple layers of security (including security groups and network access control lists) to help control access to EC2 instances in each subnet
- You can create a hardware virtual private network (VPN) connection between your corporate data center and your VPC and leverage the AWS Cloud as an extension of your corporate data center.

AWS Direct Connect
* a dedicated network connection from your premises to AWS

AWS Global Accelerator
* a networking service that improves the availability and performance of the applications that you offers to your global users
* (1) AWS GA uses highly available and congestion-free AWS global network to direct internet traffic from your users to your applications on AWS, making your users' experience more consistent.
* (2) AWS GA imporves application availability by continuously monitoring the health of your application endpoints and routing traffic to the closest heathly endpoints.
* (3) AWS GA makes it easier to manage your global applications by providing static IP address that act as a fixed entry point to your application hosted on AWS which eliminates the complexity of managing specific IP addresses for different AWS Regions and Availbility Zones.


**Security, Identity and Compliance**
Amazon Cognito
* handle user management, authentication, and sync across devices
* (1) add user sign-up, sign-in, and access control to web and mobile apps
  - authenticate users through social identity providers (Facebook, Google..) with SAML identity solutions or by using your own identity system.
* (2) enable to save data locally on users’ devices, allowing applications to work even when the devices are offline; then synchronize data across user's devices so that their app experience remains consistent regardless of the device they use.


Amazon Detective
* analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities.

Amazon GuardDuty
* a threat detection service that continuously monitors for malicious or unauthorized behavior to help you protect AWS accounts and workloads.

Amazon Inspector
* an automated security assessment service to improve the security and compliance of applications deployed on AWS.
* Amazon Inspector automatically assesses applications for exposure, vulnerabilities, and deviations from best practices.

Amazon Macie
* a security service that uses machine learning to automatically discover, classify and protect sensitive data in AWS

AWS Artifact
* go-to, central resource for compliance-related information

AWS Certificate Manager
* a service that lets you provision, manage, and deploy Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources.

AWS Cloud HSM
* a cloud-based hardware security module that enables to generate and use your own encryption keys.

AWS Identity and Access Management (IAM)
* enables you to securely control access to AWS services and resources for your users
  
AWS Key Management Service
* a secure and resilient service to create and manage keys and control the use of encryption across a wide range of AWS services and in your applications


AWS Secrets Manager
* protect secrets needed to access your applications, services, and IT resources. * enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.


AWS Shield
* a managed Distributed Denial of Service (DDoS) protection service that safeguards web applications running on AWS


AWS Single Sign-on
* centrally manage SSO access to multiple AWS accounts and business applications


AWS WAF
* a web application firewall that helps protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources



**Storage**
Amazon Elastic Block Store
* persistent block storage volumes for use with EC2 instances
* automaticlaly replicated within its AZ

Amazon Elastic File System
* a simple, scalable, elastic file system for Linux-based workloads for use with AWS Cloud services and on-premises resources
* scale on demand without disrupting applications
* provide massively parallel shared access

Amazon Simple Storage Service (S3)
* an object storage service, designed for 99.999999999% (11 9's) of durability
* Amazon S3 Glacier
  - a secure, durable, extremely low-cost storage service for data archiving and long-term backup

AWS Backup
* centralize and automate data protection across AWS services

AWS Storage Gateway
* a hybrid storage service that enables your on-premises applications to seamlessly use AWS cloud storage
  - backup and archiving, disaster recovery, cloud data processing, storage tiering, and migration





---

AWS Solution Architect


# 13. Resilient Architectures
design for a multi-tier architecture with compute, storage and database.

Resources
Get AWS Certified: Solutions Architect Challenge
Databases on AWS
Six free courses for building modern apps with purpose‑built databases
Cloud storage on AWS
Amazon S3
Amazon EC2 instance types
AWS Free Tier
High availability and scalability on AWS
Microservices on AWS
AWS FAQs

# 14. High-Performing Architectures
identify and select elastic and scalable solutions for a workload, ensuring our architecture is high-performing.


Resources
Compare NAT gateways and NAT instances
AWS Elastic Beanstalk FAQs
Amazon SQS FAQs
Shared responsibility model
AWS Storage Gateway FAQs
AWS Storage Gateway features
Cloud storage in minutes with AWS Storage Gateway
Amazon Kinesis Data Streams


# 15. Secure Applications and Architectures
Resources
Understanding how IAM works
NAT gateways
Route tables for your VPC
AWS Key Management Service FAQs
Network ACLs
Logging and monitoring in AWS Identity and Access Management
AWS Certificate Manager




# 16. Cost-Optimized Architectures
architecting for cost optimization.

Resources
Amazon S3 storage classes
Managing your storage lifecycle
Amazon EC2 pricing
Invoking AWS Lambda functions
AWS Snow Family
Caching overview


