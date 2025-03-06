import pandas as pd
import os
# Read a CSV file into a DataFrame
#df = pd.read_fwf('c:/temp/idmsuite/loaduccache_10-02-2025.txt',header=None,names=['date','time','none','pid','exe description', 'none2'])
df = pd.read_fwf('c:/temp/idmsuite/loaduccache_10-02-2025.txt')
#Sintaxis : data=pandas.read_csv('filename.txt', sep=' ', header=None, names=[“Columna1”, “Columna2”])
#Parámetros:
#filename.txt: Como su nombre lo sugiere, es el nombre del archivo de texto del que queremos leer los datos.
#sep : Es un campo separador. En el archivo de texto, utilizamos el carácter de espacio (' ') como separador.
#header: este es un campo opcional. De manera predeterminada, tomará la primera línea del archivo de texto como encabezado. Si usamos header=None, creará el encabezado.
#nombres: Podemos asignar nombres de columnas al importar el archivo de texto utilizando el argumento de nombres.
# https://www.geeksforgeeks.org/how-to-read-text-files-with-pandas/
#df = pd.read_csv('example.csv')
print(df)
print('line 15')
for line in df:
    print (line)
    #print(line.split())
print('line 17')



test = '''
2025-02-09 19:56:04.759.8325 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,9700] Info: Module:[agtaddn.exe], 4.5.2.36251 Git 6ff60b34a6ef 1, Support code: 94588106309788
2025-02-09 19:56:04.759.8396 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,9700] Info: Instance HIPAM, Log level: Info, Extended levels: perf perf_sproc perf_replication
2025-02-09 19:56:04.771.6358 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,29012] Info: List deleted is [0]
2025-02-09 19:56:04.773.5903 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,29012] Info: Attempting to connect to host [AD_PERSONAL] at address [{server=nestle.com;ssl=true;userFilter="(!(UserAccountControl:1.2.840.113556.1.4.803:=2))";listGroups={"CN=CTRHIPAMLEVEL2,OU=Admins,OU=Users and Groups,OU=GC CTR,OU=CTR,OU=Organizations,DC=nestle,DC=com";};listNestedGrps=true;listFailOnNonExistentGrp=true;listFailOnNonExistentOU=true;listDeleted=NODELETED;nameFormat=NT4;groupNameFormat=DN;grpowner_attr=managedBy;persistentSearchWait=7200;}]
2025-02-09 19:56:04.776.3162 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,29012] Info: Connecting to server [AZEUWB0007.nestle.com] with [CTRHIPAMADMIN] SSL
2025-02-09 19:56:04.817.4441 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,29012] Info: List forest: [0]
2025-02-09 19:56:04.817.4542 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,29012] Info: Connecting to server [AZEUWB0007.nestle.com] with [CTRHIPAMADMIN] SSL
2025-02-09 19:56:05.290.5655 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,29012] Perf: PerfConnector. Address: {[server=nestle.com;ssl=true;userFilter="(!(UserAccountControl:1.2.840.113556.1.4.803:=2))";listGroups=["CN=CTRHIPAMLEVEL2,OU=Admins,OU=Users and Groups,OU=GC CTR,OU=CTR,OU=Organizations,DC=nestle,DC=com";];listNestedGrps=true;listFailOnNonExistentGrp=true;listFailOnNonExistentOU=true;listDeleted=NODELETED;nameFormat=NT4;groupNameFormat=DN;grpowner_attr=managedBy;persistentSearchWait=7200;]} | AdminID: {CTRHIPAMADMIN} | Duration: {516} | Event: {connector-operation} | Message: {} | Operation: {Connect} | Result: {0} | SysID: {} | TargetID: {AD_PERSONAL}
2025-02-09 19:56:05.291.3053 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,14692] Info: operation is [reset] of type [ACCT] on targetid [AD_PERSONAL]
2025-02-09 19:56:05.291.3570 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,14692] Info: ADConnHandler: Establishing a connection to server [AZEUWB0007.nestle.com]
2025-02-09 19:56:05.291.3599 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,14692] Info: Connecting to server [AZEUWB0007.nestle.com] with [CTRHIPAMADMIN] SSL
2025-02-09 19:56:05.462.9496 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,14692] Info: Successfully bound [CTRHIPAMADMIN] to [LDAP://AZEUWB0007.nestle.com/CN=adm2Adam7,OU=Admins,OU=Users and Groups,OU=GC EUR,OU=EUR,OU=Organizations,DC=nestle,DC=com]
2025-02-09 19:56:05.493.0263 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,14692] Perf: PerfConnector. Address: {[server=nestle.com;ssl=true;userFilter="(!(UserAccountControl:1.2.840.113556.1.4.803:=2))";listGroups=["CN=CTRHIPAMLEVEL2,OU=Admins,OU=Users and Groups,OU=GC CTR,OU=CTR,OU=Organizations,DC=nestle,DC=com";];listNestedGrps=true;listFailOnNonExistentGrp=true;listFailOnNonExistentOU=true;listDeleted=NODELETED;nameFormat=NT4;groupNameFormat=DN;grpowner_attr=managedBy;persistentSearchWait=7200;]} | AdminID: {CTRHIPAMADMIN} | Duration: {201} | Event: {connector-operation} | Message: {} | Operation: {reset} | Result: {0} | SysID: {} | TargetID: {AD_PERSONAL}
2025-02-09 19:56:05.493.0587 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,14692] Info: PerfConnectorExt. AcctID: {NESTLE\adm2Adam7} | Duration: {201} | Event: {connector-extended} | ObjChildID: {} | ObjChildType: {} | ObjRelType: {} | ObjectID: {} | ObjectType: {ACCT} | Operation: {reset} | TargetID: {AD_PERSONAL}
2025-02-09 19:56:05.493.0641 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,14692] Info: Agent operation [reset] succeeded
2025-02-09 19:56:05.495.0587 - [886b544b-7c19-4529-bbe4-e736d5a3083c] agtaddn.exe [8584,9700] Perf: PerfExe. Duration: {743} | Kernel: {62} | User: {62}
2025-02-09 19:56:16.887.6266 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtazure.exe [37736,19948] Info: Module:[agtazure.exe], 4.5.2.36251 Git 6ff60b34a6ef 1, Support code: 94588106309788
2025-02-09 19:56:16.887.6301 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtazure.exe [37736,19948] Info: Instance HIPAM, Log level: Info, Extended levels: perf perf_sproc perf_replication
2025-02-09 19:56:16.889.3026 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtazure.exe [37736,19948] Notice: parallel operations will be done in serial instead
2025-02-09 19:56:16.889.9623 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtazure.exe [37736,19948] Info: Attempting to connect to host [AZURE_PERSONAL] at address [{server=graph.microsoft.com; port=443; domain=nestle.onmicrosoft.com; authsvr=login.microsoftonline.com; authport=443; listGroups={AAD-HIPAM-LEVEL2; }; }]
2025-02-09 19:56:17.105.6742 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtazure.exe [37736,19948] Perf: PerfConnector. Address: {[server=graph.microsoft.com; port=443; domain=nestle.onmicrosoft.com; authsvr=login.microsoftonline.com; authport=443; listGroups=[AAD-HIPAM-LEVEL2; ]; ]} | AdminID: {53715366-c99e-4db5-a149-ab231bc64d0b} | Duration: {215} | Event: {connector-operation} | Message: {} | Operation: {Connect} | Result: {0} | SysID: {} | TargetID: {AZURE_PERSONAL}
2025-02-09 19:56:17.106.0234 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtazure.exe [37736,19948] Info: operation is [reset] of type [ACCT] on targetid [AZURE_PERSONAL]
2025-02-09 19:56:17.263.4943 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtazure.exe [37736,19948] Perf: PerfConnector. Address: {[server=graph.microsoft.com; port=443; domain=nestle.onmicrosoft.com; authsvr=login.microsoftonline.com; authport=443; listGroups=[AAD-HIPAM-LEVEL2; ]; ]} | AdminID: {53715366-c99e-4db5-a149-ab231bc64d0b} | Duration: {157} | Event: {connector-operation} | Message: {} | Operation: {reset} | Result: {0} | SysID: {} | TargetID: {AZURE_PERSONAL}
2025-02-09 19:56:17.263.5288 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtazure.exe [37736,19948] Info: PerfConnectorExt. AcctID: {adz2Karmakar@ch.nestle.com} | Duration: {157} | Event: {connector-extended} | ObjChildID: {} | ObjChildType: {} | ObjRelType: {} | ObjectID: {} | ObjectType: {ACCT} | Operation: {reset} | TargetID: {AZURE_PERSONAL}
2025-02-09 19:56:17.263.5321 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtazure.exe [37736,19948] Info: Agent operation [reset] succeeded
2025-02-09 19:56:17.264.0916 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtazure.exe [37736,19948] Perf: PerfExe. Duration: {384} | Kernel: {0} | User: {15}
2025-02-09 19:57:18.946.9515 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,4456] Info: Module:[agtaddn.exe], 4.5.2.36251 Git 6ff60b34a6ef 1, Support code: 94588106309788
2025-02-09 19:57:18.946.9577 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,4456] Info: Instance HIPAM, Log level: Info, Extended levels: perf perf_sproc perf_replication
2025-02-09 19:57:18.958.4157 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,35256] Info: List deleted is [0]
2025-02-09 19:57:18.960.2710 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,35256] Info: Attempting to connect to host [AD_PERSONAL] at address [{server=nestle.com;ssl=true;userFilter="(!(UserAccountControl:1.2.840.113556.1.4.803:=2))";listGroups={"CN=CTRHIPAMLEVEL2,OU=Admins,OU=Users and Groups,OU=GC CTR,OU=CTR,OU=Organizations,DC=nestle,DC=com";};listNestedGrps=true;listFailOnNonExistentGrp=true;listFailOnNonExistentOU=true;listDeleted=NODELETED;nameFormat=NT4;groupNameFormat=DN;grpowner_attr=managedBy;persistentSearchWait=7200;}]
2025-02-09 19:57:18.962.7942 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,35256] Info: Connecting to server [AZEUWB0007.nestle.com] with [CTRHIPAMADMIN] SSL
2025-02-09 19:57:19.126.0829 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,35256] Info: List forest: [0]
2025-02-09 19:57:19.126.0944 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,35256] Info: Connecting to server [AZEUWB0007.nestle.com] with [CTRHIPAMADMIN] SSL
2025-02-09 19:57:19.591.7907 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,35256] Perf: PerfConnector. Address: {[server=nestle.com;ssl=true;userFilter="(!(UserAccountControl:1.2.840.113556.1.4.803:=2))";listGroups=["CN=CTRHIPAMLEVEL2,OU=Admins,OU=Users and Groups,OU=GC CTR,OU=CTR,OU=Organizations,DC=nestle,DC=com";];listNestedGrps=true;listFailOnNonExistentGrp=true;listFailOnNonExistentOU=true;listDeleted=NODELETED;nameFormat=NT4;groupNameFormat=DN;grpowner_attr=managedBy;persistentSearchWait=7200;]} | AdminID: {CTRHIPAMADMIN} | Duration: {631} | Event: {connector-operation} | Message: {} | Operation: {Connect} | Result: {0} | SysID: {} | TargetID: {AD_PERSONAL}
2025-02-09 19:57:19.592.5595 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,21116] Info: operation is [reset] of type [ACCT] on targetid [AD_PERSONAL]
2025-02-09 19:57:19.592.6456 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,21116] Info: ADConnHandler: Establishing a connection to server [AZEUWB0007.nestle.com]
2025-02-09 19:57:19.592.6489 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,21116] Info: Connecting to server [AZEUWB0007.nestle.com] with [CTRHIPAMADMIN] SSL
2025-02-09 19:57:19.784.3502 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,21116] Info: Successfully bound [CTRHIPAMADMIN] to [LDAP://AZEUWB0007.nestle.com/CN=adm2chadima,OU=Admins,OU=Users and Groups,OU=GC EUR,OU=EUR,OU=Organizations,DC=nestle,DC=com]
2025-02-09 19:57:19.823.6988 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,21116] Perf: PerfConnector. Address: {[server=nestle.com;ssl=true;userFilter="(!(UserAccountControl:1.2.840.113556.1.4.803:=2))";listGroups=["CN=CTRHIPAMLEVEL2,OU=Admins,OU=Users and Groups,OU=GC CTR,OU=CTR,OU=Organizations,DC=nestle,DC=com";];listNestedGrps=true;listFailOnNonExistentGrp=true;listFailOnNonExistentOU=true;listDeleted=NODELETED;nameFormat=NT4;groupNameFormat=DN;grpowner_attr=managedBy;persistentSearchWait=7200;]} | AdminID: {CTRHIPAMADMIN} | Duration: {231} | Event: {connector-operation} | Message: {} | Operation: {reset} | Result: {0} | SysID: {} | TargetID: {AD_PERSONAL}
2025-02-09 19:57:19.823.7509 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,21116] Info: PerfConnectorExt. AcctID: {NESTLE\adm2chadima} | Duration: {231} | Event: {connector-extended} | ObjChildID: {} | ObjChildType: {} | ObjRelType: {} | ObjectID: {} | ObjectType: {ACCT} | Operation: {reset} | TargetID: {AD_PERSONAL}
2025-02-09 19:57:19.823.7591 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,21116] Info: Agent operation [reset] succeeded
2025-02-09 19:57:19.826.2421 - [f1a39ea1-5425-4fd4-b047-c657e1652df2] agtaddn.exe [44664,4456] Perf: PerfExe. Duration: {889} | Kernel: {46} | User: {93}
2025-02-09 19:59:38.050.7637 - [] agtssh.exe [9192,40544] Error: Error messages: 
2025-02-09 19:59:38.050.8793 - [] agtssh.exe [9192,40544] Perf: PerfConnector. Address: {[script="F:\\Program Files\\Hitachi ID\\IDM Suite\\HIPAM\\component\\Custom\\Scenario\\nestle_system_type_hp_ilo\\data\\agthpilo.psl"; server="10.41.84.16"; port=22; compression=false; hostkeys=AllowAppend; ]} | AdminID: {NESTLE\CTRTPAMILOSVC} | Duration: {300002} | Event: {connector-operation} | Message: {.} | Operation: {adminverify} | Result: {1} | SysID: {} | TargetID: {024BDDC64BFC444D9279AF5E7E6CF05F}
2025-02-09 19:59:38.050.9148 - [] agtssh.exe [9192,40544] Info: PerfConnectorExt. AcctID: {HPAdmin} | Duration: {300002} | Event: {connector-extended} | ObjChildID: {} | ObjChildType: {} | ObjRelType: {} | ObjectID: {} | ObjectType: {ACCT} | Operation: {adminverify} | TargetID: {024BDDC64BFC444D9279AF5E7E6CF05F}
2025-02-09 19:59:38.050.9192 - [] agtssh.exe [9192,40544] Warning: Agent operation [adminverify] failed with error msg [.  Failed to perform operation [adminverify].]
2025-02-09 19:59:38.052.3107 - [] agtssh.exe [9192,42104] Perf: PerfExe. Duration: {600033} | Kernel: {46} | User: {0}
2025-02-09 19:59:39.031.9155 - [] agtssh.exe [44312,12700] Info: Module:[agtssh.exe], 4.5.2.36251 Git 6ff60b34a6ef 1, Support code: 94588106309788
2025-02-09 19:59:39.031.9183 - [] agtssh.exe [44312,12700] Info: Instance HIPAM, Log level: Info, Extended levels: perf perf_sproc perf_replication
2025-02-09 19:59:39.035.9984 - [] agtssh.exe [44312,9664] Notice: parallel operations will be done in serial instead
2025-02-09 19:59:39.041.1856 - [] agtssh.exe [44312,26492] Info: operation is [adminverify] of type [ACCT] on targetid [F1AA0C441E684C2388AC1FD2D5AA1145]
2025-02-09 19:59:39.042.7527 - [] agtssh.exe [44312,26492] Warning: line 296: Target's internal hostname should be specified in the address line of the target. Using '*' as default.
2025-02-09 19:59:39.557.5984 - [] agtssh.exe [44312,26492] Perf: PerfConnector. Address: {[script="F:\Program Files\Hitachi ID\IDM Suite\HIPAM\component\Custom\Scenario\nestle_system_type_checkpoint_gaia\data\agtchkptgaia.psl"; server="10.27.132.235"; port=22; compression=false; hostkeys=AllowAppend; ]} | AdminID: {TPAMUser} | Duration: {516} | Event: {connector-operation} | Message: {} | Operation: {adminverify} | Result: {0} | SysID: {} | TargetID: {F1AA0C441E684C2388AC1FD2D5AA1145}
2025-02-09 19:59:39.557.6340 - [] agtssh.exe [44312,26492] Info: PerfConnectorExt. AcctID: {admin} | Duration: {516} | Event: {connector-extended} | ObjChildID: {} | ObjChildType: {} | ObjRelType: {} | ObjectID: {} | ObjectType: {ACCT} | Operation: {adminverify} | TargetID: {F1AA0C441E684C2388AC1FD2D5AA1145}
2025-02-09 19:59:39.557.6370 - [] agtssh.exe [44312,26492] Info: Agent operation [adminverify] succeeded
2025-02-09 19:59:39.559.7705 - [] agtssh.exe [44312,12700] Perf: PerfExe. Duration: {532} | Kernel: {0} | User: {15}
2025-02-09 19:59:40.640.8834 - [] agtssh.exe [29600,42628] Info: Module:[agtssh.exe], 4.5.2.36251 Git 6ff60b34a6ef 1, Support code: 94588106309788
2025-02-09 19:59:40.640.8866 - [] agtssh.exe [29600,42628] Info: Instance HIPAM, Log level: Info, Extended levels: perf perf_sproc perf_replication
2025-02-09 19:59:40.644.9463 - [] agtssh.exe [29600,29308] Notice: parallel operations will be done in serial instead
2025-02-09 19:59:40.650.4318 - [] agtssh.exe [29600,45416] Info: operation is [adminverify] of type [ACCT] on targetid [E47FE941F5A2441CAFB4DFC2E8386421]
2025-02-09 19:59:40.652.1158 - [] agtssh.exe [29600,45416] Warning: line 296: Target's internal hostname should be specified in the address line of the target. Using '*' as default.
2025-02-09 19:59:45.983.1197 - [] agtssh.exe [29600,6520] Error: Access denied
2025-02-09 19:59:45.984.4497 - [] agtssh.exe [29600,45416] Error: Error messages: 
2025-02-09 19:59:45.984.5768 - [] agtssh.exe [29600,45416] Perf: PerfConnector. Address: {[script="F:\Program Files\Hitachi ID\IDM Suite\HIPAM\component\Custom\Scenario\nestle_system_type_checkpoint_gaia\data\agtchkptgaia.psl"; server="10.151.105.139"; port=22; compression=false; hostkeys=AllowAppend; ]} | AdminID: {TPAMUser} | Duration: {5333} | Event: {connector-operation} | Message: {.} | Operation: {adminverify} | Result: {1} | SysID: {} | TargetID: {E47FE941F5A2441CAFB4DFC2E8386421}
2025-02-09 19:59:45.984.6102 - [] agtssh.exe [29600,45416] Info: PerfConnectorExt. AcctID: {expert} | Duration: {5333} | Event: {connector-extended} | ObjChildID: {} | ObjChildType: {} | ObjRelType: {} | ObjectID: {} | ObjectType: {ACCT} | Operation: {adminverify} | TargetID: {E47FE941F5A2441CAFB4DFC2E8386421}
2025-02-09 19:59:45.984.6145 - [] agtssh.exe [29600,45416] Warning: Agent operation [adminverify] failed with error msg [.  Failed to perform operation [adminverify].]
2025-02-09 19:59:45.986.7440 - [] agtssh.exe [29600,42628] Perf: PerfExe. Duration: {5359} | Kernel: {31} | User: {31}
2025-02-09 19:59:46.945.5703 - [] agtssh.exe [38808,32264] Info: Module:[agtssh.exe], 4.5.2.36251 Git 6ff60b34a6ef 1, Support code: 94588106309788
2025-02-09 19:59:46.945.5738 - [] agtssh.exe [38808,32264] Info: Instance HIPAM, Log level: Info, Extended levels: perf perf_sproc perf_replication
2025-02-09 19:59:46.949.8421 - [] agtssh.exe [38808,47712] Notice: parallel operations will be done in serial instead
2025-02-09 19:59:46.955.4046 - [] agtssh.exe [38808,39672] Info: operation is [adminverify] of type [ACCT] on targetid [C2CF093E1E8C47FE89B8218C2A1D8422]
2025-02-09 19:59:46.957.0665 - [] agtssh.exe [38808,39672] Warning: line 296: Target's internal hostname should be specified in the address line of the target. Using '*' as default.
2025-02-09 19:59:48.868.0916 - [] agtssh.exe [38808,39672] Perf: PerfConnector. Address: {[script="F:\Program Files\Hitachi ID\IDM Suite\HIPAM\component\Custom\Scenario\nestle_system_type_checkpoint_gaia\data\agtchkptgaia.psl"; server="10.78.80.252"; port=22; compression=false; hostkeys=AllowAppend; ]} | AdminID: {TPAMUser} | Duration: {1912} | Event: {connector-operation} | Message: {} | Operation: {adminverify} | Result: {0} | SysID: {} | TargetID: {C2CF093E1E8C47FE89B8218C2A1D8422}
2025-02-09 19:59:48.868.1259 - [] agtssh.exe [38808,39672] Info: PerfConnectorExt. AcctID: {admin} | Duration: {1912} | Event: {connector-extended} | ObjChildID: {} | ObjChildType: {} | ObjRelType: {} | ObjectID: {} | ObjectType: {ACCT} | Operation: {adminverify} | TargetID: {C2CF093E1E8C47FE89B8218C2A1D8422}
2025-02-09 19:59:48.868.1288 - [] agtssh.exe [38808,39672] Info: Agent operation [adminverify] succeeded
2025-02-09 19:59:48.870.1256 - [] agtssh.exe [38808,32264] Perf: PerfExe. Duration: {1938} | Kernel: {31} | User: {15}
2025-02-09 19:59:49.958.9114 - [] agtssh.exe [37444,24140] Info: Module:[agtssh.exe], 4.5.2.36251 Git 6ff60b34a6ef 1, Support code: 94588106309788
2025-02-09 19:59:49.958.9152 - [] agtssh.exe [37444,24140] Info: Instance HIPAM, Log level: Info, Extended levels: perf perf_sproc perf_replication
2025-02-09 19:59:49.963.7188 - [] agtssh.exe [37444,10612] Notice: parallel operations will be done in serial instead
2025-02-09 19:59:49.968.9717 - [] agtssh.exe [37444,49388] Info: operation is [adminverify] of type [ACCT] on targetid [CF3D6C0164F04C61927CE634A3C81214]
2025-02-09 19:59:49.970.9727 - [] agtssh.exe [37444,49388] Warning: line 296: Target's internal hostname should be specified in the address line of the target. Using '*' as default.
2025-02-09 19:59:51.772.5954 - [] agtssh.exe [37444,49388] Perf: PerfConnector. Address: {[script="F:\Program Files\Hitachi ID\IDM Suite\HIPAM\component\Custom\Scenario\nestle_system_type_checkpoint_gaia\data\agtchkptgaia.psl"; server="10.112.138.171"; port=22; compression=false; hostkeys=AllowAppend; ]} | AdminID: {TPAMUser} | Duration: {1803} | Event: {connector-operation} | Message: {} | Operation: {adminverify} | Result: {0} | SysID: {} | TargetID: {CF3D6C0164F04C61927CE634A3C81214}
2025-02-09 19:59:51.772.6623 - [] agtssh.exe [37444,49388] Info: PerfConnectorExt. AcctID: {admin} | Duration: {1803} | Event: {connector-extended} | ObjChildID: {} | ObjChildType: {} | ObjRelType: {} | ObjectID: {} | ObjectType: {ACCT} | Operation: {adminverify} | TargetID: {CF3D6C0164F04C61927CE634A3C81214}
2025-02-09 19:59:51.772.6650 - [] agtssh.exe [37444,49388] Info: Agent operation [adminverify] succeeded
2025-02-09 19:59:51.774.6135 - [] agtssh.exe [37444,24140] Perf: PerfExe. Duration: {1823} | Kernel: {31} | User: {31}
2025-02-09 19:59:52.841.8240 - [] agtssh.exe [18468,13712] Info: Module:[agtssh.exe], 4.5.2.36251 Git 6ff60b34a6ef 1, Support code: 94588106309788
2025-02-09 19:59:52.841.8268 - [] agtssh.exe [18468,13712] Info: Instance HIPAM, Log level: Info, Extended levels: perf perf_sproc perf_replication
2025-02-09 19:59:52.845.6110 - [] agtssh.exe [18468,35304] Notice: parallel operations will be done in serial instead
2025-02-09 19:59:52.850.7185 - [] agtssh.exe [18468,47124] Info: operation is [adminverify] of type [ACCT] on targetid [D97D61A65AB14ADCB5F56999D7058401]
2025-02-09 19:59:52.852.3648 - [] agtssh.exe [18468,47124] Warning: line 296: Target's internal hostname should be specified in the address line of the target. Using '*' as default.
2025-02-09 19:59:53.312.3532 - [] agtssh.exe [18468,47124] Perf: PerfConnector. Address: {[script="F:\Program Files\Hitachi ID\IDM Suite\HIPAM\component\Custom\Scenario\nestle_system_type_checkpoint_gaia\data\agtchkptgaia.psl"; server="10.39.254.140"; port=22; compression=false; hostkeys=AllowAppend; ]} | AdminID: {TPAMUser} | Duration: {461} | Event: {connector-operation} | Message: {} | Operation: {adminverify} | Result: {0} | SysID: {} | TargetID: {D97D61A65AB14ADCB5F56999D7058401}
2025-02-09 19:59:53.312.3942 - [] agtssh.exe [18468,47124] Info: PerfConnectorExt. AcctID: {admin} | Duration: {461} | Event: {connector-extended} | ObjChildID: {} | ObjChildType: {} | ObjRelType: {} | ObjectID: {} | ObjectType: {ACCT} | Operation: {adminverify} | TargetID: {D97D61A65AB14ADCB5F56999D7058401}
2025-02-09 19:59:53.312.3974 - [] agtssh.exe [18468,47124] Info: Agent operation [adminverify] succeeded
2025-02-09 19:59:53.314.4756 - [] agtssh.exe [18468,13712] Perf: PerfExe. Duration: {477} | Kernel: {15} | User: {0}
2025-02-09 19:59:54.386.8157 - [] agtssh.exe [44024,28056] Info: Module:[agtssh.exe], 4.5.2.36251 Git 6ff60b34a6ef 1, Support code: 94588106309788
2025-02-09 19:59:54.386.8194 - [] agtssh.exe [44024,28056] Info: Instance HIPAM, Log level: Info, Extended levels: perf perf_sproc perf_replication
2025-02-09 19:59:54.391.3146 - [] agtssh.exe [44024,42568] Notice: parallel operations will be done in serial instead
2025-02-09 19:59:54.397.1953 - [] agtssh.exe [44024,10748] Info: operation is [adminverify] of type [ACCT] on targetid [C228DC80C8194CF1961856FBC1E951F2]
2025-02-09 19:59:54.398.9762 - [] agtssh.exe [44024,10748] Warning: line 296: Target's internal hostname should be specified in the address line of the target. Using '*' as default.
2025-02-09 19:59:55.322.1205 - [] agtssh.exe [44024,10748] Perf: PerfConnector. Address: {[script="F:\Program Files\Hitachi ID\IDM Suite\HIPAM\component\Custom\Scenario\nestle_system_type_checkpoint_gaia\data\agtchkptgaia.psl"; server="10.146.91.44"; port=22; compression=false; hostkeys=AllowAppend; ]} | AdminID: {TPAMUser} | Duration: {924} | Event: {connector-operation} | Message: {} | Operation: {adminverify} | Result: {0} | SysID: {} | TargetID: {C228DC80C8194CF1961856FBC1E951F2}
'''


