# **Apache Tomcat JSP Upload Bypass & Remote Code Execution (RCE) Exploit**  
This repository contains **two exploit versions**—one in **Python** and one in **C++**—for testing Apache Tomcat servers vulnerable to **CVE-2017-12617**. The vulnerability allows **unauthenticated JSP file uploads**, leading to **remote code execution (RCE)**.

---

## **📌 Features**
✅ **Python & C++ versions available**  
✅ **Bypasses authentication to upload malicious JSP**  
✅ **Detects vulnerable servers**  
✅ **Command execution (Python version only, for now)**  
✅ **Evades detection using randomized User-Agents**  
✅ **C++ version for faster execution and lower detection rates**  

---

## **⚠️ Legal Disclaimer**
This tool is provided for **educational and security testing purposes only**. Unauthorized use against systems **without explicit permission** is illegal. The author **is not responsible** for any misuse.

---

# **🚀 Installation & Usage**
## **1️⃣ Python Version**
### **🔹 Prerequisites**
- Python 3.x  
- `requests` module  
  ```bash
  pip install requests
  ```

### **🔹 Running the Python Exploit**
```bash
python3 exploit.py -u <TARGET_URL>
```


## **2️⃣ C++ Version**
### **🔹 Prerequisites**
- **Linux/macOS**: Install `g++` and `libcurl`
  ```bash
  sudo apt install g++ libcurl4-openssl-dev -y
  ```
- **Windows**: Install MinGW and `libcurl`

### **🔹 Compiling the Exploit**
```bash
g++ exploit.cpp -o exploit -lcurl
```

### **🔹 Running the C++ Exploit**
```bash
./exploit <TARGET_URL>
```


# **📜 How the Exploit Works**
1. **Uploads a JSP webshell** to a vulnerable Tomcat server.  
2. **Confirms the upload** by accessing the JSP file.  
3. **Provides an execution shell** (Python version).  

---

# **🛡️ Mitigation**
To protect against **CVE-2017-12617**, **upgrade Tomcat** to the latest version and **disable HTTP PUT** requests:
```xml
<servlet>
  <servlet-name>readonly</servlet-name>
  <servlet-class>org.apache.catalina.servlets.DefaultServlet</servlet-class>
  <init-param>
    <param-name>readonly</param-name>
    <param-value>true</param-value>
  </init-param>
</servlet>
```

---

# **👨‍💻 Contributing**
Feel free to contribute by adding:
✅ **More stealth techniques**  
✅ **Multi-threading for mass scanning**  
✅ **Interactive reverse shell (C++ version)**  

---

# **📜 Credits**
[@intx0x80] - Original PoC  
Updated by **solo925** 🚀  

