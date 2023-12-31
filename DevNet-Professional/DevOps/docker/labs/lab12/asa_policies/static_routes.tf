resource "ciscoasa_static_route" "management_static_route" {
  interface = "management"
  network   = "192.168.255.255/32"
  gateway   = "10.99.0.1"
}

