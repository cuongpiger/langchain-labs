# Danh sách metrics của vDB

Bên dưới là danh sách metrics của vDB mà chúng tôi hỗ trợ bạn:

|  |  |  |  |
| --- | --- | --- | --- |
| **Metric (Tên metric)** | **Unit (Đơn vị tính)** | **Có/ Không được xuất hiện trong Dashboard mặc định** | **Dimensions** |
| vdb.cpu.percent | percent | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.cpu.stolen_perc | percent | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.cpu.system_perc | percent | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.cpu.system_time | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.cpu.user_perc | percent | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.cpu.user_time | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.cpu.wait_perc | percent | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.cpu.wait_time | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.disk.inode_used_perc | percent | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.disk.space_used_perc | percent | Có | product: vdb, database_id, database_name, zone, engine, version |
| [vdb.io](http://vdb.io) .read_req_sec | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| [vdb.io](http://vdb.io) .write_req_sec | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.load.avg_15_min | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.load.avg_1_min | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.load.avg_5_min | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mem.free_mb | MB | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mem.swap_free_mb | MB | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mem.swap_free_perc | percent | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mem.swap_total_mb | MB | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mem.swap_used_mb | MB | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mem.total_mb | MB | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mem.usable_mb | MB | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mem.usable_perc | percent | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mem.used_buffers | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mem.used_cache | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mem.used_real_mb | MB | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mem.used_shared | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| [vdb.net](http://vdb.net) .in_bytes_sec | bytes/s | Có | product: vdb, database_id, database_name, zone, engine, version |
| [vdb.net](http://vdb.net) .out_bytes_sec | bytes/s | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.postgresql.buffer_hit | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.postgresql.commits | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.postgresql.connections | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.postgresql.disk_read | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.postgresql.rollbacks | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.postgresql.rows_deleted | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.postgresql.rows_fetched | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.postgresql.rows_inserted | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.postgresql.rows_returned | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.postgresql.rows_updated | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.innodb.buffer_pool_free | bytes | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.innodb.buffer_pool_pages_utilization | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.innodb.buffer_pool_read_requests | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.innodb.buffer_pool_reads | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.innodb.buffer_pool_total | bytes | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.innodb.buffer_pool_used | bytes | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.innodb.data_reads | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.innodb.data_writes | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.innodb.os_log_fsyncs | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.innodb.row_lock_time | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.innodb.row_lock_waits | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| [vdb.mysql.net](http://vdb.mysql.net) .aborted_clients | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| [vdb.mysql.net](http://vdb.mysql.net) .aborted_connects | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| [vdb.mysql.net](http://vdb.mysql.net) .connection_errors_internal | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| [vdb.mysql.net](http://vdb.mysql.net) .connection_errors_max_connections | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| [vdb.mysql.net](http://vdb.mysql.net) .connections | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| [vdb.mysql.net](http://vdb.mysql.net) .max_used_connections | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| [vdb.mysql.net](http://vdb.mysql.net) .threads_connected | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| [vdb.mysql.net](http://vdb.mysql.net) .threads_running | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.com_delete | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.com_delete_multi | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.com_insert | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.com_insert_select | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.com_replace_select | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.com_select | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.com_update | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.com_update_multi | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.created_tmp_disk_tables | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.created_tmp_files | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.created_tmp_tables | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.open_files | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.qcache_hits | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.queries | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.questions | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.slow_queries | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.performance.table_locks_waited | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.mysql.status | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.aof.last_rewrite_time_sec | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.aof.rewrite_in_progress | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.clients.blocked | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.clients.connected | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.cpu.sys | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.cpu.sys_children | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.cpu.user | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.cpu.user_children | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| [vdb.redis.info](http://vdb.redis.info) .latency_ms | ms | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.mem.fragmentation_ratio | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.mem.lua | bytes | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.mem.maxmemory | bytes | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.mem.peak | bytes | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.mem.rss | bytes | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.mem.total | bytes | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.mem.used | bytes | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.rdb.bgsave_in_progress | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.rdb.changes_since_last_save | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.rdb.last_bgsave_time_sec | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.repl.connected_slaves | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.server.hz | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.server.lru_clock | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.server.uptime_in_days | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.server.uptime_in_seconds | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.commands_processed_rate | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.evicted_keys | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.evicted_keys_rate | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.expired_keys | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.expired_keys_rate | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.keyspace_hits | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.keyspace_hits_rate | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.keyspace_misses | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.keyspace_misses_rate | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.latest_fork_usec | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.pubsub_channels | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.pubsub_patterns | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.rejected_connections | short | Có | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.total_commands_processed | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.total_connections_received | short | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.total_net_input_bytes | bytes | Không | product: vdb, database_id, database_name, zone, engine, version |
| vdb.redis.stats.total_net_output_bytes | bytes | Không | product: vdb, database_id, database_name, zone, engine, version |

\
