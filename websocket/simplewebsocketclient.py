import websockets
import asyncio


def lambda_handler(event, context):
    
    async def listen():
        
        # Jupyter notebook instance listen on eth2 ip 
        # run ifconfig and get the new ip address of the image
        # open a terminal window and start the server hosting on that ip
        # the name of the websocket server app is serverwebsocket.py
        url = "ws://172.51.1.254:7890"
        
        async with websockets.connect(url) as ws:
            message = """{"filename":"SageMaker/websocket.txt", "message":"Generated by lambda"}"""
            print("Sending parameters: {}".format(message))
            await ws.send(message)
    
            msg = await ws.recv()
            print(msg)
    
    asyncio.get_event_loop().run_until_complete(listen())
    
    return "Message sent to %s on port 7890" % url
