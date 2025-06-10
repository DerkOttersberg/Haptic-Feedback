# Research report: VR and haptic feedback integration in a networked XR environment

This report provides a comprehensive overview of our project, detailing the motivation, methodology, experiments, and findings related to the integration of VR streaming and haptic feedback in a networked extended reality (XR) setting. The document is intended to guide stakeholders, such as R&D Royal Dutch Army and TNO, as well as XR developers and academic peers, through our process, considerations, and outcomes.

---

## Cover page

**Title**: VR and haptic feedback integration in a networked XR environment  
**Authors**: Chevan Ramcharan, Pirmin Kalbermatter, Derk Ottersberg & Pepijn Brinkman  
**Student numbers**: 1072166, 1069542, 1076265, 1078024  
**Supervisors**: Mrs. Colleen Chen, Mr. Milan Wijnmalen  
**Submission date**: 2nd of February, 2025   

---

## Summary

This research investigates the integration of **VR streaming** and **haptic feedback** into a networked XR environment. We examine how **network degradation**—in the form of increased latency—affects both the performance of VR streaming and the accuracy of haptic feedback. The main research questions are:

1. **How does network latency affect VR streaming performance?**
2. **How does network latency influence haptic feedback accuracy?**
3. **Can VR streaming and haptic feedback function effectively as an integrated system?**

The methodology involves experimental testing combined with literature research. Key tools include **ALVR** for VR streaming, **Ultraleap** for haptic feedback, and **Clumsy** for simulating network degradation. Performance metrics (e.g., latency, frame rates, input delays) are logged and analyzed alongside user feedback.

For a more detailed account of the experimental procedures, please refer to our [experimental research](./Experimental-Research.md).

---

## Introduction

### Background

Extended reality (XR) merges virtual reality (VR), augmented reality (AR), and mixed reality (MR) to deliver immersive experiences. In this project, we explore the integration of VR streaming with haptic feedback to create an interactive, networked environment. Such environments have significant applications in training simulations (e.g., military, medical, industrial safety), where realism and responsiveness are paramount.

### Context and motivation

Our stakeholders—R&D Royal Dutch Army and TNO—are evaluating the usability of this integrated system. Their interest lies in determining whether the technology can provide reliable, high-fidelity training simulations without requiring expensive on-site hardware. With the increasing demand for remote training solutions, understanding the technical challenges (especially network latency and synchronization) is critical.

### Problem statement

The main challenges addressed in this research are:
1. **Network latency**: Increased latency disrupts VR rendering and delays user inputs.
2. **Haptic feedback sensitivity**: Haptic accuracy deteriorates under network-induced delays.
3. **Synchronization**: Achieving real-time alignment between VR visuals and haptic responses is challenging under degraded network conditions.

These issues, if unresolved, can lead to reduced immersion, compromised training effectiveness, and potential safety concerns during critical simulations.

### Research objective

The objective of this study is to evaluate the impact of network degradation on both VR streaming and haptic feedback and to determine the feasibility of their integrated operation in a networked XR environment.

**Main research question**:  
*How does network degradation impact the integration of VR streaming and haptic feedback in a networked XR environment?*

**Sub-questions**:
1. How does latency affect VR streaming performance?
2. What is the impact of latency on haptic feedback accuracy?
3. Can the integrated system function smoothly under realistic network conditions?

---

## Theoretical framework

### Existing challenges

1. **Latency in XR systems**  
   - Real-time streaming solutions (e.g., NVIDIA GeForce Now) demonstrate that even small increases in latency can disrupt user experience.
2. **Haptic feedback sensitivity**  
   - Devices such as those from Ultraleap provide tactile responses under controlled conditions, but their performance under network latency is less understood.
3. **Synchronization**  
   - Coordinating VR visuals with haptic feedback is critical; misalignments can significantly reduce immersion.

### Existing solutions

- **ALVR**: An open-source tool for wireless VR streaming, which offers adaptive mechanisms to cope with network variability.
- **Clumsy**: A network simulation tool used to introduce controlled latency, jitter, and packet loss.
- **Ultraleap**: Provides ultrasonic-based haptic feedback integrated with platforms like Unity.

### Knowledge gap

While there is substantial literature on VR streaming and on haptic feedback separately, few studies have examined the combined impact of network degradation on their integration. Our research addresses this gap by providing controlled experimental data and detailed analysis of synchronization challenges.

---

## Methodology

### Research design

We adopted a **mixed-method approach**:
- **Experimental testing**: To measure the performance of VR streaming and haptic feedback under various latency conditions.
- **Literature research**: To contextualize our findings within existing studies and industry practices.

### Tools and software

- **VR streaming**: ALVR
- **Haptic feedback**: Ultraleap Haptic Feedback Kit
- **Network simulation**: Clumsy
- **Development environment**: Unity with SteamVR

### Experimental setup

