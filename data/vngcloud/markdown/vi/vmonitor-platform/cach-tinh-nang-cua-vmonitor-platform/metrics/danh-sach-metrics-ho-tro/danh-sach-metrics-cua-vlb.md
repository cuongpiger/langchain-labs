# Danh sách metrics của vLB

Bên dưới là danh sách metrics của vLB mà chúng tôi hỗ trợ bạn:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Metric (Tên metric)** | **Unit (Đơn vị tính)** | **Trạng thái** | **Có/ Không được xuất hiện trong Dashboard mặc định L7** | **Có/ Không được xuất hiện trong Dashboard mặc định L14** | **Dimensions** |
| vlb.listener.bin | short | Đang hoạt động | Có | Có | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.bout | short | Đang hoạt động | Có | Có | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.conn_rate | short | Đang hoạt động | Có | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.dcon | short | Đang hoạt động | Không | Có | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.dreq | short | Đang hoạt động | Có | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.ereq | short | Đang hoạt động | Có | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.hrsp_1xx | short | Đang hoạt động | Có | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.hrsp_2xx | short | Đang hoạt động | Có | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.hrsp_3xx | short | Đang hoạt động | Có | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.hrsp_4xx | short | Đang hoạt động | Có | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.hrsp_5xx | short | Đang hoạt động | Có | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.rate | short | Đang hoạt động | Có | Có | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.req_rate | short | Đang hoạt động | Có | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.scur | short | Đang hoạt động | Có | Có | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.listener.slim | short | Đang hoạt động | Có | Có | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, listener_id, listener_name |
| vlb.pool.bin | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.pool.bout | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.pool.dreq | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.pool.dresp | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.pool.econ | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.pool.eresp | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.pool.hrsp_1xx | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.pool.hrsp_2xx | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.pool.hrsp_3xx | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.pool.hrsp_4xx | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.pool.hrsp_5xx | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.pool.rate | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.pool.rtime | short | Đang hoạt động | Có | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.pool.scur | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name |
| vlb.member.bin | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.bout | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.dresp | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.econ | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.eresp | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.hrsp_1xx | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.hrsp_2xx | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.hrsp_3xx | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.hrsp_4xx | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.hrsp_5xx | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.rate | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.rtime | short | Đang hoạt động | Có | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.scur | short | Đang hoạt động | Không | Không | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.status_down | short | Đang hoạt động | Có | Có | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
| vlb.member.status_up | short | Đang hoạt động | Có | Có | product: vlb, loadbalancer_id, loadbalancer_name, zone, layer, role, pool_id, pool_name, member_id |
