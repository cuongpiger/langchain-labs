# Cấu hình cho một Network Load Balancer

Tại trang \[Integrate with Network Load Balancer], chúng tôi đã hướng dẫn bạn cách thực hiện cài đặt VNGCloud LoadBalancer Controller, tạo và apply yaml file. Sau đây là chi tiết các ý nghĩa các thông tin bạn có thể thiết lập trong yaml file:

### Annotation 

Sử dụng các annotation dưới đây để tuỳ chỉnh Load Balancer phù hợp với nhu cầu của bạn:

| Annotation | Bắt buộc/ Không bắt buộc | Ý nghĩa |
| --- | --- | --- |
| vks.vngcloud.vn/load-balancer-id | Không bắt buộc | - **Nếu bạn chưa có sẵn một Network Load Balancer**  đã khởi tạo trước đó trên hệ thống vLB. Chúng tôi sẽ tự động tạo 1 NLB trên cluster của bạn. NLB này sẽ hiển thị trên vLB Portal, chi tiết truy cập tại  [đây](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb) <br> - **Nếu bạn đã có sẵn một Network Load Balancer**  đã khởi tạo trước đó trên hệ thống vLB và bạn muốn tái sử dụng NLB cho cluster của bạn. Lúc này, bạn hãy nhập thông tin Load Balancer ID vào annotation này. |
| vks.vngcloud.vn/load-balancer-name | Không bắt buộc | - Annotation  `vks.vngcloud.vn/load-balancer-name`  sẽ được sử dụng nếu bạn  **không**  sử dụng annotation  `load-balancer-id` . <br> - Annotation  `vks.vngcloud.vn/load-balancer-name`   **chỉ có ý nghĩa**  khi bạn tạo mới một load balancer. Sau khi load balancer được tạo thành công, annotation này  **sẽ tự động bị xóa** . Việc sử dụng annotation này sau khi load balancer được tạo sẽ  **không có tác dụng** . <br> - **Khi bạn sử dụng annotation này, nếu bạn chưa có sẵn một Network Load Balancer**  đã khởi tạo trước đó trên hệ thống vLB. Chúng tôi sẽ tự động tạo 1 NLB trên cluster của bạn. ALB này sẽ hiển thị trên vLB Portal, chi tiết truy cập tại  [đây](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb) <br> - **Nếu bạn đã có sẵn một Network Load Balancer**  đã khởi tạo trước đó trên hệ thống vLB và bạn muốn tái sử dụng NLB cho cluster của bạn. Lúc này, bạn hãy nhập thông tin Load Balancer Name vào annotation này. |
| vks.vngcloud.vn/package-id | Không bắt buộc | - Nếu bạn không nhập thông tin này thì mặc định chúng tôi sẽ sử dụng cấu hình  **NLB Small.** <br> - Nếu bạn đã có sẵn host vLB đang ACTIVE và bạn muốn tích hợp host này vô cụm K8S của bạn, vui lòng bỏ qua trường thông tin này. |
| vks.vngcloud.vn/tags | Không bắt buộc | - Tag được gắn thêm cho NLB của bạn. |
| vks.vngcloud.vn/scheme | Không bắt buộc | - Mặc định  **internet-facing** , bạn có thể đổi thành  **internal**  tùy theo nhu cầu sử dụng. |
| vks.vngcloud.vn/security-groups | Không bắt buộc | - Mặc định sẽ tạo một  **security group default**  theo Cluster của bạn. |
| vks.vngcloud.vn/inbound-cidrs | Không bắt buộc | - Mặc định All CIRD:  **0.0.0.0/0** |
| vks.vngcloud.vn/healthy-threshold-count | Không bắt buộc | - Mặc định  **3** |
| vks.vngcloud.vn/unhealthy-threshold-count | Không bắt buộc | - Mặc định  **3** |
| vks.vngcloud.vn/healthcheck-interval-seconds | Không bắt buộc | - Mặc định  **30** |
| vks.vngcloud.vn/healthcheck-timeout-seconds | Không bắt buộc | - Mặc định  **5** |
| vks.vngcloud.vn/healthcheck-protocol | Không bắt buộc | - Mặc định  **TCP** . Người dùng có thể chọn một trong các giá trị TCP/ HTTP/ HTTPS/ PING-UDP |
| vks.vngcloud.vn/healthcheck-http-method | Không bắt buộc | - Mặc định  **GET** . Người dùng có thể chọn một trong các giá trị GET / POST / PUT |
| vks.vngcloud.vn/healthcheck-path | Không bắt buộc | - Mặc định  **/** |
| vks.vngcloud.vn/healthcheck-http-version | Không bắt buộc | - Mặc định  **1.0** . Người dùng có thể chọn một trong các giá trị 1.0, 1.1 |
| vks.vngcloud.vn/healthcheck-http-domain-name | Không bắt buộc | - Mặc định trống |
| vks.vngcloud.vn/healthcheck-port | Không bắt buộc | - Mặc định  **traffic port** |
| vks.vngcloud.vn/success-codes | Không bắt buộc | - Mặc định  **200** |
| vks.vngcloud.vn/idle-timeout-client | Không bắt buộc | - Mặc định  **50** |
| vks.vngcloud.vn/idle-timeout-member | Không bắt buộc | - Mặc định  **50** |
| vks.vngcloud.vn/idle-timeout-connection | Không bắt buộc | - Mặc định  **5** |
| vks.vngcloud.vn/pool-algorithm | Không bắt buộc | - Mặc định  **ROUND_ROBIN** . Người dùng có thể chọn một trong các giá trị ROUND_ROBIN / LEAST_CONNECTIONS / SOURCE_IP |
| vks.vngcloud.vn/target-node-labels | Không bắt buộc | - Mặc định trống |
| vks.vngcloud.vn/enable-proxy-protocol | Không bắt buộc | - Mặc định trống. Người dùng chỉ định danh sách các service name trong Load Balancer mà Proxy Protocol sẽ được áp dụng. |

