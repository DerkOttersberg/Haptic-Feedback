# Test Plan: VR and Haptic Integration in an Extended Reality Environment

---

## Introduction
The purpose of this document is to provide the **Test Plan** for the **VR and Haptic Cloud Integration** project. The **Test Plan** outlines the testing strategy and procedures to validate requirements, while the [Test Report](Testreport.md) documents the results and observations of each test. Together, they ensure critical functionalities are implemented correctly and meet the defined acceptance criteria.

This document is structured as follows:
- **Requirements**: Describes the requirements from the product backlog.
- **Test Plan**: Contains all the tests that need to be conducted for these requirements.

---

## Requirements (Product Backlog)

The following table summarizes the project requirements, prioritized using the **MoSCoW** method:

| **ID** | **Requirement**                              | **Priority** |
| ------ | -------------------------------------------- | ------------ |
| 2      | Use an actual VR headset for the application | Must         |
| 3      | Remote Rendering Implementation              | Must         |
| 4      | Network Degradation Simulation               | Must         |
| 5      | Performance Data Logging                     | Must         |
| 6      | Data Analysis                                | Must         |
| 7      | Users get haptic feedback                    | Must         |
| 16     | Allow the usage for different VR headsets    | Could        |
| 18     | Users can connect from all over the world    | Could        |

---

## Setup Guides
Follow install and usage guides from [user guides](/Deliverables-P56/Usage-guide.md)

### Global Setup
1. Open the Unity project.
2. Follow the **ALVR** usage guide.
3. Optional steps:
   1. **Clumsy**: Follow usage guide for Clumsy.
   2. **Logging**: Follow the Logging script usage guide.
   3. **Analysis**: Follow the Graphing script usage guide.
   4. **VPN**: 
      1. Connect both headset and laptop to the same VPN (follow setup from VPN for remote streaming guide).
      2. Use the VPN IP of the client in the **ALVR** discovery.
   5. **Unity Latency**: Follow Unity Haptic Delay usage guide.
4. Press **Start** in Unity.

---

## Test Plan
> **Note:** that for all tests the WiFi or Ethernet connection quality and speed heavily impacts the performance and experience of the session.
---

### Test 1: VR Headset Usage and Compatibility  
**Requirements**: 2 (Use an actual VR headset), 16 (Allow usage for different VR headsets)  
**Objective**: Verify the application works with different VR headsets.

### Setup Steps:
1. Open the Unity project.
2. Set up **ALVR** and connect the first VR headset (e.g., Oculus Rift).
3. Run the application on the first headset.
4. Set up **ALVR** for a second VR headset (e.g., HTC Vive, Valve Index).
5. Run the application on the second headset.

### Expected Results:
- Both headsets should work smoothly with the application.
- No significant issues with performance, tracking, or visual display across devices.

### Success Criteria:
- The application should be responsive, and tracking should remain accurate with both headsets.
- The performance should not degrade below a **60 FPS** threshold on any headset.

---

### Test 2: Remote Rendering Implementation  
**Requirements**: 3 (Remote Rendering)  
**Objective**: Verify if the application can be rendered remotely when the headset is disabled.

### Setup Steps:
1. Open Unity and run the **ALVR** client.
2. Disable **ALVR** on the VR headset (disconnect or turn off the headset).
3. Observe if the VR content is rendered correctly on the laptop screen.
4. Interact with the application on the laptop and note if any functionality is missing or broken.

### Expected Results:
- The VR content should show correctly on the laptop screen when the headset is turned off.
- The application should maintain fluid visuals without noticeable delays or rendering artifacts.

### Success Criteria:
- The content should render smoothly with a frame rate of at least **30 FPS** on the laptop screen.
- There should be no major artifacts or missing functionality.

---

### Test 3: Network Degradation Simulation  
**Requirements**: 4 (Network Degradation), 5 (Performance Data Logging)  
**Objective**: Verify the performance of the application under varying network conditions.

### Setup Steps:
1. Open the Unity project and connect the VR headset.
2. Open **Clumsy** and simulate network degradation by setting **latency** to:
   - **50ms**
   - **100ms**
   - **200ms**
