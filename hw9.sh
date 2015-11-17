#!/bin/bash

wget -O test.html http://www.wsj.com/mdc/public/page/2_3021-activnyse-actives.html

java -jar tagsoup-1.2.1.jar --files test.html

