#!/bin/bash

set -eu

# All trainee
target_dir=`find /home -name "jupyter-trainee*" -type d`
# Specific trainee
#target_dir=`find /home -name "jupyter-trainee-test" -type d`


for file_path in $target_dir
do
	file_path=`echo $file_path | sed -e "s/://"`
	user=`echo $file_path | sed -e "s/://" | cut -f 3 -d "/"`

	## 研修資料配布
	cp source/training* "$file_path"
	cp -r "source/img" "$file_path"
	cp -r "source/input" "$file_path"
	cp -r "source/output" "$file_path"
	cp  "Doc/添付資料_問題一覧.pdf" "$file_path"
	chown "$user":"$user" "$file_path"/*
	
	ls -l "$file_path"
done
