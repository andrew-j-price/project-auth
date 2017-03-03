# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define :auth do |config|
    config.vm.box = "centos/7"
    config.vm.hostname = "auth"
    config.vm.boot_timeout = 300
    config.vm.network :private_network, ip: "192.168.56.171", :adapter => 2
    config.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
      vb.cpus = 1
      vb.gui = true
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      vb.customize ["modifyvm", :id, "--ioapic", "on"]
      vb.customize ['modifyvm', :id, '--clipboard', 'bidirectional']
    end
    config.vm.provision "shell", inline: $configure
    config.vm.synced_folder "ansible/", "/root/ansible", :mount_options => ["dmode=755","fmode=664"]
    config.vm.synced_folder "docker/", "/root/docker", :mount_options => ["dmode=755","fmode=664"]
    config.vm.synced_folder "www_apps/", "/var/www/apps", :mount_options => ["dmode=755","fmode=664","uid=48","gid=48"]
  end
end

$configure = <<SCRIPT
  sudo mkdir /root/.ssh/
  sudo cp /vagrant/authorized_keys /root/.ssh/authorized_keys
  cat /vagrant/authorized_keys >> /home/vagrant/.ssh/authorized_keys
  sudo yum install -y epel-release
  sudo yum install -y gcc openssl-devel python-devel python-pip
  sudo pip install ansible
  cd /vagrant/ansible
  ansible-playbook play.yml
SCRIPT
