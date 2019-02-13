#!/usr/bin/env bash

get_conf() {
    lscpu | sed 's/: */=/g' | grep -v "Flags"
}

build_conn() {
    echo "Building connection module ..."
    git clone https://github.com/libsc-arm/conn
    echo "Successfully built the connection module"
}

write_conf_file() {
    echo "Generating configuration file ..."
    get_conf >> configuration.ini
    echo "Successfully generated configuration file"
}
    
write_conf_file
build_conn
