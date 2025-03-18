# Danh sách Metrics hỗ trợ

### Linux/ Windows metrics 

Metric Agent của vMonitor Platform được xây dựng dựa trên phần mêm mã nguồn mỡ Telegraf, mặc định khi cài đặt Metric Agent, chúng tôi sẽ mở sẵn các input plugin như: 

* system
* disk
* kernel
* net
* diskio
* mem
* processes
* swap
* cpu

Bạn có thể xem thông tin chi tiết các Metric, Unit của các plugin trên tại [đây](https://github.com/influxdata/telegraf/tree/master/plugins/inputs), đồng thời bạn có thể mở thêm các input plugin để đẩy thêm Metric về vMonitor.

***

### Product metrics 

Khi các Resource trên VNG Cloud được tạo, mặc định sẽ có 2 loại monitor: Basic và Detail

|  |  |
| --- | --- |
| **Monitoring type** | **Mô tả** |
| **Basic monitoring** (Mặc định) | - Ở chế độ này, sẽ có một số lượng metric mặc định được đẩy về và lưu trữ trên hệ thống vMonitor Platform. Chi tiết tham khảo bảng thông số chi tiết bên dưới. <br> - Dữ liệu có sẵn tự động trong khoảng thời gian 1 phút. |
| **Detailed monitoring** (Nâng cao) | - Ở chế độ này, tất cả các metric đang có trên Resource được đẩy về và lưu trữ trên hệ thống vMonitor Platform. Chi tiết tham khảo bảng thông số chi tiết bên dưới. <br> - Dữ liệu có sẵn tự động trong khoảng thời gian 1 phút. |

Để biết mỗi loại monitoring bạn có thể làm những gì, vui lòng tham khảo tại [Danh sách Metrics hỗ trợ](https://docs.vngcloud.vn/vng-cloud-document/vn/vmonitor-platform/cach-tinh-nang-cua-vmonitor-platform/metrics/danh-sach-metrics-ho-tro/danh-sach-metrics-cua-host).
