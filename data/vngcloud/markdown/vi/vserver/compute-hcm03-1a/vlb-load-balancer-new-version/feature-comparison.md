# Feature Comparison

Trong bối cảnh thị trường năng động của điện toán đám mây, Load Balancer là công cụ quan trọng để nâng cao hiệu suất ứng dụng và đảm bảo trải nghiệm người dùng liền mạch. Tại VNG cloud, chúng tôi cung cấp hai loại Load Balancer chính: Application Load Balancer (ALB) và Network Load Balancer (NLB). Tài liệu này sẽ giúp người dùng hiểu được sự khác biệt và điểm mạnh của các loại Load Balancer này, từ đó đưa ra quyết định sáng suốt về loại nào phù hợp nhất với yêu cầu cho từng ứng dụng cụ thể.

| Thuộc tính/Tính năng | Application Load Balancer | Network Load Balancer |
| --- | --- | --- |
| Layer | Layer 7 | Layer 4 |
| Scheme | Internet-facing, Internal | Internet-facing, Internal |
| Deployment Mode | Active/StandBy | Active/StandBy |
| IAM Permission | Full IAM Support | Full IAM Support |
| **Listener Configurations** |  |  |
| Protocol | HTTP, HTTPS | TCP, UDP |
| Host & Path Routing | Yes | No |
| HTTP Header-Based Routing | No | No |
| Server Name Indication (SNI) | Yes | No |
| Enable Client CA (HTTPS Only) | Yes | No |
| Timeout | Yes | Yes |
| Whitelist IP Source | Yes | Yes |
| **Pool Configurations** |  |  |
| Algorithm | Round Robin, Least Connections, Source IP | Round Robin, Least Connections, Source IP |
| Pool Protocol | HTTP | TCP, Proxy, UDP |
| Enable Sticky Session | Yes | No |
| Enable TLS encryption | Yes | No |
| Health Check | TCP, HTTP | TCP, HTTP, HTTPS, Ping&UDP |
| Target type | IP, Instance | IP, Instance |
| **vMonitor-platform Integration** |  |  |
| Metric | Yes | Yes |
| Audit Log | Yes | Yes |
| Access Log | Yes | Yes |
