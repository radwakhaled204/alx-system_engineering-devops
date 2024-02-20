# A Puppet manifest to install and configure an Nginx web server

# Install the jfryman-nginx module from Puppet Forge
exec { 'install_nginx_module':
  command => 'puppet module install jfryman-nginx',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  unless  => 'puppet module list | grep nginx',
}

# Declare the nginx class with the desired parameters
class { 'nginx':
  package_ensure => 'latest',
  service_ensure => 'running',
  service_enable => true,
  require        => Exec['install_nginx_module'],
}

# Create a file named hello_world.html in /var/www/html directory
file { '/var/www/html/hello_world.html':
  ensure  => 'file',
  content => 'Hello World!',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

# Modify the default configuration file of Nginx to serve the hello_world.html file
nginx::resource::server { 'default':
  www_root => '/var/www/html',
  index_files => ['hello_world.html'],
}

# Create a file named redirect_me in /var/www/html directory
file { '/var/www/html/redirect_me':
  ensure  => 'file',
  content => 'Redirecting...',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

# Add a rewrite rule for /redirect_me to another page
nginx::resource::location { 'redirect_me':
  server         => 'default',
  location       => '/redirect_me',
  rewrite_rules  => ['^ /not_found.html permanent'],
}
