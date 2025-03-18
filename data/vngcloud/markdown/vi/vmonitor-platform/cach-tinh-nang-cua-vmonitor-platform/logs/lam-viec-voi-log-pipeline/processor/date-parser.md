# Date Parser

### Tổng quan

Date Parser là một bộ lọc giúp phân tích và chuyển đổi các chuỗi ký tự biểu diễn ngày tháng sang một định dạng khác, thường là một đối tượng ngày tháng (date object) có thể sử dụng được trong các ngôn ngữ lập trình.

***

### Cấu hình Date Parser

Để cáu hình Date Parser, hãy làm theo hướng dẫn bên dưới: 

1. Tại mục **Processor information**, nhập các thông tin chung cho một processor theo hướng dẫn tại [Processor](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/logs/lam-viec-voi-log-pipeline/processor). Trong nội dung này thì bạn sẽ chọn **Processor type** là **Date Parser**.
2. Tại mục **Parsing rule**, nhập các thông tin sau đây:

* Nhập **Source field**: field chứa logs sẽ cần parse.
* Nhập **Locate:** ngôn ngữ được sử dụng cho định dạng date mà bạn mong muốn. Locale ảnh hưởng đến cách hiển thị và sắp xếp thứ, ngày, tháng và các ký tự phân cách, ví dụ năm-tháng-ngày, ngày-tháng-năm hoặc tháng-ngay-nam.
* Nhập **Timezone:** múi giờ của một vùng địa lý. Timezone ảnh hưởng đến giá trị của ngày tháng, bởi vì cùng một thời điểm có thể có giá trị ngày tháng khác nhau tùy thuộc vào múi giờ. Nếu bạn không lựa chọn **Locale** và **Timezone** thì chúng tôi sẽ mặc định lấy Locale và Timezone của hệ thống.
* Nhập **Target field**: field sẽ được ghi đè bên destination log project, thông thường bạn sẽ không cần nhập thông tin này 
* Nhập **Pattern:** chứa date pattern để matching với source field và parse ra theo cấu trúc. 

Ví dụ: 

| Items | Value | Ý nghĩa | Source logs | Destination logs |
| --- | --- | --- | --- | --- |
| **Source field** | date | Field nguồn cần parser là  **date** . | { "date":"Apr 17 09:32:01 } | {"date":"2023-08-01T07:45:11.130Z",} |
| **Locate** | Vietnamese | Ngôn ngữ sử dụng là  **Vietnamese** . | nt | nt |
| **Timezone** | N/A | Múi giờ lấy theo hệ thống. | nt | nt |
| **Target field** | date_parser | Field được parser sẽ ghi đè vô Destination log ở field  **date_parser** . | nt | nt |
| **Pattern** | yyyy-MM-dd'T'HH:mm:ss.SSSZ | Định dạng ngày tháng của field  **date** . | nt | nt |

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(326).png?raw=true)

***

### Lưu trữ và tái sử dụng Parsing rule

* Bạn có thể lưu trữ một parsing rule bằng cách tích chọn vào **Save this rule**, sau đó nhập tên gợi nhớ cho parsing rule mà bạn muốn lưu trữ. Tên gợi nhớ có chiều dài tối thiểu là 5 ký tự, chiều dài tối đa là 255 ký tự và chỉ có thể bao gồm các chữ cái viết hoa, viết thường (a-z, A-Z), số (0-9), dấu chấm (.), khoảng trắng ( ), dấu gạch dưới (\_), dấu gạch ngang (-) và ký tự @.
* Sau khi parsing rule đã được lưu trữ, trong các lần tạo processor kế tiếp bạn có thể tái sử dụng rule này bằng cách chọn **Rule presets** tại mục Pasing rule. 