import pandas as pd
import os
# Read a CSV file into a DataFrame
#df = pd.read_fwf('c:/temp/idmsuite/loaduccache_10-02-2025.txt',header=None,names=['date','time','none','pid','exe description', 'none2'])
df = pd.read_fwf('c:/temp/idmsuite/loaduccache_10-02-2025.txt')
#Sintaxis : data=pandas.read_csv('filename.txt', sep=' ', header=None, names=[“Columna1”, “Columna2”])
#Parámetros:
#filename.txt: Como su nombre lo sugiere, es el nombre del archivo de texto del que queremos leer los datos.
#sep : Es un campo separador. En el archivo de texto, utilizamos el carácter de espacio (' ') como separador.
#header: este es un campo opcional. De manera predeterminada, tomará la primera línea del archivo de texto como encabezado. Si usamos header=None, creará el encabezado.
#nombres: Podemos asignar nombres de columnas al importar el archivo de texto utilizando el argumento de nombres.
# https://www.geeksforgeeks.org/how-to-read-text-files-with-pandas/
#df = pd.read_csv('example.csv')
#print ('df content')
#print('')
#print(df)
#for line in df:
#    print ('file start here')
#    print (line)

from collections import defaultdict # import defauldict 

a = test.split('\n') # split log items by paragraph mark \n
#df = test.split(' ') # split log items by paragraph mark \n
print('')
print ('a')
print('')
print (a)

