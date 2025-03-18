# Window OS

Để đẩy Metric về vMonitor, bạn cần cài đặt Metric Agent trên server, vMonitor sử dụng Telegraf Agent để đẩy metric về hệ thống, hiện tại Telegraf Agent hỗ trợ Service Account của IAM để xác thực và phân quyền, bạn thực hiện các bước bên dưới để thiết lập Telegraf Agent đẩy metrics về vMonitor

### **Telegraf Agent với Service Account** 

1. **Tạo Service Account và gắn policy: vMonitorMetricPush để có đủ quyền đẩy Metric về vMonitor**

Để tạo service account bạn truy cập tại [đây](https://hcm-3.console.vngcloud.vn/iam/service-accounts):

* Chọn "**Create a Service Account**", điền tên cho Service Account và nhấn **Next Step** để gắn quyền cho Service Account
* Tìm và chọn **Policy:** **vMonitorMetricPush,** sau đó nhấn "**Create a Service Account**" để tạo Service Account, Policy: vMonitorMetricPush do VNG Cloud tạo ra chỉ chứa chính xác quyền đẩy metric về hệ thống
* Sau khi tạo thành công bạn cần phải lưu lại Client\_ID và Secret\_Key để thực hiện bước tiếp theo

2\. **Tải bản cài  Agent Installer cho Windows**

* Truy cập vào link để thực hiện tải agent installer cho Windows : [https://github.com/vngcloud/vmonitor-metrics-agent/releases/download/1.26.0-2.0.1/telegraf-nightly\_windows\_amd64.exe](https://github.com/vngcloud/vmonitor-metrics-agent/releases/download/1.26.0-2.0.1/telegraf-nightly\_windows\_amd64.exe)

3\. **Cài đặt installer với Client\_ID và Secret\_Key đã sao chép ở trên**

* Chạy agent installer đã tải ở trên
* Sau khi nhận thông báo, chọn **More Info**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(115).png?raw=true)

* Sau đó chọn **Run anyway**, để bắt đầu cài agent

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(116).png?raw=true)

* Chọn **Next** để tiếp tục

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(117).png?raw=true)

* Nhập 2 thông tin **Client\_ID** và **Secret\_Key** đã sao chép ở trên vào 2 trường: **IAM\_CLIENT\_ID** và **IAM\_CLIENT\_SECRET**: 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(118).png?raw=true)

* Để mặc định, chọn Next để tiếp tục, hoặc nếu bạn muốn thay đổi thư mục cài đặt thì thực hiện thay đổi

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(119).png?raw=true)

* Chọn **Accept the license,** sau đó chọn **Next** để tiếp tục

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(120).png?raw=true)

* Để mặc định, chọn **Next** để tiếp tục, hoặc bạn có thể tùy chỉnh shortcut menu name cho agent

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(121).png?raw=true)

* Chọn **Install** để thực hiện cài đặt

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(122).png?raw=true)

* Chọn **Yes** để thực hiện grant quyền cho agent hoạt động

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(123).png?raw=true)

* Sau khi quá trình cài đặt hoàn tất, chọn **Finish**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(124).png?raw=true)

4\. **Sau khi cài đặt thành công bạn sẽ thấy server ở trang Infrastructure List/Host** 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(125).png?raw=true)

### **Telegraf Agent với API\_KEY (deprecated**) 

> **Chú ý:**
>
> * Chúng tôi khuyến cáo bạn không sử dụng phương thức này, trong thời gian sắp tới hệ thống của chúng tôi sẽ dừng hỗ trợ các API Key này.

B1: Tạo API Key (nếu chưa thực hiện tạo bất kỳ API Key nào trước đó )

* Truy cập vào portal vMonitor Platform Product: [https://hcm-3.console.vngcloud.vn/vmonitor/](https://hcm-3.console.vngcloud.vn/vmonitor/)
* Chọn **Intergration** => sau đó chọn phần **API Key**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(127).png?raw=true)

* Chọn **Create an API Key**, để thực hiện tạo mới (nếu chưa tạo bất kỳ API Key nào trước đó)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(128).png?raw=true)

B2: Download Agent Installer

* Truy cập vào link để thực hiện tải agent installer: [https://github.com/vngcloud/vmonitor-metrics-agent/releases/download/1.23.0-1.4.0/telegraf-nightly\_windows\_amd64.exe](https://github.com/vngcloud/vmonitor-metrics-agent/releases/download/1.23.0-1.4.0/telegraf-nightly\_windows\_amd64.exe)

B3: Install Agent

* Chạy agent installer
* Sau khi nhận thông báo, chọn **More Info**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(130).png?raw=true)

* Sau đó chọn **Run anyway**, để bắt đầu install agent

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(131).png?raw=true)

* Chọn **Next** để tiếp tục

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(132).png?raw=true)

* Quay về Portal vMonitor Platform, ở phần API Key, **chọn** **biểu** **tượng copy**, để copy thông tin API Key

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(133).png?raw=true)

* Paste thông tin API Key vào phần nhập **Credentials**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(134).png?raw=true)

* Có thể tùy chỉnh installation folder

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(135).png?raw=true)

* Chọn **Accept the license,** sau đó chọn **Next** để tiếp tục

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(137).png?raw=true)

* Có thể tùy chỉnh shortcut menu name cho agent, sau đó chọn **Next** để tiếp tục

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(138).png?raw=true)

* Chọn **Install** để thực hiện cài đặt

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(139).png?raw=true)

* Chọn Yes để thực hiện grant quyền cho agent hoạt động

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(140).png?raw=true)

* Sau khi quá trình cài đặt hoàn tất, chọn **Finish**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(141).png?raw=true)

#### B4: Kiểm tra agent đã hoạt động 

* Truy cập vào portal vMonitor Platform, chọn **Infrastructure list** => chọn **Host,** sau đó kiểm tra hostname của VM đã xuất hiện trong danh sách

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(142).png?raw=true)

* Chọn vào tên **Hostname**, để kiểm tra dashboard monitor

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(143).png?raw=true)
