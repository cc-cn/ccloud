echo cc123456 | sudo -S echo
sudo su -c "sync; echo 1 > /proc/sys/vm/drop_caches"
sudo su -c "sync; echo 2 > /proc/sys/vm/drop_caches"
sudo su -c "sync; echo 3 > /proc/sys/vm/drop_caches"

