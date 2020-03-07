echo "This is git tools to get trove codes, by shao"
echo "Start to cleanup old codes"
cur_pwd=$(pwd)
shao_pwd="/home/shao/github"
if [ "$cur_pwd" = "$shao_pwd" ]; then
  rm -rf trove
fi

version="v3.4.3"
echo "Start to git clone codes $version"
echo "ZKUgTmaNmGsB7hDdK45zxra+WErP0Ul9RrgQ1q2/LQ"
git clone http://shaojb@172.16.5.177/cnc_openstack/trove -b $version

echo "Start to git review my codes, input change_id or skip it"
change_id=$1
echo "change_id==>" $change_id
if [ ! -z $change_id ]; then
  cd ./trove
  git review -d $change_id
  cd -
else
  echo $change_id
  echo "skip git review"
fi

echo "start to tar code to swift"
tar -czvf trove-"$version".tar.gz trove
