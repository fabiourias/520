#!/bin/ptyhon3

import boto3
from pprint import pprint

ec2 = boto3.resource('ec2')
instances = ec2.instances.all()

for instance in instances:
  print(instance.instace_id)
  print(instance.instace_type)

  ###################################
#Outra forma
ec2 = boto3.resource("ec2")
instances = [x.instance_id for x in ec2.instances.all()]

pprint (instances)

 ###################################
#outra forma mais completo - filtrando as running

ec2 = boto3.resource("ec2")
instances = ec2.instances.filtr(
  Filters= [
    {
      "Name": "Instance-state-name",
      "Values: : ["running"]
    }
  ]
)
for x in instances:
  print(x.instance_id)
  
pprint (instances)
