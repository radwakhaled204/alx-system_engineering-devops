# 2-execute_a_command.pp

# Kill the process named killmenow
exec { 'killmenow':
  # Use the pkill command
  command => 'pkill killmenow',
  # Only run the command if the process exists
  onlyif  => 'pgrep killmenow',
  # Set the path for the command execution
  path    => '/bin:/usr/bin',
}
