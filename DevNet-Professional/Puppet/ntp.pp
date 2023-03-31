ntp_server { '8.8.8.8':
  ensure => 'absent',
  key    => 1,
  minpoll => 4,
  maxpoll => 4,
}
