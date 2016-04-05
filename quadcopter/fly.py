from donekit import connect,VehicleMode
import time

vehicle = connect('/dev/ttyAMA0',wait_ready=True)

def arm_and_takeoff(aTargetAltitude):
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True    
    while not vehicle.armed:      
        print " Waiting for arming..."
        time.sleep(1)
    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude) #Take off to target altitude
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt 
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
            print "Reached target altitude"
            break
        time.sleep(1)

arm_and_takeoff(3)
vehicle.close()
