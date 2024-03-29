import websockets
import asyncio
import json

def lambda_handler(event, context):
    
    async def listen():
        
        """
        Steps to follow on the server:        
        1. In terminal, go to the websocket directory and run the configserver.sh file
           > sh configserver.sh   
        2. In the terminal, change directory to SageMaker by typing the following:
           cd ~/SageMaker  
        3. Find the eth2 inet ip and inspect the used ports.
        4. In the terminal, start the websocket appliation by typing the follwoing: 
           python serverwebsocket.py ip port
           python serverwebsocket.py 000.00.0.000 0000
           Note: Make sure the port is not already open.
        5. The application will print the following:
            * The listening ip:port or websocket url
            * The home path of the application. It should be /home/ec2-user/SageMaker
        5. Your websocket application is listening inside the VPC within the security group firewall.
        
        How to use this client:        
        1. On the event bridge event dictionary set the ip address and port 
           to which the client will be sending the message.
           
           {"ip":"000.00.0.000", "port":0000} 
           
        2. Ensure your notebook has a markdown cell tagged as parameters.
           1. Go to Notebook Tools
           2. Add Tag + in Tags in Active Cell
           3. Name the tag parameters
           
        2. Configure the papermill_dict:
        {
            "notebook_parameters":{
                "parameter1":"argument1",
                "parameter2":"argument2",
                "parameter3":"argument3"
            }, 
            "notebook_path":"folder/subfolder/notebook_name.ipynb",
            "kernel_name":"python3"
        }        
        
        3. Trigger your Lambda function using the event bridge rule.
        """
        
        ip = event.get("ip")
        port = event.get("port")
        
        listening_websocket = "ws://{}:{}".format(ip, port)
        papermill_dict = {
            "notebook_parameters":{
                "dirname":"datageeks/projects/aws-dev/websockets",
                "basename":"nb-websocket.txt",
                "text":"Generated by Lambda function"
            }, 
            "notebook_path":"datageeks/projects/aws-dev/websockets/papermill.ipynb",
            "kernel_name":"python3"
        }        
        message = json.dumps(papermill_dict)  
        
        print(listening_websocket)
        
        async with websockets.connect(listening_websocket) as ws:
            
            print("Sending message to server: {}".format(message))
            await ws.send(message)
    
            msg = await ws.recv()
            print(msg)
    
    asyncio.get_event_loop().run_until_complete(listen())
