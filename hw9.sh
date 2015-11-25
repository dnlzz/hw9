#!/bin/bash

hr=`date +%H`

while(($hr < 16)); do
    cdate=`date +%Y_%d_%m_%H_%M_%S`
    echo $cdate
    fn="nyse_${cdate}.html"
    wget -O $fn http://www.wsj.com/mdc/public/page/2_3021-activnyse-actives.html -P home/tony/Documents/NJIT/CS-288/hw9/htmldocs
    sleep 30
    hr=`date +%H`
done

