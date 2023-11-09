import numpy as np

# Joint radia
R_MCP = 8 # mm
R_PIP = 6 # mm

# Spool radia radius (ext/flex)
ratio_MCP = 1
ratio_PIP = 1.8

# ------------------- Calculations of Tendon Lengths at single joint ------------------- #

def tendonlength_flexor_joint1(theta_joint1):
   '''Input: joint angle of joint1 in rad
      Output: total normal lengths of flexor tendon through joint1
      Kinematic calculations provided by Shubham'''
   theta_joint1 = theta_joint1/2
   l1 = R_MCP*(np.sqrt(6 - 8*np.sin(theta_joint1) - 2*np.cos(2*theta_joint1)) - 2) #normalized: 0 at 0 degrees joint angle (coincides with 0 degrees of the motor angle)
   return l1

def tendonlength_extensor_joint1(theta_joint1):
   '''Input: joint angle of joint1 in rad
      Output: total normal lengths of extensor tendon through joint1'''
   theta_joint1 = theta_joint1/2
   return ratio_MCP * tendonlength_flexor_joint1(theta_joint1)

def tendonlength_flexor_joint2(theta_joint2):
   '''Input: joint angle of joint2 in rad
      Output: total normal lengths of flexor tendon through joint2'''
   theta_joint2 = theta_joint2/2
   l2 = R_MCP*(np.sqrt(6 - 8*np.sin(theta_joint2) - 2*np.cos(2*theta_joint2)) - 2)
   return l2

def tendonlength_extensor_joint2(theta_joint2):
   '''Input: joint angle of joint2 in rad
      Output: total normal lengths of extensor tendon through joint2'''
   theta_joint2 = theta_joint2/2
   return ratio_PIP * tendonlength_flexor_joint2(theta_joint2)

# ------------------- Calculations of Tendon Lengths for all joints ------------------- #
# calculate the tendon lengths for all joints for each finger (if needed)

# all 3 fingers are identical
def pose2tendon_finger(theta_Joint1, theta_Joint2):
   '''Input: controllable joint angles
      Output: array of tendon lengths for given joint angles'''
   return [tendonlength_flexor_joint1(theta_Joint1),
            tendonlength_extensor_joint1(theta_Joint1),
            tendonlength_flexor_joint2(theta_Joint2), 
            tendonlength_extensor_joint2(theta_Joint2)]




# previous code:

# def tendonlength_flexor_joint1(theta_joint1):
#    '''Input: joint angle of joint1 in rad
#       Output: total normal lengths of flexor tendon through joint1'''
#    return np.sqrt(6.4**2 + 5.2**2 - 2*6.4*5.2*np.cos(1.92-theta_joint1))

# def tendonlength_extensor_joint1(theta_joint1):
#    '''Input: joint angle of joint1 in rad
#       Output: total normal lengths of extensor tendon through joint1'''
#    return np.sqrt(5.4**2 + 4.8**2 - 2*5.4*4.8*np.cos(1.92+theta_joint1))

# def tendonlength_flexor_joint2(theta_joint2):
#    '''Input: joint angle of joint2 in rad
#       Output: total normal lengths of flexor tendon through joint2'''
#    return np.sqrt(5.7**2 + 4.8**2 - 2*5.7*4.8*np.cos(1.81-theta_joint2))

# def tendonlength_extensor_joint2(theta_joint2):
#    '''Input: joint angle of joint2 in rad
#       Output: total normal lengths of extensor tendon through joint2'''
#    return np.sqrt(4.9**2 + 4.4**2 - 2*4.9*4.4*np.cos(1.81+theta_joint2))