3. Use the VR app and perform the following interactions:
   - Move around in the virtual space.
   - Trigger haptic feedback.
4. Repeat the test at each latency setting.
5. Record frame rates, input delay, and haptic feedback accuracy during each test.

### Expected Results:
- **50ms latency**: The system should run smoothly without noticeable lag.
- **100ms latency**: Minor delays may be noticed, but the application should remain usable.
- **200ms latency**: The system should exhibit noticeable lag, especially in haptic feedback and input response.

### Success Criteria:
1. **Frame Rate**:
   - At **50ms latency**, the **frame rate** should remain above **45 FPS**.
   - At **100ms latency**, the **frame rate** should still be above **45 FPS** but may show slight degradation.
   - At **200ms latency**, the **frame rate** might drop slightly but should **not fall below 30 FPS** to ensure the experience is still playable.

2. **Input Delay**:
   - At **50ms latency**, **input delay** should ideally be **≤ 50ms** (or close to the network latency).
   - At **100ms latency**, **input delay** should remain **≤ 100ms**.
   - At **200ms latency**, **input delay** should **not exceed 200ms**, keeping the VR experience responsive.

3. **Haptic Feedback**:
   - At **50ms latency**, haptic feedback should remain **accurate** and feel **in-sync** with user actions, with a tolerance of **≤ 50ms** difference.
   - At **100ms latency**, haptic feedback may experience a slight **delay** (≤ **100ms**), but should remain **accurate** and responsive.
   - At **200ms latency**, haptic feedback may experience a **notable delay**, but should still be **within ±150ms** of expected timing.

---

### Test 4: Performance Data Logging and Analysis  
**Requirements**: 5 (Data Logging), 6 (Data Analysis), 7 (Haptic Feedback)  
**Objective**: Verify if performance data (frame rates, latency, haptic feedback) is logged and analyzed correctly.

### Setup Steps:
1. Set up **ALVR** and connect the headset.
2. Simulate network latency using **Clumsy** (test at **50ms**, **100ms**, and **200ms**).
3. Trigger actions in the VR app (e.g., moving around, interacting with virtual objects).
4. Ensure data is being logged accurately (check log files after each test).
5. Analyze the logged data to see if frame rates, input delays, and haptic feedback are being recorded.

### Expected Results:
- Data should be logged correctly in the specified format (**JSON**).
- Performance should be captured with metrics like **frame rate** and **latency**.
- The system should log performance degradation with increasing network latency.

### Success Criteria:
- **Frame rate logs** should show a steady decline with increasing latency but not fall below **30 FPS** at **200ms latency**.
- **Input delay logs** should show increasing delay with higher latencies but stay under **100ms** even with the highest latency.
- Success is determined when the **JSON formatted logs** are accurately recorded, which can be easily graphed using the provided script.
- The graph produced from the logs should resemble the ones from the experimental research, demonstrating expected performance degradation trends.

---

### Test 5: Global Connectivity (Single User from Different Locations)  
**Requirements**: 18 (Users can connect from all over the world)  
**Objective**: Verify that a single user can connect and interact in the VR environment from different locations.

### Setup Steps:
1. **Prepare the VR system**: Set up the VR system for remote streaming and ensure it is ready to use.
2. **Connect the devices to VPN**: Ensure the **VR headset** and **laptop** are connected to the **same VPN**.
3. **Test from Different Locations**:
   - Have one user connect from one location (e.g., home or office).
   - Then, test by having the same user connect from a **different location** (e.g., different network, using VPN).
4. **Test interaction**:
   - Ensure the user can see the VR content and interact as expected in both locations.
5. **Test latency**:
   - Measure the **ping time** (latency) between the two locations using the metrics from ALVR.
   
### Expected Results:
- The VR content should load and display correctly from both locations.
- The user should be able to interact without major issues.
- **Audio and visual synchronization** should be smooth.

### Success Criteria:
- The system should work properly in both locations with a ping time of no more than **150ms**.
- The user should be able to interact in the VR environment with minimal input lag.
