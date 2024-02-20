# 0-create_a_file.pp

# Create a file resource
file { 'school':
  # Ensure the file exists
  ensure  => file,
  # Specify the file path
  path    => '/tmp/school',
  # Set the file permission
  mode    => '0744',
  # Set the file owner and group
  owner   => 'www-data',
  group   => 'www-data',
  # Set the file content
  content => "I love Puppet\n",
}
