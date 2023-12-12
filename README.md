# Scooter-Student-Detection
My first project at UCR, where we identify scooters inside a class environment as it is illegal to bring scooters to class and also count the number of students in class to find out who is proxying.

The link to our data can be found on Roboflow where we manually clicked pictures in our college and labelled them using Roboflow's Polygon Annotation tool.
We used Yolov8 since it is one of the best and latest Object detection models out there.

All the results can be seen in the COLAB file and if you would like to run this project you would need to run the test.py file after installing all the dependencies that are required to run Yolov8 and you should also have best.pt which are the weights after training from Colab as I didn't wanna destroy my laptop :) 

If you run into errors it might be because you haven't changed source to 0.0.0.0 as we used an IP camera to predict data in realtime so change it back to that and you are all good to go!!!

We also had an opportunity to test our project live inside a classroom, so we did do it. Here is the demo of our project:- [Link](https://drive.google.com/file/d/1hu87Cd5GXxHTS7kJqNSXKxVkMdvmm8YG/view?usp=sharing)
