# 🛠️ intSpLoiT Voluntary Module Contribution Guide

Welcome to the intSpLoiT community!  
This guide is for volunteers who want to contribute modules or small features to the framework. You don't have to be a core developer, just someone who wants to help expand the tool.

---

## 1. Who is this guide for?

- Security researchers  
- Pentesters  
- Hobbyist programmers interested in offensive security  
- Anyone willing to contribute safe and useful modules  

**No paid contract or formal commitment is required.**  
Contributions are voluntary and appreciated.

---

## 2. Basic Requirements

- Basic Python 3 knowledge  
- Willingness to follow the framework’s option and coding standards  
- GitHub account to submit your module via Pull Request (PR) or Issue  
- Respect for clean, safe, and well-documented code  

---

## 3. How to structure your module?

Your module should follow the intSpLoiT framework conventions. Here is an example structure inspired by a real module:

```python
# Author: YourName or Nickname
# Title: Example Exploit Module
# Description: Brief description of what your module does.

import socket
import time

# Option schema for module settings
option_schema = {
    "rhost": {
        "description": "Target IP address",
        "required": True,
        "default": ""
    },
    "rport": {
        "description": "Target port",
        "required": True,
        "default": 80
    }
}

# This dictionary will be filled by the framework at runtime
module_context = {}

def exploit():
    rhost = module_context.get("rhost")
    rport = int(module_context.get("rport", 80))
    # Your exploit logic here
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect((rhost, rport))
        # send payload or commands...
        s.close()
        print(f"Exploit sent to {rhost}:{rport}")
        return True
    except Exception as e:
        print(f"Exploit failed: {e}")
        return False
```

---

## 4. Testing your module

Load your module inside the framework:
intSpLoiT > use exploits/example_exploit

Set required options:
intSpLoiT > set rhost 192.168.1.10
intSpLoiT > set rport 80

Run the module:
intSpLoiT > run


Make sure your module works correctly without errors.


---

## 5. How to submit your module?

You have two options to contribute your module:

### 1. Pull Request (PR):

Fork the intSpLoiT repository on GitHub.

Add your module file in the appropriate folder (modules/exploits/, modules/scanners/, etc.)

Test your module thoroughly.

Create a Pull Request with a clear description and your contact info (GitHub nickname or email).

Wait for review and feedback.



### 2. GitHub Issue:

If you prefer, you can open an Issue instead of a PR.

Provide your module code as an attachment or paste it in the Issue description.

Include explanation, usage instructions, and contact information.

The core team will review and may add the module or request changes.





---

## 6. Important Notes

Modules may contain exploit or offensive code targeting remote systems.

Users acknowledge and accept full legal and ethical responsibility before using the framework and its modules.

The framework and its modules must only be used for lawful and authorized security testing.

This disclaimer and user responsibility are clearly stated in the framework’s README and License files.

Contributors must ensure their code does NOT contain any malicious or harmful code that can damage the local user’s system running the framework.

Avoid hardcoding sensitive data within modules.

Respect the framework’s coding style and option naming conventions.

Contributions are voluntary and unpaid, but highly appreciated.



---

## 7. Thank you!

Your contributions help the intSpLoiT community grow stronger and more versatile.
Every module, no matter how small, is valuable.

> Together, we build a better open-source offensive security tool.




---

If you want help or have questions, open an Issue on GitHub or reach out via the project’s communication channels.


---

Happy hacking!

---
