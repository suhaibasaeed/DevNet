resource "ciscoasa_network_object" "ssh_jumphost" {
  name  = "ssh_jumphost"
  value = "192.168.1.1"
}
resource "ciscoasa_network_object" "ssh_jumphost_range" {
  name  = "ssh_jumphost_range"
  value = "192.168.1.1-192.168.1.5"
}
resource "ciscoasa_network_object" "ssh_jumphost_subnet" {
  name  = "ssh_jumphost_subnet"
  value = "192.168.1.0/24"
}
