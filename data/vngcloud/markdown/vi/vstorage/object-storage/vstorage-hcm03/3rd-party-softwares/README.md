# 3rd party softwares

#### Tổng quan 

vStorage hỗ trợ các công cụ phía người dùng và phiên bản (version) tương ứng như bên dưới. Chúng tôi khuyến cáo bạn hãy sử dụng các phiên bản được liệt kê trong bảng này của các công cụ client để không gặp lỗi trên tất cả các tính năng mà chúng tôi cung cấp:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| STT | Công cụ | Giao thức | Hệ điều hành | Phiên bản hỗ trợ tốt nhất | Vùng (Region) |
| 1 | S3cmd | S3 | Windows, Linux | 2.3.0 | Tất cả region |
| 2 | Cyberduck | S3 | Windows, MacOS | 7.7.2 | Tất cả region |
| 3 | Swift | Windows, Linux | 7.7.2 | Tất cả region |  |
| 4 | Rclone | S3 | Windows, Linux | 1.62.2 | Tất cả region |
| 5 | Swift | Windows, Linux | 1.62.2 | Tất cả region |  |
| 6 | SwiftClient | Swift | Windows, Linux | 4.3.0 | Tất cả region |
| 7 | S3 Browser | S3 | Windows, Linux | 10.9.9 | Tất cả region |
| 8 | MinIO Client (MC) | S3 | Windows, Linux | RELEASE.2023-05-26T23-31-54Z | Tất cả region |

#### Danh sách các lỗi thường gặp trong quá trình sử dụng các công cụ phía người dùng (3rd party software, client tool) 