list_items = [] # create a list

# for loop that will get log item in a variable and add to list_items list only the items that are not empty ''
for i in a: 
    if i != '': # not empty
        list_items.append(i) # add to the list
#print (len(list_items))

Log_lines = defaultdict(list) # create a new defaultdict
print(Log_lines)
print('')
print('line 383')
print('')
#count_perf = 0
#count_info = 0
#count_other = 0

# for loop that will get Log_lines items, iterate, appending to a dictionary where the key will be the type of log
for i in list_items:
    if 'Info:' in i:
        #count_info = count_info + 1
        #print (str(count_info) + ' items')
        Log_lines['Info'].append(i)
    elif 'Perf:' in i:
        #count_perf = count_perf + 1
        #print (str(count_perf) + ' items')
        Log_lines['Perf'].append(i)
    elif 'Notice:' in i:
        #count_perf = count_perf + 1
        #print (str(count_perf) + ' items')
        Log_lines['Notice'].append(i)
    elif 'Warning:' in i:
        #count_perf = count_perf + 1
        #print (str(count_perf) + ' items')
        Log_lines['Perf'].append(i)
    elif 'Error:' in i:
        #count_perf = count_perf + 1
        #print (str(count_perf) + ' items')
        Log_lines['Error'].append(i)
    elif 'Operation:' in i:
        #count_perf = count_perf + 1
        #print (str(count_perf) + ' items')
        Log_lines['Operation'].append(i)
    else:
        #count_other = count_other + 1
        #print (str(ount_other) + ' items')
        Log_lines['Other'].append(i)    


