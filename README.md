# otterHacks

**Inspiration:**
With this project, we wanted to create a solution to detect diseases in plants.

**What it does:**
It reads an URL or uploads a file image to the website. The image will be processed to the website where the program will determine if the leave is potentially healthy or unhealthy. A new image with the rot highlighted will be generated. The results will be then displayed on the website with specific percentages and values. (percent of leaf inflicted with rot/ probability that image is of a rotting plant)

**How I built it:**
Python, HTML, Flask, CSS, OpenCV, TensorFlow

**Challenges we ran into:**
Working with HTML and Flask to update the generated image.
OpenCV was used to help identify the rot that TensorFlow determined to exist. 
TensorFlow's use of machine learning was more robust that of HAAR Cascade training. If we had more samples of rot, however,
using cascade training to create a rot classifier might've been more intune with using OpenCV.

**Accomplishments that we are proud of:**
Successfully identifying a leaf that is rotten vs healthy vs not a leaf Successfully highlighting rot location on leaves.

**What I learned:**
HTML, Flask, TensorFlow

**What's next for Plant Recognition:**
More training to recognize rot more accurately. Expansion to different plants and diseases Cleaner HTML + Flask integration
