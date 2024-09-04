import boto3

AMI_ID = "ami-02b8e85f9dc96bd0a"
VPC_ID = "vpc-001c5545c91fc5abb"
SUBNETS = ['subnet-08d316e4042a11955', 'subnet-066e3f9f381a1ada1', 'subnet-0a88260ca37a0b9cf', 'subnet-00a2ce329c24622cf', 'subnet-0dcad2ceccac1bb6f', 'subnet-065ec053f0a7d5b16']

def create_security_group(ec2, description, group_name, inbound_rules):
    sg = ec2.create_security_group(Description=description, GroupName=group_name)
    print("Created security group: " + group_name)

    ec2.authorize_security_group_ingress(GroupName=group_name, IpPermissions=inbound_rules)
    print("Added inbound rules for security group: " + group_name)

    return sg['GroupId']

def create_ec2_instance(ec2, ami_id, instance_type, key_name, security_group_id):
    instance = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group_id],
        MinCount=1,
        MaxCount=1
    )

    print("Created ec2 instance with ID: " + instance['Instances'][0]['InstanceId'])

    print("Waiting for instance to run...")
    ec2 = boto3.resource('ec2')
    resource = ec2.Instance(instance['Instances'][0]['InstanceId'])
    resource.wait_until_running()
    print("Instance running")

    return instance['Instances'][0]['InstanceId']

def create_load_balancer(elb, name, subnets, security_groups, instance_id):
    lb = elb.create_load_balancer(
        Name=name,
        Subnets=subnets,
        SecurityGroups=security_groups,
        Scheme='internet-facing',
        Type='application',
        IpAddressType='ipv4'
    )
    print("Created load balancer with ID: " + lb['LoadBalancers'][0]['LoadBalancerArn'])

    tg = elb.create_target_group(
        Name="apache-web-server1",
        Protocol="HTTP",
        Port=80,
        VpcId=VPC_ID
    )
    print("Created target group with ARN: " + tg['TargetGroups'][0]['TargetGroupArn'])

    elb.register_targets(
        TargetGroupArn=tg['TargetGroups'][0]['TargetGroupArn'],
        Targets=[
            {
                'Id': instance_id,
                'Port': 80,
            }
        ]
    )
    print("Registered target with ID: " + instance_id + " to target group with ARN: " + tg['TargetGroups'][0]['TargetGroupArn'])

    elb.create_listener(
        LoadBalancerArn=lb['LoadBalancers'][0]['LoadBalancerArn'],
        Protocol='HTTP',
        Port=80,
        DefaultActions=[
            {
                'TargetGroupArn': tg['TargetGroups'][0]['TargetGroupArn'],
                'Type': 'forward',
            },
        ],
    )
    print("Added listener to load balancer with ID: " + lb['LoadBalancers'][0]['LoadBalancerArn'])

    return lb['LoadBalancers'][0]['LoadBalancerArn']

def main():
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    elb_client = boto3.client('elbv2', region_name='us-east-1')

    # Security group for EC2
    ec2_sg_id = create_security_group(
        ec2_client,
        "EC2 web server SG",
        "web-sg1",
        [
            {'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '79.153.45.232/32'}]}
        ]
    )

    # Security group for Load Balancer
    elb_sg_id = create_security_group(
        ec2_client,
        "Load balancer SG",
        "load-balancer-sg1",
        [
            {'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'FromPort': 443, 'ToPort': 443, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ]
    )

    # Launch EC2 instance
    instance_id = create_ec2_instance(
        ec2_client,
        AMI_ID,
        "t2.micro",
        "vockey",
        ec2_sg_id
    )

    # Create Load Balancer
    lb_arn = create_load_balancer(
        elb_client,
        "load-balancer1",
        SUBNETS,
        [elb_sg_id],
        instance_id
    )

    print("---------------- SETUP COMPLETED ----------------")

if __name__ == '__main__':
    main()
