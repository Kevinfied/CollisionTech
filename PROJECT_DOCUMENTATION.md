# CollisionTech - Comprehensive Project Documentation

## Project Overview

**CollisionTech** is an intelligent collision detection and avoidance system developed for MasseyHacks hackathon. The project demonstrates real-time obstacle detection using computer vision and provides both visual and auditory warnings to prevent collisions. It combines software (computer vision, UI, API) with hardware (Arduino-controlled robot car) to create a proof-of-concept autonomous navigation system.

### Purpose
- Demonstrate advantages and disadvantages of 2D computer vision for obstacle detection
- Create a practical proof-of-concept for warehouse robot guidance systems
- Provide collision warning systems for driver safety
- Serve as an educational tool for driving safety and autonomous robot operation

### Key Achievements
- Real-time object detection and tracking using OpenCV
- Interactive parameter tuning for different lighting conditions
- Proximity-based warning system with visual and audio alerts
- Integrated hardware control for physical robot implementation
- User-friendly GUI with multiple interface modes

---

## Technology Stack

### Software Technologies
- **Python 3.x** - Primary programming language
- **OpenCV (cv2)** - Computer vision and image processing
- **Pygame** - GUI development and audio playback
- **Flask** - REST API server
- **NumPy** - Numerical computations for image processing
- **Winsound/Pygame Mixer** - Audio alert system

### Hardware Technologies
- **Arduino** - Microcontroller platform
- **L298N Motor Driver** - H-bridge motor controller
- **FlySky RC Receiver** - Radio control input
- **Webcam** - Video capture for computer vision
- **DC Motors** - Robot locomotion

### Development Tools
- **Git** - Version control
- **CAP_DSHOW** - DirectShow video capture on Windows

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     CollisionTech System                     │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐      ┌──────────────┐                     │
│  │   UI.py      │─────▶│  vision.py   │                     │
│  │  (Pygame UI) │      │  (OpenCV)    │                     │
│  └──────────────┘      └──────┬───────┘                     │
│                               │                              │
│                               │ Video Feed                   │
│                               ▼                              │
│                        ┌─────────────┐                       │
│                        │   Webcam    │                       │
│                        └─────────────┘                       │
│                                                               │
│  ┌──────────────┐                                            │
│  │   api.py     │      REST API (Optional)                  │
│  │  (Flask API) │◀─────Data Exchange                        │
│  └──────────────┘                                            │
│                                                               │
│  ┌──────────────────────────────────────────────┐            │
│  │         l298n_car.ino (Arduino)              │            │
│  │  ┌────────────┐         ┌─────────────┐     │            │
│  │  │ RC Control │────────▶│ Motor Driver│     │            │
│  │  └────────────┘         └─────────────┘     │            │
│  └──────────────────────────────────────────────┘            │
└─────────────────────────────────────────────────────────────┘
```

---

## Component Breakdown

### 1. UI.py - Graphical User Interface (348 lines)

**Purpose:** Provides an interactive menu system for the CollisionTech application with visual feedback and navigation.

**Key Features:**
- **Main Menu System** with three interactive buttons:
  - INTRODUCTION - Displays project information
  - START - Launches the vision detection system
  - ABOUT US - Links to GitHub README
- **Custom Font Integration** - Uses SunnySunday.ttf for branded appearance
- **Smooth Button Animations** - Hover effects with expanding buttons
- **Background Graphics** - Professional UI with custom assets

**Technical Implementation:**
```python
# Display Configuration
- Window Size: 960x720 pixels
- Multiple font sizes (12, 24, 56, 72pt)
- Custom background and button graphics
```

**Key Functions:**
- `cursor(x, y)` - Renders crosshair cursor for camera mode
- Menu state management with flags (button1Hover, button2Hover, button3Hover)
- Event handling for mouse clicks and keyboard shortcuts (ESC, G, C)

**Flow:**
1. Initialize Pygame and load assets
2. Display main menu with three options
3. Handle user interactions (mouse hover, clicks, keyboard)
4. Transition to vision system when START is clicked
5. Call `vision.run()` to start detection

**Resume Highlights:**
- Implemented event-driven GUI with Pygame
- Created smooth hover animations with real-time rendering
- Integrated multiple interface modes with state management
- Designed user-friendly navigation system

---

### 2. vision.py - Computer Vision Engine (161 lines)

**Purpose:** Core obstacle detection system using OpenCV for real-time video analysis and collision warning.

**Key Features:**
- **Real-time Object Detection** using binary thresholding and contour analysis
- **Adjustable Parameters** via trackbars for different lighting conditions:
  - Threshold (0-255)
  - Minimum Area (0-30,000 pixels²)
  - Maximum Area (0-30,000 pixels²)
  - Margin of Error (0-1.0)
  - Safe Radius (1.3-130 pixels)
- **Shape Recognition:**
  - Triangles (3 sides) - Detected as obstacles
  - Squares/Rectangles (4 sides) - Used for robot position tracking
- **Proximity Warning System:**
  - Visual alerts (color change from green to red)
  - Audio alerts (beep sound when too close)
- **Robot Position Tracking:**
  - Dual-marker system (triangle + square)
  - Direction vector visualization
  - Center point calculation

**Technical Implementation:**

**Image Processing Pipeline:**
```python
1. Capture frame from webcam (cv2.VideoCapture)
2. Apply Gaussian blur (7x7 kernel) for noise reduction
3. Convert to grayscale
4. Binary threshold to isolate shapes
5. Find contours (cv2.findContours)
6. Filter by area and approximate polygons
7. Classify shapes by vertex count
8. Calculate distances and trigger warnings
```

**Collision Detection Algorithm:**
```python
# For each obstacle:
distSqr = (robotX - obstacleX)² + (robotY - obstacleY)²
safeDistSqr = (safeRadius + obstacleRadius)²