|  |  |  |  |
| --- | --- | --- | --- |
| STT | Mã lỗi | Nội dung lỗi | Giải pháp |
| STT | Mã lỗi | Nội dung lỗi | Giải pháp |
| 1 | 401 Unauthorized | Sai thông tin đăng nhập | - Kiểm tra lại thông tin vStorage credentials (Swift username/password, token, s3 keys) dùng để chứng thực truy cập vào dịch vụ vStorage. Để làm việc với vStorage credentials, vui lòng tham khảo tại  [đây](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49648911) . |
| 2 | 413 Request Entity Too Large | vStorage project hết quota | - Tăng hạn mức quota của vStorage project. Để tăng hạn mức quota, vui lòng tham khảo ở <br> [đây](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49648497) . |
| 3 | 403 Forbidden | Không có quyền truy cập | - Kiểm tra lại các thiết lập liên quan đến việc truy cập project hoặc container (CORS, ACLs, IP Range ACL, public container, v.v.) trên vStorage portal. Để thay đổi thiết lập liên quan đến việc truy cập project hoặc container, vui lòng tham khảo tại  [đây](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49648906) . <br> - Kiểm tra lại các quyền (permission), chính sách (policy) được cấp cho Swift user, s3 key trên project hoặc container. Để thay đổi các thiết lập liên quan đến quyền hoặc chính sách truy cập, vui lòng tham khảo tại  [đây](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49648909) . |
| 4 | 401 Authorization Failure | Sai token | - Kiểm tra thông tin chứng thực được dùng để tạo token, đảm bảo thông tin chứng thực (vStorage credentials) chính xác. Để làm việc với vStorage credentials, vui lòng tham khảo tại  [đây](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49648911) . |
| 5 | N/A | Usage trên vStorage Portal khác với usage hiển thị trên máy local | - vStorage Portal sử dụng  **storage base = 1024**  (1 KB = 1024 B). Việc tại một số thời điểm tổng dung lượng (usage) hiển thị trên vStorage portal khác so với tổng dung lượng kích thước các file trên máy local hiển thị có thể do một số nguyên nhân liên quan đến việc truy xuất thông tin, đồng bộ thông tin, caching, v.v. của hệ thống vStorage và các hệ thống khác. Do đó, có thể sử dụng chính công cụ phía người dùng để kiểm tra chính xác thông tin dung lượng lưu trữ thực tế trên dịch vụ vStorage là bao nhiêu. <br> - Kiểm tra thông tin dung lượng lưu trữ của project, xem thông số " **bytes** " và thông tin các " **container segment (container+/_segments)** " sử dụng công cụ Swift Client theo 2 mệnh lệnh (command) sau: <br> swift stat swift list Để hiểu hơn về cách Swift Client làm việc, vui lòng tham khảo tại  [đây](https://docs.vngcloud.vn/display/VV/Swift+Client) . |
| 6 | N/A | Danh sách container trên vStorage Portal khác với danh sách container hiển thị trên các công cụ phía người dùng | - Dịch vụ vStorage hỗ trợ nhiều  **giao diện tương tác người dùng**  như: UI: vStorage Portal, Cyberduck, S3 Browser CLI: Aws CLI, mc, s3cmd, v.v. API: vStorage APIs, vStorage Restful APIs, vStorage S3 APIs SDK: MinIO SDK, AWS SDK cho các ngôn ngữ Java, Python, Golang, C#, NodeJS, v.v. <br> - UI: vStorage Portal, Cyberduck, S3 Browser <br> - CLI: Aws CLI, mc, s3cmd, v.v. <br> - API: vStorage APIs, vStorage Restful APIs, vStorage S3 APIs <br> - SDK: MinIO SDK, AWS SDK cho các ngôn ngữ Java, Python, Golang, C#, NodeJS, v.v. <br> - Mỗi trong số các  **giao diện tương tác người dùng**  này sẽ lựa chọn hiển thị các tài nguyên vStorage (project, container, object, version, metadata, v.v.) theo các mục đích khác nhau nên có thể có sự khác nhau trong danh sách các tài nguyên vStorage được liệt kê, hiển thị. <br> - Phần lớn các  **giao diện tương tác người dùng**  có sự khác biệt trong việc liệt kê, hiển thị các container. Một số hiển thị container segment, container version, v.v và một số không hiển thị. Để hiểu rõ hơn về các loại container trong hệ thống lưu trữ vStorage, vui lòng tham khảo tại  [đây](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49648674) . |
| 7 |  | Danh sách các tính năng trên vStorage Portal khác với danh sách các tính năng trên các công cụ phía người dùng | - Dịch vụ vStorage hỗ trợ nhiều  **giao diện tương tác người dùng**  như: UI: vStorage Portal, Cyberduck, S3 Browser CLI: Aws CLI, mc, s3cmd, v.v. API: vStorage APIs, vStorage Restful APIs, vStorage S3 APIs SDK: MinIO SDK, AWS SDK cho các ngôn ngữ Java, Python, Golang, C#, NodeJS, v.v. <br> - UI: vStorage Portal, Cyberduck, S3 Browser <br> - CLI: Aws CLI, mc, s3cmd, v.v. <br> - API: vStorage APIs, vStorage Restful APIs, vStorage S3 APIs <br> - SDK: MinIO SDK, AWS SDK cho các ngôn ngữ Java, Python, Golang, C#, NodeJS, v.v. <br> - Mỗi trong số các  **giao diện tương tác người dùng**  này sẽ lựa chọn cung cấp các tính năng theo các mục đích khác nhau. <br> - Bên cạnh đó, do mục đích của phần lớn các giao diện tương tác người dùng là để hỗ trợ nhiều nhà cung cấp (provider) dịch vụ lưu trữ khác nhau nên sẽ không đảm bảo tương thích 100% với các tính năng do dịch vụ vStorage cung cấp. |
| 8 | 403 Forbidden | Không xóa được object trên container | - Kiểm tra các thiết lập liên quan đến quyền truy cập và thao tác object đó, tham khảo  **mục #3.** <br> - Kiểm tra xem object đó được lưu trữ trên các container thuộc archive project không? Nếu phải, vui lòng tham khảo các quy định liên quan đến việc xóa các object trên archive project tại  [đây](https://docs.vngcloud.vn/pages/viewpage.action?pageId=59803037) . |
| 9 | N/A | Đang upload giữa chừng thì bị lỗi | - Khi đang upload object giữa chừng thì bị lỗi, nguyên nhân có thể là do: Rớt mạng Hết quota Upload quá 1000 segment (segment size quá nhỏ) Upload file đơn quá 5 GB (không chia file ra thành các segment nhỏ) <br> - Rớt mạng <br> - Hết quota <br> - Upload quá 1000 segment (segment size quá nhỏ) <br> - Upload file đơn quá 5 GB (không chia file ra thành các segment nhỏ) <br> Kiểm tra các nguyên nhân này để có giải pháp tương ứng. |
| 10 | N/A | Dung lượng lưu trữ trên dịch vụ vStorage không đúng với tổng dung lượng các object cần lưu | - Khi bạn sử dụng các công cụ phía người dùng để tải lên tệp tin lớn (multipart upload), tệp tin được chia thành nhiều segment để tải lên hệ thống vStorage. Trong quá trình tải của tệp tin, có thể có một số segment được tải lên, một số segment không được tải lên do gặp lỗi như network có vấn đề, upload > 1000 segment, công cụ phía người dùng của bạn bị dừng chạy, treo, v.v. Tệp tin khi đó được xem như tải lên không thành công, các segment đã được tải lên được xem như là các incomplete segment hay là segment rác và đang chiếm dụng dung lượng lưu trữ của bạn. <br> - Bạn có thể lựa chọn một số công cụ phía người dùng có hỗ trợ dọn các segment rác này để dọn chúng và giải phóng dung lượng lưu trữ. Danh sách các công cụ người dùng có hỗ trợ dọn segment rác và hướng dẫn dọn, bạn vui lòng tham khảo hướng dẫn sử dụng của từng công cụ bên trong mục  [này](https://docs.vngcloud.vn/pages/viewpage.action?pageId=49649900) . <br> - Tại thời điểm hiện tại, vStorage chưa hỗ trợ tính năng dọn các segment rác này. Chúng tôi đang xem xét giải pháp để hỗ trợ trong tương lai. Hiện tại nếu có vấn đề liên quan đến segment rác, chúng tôi khuyến nghị bạn sử dụng giải pháp dọn rác của các công cụ phía người dùng (client tool). |

\


***

#### Hướng dẫn sử dụng 3rd party software 

Để sử dụng các công cụ phía người dùng (3rd party software), bạn cần cung cấp thông tin chứng thực cho các công cụ này để truy cập vào dịch vụ lưu trữ vStorage. Bạn có thể sử dụng danh tính Service Account để chứng thực khi truy cập vào tài nguyên vStorage thông qua các công cụ mà chúng tôi nêu bên trên. Để sử dụng Service Account, bạn cần khởi tạo S3 key, tài khoản swift thông qua dịch vụ vIAM, chi tiết xem tại [đây.](https://docs.vngcloud.vn/pages/viewpage.action?pageId=59805240)

Sau khi khởi tạo s3 key, tài khoản swift  thông qua dịch vụ vIAM, hãy thu thập thông tin sau để làm thông tin chứng thực khi truy cập dịch vụ vStorage. Nếu bạn không có thông tin này, hãy liên hệ với quản trị viên của tài khoản VNG CLoud.

* Thông tin access key, secret key, project, restriction by IAM của S3 key được tạo nếu có. 
* Thông tin username, password, project, restriction by IAM của tài khoản swift được tạo nếu có.
* Tên người dùng Service Account, Client ID, Client Secret được tạo.

Bạn có thể tìm thấy các thông tin cấu hình một Service account đã tạo này trên hệ thống vIAM. Để biết thêm thông tin, hãy xem tại [đây.](https://docs.vngcloud.vn/vng-cloud-document/vn/identity-and-access-management-iam)

Để truy cập đến dịch vụ lưu trữ vStorage sử dụng thông tin chứng thực thu thập ở trên, hãy xem hướng dẫn chi tiết cách thực hiện của từng công cụ theo chủ đề bên dưới.

***

#### Chủ đề 

* S3cmd
* Cyberduck
* Rclone
* Swift Client
* S3 SDK
* MinIO Client (MC)
* S3 Browser
* AWS CLI

\
