# galera 集群压测脚本
# 目的:观察多节点更新同一行数据时->出现死锁
# 解决方法:单节点写入数据,多节点读取数据，放弃高可用
# 数据表特性：表中只有一行数据,在多个节点中分别更新同一行数据
# 数据库事务隔离机制：REPEATABLE-READ


i=1
select_sql="select num from seq_num limit 1;"
while [ $i -le 10000000000 ]
do
    mysql -h 10.1.12.27 -uneutron -pfjgsf92348236 neutron -e "$select_sql;update seq_num set num=($num+$i)";
    mysql -h 10.1.12.26 -uneutron -pfjgsf92348236 neutron -e "$select_sql;update seq_num set num=($num+$i)";
    mysql -h 10.1.12.28 -uneutron -pfjgsf92348236 neutron -e "$select_sql;update seq_num set num=($num+$i)";
    i=$(($i+1))
done