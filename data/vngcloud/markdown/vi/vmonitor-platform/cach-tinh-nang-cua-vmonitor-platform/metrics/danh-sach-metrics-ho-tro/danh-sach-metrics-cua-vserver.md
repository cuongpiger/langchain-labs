# Danh sách metrics của vServer

Bên dưới là danh sách metrics của vServer mà chúng tôi hỗ trợ bạn:

| Metric | Unit | Statistic | Có/ Không được xuất hiện trong Dashboard mặc định | Dimensions |
| --- | --- | --- | --- | --- |
| vserver.cpu.utilization_norm_perc | percent | avg | Có | resource_id hostname product zone |
| vserver.io.read_bytes_sec | bytes/s | avg group_by: device | Có | resource_id hostname product zone device |
| vserver.io.read_ops_sec | short | avg group_by: device | Có | resource_id hostname product zone device |
| vserver.io.write_bytes_sec | bytes/s | avg group_by: device | Có | resource_id hostname product zone device |
| vserver.io.write_ops_sec | short | avg group_by: device | Có | resource_id hostname product zone device |
| vserver.io.percent_bytes_total_sec | short | avg group_by: device | Không | resource_id hostname product zone device volume_id volume_name |
| vserver.io.percent_ops_total_sec | short | avg group_by: device | Không | resource_id hostname product zone device volume_id volume_name |
| vserver.net.in_bytes_sec | bytes/s | avg group_by: device | Có | resource_id hostname product zone device |
| vserver.net.in_packets_sec | short | avg group_by: device | Có | resource_id hostname product zone device |
| vserver.net.out_bytes_sec | bytes/s | avg group_by: device | Có | resource_id hostname product zone device |
| vserver.net.out_packets_sec | short | avg group_by: device | Có | resource_id hostname product zone device |

\
