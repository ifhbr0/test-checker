#!/usr/bin/python

import os, argparse, glob, subprocess, sys
from ConfigParser import SafeConfigParser

def parse_configs():
    indir = './conf.d/*.conf'
    configs = []
    for filename in glob.glob(indir):
        parser = SafeConfigParser()
        parser.read(filename)
	configs.append(parser)
    return configs

def read_print_status(configs, severity_level=0):
    for conf in configs:
        name = conf.get('config', 'name')
        status_file = conf.get('config', 'status')
        f = open(status_file, 'r')
        level_desc = f.read().split(';', 1)
	if int(level_desc[0]) >= severity_level:
        	print name, ': ', level_desc[0], ' (',level_desc[1].strip(),')'

def run(name, configs):
	for conf in configs:
		check_name = conf.get('config', 'name')
		if name == check_name:
			binary = conf.get('config', 'binary')
			subprocess.call(binary, shell=True)
			print
	
parser = argparse.ArgumentParser()
parser.add_argument('--crit', help='show errors only', action="store_true")
parser.add_argument('--warn', help='show warnings and errors', action="store_true")
parser.add_argument('--run', help='run check by name', action="store_true")
parser.add_argument("name_to_run", nargs='?')
args = parser.parse_args()

cfgs = parse_configs()

if args.run:
	run(args.name_to_run, cfgs)
	exit(0)

if args.warn:
	read_print_status(cfgs,1)
elif args.crit:
	read_print_status(cfgs, 2)
else:
	read_print_status(cfgs)
