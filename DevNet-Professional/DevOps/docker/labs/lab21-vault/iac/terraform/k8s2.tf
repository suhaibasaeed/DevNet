###  k8s2 vm
resource "vsphere_virtual_machine" "k8s2" {
  name             = "k8s2"
  resource_pool_id = "${data.vsphere_resource_pool.pool.id}"
  datastore_id     = "${data.vsphere_datastore.datastore.id}"

  num_cpus                   = 2
  memory                     = 8192
  guest_id                   = "ubuntu64Guest"
  wait_for_guest_net_timeout = 0
  wait_for_guest_ip_timeout  = 5
  shutdown_wait_timeout      = 1
  force_power_off            = true

  # eth0 (management)
  network_interface {
    network_id   = "${data.vsphere_network.network.id}"
    adapter_type = "vmxnet3"
  }

  # eth1
  network_interface {
    network_id   = "${data.vsphere_network.vm_network_3.id}"
    adapter_type = "vmxnet3"
  }

  disk {
    label        = "disk0"
    attach       = true
    path         = "k8s2/k8s2.vmdk"
    disk_mode    = "independent_nonpersistent"
    datastore_id = "${data.vsphere_datastore.datastore.id}"
  }

  depends_on = [
    vsphere_host_port_group.pg
  ]

}
