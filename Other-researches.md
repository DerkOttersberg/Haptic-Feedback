# Other researches
## VR
### Streaming
#### Comparisons table

| Feature                  | **NVIDIA CloudXR**                 | **ALVR**                                         | **Moonlight & Parsec**                                                                     |
| ------------------------ | ---------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **Cost**                 | Paid*                              | Free & Open-source                               | Free                                                                                     |
| **Purpose**              | Professional VR/AR cloud streaming | PC VR wireless streaming to headsets             | General game streaming (non-VR focus)                                                    |
| **Supported Platforms**  | Cloud & PC                         | PC (Windows, Linux)                              | PC (Windows, Linux, macOS)                                                               |
| **Wireless Streaming**   | Yes (optimized for cloud-based VR) | Yes                                              | Yes (but focused on general gaming)                                                      |
| **VR Support**           | Fully optimized for VR & AR        | Designed specifically for VR streaming           | Not designed for VR                                                                      |
| **Additional Advantage** | Clearly supports for cloud         | Supports PhoneVR, which can be great for testing | Ease of setup, with regards to streaming, unsure about the controls, or a second client. |

To get access to NVIDIA CloudXR, you need to join as a developer and accept the [terms and conditions](https://developer.nvidia.com/legal/terms), meaning we cannot distribute the demo we would make.
Sources:
- Moonlight: https://moonlight-stream.org/ 
- NVIDIA CloudXR: https://developer.nvidia.com/cloudxr-sdk  
- ALVR: https://github.com/alvr-org/ALVR 
- Parsec: https://parsec.app/
### Network latency
After short research a tool called clumsy was found, testing the software a bit, it was found to live up to the standards of introducing artificial degradation.

## Remote server
### Virtualization Solutions

| **Solution**          | **Advantages**                | **Disadvantages**                                                                                                                                                                                 |
| --------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Docker**            | Easiest to actually implement | Not designed for running GUI applications (e.g., ALVR). Rendering games in Docker is reported to be very slow.                                                                                    |
| **Oracle VirtualBox** | No clear advantages yet       | Does not support GPU passthrough, making it impossible to run ALVR or play SteamVR games.                                                                                                         |
| **Hyper-V**           | No clear advantages yet       | Does not support vGPUs on laptops. "Laptops with NVIDIA GPUs are not supported at this time." <br> Source: [Easy GPU-PV GitHub](https://github.com/jamesstringerparsec/Easy-GPU-PV#prerequisites) |

They all did not work with the limited resources, thus a actual server with maybe Hyper-V is the best advise.

## Unity
### Multiplayer

| **Network Solution** | **Advantages**                                           | **Disadvantages**                                         | **Best Use**                                         |
| -------------------- | -------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------- |
| **Photon PUN 2**     | Easy setup with cloud hosting and free for small groups. | Limited scalability and less control over servers.        | Small/medium multiplayer projects (1-20 players).    |
| **Unity Netcode**    | Full Unity integration and control over servers.         | Steeper learning curve and more network code.             | Custom server management and deep Unity integration. |
| **Mirror**           | Open source and scalable for large projects.             | Requires server management and more networking knowledge. | Large multiplayer games.                             |
| **Photon Fusion**    | Highly scalable and suitable for high performance.       | More complex and no free development plan.                | Larger multiplayer projects.                         |

The first choice was using Photon PUN 2, because of its advantages for 'Easy' setup, which should reduce development time in the short time period for this project.  
Yet after actually trying to implement it, it wasn't as 'easy' as first thought, and it worked a lot better using Unity Netcode.