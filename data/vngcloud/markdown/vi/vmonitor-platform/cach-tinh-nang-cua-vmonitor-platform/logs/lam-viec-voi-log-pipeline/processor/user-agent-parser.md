# User-agent Parser

### Tổng quan

User-agent Parser là một bộ phân tích và xác định các thông tin về trình duyệt, hệ điều hành, thiết bị, nhà sản xuất, và phiên bản của người dùng truy cập tới một trang web hoặc một ứng dụng. User-agent parser sử dụng một chuỗi ký tự gọi là user-agent để nhận diện người dùng.

***

### Cấu hình User-agent Parser

Để cáu hình User-agent Parser, hãy làm theo hướng dẫn bên dưới: 

1. Tại mục **Processor information**, nhập các thông tin chung cho một processor theo hướng dẫn tại [Processor](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/logs/lam-viec-voi-log-pipeline/processor). Trong nội dung này thì bạn sẽ chọn **Processor type** là **User-agent Parser**.
2. Tại mục **Parsing rule**, nhập các thông tin sau đây:

* Nhập **Source field**: field chứa logs sẽ cần parse.
* Nhập **Target field**: field sẽ được ghi đè bên destination log project, thông thường bạn sẽ không cần nhập thông tin này.

Ví dụ: 

|  |  |  |  |
| --- | --- | --- | --- |
| Source log project | Destination log project | user_agent (field logs mà chúng tôi thực hiện parser) | Kết quả parser |
| webserver | webserver-parse | "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0" | "user_agent_parse": { "os_minor": "11", "name": "Firefox", "version": "45.0", "major": "45", "os_full": "Mac OS X 10.11", "os": "Mac OS X", "os_version": "10.11", "os_name": "Mac OS X", "device": "Mac", "minor": "0", "os_major": "10" }, |

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(330).png?raw=true)

***

### Lưu trữ và tái sử dụng Parsing rule

* Bạn có thể lưu trữ một parsing rule bằng cách tích chọn vào **Save this rule**, sau đó nhập tên gợi nhớ cho parsing rule mà bạn muốn lưu trữ. Tên gợi nhớ có chiều dài tối thiểu là 5 ký tự, chiều dài tối đa là 255 ký tự và chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), khoảng trắng ( ), dấu gạch dưới (\_), dấu gạch ngang (-) và ký tự @.
* Sau khi parsing rule đã được lưu trữ, trong các lần tạo processor kế tiếp bạn có thể tái sử dụng rule này bằng cách chọn **Rule presets** tại mục Pasing rule. 
