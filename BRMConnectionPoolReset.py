########################################################################################
# WLST AIA Reset JCA Utility Script                                                    #
# By Tomasz Wiacek                                                                     #
########################################################################################

import java.lang
import string
import sys

serverUrl=sys.argv[1]
ConfigFile='/opt/aia/config/domains/aiafp12c_domain/security/WeblogicConfigFile'
KeyFile='/opt/aia/config/domains/aiafp12c_domain/security/WeblogicKeyFile'

def helpUsage():
    print 'Usage: BRMConnectionPoolReset.py serverUrl [-help]'
    print '       BRMConnectionPoolReset.py serverUrl [-all] - reset JCA for all managed server'
    print '       BRMConnectionPoolReset.py serverUrl [-ms ServerName] - reset JCA for only this managed server name'
    print '       example: BRMConnectionPoolReset.py t3://localhost:7001 -ms SOA_MS1'
    print '       example: BRMConnectionPoolReset.py t3://localhost:7001 -all'
    exit()

def resetOneMS(serverName):
    connect(userConfigFile=ConfigFile,userKeyFile=KeyFile,url=serverUrl)
    domainRuntime()
    print 'INFO:Resetting JCA BRM connection pool for server: ' + ServerName
    try:
        path='/ServerRuntimes/'+serverName+'/ApplicationRuntimes/OracleBRMJCA15Adapter/ComponentRuntimes/OracleBRMJCA15Adapter/ConnectionPools/eis/BRM'
        cd(path)
        cmo.forceReset()
    except:
        print 'ERROR: Path not found: '+path
    disconnect()

def resetAll():
    connect(userConfigFile=ConfigFile,userKeyFile=KeyFile,url=serverUrl)
    serverList = cmo.getServers()
    domainRuntime()
    for server in serverList:
        serverName=server.getName()
        if serverName.find("SOA_MS")>=0:
            print 'INFO:Resetting JCA BRM connection pool for server: '+serverName
            try:
                path='/ServerRuntimes/'+serverName+'/ApplicationRuntimes/OracleBRMJCA15Adapter/ComponentRuntimes/OracleBRMJCA15Adapter/ConnectionPools/eis/BRM'
                cd(path)
                cmo.forceReset()
            except:
                print 'ERROR: Path not found: '+path
    disconnect()

#main

if sys.argv[2] in ("-help"):
    helpUsage()
elif sys.argv[2] in ("-all"):
    print 'INFO:Trying JCA BRM connection pool reset for all ManagedServer'
    resetAll()
elif sys.argv[2] in ("-ms"):
    ServerName=sys.argv[3]
    print 'INFO:Trying JCA BRM connection pool for only one server: ' + ServerName
    resetOneMS(ServerName)
else:
    helpUsage()

