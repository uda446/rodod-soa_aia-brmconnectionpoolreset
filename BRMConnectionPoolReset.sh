#!/bin/bash
#############################################################################################
# File Description: Script to invoke BRMConnectionPoolReset.py                              #
# File Name: BRMConnectionPoolReset.py                                                      #
# Author: Wiacek, Tomasz        date: 2020-09-22                                            #
# Version History:                                                                          #
# v01 - 2020-09-22 - Initial Script creation                                                #
#############################################################################################

URL=t3://$(hostname):7001
export CONFIG_JVM_ARGS="-Djava.security.egd=file:/dev/./urandom -Dwlst.offline.log=disable"
WLST_HOME=/opt/aia/Middleware_WLS12C/oracle_common/common/bin
PY_HOME=/opt/aia/OperationalScript/BRMConnectionPoolReset

#run wlst script
$WLST_HOME/wlst.sh $PY_HOME/BRMConnectionPoolReset.py $URL $1 $2
