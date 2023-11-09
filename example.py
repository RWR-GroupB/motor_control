from gripper_controller import GripperController
import time


"""
Example script to control the finger joint angles
"""

homepos = [0, 0]
goalpos = [50, 80]


def main():
    global gc
    port_mac = "/dev/tty.usbserial-FT89F9JC"
    port_linux = "/dev/ttyUSB0"
    gc = GripperController(port=port_linux,calibration=False)

    gc.write_desired_joint_angles(goalpos)

    gc.wait_for_motion()

    time.sleep(1)

    gc.write_desired_joint_angles(homepos)

    gc.wait_for_motion()

    time.sleep(1)

    gc.terminate()


if __name__ == "__main__":
    main()