if distSqr < safeDistSqr:
    # Trigger visual and audio warning
```

**Key Functions:**
- `th(*args)` - Threshold adjustment callback
- `minArea(*args)` - Minimum area filter callback
- `maxArea(*args)` - Maximum area filter callback
- `errorMargin(*args)` - Shape approximation tolerance callback
- `changeSaftey(*args)` - Safe distance radius callback
- `run()` - Main detection loop

**Global Variables:**
- `counter` - Threshold value (0-255)
- `minA`, `maxA` - Area filters (in pixels²)
- `errorMar` - Contour approximation epsilon
- `safeRadius` - Safe distance around robot
- `obsticles` - List of detected obstacle coordinates (x, y, radius)

**Resume Highlights:**
- Developed real-time computer vision system using OpenCV
- Implemented adaptive thresholding and contour detection algorithms
- Created proximity-based collision warning system with multi-modal alerts
- Optimized image processing pipeline for real-time performance
- Designed adjustable parameter system for environmental adaptability

---

### 3. api.py - REST API Server (24 lines)

**Purpose:** Provides a lightweight Flask-based REST API for potential data exchange between components.

**Key Features:**
- **Simple in-memory database** (dictionary-based storage)
- **Three endpoints:**
  - `GET /` - Health check endpoint
  - `POST /base` - Store robot position data
  - `GET /base` - Retrieve stored position data

**API Endpoints:**

```python
# Health Check
GET /
Response: {"message": "It works!"}

# Store Data
POST /base
Body: JSON object with robot coordinates
Response: Stored data

