
# Import DroneKit-Python
from dronekit import time,connect, VehicleMode

# Connect to the Vehicle.
print "Connecting to vehicle on: '/ttyACM0'"
vehicle = connect('/dev/ttyACM0', wait_ready=True)

# Get some vehicle attributes (state)
print "Get some vehicle attribute values:"
print " GPS: %s" % vehicle.gps_0
print " Battery: %s" % vehicle.battery
print " Last Heartbeat: %s" % vehicle.last_heartbeat
print " Is Armable?: %s" % vehicle.is_armable
print " Vehicle Arm?: %s" % vehicle.armed
print " System status: %s" % vehicle.system_status.state
print " Mode: %s" % vehicle.mode.name    # settable

def arm_and_takeoff(aTargetAltitude):
    """
        Arms vehicle and fly to aTargetAltitude.
    """
    print "Basic pre-arm checks"
     # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print " Waiting for vehicle to initialise..."
        time.sleep(1)
    print "Arming motors"
    vehicle.mode    = VehicleMode("GUIDED")
    vehicle.armed   = True
    while not vehicle.armed:
        print " Waiting for arming..."
        time.sleep(1)
    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
            print "Reached target altitude"
            break
        time.sleep(1)

arm_and_takeoff(20)
# Close vehicle object before exiting script
#vehicle.close()

