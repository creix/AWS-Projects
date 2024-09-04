# Review of Federated Learning Tutorial
This tutorial offers a comprehensive guide on setting up a federated learning system using Flower. Below are my detailed observations and suggestions for each section.

## What is Federated Learning?
This section of the tutorial was very good. It explained the idea of federated learning and showed also some use cases for it. The inserted images help to understand the difference between centralized and decentralized systems. All in all we can say that this section gives a good introduction into the topic. 

## Flower Client & Flower Server

In this section the heading of Flower Client should be ### and not ##. It is part of project setup and not an own section. At least flower client and flower server should have the same heading. 

They provide all the needed code to run a server and a client. It was straight forward to follow this section and to train a model federated with multiple clients. The code for client and server was valid and also to start a server and clients was an easy task with the given commands in the secion 'Train model (locally), federated'. However there should be a typo in the second command to run a client (shown below). 

```
python /client.py --partition-id 0 --server-address 127.0.0.1:8080
```

The / before client.py has to be removed to run a client. With it we get the following error:

```
python: can't open file '/client.py': [Errno 2] No such file or directory
```

However, even if everything runs straight out of the box, a few images of the server and client output would be good in this section. Therefore a user could check if his server/client works as it should. This is the output when we start a server and two clients:

Server output:

```
INFO :      Starting Flower server, config: num_rounds=2, no round_timeout
INFO :      Flower ECE: gRPC server running (2 rounds), SSL is disabled
INFO :      [INIT]
INFO :      Requesting initial parameters from one random client
INFO :      Received initial parameters from one random client
INFO :      Evaluating initial global parameters
INFO :      initial parameters (loss, other metrics): 0, {'Aggregated histograms': []}
INFO :
INFO :      [ROUND 1]
INFO :      configure_fit: strategy sampled 2 clients (out of 2)
INFO :      aggregate_fit: received 2 results and 0 failures
INFO :      fit progress: (1, 0, {'Aggregated histograms': ['Length:', '4', '2', '0', '6', '2', '4', '2', '4', '2', '4', 'Width:', '2', '8', '2', '6', '4', '4', '2', '0', '0', '2']}, 57.245370004000506)
INFO :      configure_evaluate: no clients selected, skipping evaluation
INFO :
INFO :      [ROUND 2]
INFO :      configure_fit: strategy sampled 2 clients (out of 2)
INFO :      aggregate_fit: received 2 results and 0 failures
INFO :      fit progress: (2, 0, {'Aggregated histograms': ['Length:', '4', '2', '0', '6', '2', '4', '2', '4', '2', '4', 'Width:', '2', '8', '2', '6', '4', '4', '2', '0', '0', '2']}, 57.250813433000076)
INFO :      configure_evaluate: no clients selected, skipping evaluation
INFO :
INFO :      [SUMMARY]
INFO :      Run finished 2 rounds in 57.25s
INFO :      History (loss, centralized):
INFO :          '\tround 0: 0\n\tround 1: 0\n\tround 2: 0\n'History (metrics, centralized):
INFO :          {'Aggregated histograms': [(0, []),
INFO :                                     (1,
INFO :                                      ['Length:',
INFO :                                       '4',
INFO :                                       '2',
INFO :                                       '0',
INFO :                                       '6',
INFO :                                       '2',
INFO :                                       '4',
INFO :                                       '2',
INFO :                                       '4',
INFO :                                       '2',
INFO :                                       '4',
INFO :                                       'Width:',
INFO :                                       '2',
INFO :                                       '8',
INFO :                                       '2',
INFO :                                       '6',
INFO :                                       '4',
INFO :                                       '4',
INFO :                                       '2',
INFO :                                       '0',
INFO :                                       '0',
INFO :                                       '2']),
INFO :                                     (2,
INFO :                                      ['Length:',
INFO :                                       '4',
INFO :                                       '2',
INFO :                                       '0',
INFO :                                       '6',
INFO :                                       '2',
INFO :                                       '4',
INFO :                                       '2',
INFO :                                       '4',
INFO :                                       '2',
INFO :                                       '4',
INFO :                                       'Width:',
INFO :                                       '2',
INFO :                                       '8',
INFO :                                       '2',
INFO :                                       '6',
INFO :                                       '4',
INFO :                                       '4',
INFO :                                       '2',
INFO :                                       '0',
INFO :                                       '0',
INFO :                                       '2'])]}
INFO :
```

client1 output:
```
UserWarning: The currently tested dataset are ['mnist', 'cifar10', 'fashion_mnist', 'sasha/dog-food', 'zh-plus/tiny-imagenet']. Given: hitorilabs/iris.
  warnings.warn(
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: get_parameters message 15b42f43-eba6-492c-bb2c-79b805d450fa
INFO :      Sent reply
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 7f34e1c2-d7c0-455b-8b90-8d9db0604b84
INFO :      Sent reply
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message c6b4ea98-39e5-43fb-a40b-91ff5b1c4961
INFO :      Sent reply
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: reconnect message 2209b00f-4bfe-4191-8f0d-db219efcfe62
INFO :      Disconnect and shut down
```

client2 output:
```
UserWarning: The currently tested dataset are ['mnist', 'cifar10', 'fashion_mnist', 'sasha/dog-food', 'zh-plus/tiny-imagenet']. Given: hitorilabs/iris.
  warnings.warn(
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message b6782d94-d4e8-4964-9bbb-c862017b5620
INFO :      Sent reply
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 806ab92e-4a5c-464a-bba3-8b1029bda65e
INFO :      Sent reply
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: reconnect message 2fe19b6b-a0f1-452f-a809-671698baa159
INFO :      Disconnect and shut down
```

As we can see the clients trained something and sended it to the server, which than updated the model from the server. Some explanation of it would be good in this section. I am also not sure if it is correct that the server and clients get shut down, if we start a second client. 


## Run Project

After cloning the repository you have to go into the folder and therefore the correct command would be:
```
cd Research-Projects-2024/tutorial-1
```

To start a docker container we need docker-compose installed. This should also be mentioned in the installation section. 

When we tried to start a docker container with the given command we got the following error:
```
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```
Therefore we had to execute the following command to start the docker daemon:
```
sudo systemctl start docker
```
Now we could execute the docker-compose command but had to do it with sudo permissions. It could be possible that this was only for me necessary because of my arch system. 

However, we really liked the explanation of the docker-compose.yml file. It gave a better understanding of docker and what happens behind the command we executed.


## Running a Dynamic System with Federated Learning

When running the following command:
```
docker build -t federated_learning_server:latest server/.
```

We get this error:
```
Step 3/6 : COPY ../requirements.txt requirements.txt
COPY failed: forbidden path outside the build context: ../requirements.txt ()
```

The problem is the following line in the server/Dockerfile file:
```
COPY ../requirements.txt requirements.txt
```
It has to be replaced with 
```
COPY . .
```

and the requirements.txt has to be copied manually into the server folder before executing the docker build command. 

After making this changes the command can be executed to build the docker image for the server. 

When creating a shell script you always have to change it to an executable file. The following line has to be executed before running the script. 
```
chmod +x run_random_clients.sh
```

After running the script, the clients were created and updated the server model as described in the tutorial.


## Summary
We liked the tutorial. It was simple and gave a good look into federated learning. It showed a simple way to implement such a system. Also the theory explained in this tutorial helped to understand the topic. We had some issues which were not covert in this tutorial but it could also be because of my arch system. All in all the tutorial was good structured and easy to follow. 

## Grade
8/10 because of small mistakes. All in all it is a good tutorial, which gives a good look into federated learning. 
