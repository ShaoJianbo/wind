#!/bin/bash
# 保留天数
RESERVE_DAYS=7
function clean_trove_instalce() {
  TMP_RES_INFO_FILE=/tmp/trove_res_info.txt
  source /root/keystonerc_trove
  # 输出trove list到临时文件
  trove list >$TMP_RES_INFO_FILE
  comp_date=$(date -d "-$RESERVE_DAYS days" +%Y%m%d)
  echo "Delete instance created before" $comp_date "..."

  # 读取|开头，简单过滤DoNotDelete关键字，且不是| Group ID开头的记录
  # 清理无DoNotDelete, DTS_DTLE, DMP_CLUSTER关键字且超过保留时间的实例
  cat $TMP_RES_INFO_FILE | grep '^|.*' | grep -vE '(DoNotDelete|DTS_DTLE|DMP_CLUSTER)' | grep -v '^| Group ID' | while read LINE_RES; do
    # 以|分割读取所需字段
    group_id=$(echo $LINE_RES | cut -d '|' -f 2)
    str_create_time=$(echo $LINE_RES | cut -d '|' -f 6)
    create_time=$(date "+%Y%m%d" -d $str_create_time)
    if [ "$create_time" -lt "$comp_date" ]; then
      echo "Instance $group_id created time $create_time < compared time $comp_date"
      echo "trove delete $group_id"
      trove delete $group_id
    fi
  done
}
function clean_nova_server() {
  # 清理trove中存在的nova主机
  # 安全起见，这里只删除trove中有记录并且标识为已经删除的nova主机
  TMP_TROVE_NOVA_FILE=/tmp/trove_dba_nova_servers.txt
  TMP_TROVE_NOVA_DELETED_FILE=/tmp/trove_nova_deleted.txt
  source /root/keystonerc_trove && nova list >$TMP_TROVE_NOVA_FILE
  mysql trove -e "select compute_instance_id from instances ins where compute_instance_id is not NULL and not exists(select 1 from group_menbers gm where gm.instance_id=ins.id and gm.deleted=0);" >$TMP_TROVE_NOVA_DELETED_FILE
  cat $TMP_TROVE_NOVA_FILE | grep '^|.*' | grep -v '^| ID' | while read LINE_RES; do
    nova_id=$(echo $LINE_RES | cut -d '|' -f 2)
    grep $nova_id $TMP_TROVE_NOVA_DELETED_FILE
    if [ $? == 0 ]; then
      echo "nova_id: $nova_id already deleted in trove db, exists in $TMP_TROVE_NOVA_DELETED_FILE"
      echo "nova delete $nova_id"
      nova delete $nova_id
    fi
  done
}

fucntion clean_cinder(){
  # 清理error卷和avalibale卷(有可能勿删除)
  cinder list |grep 'error' | awk '{print $2}' |while read i; do cinder delete $i; done
  cinder list |grep 'available' | awk '{print $2}' | while read i; do cinder delete $i; done
}

function clean_mysql_dirty_data(){
  # 清理mysql数据库中的脏字源
}
function clean_glance(){
  # 清理glance镜像
}

clean_trove_instalce
clean_nova_server
clean_cinder
clean_mysql
clean_glacne