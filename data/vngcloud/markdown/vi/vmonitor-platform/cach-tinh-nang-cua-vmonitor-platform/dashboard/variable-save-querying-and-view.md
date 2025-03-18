# Variable, Save Querying and View

ariable

**Variable** cho phép bạn vẽ các thông tin theo dõi ở dashboard một cách linh động hơn, chỉ từ 1 dashboard bạn có thể chọn giá trị cho variable để xem thông tin của nhiều đối tượng khác nhau

Để có thể tạo variable bạn vào 1 dashboard, hãy làm theo hướng dẫn bên dưới:

1. Truy cập vào Dashboard bạn muốn tạo Variable, chọn **Create a variable**.
2. Chọn **Add a variable**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(81).png?raw=true)

3\. Chọn/ nhập các thông tin bao gồm:

* **Dimension Key**: lựa chọn dimension key sẽ cung cấp danh sách giá trị cho variable của bạn, ví dụ hostname
* **Name**: đặt tên cho variable, hệ thống sẽ tự động sinh ra phù hợp với tên dimension key bạn chọn
* **Filter**: bạn có thể filter tập giá trị của variable này với các dimension key hoặc variablekhác
* **Default value**: giá trị mặc định cho variable
* **Vaules**: danh sách các giá trị của variable, được lấy từ dimension key bạn đã chọn ở trên

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(82).png?raw=true)

Giả sử ở đây chúng ta chọn dimension key là **hostname,** bạn sẽ thấy các giá trị của variable sẽ có, chính là danh sách tất cả các host trong hệ thống, tại đây bạn có thể chọn **Dynamic by time range** để hệ thống tự động lấy tất cả hostname theo time range bạn chọn, hoặc chọn cố định các hostname như danh sách được hiển thị trong danh sách. Để tối ưu hơn chúng tôi khuyến khích bạn nên sử dụng **Dynamic by time range**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(83).png?raw=true)

4\. Để ứng dụng variable này cho các widget, bạn có thể tự thêm bằng cách add/edit widget và thêm vào chỗ filter, hoặc sử dụng tính năng tự động thêm tại đây, khi bạn nhấn + hệ thống sẽ tự thêm tất cả widget trong dashboard sử dụng variable này, tương tự là - sẽ tự động bỏ đi

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(84).png?raw=true)

5\. Sau đó nhấn "**Save**" để tạo variable

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(85).png?raw=true)

Bạn có thể thấy khi sử dụng tính năng tự động thêm ( + ) thì các widget trong dashboard sẽ tự động thêm $hostname vào filter, tuy nhiên khi sử dụng tính năng này bạn cũng cần xem xét lại danh sách dimension lựa chọn có hợp lý hay không để điều chỉnh phù hợp. 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(86).png?raw=true)

Nếu không dùng tính năng tự động thêm thì bạn có thể tự thêm vào filter như bình thường, hệ thống sẽ hiển thị variable như 1 dimension key

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(87).png?raw=true)

Khi biến tạo thành công variable bạn sẽ thấy variable hiển thị ở dashboard và có thể lựa chọn giá trị để hiển thị dashboard theo giá trị được chọn

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(88).png?raw=true)

Từ đây bạn có thể chọn các host khác nhau để theo dõi thông số rất linh động mà không cần phải tạo hay xem nhiều dashboard.

***

### View

**View** cho phép bạn tạo các góc nhìn cho dashboard, mà sẽ lưu các giá trị của variable để sử dụng sau này.

Để có thể tạo **View** cho 1 dashboard, hãy làm theo hướng dẫn bên dưới:

1. Sau khi có variable và bạn muốn lưu giá trị variable để tiện truy cập sau này, thì bạn sử dụng tính năng **View,** nhấn "Save views" để lưu lại

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(89).png?raw=true)

2\. Đặt tên cho view và khi bạn chọn view này hệ thống sẽ tự động điền danh sách variables bên dưới

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(90).png?raw=true)

3\. Sau khi tạo thành công view bạn sẽ thấy danh sách view để bạn lựa chọn, giả sử ở đây có 2 view là: host-storagegw và host-nginx

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(91).png?raw=true)

4\. Khi bạn chọn view: host-nginx thì sẽ hệ thống sẽ tự động tải danh sách và giá trị khác cho variable

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(92).png?raw=true)

5\. Để quản lý View và Variable bạn có thể nhấn vào hình răng cưa:

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(93).png?raw=true)

***

### Save query

vMonitor Platform cung cấp cho bạn khả năng tái sử dụng lại một query mà bạn đã tạo trước đó thông qua tính năng Save query mà chúng tôi cung cấp. 

#### Save query

Để lưu một query, hãy làm theo hướng dẫn bên dưới:

1. Tại vùng chứa câu lệnh truy vấn, chọn icon **Save**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(94).png?raw=true)

2\. Nhập **Query name**.

3\. Chọn **Save**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(95).png?raw=true)

Lúc này query đã được lưu trữ với tên gợi nhớ mà bạn nhập. 

#### Tái sử dụng query đã có

Sau khi bạn đã thực hiện lưu query, bạn có thể tái sử dụng query này bằng cách: 

1. Tại vùng chứa câu lệnh truy vấn, chọn biểu tượng sổ xuống (biểu tượng này nằm bên cạnh biểu tượng Save query.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(96).png?raw=true)

2. Lúc này hệ thống hiển thị danh sách query đã lưu, bạn có thể tái sử dụng bằng cách chọn query đó. 

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(97).png?raw=true)

3\. Bạn có thể chỉnh sửa query này và lưu trữ chúng thành một query mới độc lập với query mà bạn tái sử dụng bằng cách chọn Save as new query.

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(98).png?raw=true)

#### Quản lý query

Bạn có thể xem các query đang được lưu trữ hoặc xóa một query bằng cách chọn Manage saved queries và chọn biểu tượng **Xóa**

![Image](https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets/image%20(99).png?raw=true)

\


\
