#!/usr/bin/env bash

HTTP_TIME=$(curl -sS -w '%{time_total}' nolife.info -o /dev/null)
if [[ $HTTP_TIME < 0.1 ]]; then
	echo "0;nolife.info http_time < 0.1"
elif [[ $HTTP_TIME < 0.3 ]]; then
	echo "1;nolife.info http_time < 0.3"
else
	echo "2;nolife.info http_time = $HTTP_TIME"
fi
