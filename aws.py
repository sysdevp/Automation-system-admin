import boto3
import pandas as pd
import numpy as np
from datetime import datetime

def AWS_data():

    ec2 = boto3.client('ec2',region_name='ap-south-1',aws_access_key_id='AKIAIXZZQ4JTBNDPYDOA',aws_secret_access_key='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')

    response = ec2.describe_instances()

    #print(response)
    ip = []
    id = []
    #"Reservations[*].Instances[*].[PublicIpAddress, Tags[?Key=='Name'].Value|[0]]" --output=text
    for r in response['Reservations']:
        
        for i in r['Instances']:
            
            values = i['PublicIpAddress']
            
            ids = i['InstanceId']
            
            ip.append(values)
            id.append(ids)
            
    #print(ip)
    #print(id)

    data_frame = pd.DataFrame(list(zip(id,ip)),columns=['Instance - ID','Public - IP'])

    date = datetime.now()

    today = date.strftime('%d%m%Y%H')

    filename = "{}.txt".format(today)  #'0801202111'

    numpy_array = data_frame.to_numpy()

    np.savetxt(filename, numpy_array,header='Instance-ID,Public-IP', fmt = "%s", delimiter=',')


