#!/usr/bin/env bash

HTTP_CODE=$(curl -sS -w '%{http_code}' nolife.info -o /dev/null)
if [[ $HTTP_CODE -eq "200" ]]; then
	echo "0;nolife.info http_code=200"
else
	echo "2;nolife.info http_code=$HTTP_CODE"
fi
