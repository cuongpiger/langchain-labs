# Làm việc với vStorage-Metric

Khi bạn tạo các vStorage Project, hệ thống sẽ tự động thu thập các vStorage metric và hiển thị ở tab Infrastructure List/vStorage, giúp bạn có thể theo dõi được các vStorage Project trên VNG Cloud hoàn toàn miễn phí

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(154).png?raw=true)

Tại trang này ở mỗi vStorage Project bạn sẽ thấy các thông tin như sau:

* **Host**: tên và ID của vStorage Project
* **Status**: trạng thái về monitor của vStorage Project, UP là đang có dữ liệu, UNDERTERMINE là trong vòng 5p chưa có dữ liệu mới
* **Usage**: thông tin về usage/quota của vStorage Project
* **Detailed Monitoring**: mặc định sẽ là tắt, khi bạn có nhu cầu cần vẽ các vStorage metric khác ngoài các Metric mà dashboard mặc định chúng tôi đã vẽ và tạo các Alarm để cảnh báo với tài nguyên này, thì bạn cần bật tính năng này lên. Để bật tính năng này bạn cần mua gói Metric Quota (gói có phí hay miễn phí đều được), tuy nhiên bạn sẽ không bị tính là 1 Host khi bật và hoàn toàn miễn phí, chỉ khi tạo Alarm là sẽ bị tính vào Alarm quota.

 Khi nhấn vào tên của vStorage Project, bạn sẽ được chuyển sang trang Dashboard, và xem default dashboard của vStorage Project này, quy tắc đặt tên dashboard của vStorage sẽ là vStorage-Project\_Name-ID (lấy block thứ 3 của ID vStorage)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(155).png?raw=true)

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(156).png?raw=true)

> **Chú ý:**
>
> * Hệ thống vMonitor sẽ mất 1 khoảng thời gian trung bình 5-10 phút (có thể có trường hợp tệ nhất là 20 phút) để cập nhập vStorage Project mới sau khi bạn tạo.
> * Để xem danh sách metrics tương ứng của mỗi product này, hãy xem tại [Danh sách Metrics hỗ trợ](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/metrics/danh-sach-metrics-ho-tro).

\
