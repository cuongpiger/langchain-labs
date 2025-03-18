# Danh sách metrics của Host

### Linux OS

| Linux Metric | Metric (Tên metric) | Unit (Đơn vị tính), Loại OS hỗ trợ |
| --- | --- | --- |
| CPU (22 metrics) | Prefix sẽ là cpu.<tên_metric>, tên metric bao gồm: |  |
|  | time_user | float |
|  | time_system | float |
|  | time_idle | float |
|  | time_active | float |
|  | time_nice | float |
|  | time_iowait | float |
|  | time_irq | float |
|  | time_softirq | float |
|  | time_steal | float |
|  | time_guest | float |
|  | time_guest_nice | float |
|  | usage_user | float, percent |
|  | usage_system | float, percent |
|  | usage_idle | float, percent |
|  | usage_active | float |
|  | usage_nice | float, percent |
|  | usage_iowait | float, percent |
|  | usage_irq | float, percent |
|  | usage_softirq | float, percent |
|  | usage_steal | float, percent |
|  | usage_guest | float, percent |
|  | usage_guest_nice | float, percent |
| DISK (7 metrics) | Prefix sẽ có dạng disk.<tên_metric>, tên metric sẽ bao gồm: |  |
|  | free | integer, bytes |
|  | total | integer, bytes |
|  | used | integer, bytes |
|  | used_percent | float, percent |
|  | inodes_free | integer, files |
|  | inodes_total | integer, files |
|  | inodes_used | integer, files |
| DISKIO (11 metrics) | Prefix sẽ có dạng diskio.<tên_metric>, tên metric sẽ bao gồm: |  |
|  | reads | integer, counter |
|  | writes | integer, counter |
|  | read_bytes | integer, counter, bytes |
|  | write_bytes | integer, counter, bytes |
|  | read_time | integer, counter, milliseconds |
|  | write_time | integer, counter, milliseconds |
|  | io_time | integer, counter, milliseconds |
|  | weighted_io_time | integer, counter, milliseconds |
|  | iops_in_progress | integer, gauge |
|  | merged_reads | integer, counter |
|  | merged_writes | integer, counter |
| KERNEL (7 metrics) | Prefix sẽ có dạng kernel.<tên_metric>, tên metric và dimension tương ứng sẽ bao gồm: |  |
|  | boot_time | integer, seconds since epoch, btime |
|  | context_switches | integer, ctxt |
|  | disk_pages_in | integer, page |
|  | disk_pages_out | integer, page |
|  | interrupts | integer, intr |
|  | processes_forked | integer, processes |
|  | entropy_avail | integer, entropy_available |
| MEM (34 metrics) | Prefix sẽ có dạng mem.<tên_metric>, tên metric tương ứng loại OS hỗ trợ sẽ bao gồm: |  |
|  | active | integer, Darwin, FreeBSD, Linux, OpenBSD |
|  | available | integer |
|  | available_percent | float |
|  | buffered | integer, FreeBSD, Linux |
|  | cached | integer, FreeBSD, Linux, OpenBSD |
|  | commit_limit | integer, Linux |
|  | committed_as | integer, Linux |
|  | dirty | integer, Linux |
|  | free | integer, Darwin, FreeBSD, Linux, OpenBSD |
|  | high_free | integer, Linux |
|  | high_total | integer, Linux |
|  | huge_pages_free | integer, Linux |
|  | huge_page_size | integer, Linux |
|  | huge_pages_total | integer, Linux |
|  | inactive | integer, Darwin, FreeBSD, Linux, OpenBSD |
|  | laundry | integer, FreeBSD |
|  | low_free | integer, Linux |
|  | low_total | integer, Linux |
|  | mapped | integer, Linux |
|  | page_tables | integer, Linux |
|  | shared | integer, Linux |
|  | slab | integer, Linux |
|  | sreclaimable | integer, Linux |
|  | sunreclaim | integer, Linux |
|  | swap_cached | integer, Linux |
|  | swap_free | integer, Linux |
|  | swap_total | integer, Linux |
|  | total | integer |
|  | used | integer |
|  | used_percent | float |
|  | vmalloc_chunk | integer, Linux |
|  | vmalloc_total | integer, Linux |
|  | vmalloc_used | integer, Linux |
|  | wired | integer, Darwin, FreeBSD, OpenBSD |
|  | write_back | integer, Linux |
|  | write_back_tmp | integer, Linux |
| PROCESSES (11 metrics) | Prefix sẽ có dạng processes.<tên_metric>, tên metric kèm loại OS hỗ trợ sẽ bao gồm |  |
|  | blocked | aka disk sleep or uninterruptible sleep |
|  | running | N/A |
|  | sleeping | N/A |
|  | stopped | N/A |
|  | total | N/A |
|  | zombie | N/A |
|  | dead | N/A |
|  | wait | freebsd only |
|  | idle | bsd and Linux 4+ only |
|  | paging | linux only |
|  | parked | linux only |
|  | total_threads | linux only |
| SWAP (6 metrics) | Prefix sẽ có dạng swap.<tên_metric>, tên metric sẽ bao gồm: |  |
|  | free | int, bytes |
|  | total | int, bytes |
|  | used | int, bytes |
|  | used_percent | float, percent |
|  | in | int, bytes |
|  | out | int, bytes |
| SYSTEM (7 metrics) | Prefix sẽ có dạng system.<tên_metric>, tên metric sẽ bao gồm: |  |
|  | load1 | float |
|  | load15 | float |
|  | load5 | float |
|  | n_users | integer |
|  | n_cpus | integer |
|  | uptime | integer, seconds |
|  | uptime_format | string, deprecated in 1.10, use uptime field |
| NET (8 metrics) | Prefix sẽ có dạng net.<tên_metric>, tên metric sẽ bao gồm: |  |
|  | bytes_sent | N/A |
|  | bytes_recv | N/A |
|  | packets_sent | N/A |
|  | packets_recv | N/A |
|  | err_in | N/A |
|  | err_out | N/A |
|  | drop_in | N/A |
|  | drop_out | N/A |