print(Log_lines)
#print ('Log_lines keys')
#print(Log_lines.keys())
#print('Log_lines values')
#print(Log_lines.values())
print ('')
print ('---------------------------------------------------')
print ('')

print ('Len log lines')
print ('')
print(len(Log_lines))
print ('')
print ('---------------------------------------------------')
print ('')

print ('Log lines: Perf')
print ('')
print(Log_lines['Perf'])
print ('')
print ('---------------------------------------------------')
print ('')

print ('Log lines: Info')
print ('')
print(Log_lines['Info'])
print ('')
print ('---------------------------------------------------')
print ('')

print ('Log lines: Notice')
print ('')
print(Log_lines['Notice'])
print ('')
print ('---------------------------------------------------')
print ('')

print ('Log lines: Warning')
print ('')
print(Log_lines['Warning'])
print ('')
print ('---------------------------------------------------')
print ('')

print ('Log lines: Error')
print ('')
print(Log_lines['Error'])
print ('')
print ('---------------------------------------------------')
print ('')

print ('Log lines: Operation')
print ('')
print(Log_lines['Operation'])
print ('')
print ('---------------------------------------------------')
print ('')

print ('Log lines: Other')
print ('')
print(Log_lines['Other'])
print ('')
print ('---------------------------------------------------')
print ('')




