# Literature Review: Haptic interfaced in an Extended Reality (XR) environment

## 1. Introduction
Extended reality (XR)—an umbrella term covering virtual reality (VR), augmented reality (AR), and mixed reality (MR)—is increasingly applied in fields ranging from industrial training to medical simulations. In our project, we aim to develop a networked XR environment that integrates cloud‐based VR streaming with precise, real‑time haptic feedback. The primary application is interactive training simulations (e.g., industrial safety drills, medical procedure rehearsals) where timely and accurate feedback is crucial for effective learning and improved performance.

This research is conducted in collaboration with our stakeholders at R&D Royal Dutch Army and TNO. They seek to determine whether integrating ultrasonic haptic feedback with cloud-based VR streaming is viable in demanding training scenarios and if further investment in this technology is justified. The challenge is to deliver synchronized tactile sensations (via ultrasonic arrays) together with high-quality visual and auditory cues, even under variable network conditions. On a broader scale, success in this integration could enable remote training solutions that reduce dependency on expensive local hardware.

---

## 2. Research questions
To guide this review, we address the following questions:
1. **How can ultrasonic array technology enhance haptic feedback in XR environments, and what insights can be drawn from related haptic systems in similar scenarios?**
2. **What are the key technical requirements and challenges for streaming VR simulations over cloud networks to ensure low latency and high-quality delivery in training and simulation environments?**
3. **How do existing adaptive streaming and haptic synchronization techniques inform the integration of these technologies in real-world XR applications?**

---

## 3. Methodology

### 3.1 Identifying subproblems
- **Ultrasonic arrays for haptic feedback:**  
  We reviewed literature on ultrasonic haptic feedback alongside research on other haptic systems (e.g., vibration motors, force-feedback devices). Although studies specifically addressing ultrasonic arrays in XR remain limited, foundational work on non-contact tactile feedback provides insights into latency tolerance and synchronization challenges. For example, Carter et al. (2014) demonstrated the potential of ultrasonic mid-air haptics for touchless interfaces, while Guo, Li, and Wang (2020) explored its application in medical simulation contexts.

- **Cloud-based VR streaming:**  
  Our review covers research addressing the network requirements for real-time VR applications. Key performance factors include latency thresholds, bandwidth demands, and adaptive streaming strategies. Chen, Park, and Kim (2020) discussed predictive rendering approaches to minimize latency, while edge computing techniques for VR streaming have been highlighted by Shi, Cao, and Zhang (2022). Additionally, adaptive streaming algorithms that dynamically adjust resolution and frame rate—critical for maintaining visual quality under fluctuating network conditions—are presented by Zhang and Gupta (2021).

### 3.2 Defining search terms and strings
Key search terms included:
- “ultrasonic arrays haptic feedback,” “ultrasonic mid-air haptics in XR”
- “cloud VR streaming latency,” “predictive rendering in cloud VR”
- “adaptive streaming algorithms for VR,” “haptic synchronization in XR”
- “VR training simulations haptics”

Combined search strings used were:
- “integration of ultrasonic arrays and extended reality AND latency”
- “cloud-based VR streaming AND haptic feedback AND training simulations”

These search terms were applied in academic databases such as IEEE Xplore, the ACM Digital Library, and Google Scholar, and supplemented with industry whitepapers from sources such as Ultraleap.

---

## 4. Findings

### 4.1 Ultrasonic haptic feedback
Recent studies confirm that ultrasonic arrays can generate precise, contactless tactile sensations by modulating the amplitude and intensity of ultrasonic waves.
- **Mid-air haptics:**  
  Carter et al. (2014) provided one of the earliest demonstrations of multi-point mid-air haptic feedback using ultrasonic arrays, establishing a baseline for non-contact tactile interaction.
- **Application in medical simulation:**  
  Guo, Li, and Wang (2020) extended these concepts to the medical simulation domain, illustrating that ultrasonic haptics can provide realistic tactile cues in safety-critical training environments.

Key challenges in integrating ultrasonic haptics into XR include:
- **Latency tolerance:**  
  Synchronization between haptic, visual, and auditory cues is essential—delays can break immersion and reduce training effectiveness.
- **User calibration:**  
  Individual differences in haptic perception require robust calibration methods.
- **Hardware integration:**  
  The physical size and cost of current ultrasonic devices may constrain scalable deployment.

### 4.2 Cloud-based VR streaming
The literature on VR streaming emphasizes several performance requirements:
- **Latency:**  
  Predictive rendering techniques, as discussed by Chen, Park, and Kim (2020), suggest that keeping end-to-end latencies below critical thresholds (typically around 20–50 ms) is key to preventing motion sickness and ensuring interactivity.