***

### Windows OS

|  |  |
| --- | --- |
| **Window Metric** | **Metric (Tên metric)** |
| Processor | Prefix sẽ có dạng win_cpu.<tên_metric>, tên metric sẽ bao gồm: |
|  | win_cpu.Percent_DPC_Time |
|  | win_cpu.Percent_Idle_Time |
|  | win_cpu.Percent_Interrupt_Time |
|  | win_cpu.Percent_Privileged_Time |
|  | win_cpu.Percent_Processor_Time |
|  | win_cpu.Percent_User_Time |
| Win_Disk | Prefix sẽ có dạng win_disk.<tên_metric>, tên metric sẽ bao gồm: |
|  | win_disk.Current_Disk_Queue_Length |
|  | win_disk.Free_Megabytes |
|  | win_disk.Percent_Disk_Read_Time |
|  | win_disk.Percent_Disk_Time |
|  | win_disk.Percent_Disk_Write_Time |
|  | win_disk.Percent_Free_Space |
|  | win_disk.Percent_Idle_Time |
| Win_DiskIO | Prefix sẽ có dạng win_diskio.<tên_metric>, tên metric sẽ bao gồm: |
|  | win_diskio.Current_Disk_Queue_Length |
|  | win_diskio.Disk_Read_Bytes_persec |
|  | win_diskio.Disk_Reads_persec |
|  | win_diskio.Disk_Write_Bytes_persec |
|  | win_diskio.Disk_Writes_persec |
|  | win_diskio.Percent_Disk_Read_Time |
|  | win_diskio.Percent_Disk_Time |
|  | win_diskio.Percent_Disk_Write_Time |
| Network Interface | Prefix sẽ có dạng win_net.<tên_metric>, tên metric sẽ bao gồm: |
|  | win_net.Bytes_Received_persec |
|  | win_net.Bytes_Sent_persec |
|  | win_net.Packets_Outbound_Discarded |
|  | win_net.Packets_Outbound_Errors |
|  | win_net.Packets_Received_Discarded |
|  | win_net.Packets_Received_Errors |
|  | win_net.Packets_Received_persec |
|  | win_net.Packets_Sent_persec |
| System | Prefix sẽ có dạng win_system.<tên_metric>, tên metric sẽ bao gồm: |
|  | win_system.Context_Switches_persec |
|  | win_system.Processor_Queue_Length |
|  | win_system.System_Calls_persec |
|  | win_system.System_Up_Time |
| Memory | Prefix sẽ có dạng win_mem.<tên_metric>, tên metric sẽ bao gồm: |
|  | win_mem.Available_Bytes |
|  | win_mem.Cache_Faults_persec |
|  | win_mem.Demand_Zero_Faults_persec |
|  | win_mem.Page_Faults_persec |
|  | win_mem.Pages_persec |
|  | win_mem.Pool_Nonpaged_Bytes |
|  | win_mem.Pool_Paged_Bytes |
|  | win_mem.Standby_Cache_Core_Bytes |
|  | win_mem.Standby_Cache_Normal_Priority_Bytes |
|  | win_mem.Standby_Cache_Reserve_Bytes |
| Paging File | Prefix sẽ có dạng win_swap.<tên_metric>, tên metric sẽ bao gồm: |
|  | win_swap.Percent_Usage |

\