# Retrieve Data
GET /base
Response: Previously stored JSON data
```

**Technical Implementation:**
- Runs on `0.0.0.0:8000` (accessible on local network)
- Debug mode enabled for development
- Global state management with `verySecureDatabase` dictionary

**Resume Highlights:**
- Developed RESTful API using Flask framework
- Implemented JSON-based data exchange protocol
- Created endpoints for real-time data storage and retrieval
- Configured for network accessibility and debugging

---

### 4. l298n_car.ino - Arduino Motor Controller (212 lines)

**Purpose:** Controls a two-wheeled robot car using L298N motor driver with RC receiver input.

**Key Features:**
- **Dual Motor Control** (Motor A and Motor B)
- **PWM Speed Control** (0-255 range)
- **Two Drive Modes:**
  - **Arcade Drive** - Single stick controls forward/backward and turning
  - **Tank Drive** - Independent left/right motor control
- **RC Receiver Integration** - FlySky receiver with PWM input (1000-2000µs)
- **Joystick Deadzone** - Prevents drift when joystick is centered
- **Variable Speed Control** - Smooth acceleration/deceleration

**Hardware Connections:**

```
Motor A (Left):
- Enable: Pin 9 (PWM)
- IN1: Pin 2
- IN2: Pin 3

Motor B (Right):
- Enable: Pin 6 (PWM)
- IN3: Pin 4
- IN4: Pin 5

RC Receiver:
- Channel 2 (Vertical): Pin 21
- Channel 4 (Horizontal): Pin 19
```

**Key Functions:**

**1. `setup()`**
- Initializes pin modes (OUTPUT for motors, INPUT for RC)
- Sets initial motor state (all LOW)
- Begins serial communication at 9600 baud

**2. `loop()`**
- Reads PWM signals from RC receiver
- Maps and filters joystick values
- Calls active drive mode function

**3. `arcadeDrive()`**
- **Forward/Backward:** Controlled by vertical stick (va2b)
- **Turning:** Controlled by horizontal stick (va4b)
- **Left Motor Speed:** `fwd - turn`
- **Right Motor Speed:** `fwd + turn`
- Allows for smooth curved driving

**4. `tankDrive()`**
- Independent control of left and right motors
- More precise turning capability
- Better for tight spaces

**5. `directionControl()`**
- Test function for motor direction verification
- Not used in main loop

**PWM Signal Processing:**
```cpp
// Input: 1000-2000µs from RC receiver
// Deadzone: 1485-1515µs (centered stick)
// Output: -255 to +255 (motor speed and direction)

Mapping:
1000µs → -255 (full reverse)
1500µs → 0 (stopped)
2000µs → +255 (full forward)
```

**Resume Highlights:**
- Programmed Arduino microcontroller for motor control
- Implemented dual-mode drive system (arcade and tank)
- Developed PWM signal processing with deadzone filtering
- Created differential drive algorithm for smooth turning
- Integrated RC receiver input with motor output mapping

---

## Data Flow and Integration

### Vision System to Robot Control (Conceptual)

While the current implementation doesn't have complete integration, the architecture supports:

```
Camera → vision.py → api.py → Robot Controller
   │         │          │            │
   │         │          │            └─► Motor Commands
   │         │          └─────────────► Position Data
   │         └────────────────────────► Obstacle Detection
   └──────────────────────────────────► Video Feed
```

**Potential Integration Points:**
1. `vision.py` detects obstacles and robot position
2. Sends data via `api.py` POST endpoint
3. Arduino code could query API for navigation decisions
4. Automatic avoidance maneuvers based on proximity warnings

---

## File Structure

```
CollisionTech/
├── UI.py                    # Main GUI application
├── vision.py                # Computer vision detection system
├── api.py                   # Flask REST API server
├── README.md                # Contributor information
├── introduction.txt         # Project goals
├── beep-02.mp3             # Warning sound effect
├── .gitignore              # Git ignore rules
├── assets/                 # UI assets directory
│   ├── SunnySunday.ttf     # Custom font
│   ├── background2.png     # Main background
│   ├── MHlogo.png          # MasseyHacks logo
│   ├── betterCamera.png    # Camera icon
│   ├── button*.png         # Button graphics
│   └── github.png          # GitHub icon
└── l298n_car/              # Arduino project
    └── l298n_car.ino       # Motor control code
