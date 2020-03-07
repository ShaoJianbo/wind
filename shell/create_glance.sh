# 收集glance-image的信息
image_info=$(glance image-list|grep -v "^$"|grep -v "ID"|awk '{print $2"+"$4}')

function insert_image_info() {
  image_id=$1
  name=$2
  value=$3
  echo "image_id:$image_id, name:$name, value:$value"
  if [[ (-z "$image_id") || (-z "$name") || (-z "$value")  ]]; then
    return 1
  fi
  mysql -e '$use glance;insert into image_properties(image_id,name,value) values("$image_id","$name","$value")'
}

function get_image_os_type() {
  # trove-->os_type:linux
  # mysql5.7, redis:4.0 ==>os_name:centos
  image_name=$1
  echo "image_name==>$image_name"
  mysql_type="mysql"
  redis_type="redis"
  mysql_centos_type="5.7"
  redis_centos_type="4.0"
  os_type="ubuntu"

  if [[ ($image_name =~ $"bastion") || ($image_nanam =~ $"dmp") ]]
  then
    os_type="centos"
  fi

  if [[ ($image_name =~ $"windows")]]
  then
    os_type="windows"
  fi

  if [[ ($image_name =~ $mysql_type) && ($image_name =~ $mysql_centos_type) ]]
  then
    os_type="centos"
  fi

  if [[ ($image_name =~ $redis_type) && ($image_nanam =~ $redis_centos_type) ]]
  then
    os_type="centos"
  fi

  echo $os_type

}

function main(){
# 更新镜像信息

for image_info in ${image_info[@]}; do
  image_id=$(echo $image_info |cut -d'+' -f1)
  image_name=$(echo $image_info | cut -d'+' -f2)
  echo "image_id=>" $image_id "image_name=>" $image_name
  name="os_type"
  value="linux"
  echo "name=>" $name "value=>" $value
  insert_image_info $image_id $name $value

  name="os_name"
  value="os_ubuntu"
  echo "name=>" $name "value=>" $value

  value=$(get_image_os_type image_name)
  insert_image_info $image_id $name $value
done

}

main