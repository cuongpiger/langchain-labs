# Chuẩn bị kết nối đẩy log

#### Kết nối từ máy đẩy log tới hệ thống vMontior Platform.

|  |  |  |
| --- | --- | --- |
| **Nguồn** | **Đích** | **Port** |
| IP máy đẩy log | Dải subnet: 116.118.93.130/28, tức 116.118.93.128 -> 116.118.93.143 | 10092 TCP |
| IP máy đẩy log | Domain: [hcm01-loghub01.vngcloud.vn](http://hcm01-loghub01.vngcloud.vn)   [hcm02-loghub01.vngcloud.vn](http://hcm02-loghub01.vngcloud.vn)   [hcm03-loghub01.vngcloud.vn](http://hcm03-loghub01.vngcloud.vn) | 10092 TCP |

* Kết nối trên cần mở trong suốt quá trình agent đẩy log

Nếu các máy cần thu thập log có máy không thể mở kết nối trực tiếp trên. Tham khảo sử dụng mô hình [collector](https://opentelemetry.io/docs/collector/) để đẩy qua một host trung gian.

***

#### Phân giải domain

Do dữ liệu kênh truyền được **bảo mật** bằng chuẩn mã hóa SSL. Nếu máy đẩy log có khả năng truy vấn DNS public thì không vấn đề gì. Tuy nhiên nếu không (có thể gặp trong môi trường on-premise) thì bạn cần thêm phân giải domain theo bảng sau:

| <pre><code># IP---------------| Domain
116.118.93.131      hcm01-loghub01.vngcloud.vn 
116.118.93.132      hcm02-loghub01.vngcloud.vn 
116.118.93.133      hcm03-loghub01.vngcloud.vn
116.118.93.134      hcm04-loghub01.vngcloud.vn
116.118.93.135      hcm05-loghub01.vngcloud.vn
116.118.93.136      hcm06-loghub01.vngcloud.vn
</code></pre> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

\
