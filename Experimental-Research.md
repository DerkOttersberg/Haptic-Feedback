# Experimental Research: Measuring VR latency impact and haptic feedback delays

## 1. Introduction
This experiment evaluates the impact of **network latency** on the **VR user experience** and task performance while investigating the latency tolerance of ultrasonic **haptic feedback devices**. Our broader project focuses on integrating cloud-based VR streaming with ultrasonic haptic feedback within a networked extended reality (XR) environment, building on previous work by Chen et al. (2020) and Freeman et al. (2021). In this context, real-time user interaction is critical. Therefore, understanding how varying latency levels affect usability, task performance, and the effectiveness of haptic feedback is essential for optimizing system performance and enhancing user immersion.

The experiment provides valuable context for our overall project by simulating realistic network conditions and measuring their impact on both VR performance and haptic responsiveness. The insights gained will help guide future system optimizations and integration strategies.

---

## 2. Research questions
1. **What is the maximum acceptable latency (in ms) in VR environments before performance, usability, and user comfort are significantly disrupted?**  
2. **How much delay (in ms) can ultrasonic arrays introduce before the haptic feedback becomes ineffective?**

---

## 3. Methodology

### 3.1 VR Latency impact testing

**Setup:**
- **Hardware:**  
  - Oculus Meta Quest 3  
  - Laptop with Intel i7 12700h, RTX A1000, and 32 GB 4800 MHz RAM  
