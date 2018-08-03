import subprocess as spr
import time

spr.run(['clear'])
while(1):
    for k in range(200,220):
        print( "hello {}".format(k) )

    time.sleep(1)
    spr.run(['clear'])
    
    for k in range(100,120):
        print( "hello {}".format(k) )
    
    
    time.sleep(1)
    spr.run(['clear'])
