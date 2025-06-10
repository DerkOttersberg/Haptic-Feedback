# Degradation output explantation
Refer to [Usage guide](/Deliverables-P56/Usage-guide.md) for and explanation on how to read the data.

The folder structure is as follows:
```graphsql
📂 ALVR data/
│── 📂 html/        # Contains HTML reports from ALVR tests  
│── 📂 json/        # JSON-formatted ALVR test data  
│  
📂 Experience data/
│── 📂 Combined/    # Merged user experience data (VR + Haptic)  
│   │── 📂 json/    # JSON files with combined data  
│   │── 📂 .png     # PNG images combining VR and Haptic experience  
│  
│── 📂 VR/          # Virtual Reality experience data  
│   │── 📂 json/    # JSON files for VR experience  
│   │── 📂 .png     # PNG visualizations of VR data  
│  
│── 📂 Haptic/      # Haptic feedback experience data  
│   │── 📂 json/    # JSON files for Haptic experience  
│   │── 📂 .png     # PNG visualizations of Haptic feedback  
│  
📂 other/  
│── cable-port-only.html  # Test file for wired TCP connection (can be ignored)  
```