- **Software:**  
  - [ALVR](https://github.com/alvr-org/ALVR) for VR streaming (ALVR, n.d.)  
  - [Unity](https://docs.unity3d.com) for latency simulation and task execution (Unity Technologies, n.d.)  
  - [Clumsy](https://jagt.github.io/clumsy/) for simulating network latency (Clumsy, n.d.)  
- **Measurement tools:**  
  - Unity Profiler (to measure input latency and frame timing)  
  - User feedback forms (collecting ratings on motion sickness, task performance, and overall usability)

**VR Tasks:**  
Participants performed a series of predefined VR tasks designed to test various aspects of user interaction:
1. **Object manipulation:** Grabbing, moving, and releasing virtual objects.  
2. **Navigation:** Moving through a virtual environment modeled after a lab setting (inspired by *The Lab*).  
3. **Interactive Task:** Using a bow to shoot targets, which tests both precision and reaction time.

**Procedure:**
1. **Latency simulation:**  
   Network latency was simulated using Clumsy, with increments of 0 ms, 50 ms, 100 ms, 150 ms, 200 ms, 300 ms, and 400 ms.  
2. **User testing:**  
   Participants performed the VR tasks under each latency condition. After each test, they rated their experience on:  
   - **Motion sickness (scale 1–10)**  
   - **Task performance (scale 1–10)**  
   - **Overall usability (scale 1–10)**  
3. **Data collection:**  
   - **Quantitative data:** Frame rates and input delays (in ms) recorded using Unity Profiler.  
   - **Qualitative data:** User feedback logs addressing motion sickness, comfort, and usability (Freeman et al., 2021).

---

## 4. Results

### 4.1 VR Streaming performance

*Setup details:*
- **Streaming mode:**  
  - Testers 1–2: Wired (TCP) connection with Oculus Meta Quest 3  
  - Testers 3–4: Wireless (UDP) connection with VIVE Focus 3  
  - Tester 1: Localhost degradation simulation; Tester 2: ALVR streaming port latency  
- **ALVR Settings:**  
  - Resolution: 4288  
  - Preferred framerate: 90 Hz  
  - Encoder preset: Speed  
  - Bitrate: 30 Mbps (constant)  
  - Adaptive framerate: Enabled  
  - Preferred codec: H.264  

For more details, see the [Usage Guide](/Deliverables-P56/Usage-guide.md).

### 4.2 Measured latency effects

> **Note:** In the graphs below, the horizontal axis indicates **Latency (ms)**, and the vertical axis indicates the average user ratings (scale 1–10).  

#### Motion sickness vs. Latency (ms)

| **Latency (ms)** | **Avg. Score** | **Tester 1** | **Tester 2** | **Tester 3** | **Tester 4** |
|------------------|----------------|--------------|--------------|--------------|--------------|
| 0                | 10             | 10           | 10           | 10           | 10           |
| 50               | 10             | 10           | 10           | 10           | 10           |
| 100              | 9.25           | 10           | 10           | 7            | 10           |
| 150              | 9.0            | 10           | 10           | 7            | 10           |
| 200              | 8.25           | 10           | 10           | 7            | 10           |
| 300              | 8.25           | 10           | 10           | 7            | 10           |
| 400              | 8.25           | 10           | 10           | 3            | 10           |

#### Task performance (Hitting Target with Bow) vs. Latency (ms)

| **Latency (ms)** | **Avg. Score** | **Tester 1** | **Tester 2** | **Tester 3** | **Tester 4** |
|------------------|----------------|--------------|--------------|--------------|--------------|
| 0                | 10             | 10           | 10           | 10           | 10           |
| 50               | 9.75           | 10           | 10           | 9            | 9            |
| 100              | 7.5            | 8            | 8            | 6            | 8            |
| 150              | 5.5            | 6            | 5            | 4            | 7            |
| 200              | 4.5            | 4            | 4            | 4            | 6            |
| 300              | 3.25           | 2            | 3            | 4            | 4            |
| 400              | 2.0            | 2            | 2            | 2            | 2            |

#### Overall usability vs. Latency (ms)

| **Latency (ms)** | **Avg. Score** | **Tester 1** | **Tester 2** | **Tester 3** | **Tester 4** |
|------------------|----------------|--------------|--------------|--------------|--------------|
| 0                | 10             | 10           | 10           | 10           | 10           |
| 50               | 9.25           | 10           | 10           | 7            | 10           |
| 100              | 8.75           | 9            | 9            | 7            | 10           |
| 150              | 7.75           | 8            | 7            | 4            | 8            |
| 200              | 6.0            | 6            | 6            | 4            | 6            |
| 300              | 3.5            | 4            | 4            | 2            | 4            |
| 400              | 2.0            | 2            | 2            | 2            | 2            |

A combined graph of the user experience data is shown below.  
*(Horizontal axis: **Latency (ms)**; Vertical axis: **User Experience Score**.)*  

![User Experience vs. Latency (ms)](/Deliverables-P56/Degradation/output/Experience%20data/VR/user-experience.png)

---

#### Bitrate testing
For testers 3 and 4, the following boundaries were observed:
- **Artifacts:** Begin to appear at ~3800 KB/s.  
- **Usability limit:** Around 2600 KB/s.  
- **Crash limit:** Occurs at ~1300 KB/s.

*Note: Bitrate values may vary based on protocol, settings, or hardware used (Chen et al., 2020).*

#### ALVR Logging outcome
Analysis of the [ALVR streaming data](/Deliverables-P56/Degradation/output/ALVR%20data/html/) indicates a correlation between increased latency and reduced bitrate. For instance, higher latency leads to later frame transmissions, which may reduce the required bitrate due to ALVR's adaptive streaming behavior. Although the frame rate remains stable due to the adaptive framerate option, these findings help explain network performance under different latency conditions (Chen et al., 2020).

---

## 5. Part 2: Haptic feedback delay testing

### 5.1 Setup
*Note: Users 1–4 were tested without active haptic feedback during these trials.*  
- **VR Streaming:**  
  - Wired (TCP) connection using ALVR.  
  - Latency introduced via the ALVR streaming port.  
- **ALVR Settings:**  
  - Resolution: 4288  
  - Preferred framerate: 90 Hz  
  - Encoder preset: Speed  
  - Bitrate: adaptive (approximately 300–600 Mbps)  
  - Adaptive framerate: Enabled  
  - Preferred codec: H.264  
- **Additional setup:**  
  - Unity environment (Unity Technologies, n.d.).  
  - Clumsy for network degradation (Clumsy, n.d.).  
  - Ultrasonic array for haptic feedback (Ultraleap, n.d.).  
  - Laptop with Intel i7 12700h, RTX A1000, 32 GB 4800 MHz RAM.

### 5.2 Results
Below is the graph from the haptic feedback tests.  
*(Horizontal axis: **Latency (ms)**; Vertical axis: **User Experience Score**.)*  

![Haptic Experience vs. Latency (ms)](/Deliverables-P56/Degradation/output/Experience%20data/Haptic/user-experience.png)

---

## 6. Part 3: Combined VR and Haptic Feedback Testing

### 6.1 Setup
*Note: Users 1–4 were tested without active haptic feedback during these trials.*  
- **VR Streaming:**  
  - Wired (TCP) connection using ALVR.  
  - Latency introduced via the ALVR streaming port.  
- **ALVR Settings:**  
  - Resolution: 4288  
  - Preferred framerate: 90 Hz  
  - Encoder preset: Speed  
  - Bitrate: adaptive (approximately 300–600 Mbps)  
  - Adaptive framerate: Enabled  
  - Preferred codec: H.264  
- **Other setup elements:**  
  - Unity environment (Unity Technologies, n.d.).  
  - Clumsy for network degradation (Clumsy, n.d.).  
  - Ultrasonic array for haptic feedback (Ultraleap, n.d.).  
  - Laptop with Intel i7 12700h, RTX A1000, 32 GB 4800 MHz RAM.

### 6.2 Results
The combined test graphs indicate that VR latency directly affects the performance of the haptic device. In the graphs below, **red dots** represent the combined haptic and VR latency, while **blue dots** show the baseline haptic delay.  
*(Horizontal axis: **Latency (ms)**; Vertical axis: **User Experience Score**.)*

- **User 5:**  
  ![](/Deliverables-P56/Degradation/output/Experience%20data/Combined/user5.png)

- **User 6:**  
  ![](/Deliverables-P56/Degradation/output/Experience%20data/Combined/user6.png)

- **User 7:**  
  ![](/Deliverables-P56/Degradation/output/Experience%20data/Combined/user7.png)

---

## 7. Analysis Summary

### Latency impact
- **Motion sickness:**  
  - Stable for most users up to 300 ms, although Tester 3 reported discomfort starting at 100 ms (Freeman et al., 2021).  
- **Task performance:**  
  - Noticeable degradation begins at 100 ms, with near failure beyond 200 ms.  
- **Usability:**  
  - Usability declines significantly beyond 150 ms, rendering the system largely unusable at 300 ms.

### Bitrate findings
- **Artifacts:** Appear at ~3800 KB/s.  
- **Usability limit:** ~2600 KB/s.  
- **Crash limit:** ~1300 KB/s.

### Combined System Impact
- VR latency adversely affects haptic feedback responsiveness and accuracy.  
- The small sample size suggests further testing is needed to precisely quantify the impact on haptic performance.  
- The ultrasonic device is unsuitable for use with wireless headsets or microphones due to interference from generated noise (Ultraleap, n.d.).

---

## 8. Conclusion
1. **VR Streaming:**  
   - Optimal performance is achieved below ~125 ms latency.  
   - Usability degrades significantly beyond ~150 ms latency.  
   - Maintaining a bitrate above ~4000 KB/s is crucial to prevent visual artifacts (may vary with scenario).  

2. **Motion sickness:**  
   - Latency is tolerable up to ~300 ms, with individual sensitivity varying.  

3. **Haptic Feedback:**  
   - Both accuracy and responsiveness are acceptable up to ~300 ms latency.  
   - For effective communication within VR, the ultrasonic array is not recommended due to interference issues.

---

## 9. Future work
1. **Refine haptic testing:**  
   - Improve measurement tools to isolate haptic response times more accurately.  
2. **Expand user testing:**  
   - Increase participant diversity to validate thresholds across a broader user base.  
3. **System optimization:**  
   - Explore predictive algorithms and network optimization techniques to mitigate latency effects (Chen et al., 2020).

---

## 10. References
- ALVR. (n.d.). *Open Source VR Streaming*. Retrieved from [https://github.com/alvr-org/ALVR](https://github.com/alvr-org/ALVR) (Accessed: June 2024).  
- Ultraleap. (n.d.). *Haptics Development Kit*. Retrieved from [https://leap2.ultraleap.com](https://leap2.ultraleap.com) (Accessed: June 2024).  
- Unity Technologies. (n.d.). *Unity VR Overview*. Retrieved from [https://docs.unity3d.com](https://docs.unity3d.com) (Accessed: June 2024).  
- Clumsy. (n.d.). *Network Latency Simulator*. Retrieved from [https://jagt.github.io/clumsy/](https://jagt.github.io/clumsy/) (Accessed: June 2024).  
- Chen, L., Park, S., & Kim, J. (2020). *Predictive rendering in cloud VR environments.* IEEE Transactions on Visualization and Computer Graphics, 26(5), 2350–2360.  
- Freeman, I., Kelly, S., & Patel, R. (2021). *Evaluating user acceptance of haptic feedback in VR training.* International Journal of Human–Computer Interaction, 37(4), 303–315.  
