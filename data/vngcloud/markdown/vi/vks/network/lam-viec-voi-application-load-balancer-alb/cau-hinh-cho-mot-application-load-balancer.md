# Cấu hình cho một Application Load Balancer

Tại trang \[Ingress for an Application Load Balancer], chúng tôi đã hướng dẫn bạn cách thực hiện cài đặt VNGCloud LoadBalancer Controller và tạo ingress thông qua Ingress Yaml file. Sau đây là chi tiết các ý nghĩa các thông tin bạn có thể thiết lập cho một Ingress

### Annotation 

Sử dụng các annotation dưới đây khi thực thiện tạo ingress để tuỳ chỉnh Load Balancer phù hợp với nhu cầu của bạn:

| Annotation | Bắt buộc/ Không bắt buộc | Ý nghĩa |
| --- | --- | --- |
| vks.vngcloud.vn/load-balancer-id | Không bắt buộc | - **Nếu bạn chưa có sẵn một Application Load Balancer**  đã khởi tạo trước đó trên hệ thống vLB. Lúc này, khi tạo một Ingress, bạn hãy để trống thông tin này. Sau khi bạn đã thực hiện triển khai Ingress theo hướng dẫn tại  [Ingress for an Application Load Balancer](https://docs.vngcloud.vn/display/VKSVI/Ingress+for+an+Application+Load+Balancer) . Chúng tôi sẽ tự động tạo 1 ALB trên cluster của bạn. ALB này sẽ hiển thị trên vLB Portal, chi tiết truy cập tại  [đây](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb) <br> - **Nếu bạn đã có sẵn một Application Load Balancer**  đã khởi tạo trước đó trên hệ thống vLB và bạn muốn tái sử dụng ALB cho cluster của bạn. Lúc này, khi tạo một Ingress, bạn hãy nhập thông tin Load Balancer ID vào annotation này. Sau khi bạn đã thực hiện tạo Ingress theo hướng dẫn tại  [Ingress for an Application Load Balancer](https://docs.vngcloud.vn/display/VKSVI/Ingress+for+an+Application+Load+Balancer) . Nếu: ALB của bạn đang có sẵn 2 listener trong đó: 1 listener có cấu hình protocol HTTP và port 80 1 listener có cấu hình protocol HTTPS và port 443 thì chúng tôi sẽ sử dụng 2 listener này. ALB của bạn chưa có một trong hai hoặc cả 2 listener có cấu hình trên, chúng tôi sẽ tự động khởi tạo chúng. <br> - ALB của bạn đang có sẵn 2 listener trong đó: 1 listener có cấu hình protocol HTTP và port 80 1 listener có cấu hình protocol HTTPS và port 443 thì chúng tôi sẽ sử dụng 2 listener này. <br> - 1 listener có cấu hình protocol HTTP và port 80 <br> - 1 listener có cấu hình protocol HTTPS và port 443 thì chúng tôi sẽ sử dụng 2 listener này. <br> - ALB của bạn chưa có một trong hai hoặc cả 2 listener có cấu hình trên, chúng tôi sẽ tự động khởi tạo chúng. <br> - 1 listener có cấu hình protocol HTTP và port 443 <br> - Hoặc 1 listener có cấu hình protocol HTTPS và portal 80 <br> Chú ý: Nếu ALB của bạn có: thì khi tạo Ingress sẽ xảy ra lỗi. Lúc này, bạn cần chỉnh sửa lại thông tin listener hợp lệ trên hệ thống vLB và thực hiện tạo lại ingress. |
| vks.vngcloud.vn/load-balancer-name | Không bắt buộc | - Annotation  `vks.vngcloud.vn/load-balancer-name`  sẽ được sử dụng nếu bạn  **không**  sử dụng annotation  `load-balancer-id` . <br> - Annotation  `vks.vngcloud.vn/load-balancer-name`   **chỉ có ý nghĩa**  khi bạn tạo mới một Ingress resource. Sau khi Ingress resource được tạo thành công, annotation này  **sẽ tự động bị xóa** . Việc sử dụng annotation này sau khi Ingress resource được tạo sẽ  **không có tác dụng** . <br> - **Khi bạn sử dụng annotation này, nếu bạn chưa có sẵn một Application Load Balancer**  đã khởi tạo trước đó trên hệ thống vLB. Chúng tôi sẽ tự động tạo 1 ALB trên cluster của bạn. ALB này sẽ hiển thị trên vLB Portal, chi tiết truy cập tại  [đây](https://hcm-3.console.vngcloud.vn/vserver/load-balancer/vlb) <br> - **Nếu bạn đã có sẵn một Application Load Balancer**  đã khởi tạo trước đó trên hệ thống vLB và bạn muốn tái sử dụng ALB cho cluster của bạn. Lúc này, bạn hãy nhập thông tin Load Balancer Name vào annotation này. |
| vks.vngcloud.vn/package-id | Không bắt buộc | - Nếu bạn không nhập thông tin này thì mặc định chúng tôi sẽ sử dụng cấu hình  **ALB Small.** <br> - Nếu bạn đã có sẵn host vLB đang ACTIVE và bạn muốn tích hợp host này vô cụm K8S của bạn, vui lòng bỏ qua trường thông tin này. |
| vks.vngcloud.vn/tags | Không bắt buộc | - Tag được gắn thêm cho ALB của bạn. |
| vks.vngcloud.vn/scheme | Không bắt buộc | - Mặc định  **internet-facing** , bạn có thể đổi thành  **internal**  tùy theo nhu cầu sử dụng. |
| vks.vngcloud.vn/security-groups | Không bắt buộc | - Mặc định sẽ tạo một  **security group default**  theo Cluster của bạn. |
| vks.vngcloud.vn/inbound-cidrs | Không bắt buộc | - Mặc định All CIRD:  **0.0.0.0/0** |
| vks.vngcloud.vn/healthy-threshold-count | Không bắt buộc | - Mặc định  **3** |
| vks.vngcloud.vn/unhealthy-threshold-count | Không bắt buộc | - Mặc định  **3** |
| vks.vngcloud.vn/healthcheck-interval-seconds | Không bắt buộc | - Mặc định  **30** |
| vks.vngcloud.vn/healthcheck-timeout-seconds | Không bắt buộc | - Mặc định  **5** |
| vks.vngcloud.vn/healthcheck-protocol | Không bắt buộc | - Mặc định  **TCP** . Người dùng có thể chọn một trong các giá trị TCP/ HTTP |
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
| vks.vngcloud.vn/enable-sticky-session | Không bắt buộc | - Mặc định  **false** . |
| vks.vngcloud.vn/enable-tls-encryption | Không bắt buộc | - Mặc định  **false** |
| vks.vngcloud.vn/target-node-labels | Không bắt buộc | - Mặc định trống |
| vks.vngcloud.vn/certificate-ids | Không bắt buộc | - Mặc định trống |
| vks.vngcloud.vn/is-poc | Không bắt buộc | - Mặc định false. <br> - Nếu người dùng chỉ định field này là true, hệ thống sẽ tạo Load Balancer và thực hiện thanh toán bởi số dư ví POC. |
| vks.vngcloud.vn/enable-autoscale | Không bắt buộc | - Mặc định false. <br> - Nếu người dùng chỉ định field này là true, hệ thống sẽ tạo Load Balancer với mode autoscale được bật. |
| vks.vngcloud.vn/ignore | Không bắt buộc | - Mặc định false. <br> - Nếu người dùng chỉ định field này là false, operator của chúng tối sẽ không quản lý Service và Ingress. Mọi thay đổi đối với resource sẽ bị bỏ qua và LoadBalancer sẽ không được cập nhật. |
| vks.vngcloud.vn/implementation-specific-params | Không bắt buộc | - Mặc định trống <br> - Theo mặc định,  **ALB policy**  chỉ có 1 rule dành cho host và path, với các thao tác giới hạn như  **EQUAL_TO**   **(Exact)**  và  **START_WITH (Prefix)** . Nếu người dùng muốn tạo thêm policy hoặc sử dụng các thao tác khác như  **ENDS_WITH**  hoặc  **REGEX** , cần thay đổi  **pathType**  thành  **ImplementationSpecificParams**  và sử dụng  **annotation**  với giá trị JSON để cấu hình. Ví dụ: <br> `[{
  "path": "/haha",
  "rules": [
    {
      "type": "PATH",
      "compare": "EQUAL_TO",
      "value": "/foo#"
    },
    {
      "type": "PATH",
      "compare": "REGEX",
      "value": "/foo#anchor"
    }
  ],
  "action": {
    "action": "REJECT",
    "redirectUrl": "http://golang.cafe/a",
    "redirectHttpCode": 301
  }
}]` |
| vks.vngcloud.vn/header | Không bắt buộc | - Mặc định: {"http":["X-Forwarded-For", "X-Forwarded-Proto", "X-Forwarded-Port"],"https":["X-Forwarded-For", "X-Forwarded-Proto", "X-Forwarded-Port"]} |
| vks.vngcloud.vn/client-certificate-id | Không bắt buộc | - Mặc định trống <br> - **Client CA**  là một tính năng bảo mật của  **Load Balancer**  giúp xác thực client bằng cách sử dụng  **client certificate**  để cho phép các client được ủy quyền truy cập vào ứng dụng hoặc dịch vụ. Truyền một  **certificate id**  trong  **portal**  vào  **annotation**  này sẽ kích hoạt  **Client CA**  cho  **https listener** . |

***

### IngressClassName 

Các Ingress được cài đặt bởi các VNGCloud LoadBalancer Controller sẽ có thông tin IngressClassName = "vngcloud". Bạn không được thay đổi thông tin này.

***

### DefaultBackend

* Một Ingress không có rule nào sẽ gửi tất cả traffic đến 1 service default backend mặc định duy nhất hoặc nếu không có _host_ và _path_ nào khớp với HTTP request trong Ingress Yaml file thì traffic sẽ được route đến service default backend. Ví dụ như bên dưới, chúng tôi đang cấu hình mặc định nếu request không thỏa mãn rule nào trong Ingress yaml file thì sẽ đi vào service name: example-svc-1 với port number 8080

```
defaultBackend:
    service:
      name: example-svc-1
      port:
        number: 8080
```

***

### TLS 

Bạn có thể bảo mật Ingress bằng cách chỉ định 1 Secret có chứa TLS key và certificate. Hiện tại Ingress chỉ hỗ trợ duy nhất TLS port 443 và là điểm kết thúc cho TLS (TLS termination). TLS Secret phải chứa các trường với tên key là tls.crt và tls.key, đây chính là certificate và private key để sử dụng cho TLS. Cụ thể, bạn cần chỉ định:

* Host: các host được chỉ định sẽ dùng cert.
* SecretName: tên secret chứa cert.

***

### Path types 

Mỗi path (đường dẫn) trong Ingress có một pathType (loại đường dẫn) tương ứng. Có ba pathType được hỗ trợ:

* Exact: Khớp với đường dẫn URL một cách chính xác tuyệt đối và phân biệt chữ hoa chữ thường.
* Prefix: Khớp dựa trên tiền tố của đường dẫn URL được phân tách bởi dấu /. Việc so khớp (match) là có phân biệt chữ hoa thường và được thực hiện trên từng thành phần của đường dẫn URL. Một thành phần của đường dẫn URL chính là 1 label được phân tách bằng dấu phân cách / trong đường dẫn URL (Nghĩa là đường dẫn URL có thể bao gồm nhiều cấp phân tách nhau bởi dẫu /, mỗi chuỗi đứng giữa 2 dấu / chính là 1 label, mỗi label chính là 1 thành phần của đường dẫn URL). Một request URL được xem như là khớp với 1 trường path (được cấu hình trong đặc tả Ingress) khi toàn bộ giá trị của path (có thể gồm nhiều thành phần phân tách bằng dấu /) khớp với các label đầu tiên (tính từ bên trái của đường dẫn URL). Ví dụ /example1/path1 khớp với /example1/path1/path2, nhưng không khớp với /example1/path1path2

Ví dụ cụ thể:

| Path type | Path(s)                             | Request path(s)           | Có match hay không? |
| --------- | ----------------------------------- | ------------------------- | ------------------- |
| Exact     | `/example1`                         | `/example1`               | Có                  |
| Exact     | `/example1`                         | `/host1`                  | Không               |
| Exact     | `/example1`                         | `/example1/`              | Không               |
| Exact     | `/example1/`                        | `/example1`               | Không               |
| Prefix    | `/`                                 | (all paths)               | Có                  |
| Prefix    | `/example1`                         | `/example1`, `/example1/` | Có                  |
| Prefix    | `/example1/`                        | `/example1`, `/example1/` | Có                  |
| Prefix    | `/example1/host11`                  | `/example1/host1`         | Không               |
| Prefix    | `/example1/host1`                   | `/example1/host1`         | Có                  |
| Prefix    | `/example1/host1/`                  | `/example1/host1`         | Có                  |
| Prefix    | `/example1/host1`                   | `/example1/host1/`        | Có                  |
| Prefix    | `/example1/host1`                   | `/example1/host1/ccc`     | Có                  |
| Prefix    | `/example1/host1`                   | `/example1/host1xyz`      | Không               |
| Prefix    | `/`, `/example1`                    | `/example1/ccc`           | Có                  |
| Prefix    | `/`, `/example1`, `/example1/host1` | `/example1/host1`         | Có                  |
| Prefix    | `/`, `/example1`, `/example1/host1` | `/ccc`                    | Có                  |
| Prefix    | `/example1`                         | `/ccc`                    | Không               |

* Trong một số trường hợp, nhiều path bên trong Ingress sẽ khớp với đường dẫn của request URL. Trong những trường hợp đó, quyền ưu tiên sẽ được trao cho path khớp dài nhất đầu tiên. Nếu hai path vẫn có độ dài khớp bằng nhau thì quyền ưu tiên sẽ theo thứ tự rule được tạo trên Ingress Yaml file.

***

### Ingress rule 

Mỗi HTTP rule chứa các thông tin sau:

* **1 host tùy chọn**. Nếu không có host (ta có thể hiểu là 1 tên miền) nào được chỉ định nên rule sẽ được áp dụng cho tất cả HTTP traffic đi vào (inbound) địa chỉ IP đã được chỉ định. Nếu có chỉ định host (ví dụ example1.com) thì rule chỉ áp dụng cho host đó thôi.
* **1 danh sách các đường dẫn (path)** (ví dụ `/example1/host1`), mỗi path có 1 service backend gắn liền với nó được định nghĩa bởi Service Name và Port Number. Cả host và path phải khớp với nội dung của incoming request trước khi bộ cân bằng tải điều hướng traffic đến Services mong muốn.
* **1 backend** là tổ hợp của tên Services và Port Number. HTTP và HTTPS request đi đến Ingress và có URL khớp với host và path của rule sẽ được gửi đến danh sách các backend.

Ví dụ: Host có khớp với Host header theo bảng:

| Host                                       | Host header                                                      | Có match hay không? |
| ------------------------------------------ | ---------------------------------------------------------------- | ------------------- |
| `*.`[`example1.com`](http://example1.com/) | [`example2.example1.com`](http://example2.example1.com/)         | Có                  |
| `*.`[`example1.com`](http://example1.com/) | [`baz.example2.example1.com`](http://baz.example2.example1.com/) | Không               |
| `*.`[`example1.com`](http://example1.com/) | [`example1.com`](http://example1.com/)                           | Không               |
