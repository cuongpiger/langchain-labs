# Giám sát hoạt động LB

Giám sát hoạt động (monitoring) là một nhu cầu bắt buộc đối với mọi hệ thống. Tại VNG Cloud, bạn có thể giám sát vLB bằng cách sử dụng dịch vụ **vMonitor Platform**.

**vMonitor Platform là gì?**

**vMonitor Platform** là một dịch vụ Monitoring as a Service giúp thu thập các chỉ số sức khỏe **(metric)**, bản ghi hoạt động **(log)** của các resource trên VNG Cloud (hoặc ngoài VNG Cloud). Bên cạnh đó, bạn có thể vẽ các dashboard trực quan, thiết lập cảnh báo (alarm) và gửi thông báo (notification) khi xảy ra sự cố. Chi tiết về dịch vụ này bạn có thể tham khảo tại: [vMonitor Platform](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor).

Để bắt đầu sử dụng, bạn truy cập vMonitor Platform, mục Infrastructure List:

* Tab [vLB - Loadbalancer](https://hcm-3.console.vngcloud.vn/vmonitor/infrastructure/vlb): giúp bạn xem các metric của vLB. **Bạn tham khảo mô tả tại:** [**Quản lý vLB với Infrastructure Host**](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/metrics/lam-viec-voi-product-metric/lam-viec-voi-vlb-metric)**.**
* Tab [vLB-Log](https://hcm-3.console.vngcloud.vn/vmonitor/infrastructure/vlb-log): giúp bạn xem access log (Application Load Balancer) hoặc tcp log (Network Load Balancer). **Bạn tham khảo mô tả tại link:** [**vLB-Log**](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/logs/lam-viec-voi-product-logs/lam-viec-voi-vlb-log)