1. **Baseline testing**: Establish performance metrics (latency, FPS, input delay) at 0ms added latency.
2. **Simulated network degradation**: Incrementally add latency (50ms, 100ms, 200ms, etc.) using Clumsy.
3. **Performance logging**: Record frame rates, input delays, and haptic response times in JSON format.
4. **User feedback**: Collect subjective data through surveys on usability, task performance, and motion sickness.

---

## Results

### VR streaming performance

| **Latency (ms)** | **Frame Rate (FPS)** | **Input Delay (ms)** | **User Feedback**               |
| ---------------- | -------------------- | -------------------- | ------------------------------- |
| 50               | 72                   | 20                   | "Smooth and responsive."        |
| 100              | 60                   | 50                   | "Slight lag, still acceptable." |
| 200              | 40                   | 150                  | "Severe lag, unusable."         |

### Haptic feedback performance

| **Latency (ms)** | **Feedback Accuracy (%)** | **User Comments**                      |
| ---------------- | ------------------------- | -------------------------------------- |
| 50               | 95                        | "Accurate and immersive response."     |
| 100              | 80                        | "Slight delay, still functional."      |
| 200              | 50                        | "Noticeable lag, unreliable feedback." |

### Integrated system performance

Our findings indicate:
- **VR streaming**: Performance declines noticeably at latencies above **125ms**.
- **Haptic feedback**: Functions adequately up to **300ms** latency, with clear degradation beyond.
- **Combined system**: For smooth operation, latency should ideally be maintained below **125ms**.

Additional details and graphs can be found in our [experimental research report](./Experimental-Research.md).

---

## Architecture diagram

![Architecture Diagram](Architecture%20diagram.png)

*Note: The diagram illustrates the overall system architecture, including data flows between VR streaming, haptic feedback modules, and network simulation. Latency parameters can be adjusted to reflect different network conditions.*

**Sources for visual aids:**
- **Haptic**: [Ultraleap](https://leap2.ultraleap.com/wp-content/uploads/2024/05/compact-array.png)
- **Unity script**: [Cloudinary](https://res.cloudinary.com/upwork-cloud/image/upload/c_scale,w_1000/v1709143446/catalog/1597899066014560256/qtkclgncqpdd7ciftxfc.webp)
- **Clumsy**: (Screenshot)
- **ALVR**: [ALVR GitHub](https://github.com/alvr-org/alvr)
- **Unity**: [Logos World](https://logos-world.net/wp-content/uploads/2021/11/Unity-Emblem.png)
- **SteamVR**: [Kxcdn](https://roadtovrlive-5ea0.kxcdn.com/wp-content/uploads/2020/07/steamvr-logo.png)
- **VR headset**: [Notebookcheck](https://www.notebookcheck.net/fileadmin/Notebooks/News/_nc3/FxivtNGaEAYau59.jpeg)

---

## Conclusion and recommendations

### Conclusion

The integration of VR streaming and haptic feedback into a networked XR environment is feasible, but both components are highly sensitive to network latency. Our experiments show:
1. VR streaming performance degrades significantly beyond **125ms** latency.
2. Haptic feedback remains viable up to **300ms**, though its accuracy diminishes.
3. For seamless integration, network latency should ideally be maintained below **125ms**.
4. The ultrasonic haptic system is also affected by environmental factors (e.g., interference from headsets and microphones within a ~5m radius).

### Recommendations

1. **Optimize network conditions**: Efforts should be made to keep latency below **125ms** to ensure effective training simulations.
2. **Enhance synchronization**: Develop advanced algorithms to better align VR visuals with haptic feedback.
3. **Expand testing**: Conduct broader experiments under various real-world conditions to further validate and refine the system.
4. **Consider hardware constraints**: Address the limitations of current ultrasonic arrays, particularly regarding interference and bulkiness, to make the system more practical for deployment.

---

## References

1. ALVR. (n.d.). *Open source VR streaming*. Retrieved from [https://github.com/alvr-org/ALVR](https://github.com/alvr-org/ALVR)  
2. Ultraleap. (n.d.). *Haptics development kit*. Retrieved from [https://leap2.ultraleap.com](https://leap2.ultraleap.com)  
3. Clumsy. (n.d.). *Network latency simulator*. Retrieved from [https://jagt.github.io/clumsy/](https://jagt.github.io/clumsy/)  
4. Unity Technologies. (n.d.). *Unity VR overview*. Retrieved from [https://docs.unity3d.com](https://docs.unity3d.com)

---

## Glossary

- **Latency**: The delay between a user action and the system's response.
- **Haptic feedback**: Tactile sensations generated by ultrasonic arrays.
- **ALVR**: Open-source software for VR streaming.
- **XR**: Extended reality, encompassing VR, AR, and MR.

---

## Appendices

1. **Performance logs**: JSON files recording latency, FPS, and input delays.
2. **C# scripts**: Source code for integrating VR and haptic feedback.
3. **User surveys**: Questionnaires used to collect subjective feedback.
4. **Latency simulation settings**: Configuration files for Clumsy.

---

*This report synthesizes our process, experimental results, and critical reflections. It is designed to inform stakeholders and guide future research directions in developing robust, networked XR training environments.*
