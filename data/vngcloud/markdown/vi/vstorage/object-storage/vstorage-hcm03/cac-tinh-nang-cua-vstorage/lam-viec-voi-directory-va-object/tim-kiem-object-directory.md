# Tìm kiếm object/ directory

Sau khi tạo container và tải lên tệp tin vào container đó, bạn có thể tìm kiếm object/ directory thông qua:



{% tabs %}
{% tab title="Sử dụng vStorage Portal" %}


1. Đăng nhập vào [https://vstorage.console.vngcloud.vn](https://vstorage.console.vngcloud.vn/storage/list).
2. Chọn **project** và **container** mà bạn muốn thực hiện tìm kiếm object/ directory.
3. Tại ô **Search directories and objects**, bạn có thể thực hiện tìm kiếm object/ directory theo các cách sau:
   1. Nếu bạn muốn tìm kiếm object theo tiền tố:
      1. Chọn Search by **Name match by prefix**
      2. Nhập chuỗi ký tự là tiền tố bạn muốn tìm kiếm. 
      3. Nhấn **Enter** hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/64553917/image2023-9-15\_15-53-6.png?version=1\&modificationDate=1694767987000\&api=v2).
   2. Nếu bạn muốn tìm kiếm theo một chuỗi ký tự bất kỳ được chứa trong tên object:
      1. Chọn Search by **Name match phrase**
      2. Nhập chuỗi ký tự là tiền tố bạn muốn tìm kiếm. 
      3. Nhấn **Enter** hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/64553917/image2023-9-15\_15-53-6.png?version=1\&modificationDate=1694767987000\&api=v2).
   3. Nếu bạn muốn tìm kiếm theo toàn bộ tên object: 
      1. Chọn Search by **Name match all**
      2. Nhập chuỗi ký tự là tiền tố bạn muốn tìm kiếm. 
      3. Nhấn **Enter** hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/64553917/image2023-9-15\_15-53-6.png?version=1\&modificationDate=1694767987000\&api=v2).
   4. Nếu bạn muốn tìm kiếm theo thông tin tags của object:\

      1. Chọn Search by **Tags**
      2. Nhập chuỗi ký tự là tiền tố bạn muốn tìm kiếm. 
      3. Nhấn **Enter** hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/64553917/image2023-9-15\_15-53-6.png?version=1\&modificationDate=1694767987000\&api=v2).

Ví dụ: nếu bạn muốn tìm kiếm các object có điểm chung là tiền tố trong tên object là **file** thì bạn cần thực hiện:

