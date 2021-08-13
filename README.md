# BouncingBallOnASpikyTrack

The objective of the game is to find a way to stop the ball in a safe place on the track

example
consider a track given below, 1 represents spikes and 0 represents safe places to land
index : [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
track : [0,0,0,1,1,0,0,1,1,1,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ]

now consider a ball with a given initial speed, 3
for every move the player can chose to retain the speed, increase the speed by 1, decrease the speed by 1

consider on senario,

the ball starts in index 0 with speed 3,
if the player retain the speed, the ball lands in spike
hence the player has to decrease the speed to 2
then the ball lands in index 2,
next the player has to incerease the speed to 3
ball lands in index 5

and so on, the success full end for then game is when the ball can land safely in a index and the speed is 0
everything else is a failure

the game returs succees or failure, for a given track and initial speed
