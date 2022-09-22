#!/bin/bash
# bash -c "$(curl -fsSL '')" 

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install dkms
apt-get install virtualbox-guest-additions
apt-get install build-essential linux-headers-$(uname -r)
apt-get install virtualbox-ose-guest-x11