# snowplow-Vision-system

## Dependencies

### April tag

1. somewhere not in the snowplow repo clone this guy: https://github.com/AprilRobotics/apriltag
2. Follow build instructions defined in the read of the projects.
basically:

```bash

sudo apt install python3 python3-pip
sudo pip3 install numpy
cmake .
sudo make install
```

### Real sense camera

**References:**
- https://github.com/IntelRealSense/librealsense/blob/development/doc/distribution_linux.md
- https://www.intelrealsense.com/get-started-depth-camera/


install dependencies:

```bash
sudo apt-key adv --keyserver keys.gnupg.net --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key
sudo add-apt-repository "deb http://realsense-hw-public.s3.amazonaws.com/Debian/apt-repo bionic main" -u
sudo apt install  librealsense2-dkms librealsense2-utils librealsense2-dev librealsense2-dbg

```