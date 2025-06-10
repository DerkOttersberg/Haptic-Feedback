# User Analysis for Project 5/6

## 1. Define the End Users
The following is no real information but some educated guesses.
- **Age Group:** Primarily between **25-40 years old**.
- **Gender:** Both **male** and **female**.
- **Experience Level:**
  - Includes both users with **prior experience in VR** and those who are **new to VR**.
  - Experience with haptic feedback devices varies, but familiarity with its purpose will be essential for evaluating its effectiveness in real-time VR environments.
- **Digital Skills:** Users range from **novice to advanced**, which might affect their adaptability in environments requiring high levels of immersion and interaction, such as **VR mission planning** or **simulated tasks**.

## 2. Context
The product will be used for **mission planning in a VR environment**, where users communicate via **headset and microphone**, and may experience terrain elevation through a **haptic device**.

- **Use Case:** Users will interact within a **virtual environment** to plan missions, likely simulating real-world scenarios.
- **Technology Requirements:** Users will need **VR headsets, microphones, and possibly controllers** to interact with the system.
- **Remote Access:** Users log in remotely, meaning the VR experience is rendered and streamed from a **remote server**. This reduces local hardware requirements but demands a **stable internet connection and low-latency streaming**.

## 3. How and When to Gather Input
- **Input will be collected during adaptable VR sessions** that test various latency levels and different haptic feedback delays.
  - **VR Sessions**: These sessions will include a combination of real-time collaboration and task-based scenarios. Users will be asked to perform tasks under various **latency conditions**, such as:
    - Basic movement and navigation.
    - Object manipulation.
    - Collaborative mission planning and decision-making.
  
- **Latency Impact Testing**: Network latency will be varied during testing to determine **user performance** and **comfort thresholds**.
- **Haptic Feedback Testing**: Users will experience **delayed feedback** through ultrasonic haptic devices to assess at what point feedback becomes **ineffective or distracting**.

- **Real-Time Feedback** will be gathered from users after each session, noting:
  - Task performance (e.g., accuracy, time to complete tasks, number of errors).
  - User comfort and satisfaction (e.g., perceived latency and comfort level during tasks).
  - Feedback on haptic feedback (e.g., effectiveness, accuracy, delay tolerance).

> **Note:** not everything that can be tested will be tested as of now, it is not certain yet what the final product will contain, such that it can be tested with users.

## 4. Testing Plan
**What needs to be tested**:
- **Usability**: How easily can users interact with the VR environment and complete tasks under varying latency conditions?
- **Performance**: How does latency affect user task completion, navigation accuracy, and collaboration?
- **User Comfort**: How do users perceive delays in both VR movement and haptic feedback, and what levels of latency are acceptable before discomfort occurs?
- **Haptic Feedback Tolerance**: How much delay can ultrasonic haptic arrays introduce before feedback becomes unusable or noticeable?

**How the testing will be done**:
- **Dynamic Testing Sessions**: Users will engage in **VR tasks** with network latency varying between **low, moderate, and high latency** conditions.
- **Real-Time Feedback**: After each session, users will provide subjective feedback about their experience, including discomfort levels, task difficulty, and overall satisfaction.
- **Task-Based Evaluation**: Tasks will be designed to test the interaction between latency, VR system responsiveness, and the effectiveness of haptic feedback.

## 5. Realistic Approach
- **User Group**: The testing will involve **team members** and other **study participants** familiar with VR or haptic feedback devices. Professional **end-users** may be involved in future testing if the timeline allows.
- **Real-Time Collaboration Testing**: Special attention will be paid to the **collaborative aspect** of mission planning and the effect of latency on team communication and task coordination, if the multiplayer aspect of the project have developed far enough.

## 6. Final Testing and Recommendations
- Test findings will directly inform **product refinement** to optimize for **acceptable latency levels** and **haptic feedback responsiveness**.
- **User feedback** will guide the development of solutions to reduce perceived delays and enhance overall **user comfort and performance** during extended VR sessions.  

To read about the final results one can read the [Experimental research](/Deliverables-P56/Evaluatie-Opdrachtgever.md).