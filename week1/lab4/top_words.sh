#!/bin/bash

if [ $# -lt 1 ] ; then
	echo "Usage: $0 <filename> [count]"
	exit 1
fi

file=$1
count=${2:-10}

tr -cs '[:alpha:]' '\n' < "$file" \
 | tr '[:upper:]' '[:lower:]' \
 | sort \
 | uniq -c\
 | sort -nr \
 | head -n "$count"
