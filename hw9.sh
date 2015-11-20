#!/bin/bash

cdate=`date +%Y_%d_%m_%H_%M_%S`

fn="nyse_${cdate}.html"

wget -O $fn http://www.wsj.com/mdc/public/page/2_3021-activnyse-actives.html

#java -jar tagsoup-1.2.1.jar --files $fn

