#!/bin/ptyhon3
import jenkins, json
from pprint import pprint

try:
    con = jenkins.Jenkins('http://localhost:8080', username='Fabio', password='urias!777')
    #pprint(con.get_whoami())
except Exception as e:
    pprint('Error: {}'.format(e))
    exit()


#Get xml config and change job with this new XML
xml = '<?xml version="1.1" encoding="UTF-8"?>\
 <project>\
   <actions/>\
   <description></description>\
   <keepDependencies>false</keepDependencies>\
   <properties/>\
   <scm class="hudson.scm.NullSCM"/>\
   <canRoam>true</canRoam>\
   <disabled>false</disabled>\<blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>\
   <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>\
   <triggers/>\
   <concurrentBuild>false</concurrentBuild>\
   <builders>\
     <hudson.tasks.Shell>\
       <command></command>\
     </hudson.tasks.Shell>\
   </builders>\
   <publishers/>\
   <buildWrappers/>\
 </project>'
con.reconfig_job('4521 - exemplo', xml)



#Get xml config
#job_xml = con.get_job_config('jobs-python2')
#pprint(job_xml)

#Get all jobs
#pprint (con.get_all_jobs())

#Building o Job
#queue = con.build_job('4521 - exemplo')
#pprint(con.get_queue_item(queue))

#Creando o Job

#con.create_job('4521 - exemplo', jenkins.EMPTY_CONFIG_XML)
#traz infoamrcoes do usuario logado
#pprint(con.get_whoami())

#traz informacoes de version do jenkins
#pprint(con.get_version())


