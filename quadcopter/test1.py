
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

# Close vehicle object before exiting script
vehicle.close()

