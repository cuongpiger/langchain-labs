# Grok Parser

### Tổng quan

Grok parser là một bộ lọc (filter) giúp phân tích và cấu trúc hóa dữ liệu không có cấu trúc. Grok parser sử dụng các pattern (mẫu) để parser dữ liệu logs.

***

### Cấu hình Grok parser

Để tạo cấu hình Grok parser, hãy làm theo hướng dẫn bên dưới: 

1. Tại mục **Processor information**, nhập các thông tin chung cho một processor theo hướng dẫn tại [Processor](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/logs/lam-viec-voi-log-pipeline/processor). Trong nội dung này thì bạn sẽ chọn **Processor type** là **Grok Parser**.
2. Tại mục **Parsing rule**, nhập các thông tin sau đây:

2.1 Nhập **Source field**: field chứa logs sẽ cần parse.

2.2 Nhập **Target field**: field sẽ được ghi đè bên destination log project, thông thường bạn sẽ không cần nhập thông tin này 

2.3 Nhập **Rule pattern**: chứa grok pattern để matching với source field và parse ra theo cấu trúc. 

Ví dụ: 

| Source log project | Destination log project | Message (field logs mà chúng tôi thực hiện parser) | Rule pattern | Kết quả parser |
| --- | --- | --- | --- | --- |
| webserver | webserver-parse | `87.251.81.179 - 
- [01/Aug/2023:12:16:39 +0200] 
"GET /core/themes/theme.inc/?post
== HTTP/1.0" 200 63388` | %{IP:client_ip} %{USER:ident} %{USER:auth} \[%{HTTPDATE:timestamp}\] "%{WORD:http_method} %{URIPATHPARAM:request} HTTP/%{NUMBER:http_version}" %{NUMBER:response_code} %{NUMBER:response_size} | { "request": "/core/themes/theme.inc/?post==", "MONTH": "Aug", "response_code": "200", "IPV6": null, "auth": "-", "HOUR": "12", "ident": "-", "IPV4": "87.251.81.179", "BASE10NUM": [ "1.0", "200", "63388" ], "http_version": "1.0", "TIME": "12:16:39", "URIQUERY": "post==", "INT": "+0200", "response_size": "63388", "http_method": "GET", "YEAR": "2023", "URIPATH": "/core/themes/theme.inc/", "USERNAME": [ "-", "-" ], "client_ip": "87.251.81.179", "MINUTE": "16", "SECOND": "39", "MONTHDAY": "01", "timestamp": "01/Aug/2023:12:16:39 +0200" } |

3\. Tại mục **Test rules**, nhập các thông sau sau đây:

* Nhập **Log samples** là các dòng logs mẫu để bạn kiểm tra xem rule pattern có parse thành công không.
* Nhấn **Test your rules** để xem hệ thống có parse thành công không

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(322).png?raw=true)

***

### Lưu trữ và tái sử dụng Parsing rule

* Bạn có thể lưu trữ một parsing rule bằng cách tích chọn vào **Save this rule**, sau đó nhập tên gợi nhớ cho parsing rule mà bạn muốn lưu trữ. Tên gợi nhớ có chiều dài tối thiểu là 5 ký tự, chiều dài tối đa là 255 ký tự và chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), khoảng trắng ( ), dấu gạch dưới (\_), dấu gạch ngang (-) và ký tự @.
* Sau khi parsing rule đã được lưu trữ, trong các lần tạo processor kế tiếp bạn có thể tái sử dụng rule này bằng cách chọn **Rule presets** tại mục Pasing rule. 
