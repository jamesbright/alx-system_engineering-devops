# execute a command to kill a process
exec { 'pkill':
  command => 'pkill -f killmenow',
  path    => '/usr/bin'
}