```

---

## Setup and Installation

### Software Requirements

**Python Dependencies:**
```bash
pip install opencv-python
pip install pygame
pip install flask
pip install numpy
```

**Hardware Requirements:**
- Webcam (USB or built-in)
- Arduino board (Uno, Nano, or compatible)
- L298N motor driver module
- 2x DC motors
- FlySky RC transmitter and receiver (optional)
- Power supply (7-12V for motors)

### Running the Application

**1. Start the UI:**
```bash
python UI.py
```

**2. Start the API Server (optional):**
```bash
python api.py
```

**3. Upload Arduino Code:**
- Open `l298n_car/l298n_car.ino` in Arduino IDE
- Select correct board and port
- Upload to Arduino

**4. Vision System:**
- Click "START" in the UI to launch vision detection
- Adjust parameters using trackbars for optimal detection
- Press 'Q' to quit vision mode

---

## Usage Instructions

### Vision Detection System

**Parameter Tuning:**
1. **Threshold** - Adjust based on lighting conditions
   - Higher values (200+) for bright environments
   - Lower values (100-150) for dim lighting
   
2. **Min/Max Area** - Filter detected objects by size
   - Prevents false positives from noise or irrelevant objects
   - Adjust based on camera distance and object size
   
3. **Margin of Error** - Shape approximation tolerance
   - Lower values require more precise shapes
   - Higher values allow for imperfect shapes
   
4. **Safe Radius** - Collision warning distance
   - Larger radius provides earlier warnings
   - Smaller radius reduces false alarms

**Keyboard Shortcuts:**
- `ESC` - Return to main menu
- `G` - Open GitHub repository
- `C` - Toggle camera mode
- `Q` - Quit vision system

### Robot Control

**Arcade Drive Mode:**
- Vertical stick: Forward/Backward
- Horizontal stick: Turn left/Right
- Combined input creates curved paths

**Tank Drive Mode:**
- Left stick: Left motor speed/direction
- Right stick: Right motor speed/direction
- Better for precise positioning

---

## Technical Highlights for Resume

### Computer Vision & Image Processing
- **Real-time object detection** using OpenCV contour analysis
- **Adaptive thresholding** with user-adjustable parameters
- **Shape classification** using polygon approximation
- **Gaussian blur** for noise reduction
- **Distance calculation** for proximity detection
- **Multi-object tracking** with coordinate mapping

### GUI Development
- **Event-driven architecture** with Pygame
- **State machine** for menu navigation
- **Animation system** for interactive elements
- **Custom font rendering** and text layout
- **Image asset management** and scaling
- **Responsive design** with hover effects

### Embedded Systems
- **Arduino programming** in C/C++
- **PWM motor control** with H-bridge driver
- **RC receiver integration** via pulse width reading
- **Signal processing** with mapping and filtering
- **Differential drive algorithms**
- **Serial debugging** and monitoring

### Software Engineering
- **Modular architecture** with separated concerns
- **RESTful API** design with Flask
- **Global state management**
- **Error handling** and input validation
- **Code documentation** with inline comments
- **Version control** with Git

### Problem Solving
- **Real-world application** of computer vision
- **Hardware-software integration**
- **Environmental adaptation** through parameter tuning
- **Multi-modal feedback** (visual + audio)
- **Proof-of-concept development**

---

## Algorithms and Techniques

### 1. Contour Detection Algorithm

```python
# Pseudocode
for each frame:
    blur = GaussianBlur(frame, kernel_size=7x7)
    grayscale = convertToGray(blur)
    binary = threshold(grayscale, threshold_value)
    contours = findContours(binary)
    
    for each contour:
        if area_is_valid(contour):
            vertices = approximatePolygon(contour)
            
            if vertices == 3:
                classify_as_obstacle()
            elif vertices == 4:
                classify_as_robot_marker()
```

### 2. Proximity Warning Algorithm

```python
# Pseudocode
robot_center = calculate_midpoint(marker1, marker2)

