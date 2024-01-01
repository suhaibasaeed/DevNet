###  csr1kv2 vm
resource "vsphere_virtual_machine" "csr1kv2" {
  name             = "csr1kv2"
  resource_pool_id = "${data.vsphere_resource_pool.pool.id}"
  datastore_id     = "${data.vsphere_datastore.datastore.id}"

  num_cpus                   = 4
  memory                     = 4096
  guest_id                   = "other26xLinux64Guest"
  wait_for_guest_net_timeout = 0
  wait_for_guest_ip_timeout  = 5
  shutdown_wait_timeout      = 1
  force_power_off            = true

  # Gi1
  network_interface {
    network_id   = "${data.vsphere_network.vm_network_3.id}"
    adapter_type = "vmxnet3"
  }

  # Gi2
  network_interface {
    network_id   = "${data.vsphere_network.vm_network_5.id}"
    adapter_type = "vmxnet3"
  }

  # Gi3
  network_interface {
    network_id   = "${data.vsphere_network.vm_network_2.id}"
    adapter_type = "vmxnet3"
  }

  # Gi4 (not connected in topology, declared to preserve ordering)
  network_interface {
    network_id   = "${data.vsphere_network.vm_network_0.id}"
    adapter_type = "vmxnet3"
  }

  # Gi5 (management)
  network_interface {
    network_id   = "${data.vsphere_network.network.id}"
    adapter_type = "vmxnet3"
  }

  cdrom {
    datastore_id = "${data.vsphere_datastore.datastore.id}"
    path         = "csr1kv2/bootstrap.iso"
  }

  disk {
    label        = "disk0"
    attach       = true
    path         = "csr1kv2/csr.vmdk"
    disk_mode    = "independent_nonpersistent"
    datastore_id = "${data.vsphere_datastore.datastore.id}"
  }

  depends_on = [
    vsphere_host_port_group.pg
  ]

}