* Chọn Search by **Name match by prefix**
* Nhập tiền tố **file**
* Nhấn **Enter** hoặc chọn biểu tượng ![](https://docs.vngcloud.vn/download/thumbnails/64553917/image2023-9-15\_15-53-6.png?version=1\&modificationDate=1694767987000\&api=v2)

Bạn có thể tìm hiểu thêm cách chúng tôi tìm kiếm kết quả Search theo mỗi phương thức tại bảng bên dưới:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **STT** | **Phương thức (Search by)** | **Cú pháp mẫu** | **Kết quả tìm kiếm** | **Giải thích ý nghĩa** |
| 1 | Name match all | Name match all  **abc.txt**  (object nằm trong container) Name match all  **directoryA/abc.txt**  (object nằm trong directoryA) | **abc.txt**  có phân biệt hoa thường. | Tìm kiếm bằng cách so sánh chuỗi ký tự nhập vào với toàn bộ tên object. |
| 2 | Name match by prefix | Name match by prefix  **abc**  (object nằm trong container) Name match by prefix  **directoryA/abc**  (object nằm trong directoryA) | **abc1, abc2** ,…có phân biệt hoa thường. | Tìm kiếm bằng cách so sánh chuỗi ký tự nhập vào với tiền tố của tên object. |
| 3 | Name match phase | Name match phase  **abc**  (object nằm trong container) Name match phase  **directoryA/abc**  (object nằm trong directoryA) | **abc1.exe, xabce.ill, 1abc.gif,** …có phân biệt hoa thường. | Tìm kiếm bằng cách so sánh chuỗi ký tự nhập có được chứa trong tên object. |
| 4 | Name match by wildcard | Name match by wildcard  **ab*c**  (object nằm trong container) Name match by wildcard  **?abc?**  (object nằm trong container) Name match by wildcard  **abc*.?xt**  (object nằm trong container) Name match by wildcard  **ab\*c.txt**  (object nằm trong container) Name match by wildcard  **directoryA/ab*c**  (object nằm trong directoryA) Name match by wildcard  **directoryA/?abc?**  (object nằm trong directoryA) Name match by wildcard  **directoryA/abc*.?xt**  (object nằm trong directoryA) Name match by wildcard  **directoryA/ab\*c.txt**  (object nằm trong directoryA) | **abc, abdc, ab)c, abUUc, ab&-Bc** …có phân biệt hoa thường. **1abcx, -abc*, 1abcD,…**  có phân biệt hoa thường. **abc.txt, abc123.^xt,** … có phân biệt hoa thường. **ab*c.txt**  có phân biệt hoa thường. | ***** : 0 tới n ký tự bất kỳ, ký tự này có thể là chữ cái in hoa, in thường, ký tự số hoặc ký tự đặc biệt. **?** : 1 ký tự bất kỳ, ký tự này có thể là chữ cái in hoa, in thường, ký tự số hoặc ký tự đặc biệt. **\** *,  **\** ?: ký tự *, ? lúc này được coi là một ký tự trong bình thường, không phải là toán tử đại diện sử dụng để search. |
| 5 | Name match by regex | Name match by regex  **ab.**  (object nằm trong container) Name match by regex  **directoryA/ab.**  (object nằm trong directoryA) | **ab1,ab2,ab3, abx, ab*,** … có phân biệt hoa thường. | **.** : 1 ký tự bất kỳ, ký tự này có thể là chữ cái in hoa, in thường, ký tự số hoặc ký tự đặc biệt. |
| 5 | Name match by regex | Name match by regex  **abc?**  (object nằm trong container) Name match by regex  **directoryA/abc?**  (object nằm trong directoryA) | **ab, abc**  có phân biệt hoa thường. | **?** : không lặp lại ký tự liền kề gần nhất hoặc lặp lại ký tự gần nhất 1 lần. |
| 5 | Name match by regex | Name match by regex  **ab+**  (object nằm trong container) Name match by regex  **directoryA/ab+**  (object nằm trong directoryA) | **ab, abb, abbb** ,… có phân biệt hoa thường. | **+** : lặp lại ký tự liền kề gần nhất 1 hoặc nhiều lần. |
| 5 | Name match by regex | Name match by regex  **ab***  (object nằm trong container) Name match by regex  **directoryA/ab***  (object nằm trong directoryA) | **a, ab, abb, abbb** ,… có phân biệt hoa thường. | ***** : không lặp lại ký tự liền kề gần nhất hoặc lặp lại ký tự gần nhất 1 hoặc nhiều lần. |
| 5 | Name match by regex | Name match by regex  **a{2}**  (object nằm trong container) Name match by regex  **directoryA/a{2}**  (object nằm trong directoryA) Name match by regex  **a{2,4}**  (object nằm trong container) Name match by regex  **directoryA/a{2,4}**  (object nằm trong directoryA) Name match by regex  **a{2,}**  (object nằm trong container) Name match by regex  **directoryA/a{2,}**  (object nằm trong directoryA) | **aa**  có phân biệt hoa thường. **aa, aaa, aaaa**  có phân biệt hoa thường. **aa, aaa, aaaa, aaaaa,** … có phân biệt hoa thường. | {}: số ký tự tối thiếu và tối đa mà ký tự liền kề gần nhất lặp lại. **Hạn chế sử dụng số lớn trong ngoặc** |
| 5 | Name match by regex | Name match by regex  **abc|xyz**  (object nằm trong container) Name match by regex  **directoryA/abc|xyz**  (object nằm trong directoryA) | **abc, xyz**  có phân biệt hoa thường. | | hoặc. |
| 5 | Name match by regex | Name match by regex Name match by regex  **abc(xyz)**  (object nằm trong container) Name match by regex  **directoryA/abc(xyz)**  (object nằm trong directoryA) | **abc, abcxyz**  có phân biệt hoa thường. | () hoặc tồn tại. |
| 5 | Name match by regex | Name match by regex  **[abc]**  (object nằm trong container) Name match by regex  **directoryA/ [abc]**  (object nằm trong directoryA) Name match by regex  **[a-d]**  (object nằm trong container) Name match by regex  **directoryA/ [a-d]**  (object nằm trong directoryA) Name match by regex  **[^abc\-]**  (object nằm trong container) Name match by regex  **directoryA/ [^abc\-]**  (object nằm trong directoryA) | **a, b, c**  có phân biệt hoa thường. **a, b, c, d**  có phân biệt hoa thường. **khác a, b, c, hoặc -**  có phân biệt hoa thường. | [ ] một trong các ký tự trong ngoặc. ^: ngoại trừ \: hoặc |
| 5 | Name match by regex | Name match by regex  **a{2,6}+d?*** Name match by regex  **directoryA/ a{2,6}+d?*** Name match by regex  **directoryA{2,6}+d?*/ a{2,6}+d?*/ a{2,6}+d?*** | **aaaaaaa, aaaaaaaaaaaaddddd,** … có phân biệt hoa thường. | Sử dụng lồng các toán tử lại trong một cú pháp tìm kiếm regex. |
| 6 | Tags | Tags  **abc** | Object, directory có tags chính xác là abc | Tìm kiếm bằng tags được thiết lập trên object. |
{% endtab %}

{% tab title="Sử dụng vStorage API" %}
Ngoài cổng giao diện quản lý truyền thống, chúng tôi cũng cung cấp API cho phép bạn tích hợp với các ứng dụng, công cụ phía người dùng của bạn với vStorage để lưu trữ dữ liệu.

Để tìm kiếm object/ directory qua vStorage API, hãy xem [API Developers](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/api-developers).
{% endtab %}

{% tab title="Sử dụng 3rd party softwares" %}
vStorage cũng tương thích với các công cụ phía người dùng sử dụng S3 protocol. Bạn có thể dễ dàng sử dụng các công cụ đã quen thuộc như Rclone, s3cmd, Cyberduck,...Hãy xem [3rd party softwares](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/3rd-party-softwares) và sử dụng các công cụ này. 

Để tìm kiếm object/ directory qua 3rd party software, hãy xem [3rd party softwares](https://docs.vngcloud.vn/vng-cloud-document/vn/vstorage/object-storage/vstorage-hcm03/3rd-party-softwares).
{% endtab %}
{% endtabs %}