for each obstacle:
    distance = euclidean_distance(robot_center, obstacle)
    safe_distance = safe_radius + obstacle_radius
    
    if distance < safe_distance:
        trigger_warning()
        change_visual_indicator()
        play_audio_alert()
```

### 3. Arcade Drive Algorithm

```cpp
// Differential drive calculation
left_motor = forward_speed - turn_rate
right_motor = forward_speed + turn_rate

// Example:
// Forward only: left=100, right=100 → straight
// Turn right: left=100, right=50 → curve right  
// Spin right: left=100, right=-100 → rotate in place
```

---

## Performance Considerations

### Vision System Optimization
- **Gaussian blur** reduces noise and improves contour detection
- **Binary thresholding** simplifies shape detection
- **Area filtering** eliminates unnecessary computations
- **Frame-by-frame processing** achieves real-time performance

### Memory Management
- **In-place operations** for image processing
- **List clearing** for obstacle tracking each frame
- **Efficient data structures** (lists and tuples)

### Real-time Constraints
- **OpenCV optimization** using compiled C++ backend
- **Minimal frame delay** with `cv2.waitKey(1)`
- **Direct hardware access** via CAP_DSHOW

---

## Future Enhancements

### Software Improvements
- [ ] Complete API integration for autonomous control
- [ ] Machine learning for obstacle classification
- [ ] Multi-camera support for 360° awareness
- [ ] Path planning algorithms
- [ ] Automatic lighting adjustment
- [ ] Data logging and analytics

### Hardware Enhancements
- [ ] Ultrasonic sensors for depth perception
- [ ] IMU for orientation tracking
- [ ] GPS for outdoor navigation
- [ ] Servo-mounted camera for pan/tilt
- [ ] LED indicators for warning states
- [ ] LCD display for status information

### Feature Additions
- [ ] Recording and playback of detection sessions
- [ ] Configurable profiles for different environments
- [ ] Network streaming of video feed
- [ ] Mobile app integration
- [ ] Voice commands and feedback
- [ ] Advanced analytics dashboard

---

## Project Context

**Developed for:** MasseyHacks Hackathon  
**Team Members:**
- Noah Levy (ThePillowCat) - Competitive Programming
- Raymond Wu (Raymond131) - Arduino & Robotics
- Kevin Xu (Kevinfied) - Python & C++ Development
- Kevin Lu (kevin21studios) - CAD & Physical Design

**Educational Value:**
This project serves as an excellent learning experience in:
- Computer vision application development
- Hardware-software integration
- Real-time systems programming
- Team collaboration and project management
- Proof-of-concept prototyping

---

## Code Quality and Best Practices

### Implemented Practices
✅ Modular code organization  
✅ Descriptive variable names  
✅ Inline documentation  
✅ Error handling for file loading  
✅ Configurable parameters  
✅ Version control with Git  
✅ Separation of concerns (UI, Vision, API, Hardware)  

### Areas for Production Enhancement
- Add comprehensive error handling
- Implement unit tests
- Create configuration files for parameters
- Add logging system
- Document API with OpenAPI/Swagger
- Create installation scripts
- Add requirements.txt for Python dependencies

---

## Summary

CollisionTech demonstrates a complete robotics system integrating:
- **Computer Vision** - Real-time obstacle detection
- **User Interface** - Interactive GUI with Pygame
- **API Services** - REST endpoints for data exchange  
- **Embedded Control** - Arduino motor control
- **Multi-modal Feedback** - Visual and audio warnings

This project showcases practical application of multiple technologies working together to solve a real-world problem, making it an excellent portfolio piece for demonstrating full-stack development capabilities spanning software and hardware domains.

---

## License and Usage

This is an educational project developed for MasseyHacks. Feel free to use as reference for learning purposes.

**GitHub Repository:** https://github.com/Kevinfied/CollisionTech

---

**Documentation Generated:** November 2024  
**Project Version:** 1.0 (Hackathon Proof-of-Concept)