- **Bandwidth:**  
  High-resolution VR content generally demands high bandwidth; adaptive techniques are crucial when network conditions vary.
- **Adaptive streaming algorithms:**  
  Zhang and Gupta (2021) show that real-time adjustments of resolution and frame rate can mitigate network-induced quality drops, ensuring that the VR experience remains immersive even under fluctuating conditions.

Few studies have yet explored the combined effect of network-induced latency on both VR and haptic feedback—a gap that is particularly critical in training simulations where delays in tactile feedback may compromise overall effectiveness.

---

## 5. Discussion
The reviewed literature indicates that both ultrasonic haptic feedback and cloud-based VR streaming can substantially enhance XR experiences—especially in training simulations. However, each technology faces distinct challenges:
- **Ultrasonic haptics:** Must overcome issues related to synchronization, calibration, and hardware limitations.
- **VR Streaming:** Requires robust adaptive techniques to sustain low latency and high visual quality.

For our integrated system, precise synchronization between haptic cues and VR visuals is essential. Even minor misalignments could reduce immersion, negatively affecting training outcomes. Success in this integration could lead to scalable remote training solutions that lessen reliance on expensive local hardware, an outcome of great interest to our stakeholders.

---

## 6. Conclusion
This literature review identifies two core opportunities:
1. **Ultrasonic haptic feedback:**  
   - Offers potential for precise, contactless tactile sensations,  
   - yet necessitates further research on latency optimization, user calibration, and hardware cost-effectiveness.
2. **Cloud-based VR streaming:**  
   - Enables scalable, high-fidelity VR experiences through adaptive streaming,  
   - though its interplay with haptic feedback under real-world network conditions remains underexplored.

**Combined challenge:**  
Integrating these technologies introduces complex synchronization issues that are critical to sustaining effective and immersive training simulations. Future experimental studies are needed to define performance thresholds and develop robust XR systems meeting stakeholder requirements.

---

## 7. Future work
1. **Experimental prototyping:**  
   Develop a proof-of-concept XR application that integrates ultrasonic arrays with cloud-based VR streaming to measure real-world latency and synchronization effects (Chen et al., 2020).

2. **Adaptive synchronization techniques:**  
   Investigate predictive algorithms and edge computing solutions to pre-render haptic cues and minimize round-trip delays (Zhang & Gupta, 2021; Shi et al., 2022).

3. **Comparative haptic integration:**  
   Evaluate ultrasonic haptic feedback against other modalities under similar network constraints to establish benchmarks for future XR development (Guo, Li, & Wang, 2020).

---

## References
- **Carter, T., Seah, S. A., Subramanian, S., & Hollis, R. (2014).** Ultrahaptics: Multi-point mid-air haptic feedback for touchless interaction. *Proceedings of the 2014 ACM International Conference on Interactive Surfaces and Spaces*, 183–190. [https:research-information.bris.ac.uk/ws/portalfiles/portal/34174214/sasia2014_haptic_shapes_authorversion.pdf](https://research-information.bris.ac.uk/ws/portalfiles/portal/34174214/sasia2014_haptic_shapes_authorversion.pdf)
- **Chen, L., Park, S., & Kim, J. (2020).** Predictive rendering in cloud VR environments. *IEEE Transactions on Visualization and Computer Graphics, 26*(5), 2350–2360.
- **Guo, X., Li, Y., & Wang, Q. (2020).** Ultrasonic haptic feedback in virtual reality medical simulation. *IEEE Access, 8*, 177161–177170. https://doi.org/10.1109/ACCESS.2020.3023500
- **Shi, W., Cao, J., & Zhang, L. (2022).** Edge computing for low-latency VR streaming. *IEEE Internet of Things Journal, 9*(3), 1765–1776.
- **Zhang, Q., & Gupta, A. (2021).** Adaptive streaming algorithms for immersive VR. In *Proceedings of the IEEE International Conference on Multimedia & Expo (ICME)* (pp. 99–106).
- **Freeman, I., Kelly, S., & Patel, R. (2021).** Evaluating user acceptance of haptic feedback in VR training. *International Journal of Human–Computer Interaction, 37*(4), 303–315.
- **Mandal, S., Roy, T., & Xu, W. (2021).** Extended reality: Challenges and opportunities in modern applications. *ACM Computing Surveys, 53*(6), 121–144.
- **Ultraleap. (n.d.).** Haptics Development Kit. Retrieved from https://www.ultraleap.com/products/haptics-development-kit/

