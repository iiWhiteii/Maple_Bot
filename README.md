# Maple Bot 2

Presently, the development of this bot is ongoing. I am currently working on integrating YOLOv8 to establish a gym environment. A gym environment is a framework where the agent can undergo training based on past experiences to enhance its intelligence. This approach enables the agent to learn and improve its gameplay over time.

## OpenCV for template matching
<div style="position: relative; display: flex; align-items: flex-start;">
    <!-- Image on the left -->
    <div style="width: 50%;">
        <a href="https://www.youtube.com/watch?v=jl7Z8Bxk6uc&ab_channel=Liang" target="_blank">
            <img src="https://github.com/Whiteii/Maple_Bot/blob/main/Images/Animation.gif" alt="GIF" style="width: 100%;">
        </a>
    </div>
    <!-- Text on the right -->
    <div style="width: 50%; padding-left: 20px;">
        <p style="position: absolute; bottom: 0; left: 0;">
            Before, I had utilized OpenCV template matching and encountered various limitations, particularly in the detection of non-playable characters (NPCs). Now, I have opted to proceed with YOLOv8, and the performance is significantly improved.
        </p>
    </div>
</div>



## Yolov8
Currently, I am implementing YOLOv8 to capture faces of monsters and my character's position on the minimap. Additionally, there is a green circle on the minimap indicating a certain aspect of the environment.


<div style="float: right; margin-left: 2%;">
  <img src="https://github.com/Whiteii/Maple_Bot/blob/main/Images/image.png" alt="Bottom Image" width="450"/>
  <p>In the present implementation of YOLOv8, there are anticipated changes in the future. Instead of identifying the entire body of an NPC, the system will be configured to specifically detect their faces.</p>
</div> 

<div style="float: right; margin-left: 2%;">
    <a href="https://www.youtube.com/watch?v=Ys0eVH3Zu00&t=398s&ab_channel=Liang">
        <img src="https://raw.githubusercontent.com/Whiteii/Maple_Bot/main/Images/Animation7.gif" alt="Bottom Image" width="600"/>
    </a>
</div>

<p>
    Currently, I'm in the final stage of this project. The last part involves collecting specific data from my gameplay and feeding that data into a reinforcement learning algorithm known as DQN (Deep Q Learning). This allows our agent to learn in an environment where it gets rewarded for certain right actions and penalized for certain bad actions.
    <br><br>
    The algorithm has been successful in learning to play games like Breakout, Pong, and Space Invaders at or above human-level performance. I have currently implemented it in the modern 2D game known as Maplestory. During the current training of MapleBot, two issues have been identified: one related to computer vision and the other involving delayed rewards. For instance, if an agent presses 'Q' and defeats a monster, the computer vision delay may result in the reward being attributed to a subsequent right dash action.
</p>






