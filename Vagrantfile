# -*- mode: ruby -*-
# vi: set ft=ruby :

#
# Memrise scraper
#

Vagrant.configure("2") do |config|
    config.vm.define "Memrise-scraper" do |foo|
    end

    # base box
    config.vm.box = "ubuntu/trusty64"

    # virtualbox
    config.vm.provider "virtualbox" do |v|
        v.memory = 1024
        v.cpus = 2
    end

    # static IP
    config.vm.network "private_network", ip: "10.0.0.10"

    # provisioned files
    config.vm.provision "file", source: "~/.gitconfig", destination: ".gitconfig"
    config.vm.provision "file", source: "vagrant/bash_aliases", destination: ".bash_aliases"
    config.vm.provision "file", source: "vagrant/exrc", destination: ".exrc"
    config.vm.provision "file", source: "vagrant/inputrc", destination: ".inputrc"

    # provisioning script
    config.vm.provision :ansible_local do |ansible|
        ansible.provisioning_path = "/vagrant/vagrant"
        ansible.playbook = "playbook.yml"
        ansible.limit = "all"
    end
end
