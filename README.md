# Information
This script is used to manage the BRM JCA Adapter Connection Pool

# Prerequisites
````
1. 
Make sure that WebLogic ConfigFile and KeyFile is available on the server.
/opt/aia/config/domains/aiafp12c_domain/security/WeblogicConfigFile
/opt/aia/config/domains/aiafp12c_domain/security/WeblogicKeyFile

2. If files is not present in section 1. is not present please follow this section otherwise proceed to section 3.

2a: Start the WebLogic Scripting Tool (WLST)
cd /opt/aia/Middleware_WLS12C/oracle_common/common/bin
./wlst.sh

2b: Connect to the server AdminServer/NodeManager
wls:/offline>connect('weblogic','<PASSWORD>','t3://<HOSTNAME>:7001')

2c: Generate ConfigFile & KeyFile while connected to the AdminServer/NodeManager
wls:/aiafp12c_domain/serverConfig/>storeUserConfig('/opt/aia/config/domains/aiafp12c_domain/security/WeblogicConfigFile', '/opt/aia/config/domains/aiafp12c_domain/security/WeblogicKeyFile')

2d: Exit the WLST.
wls:/aiafp12c_domain/serverConfig/> exit()
````
# Usage of this Script
````
sh BRMConnectionPoolReset.sh -<action>

Actions:
help
all
ms <SOA_MS[1-4]>
````
