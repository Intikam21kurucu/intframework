# Contributing to intSpLoiT Framework

Thank you for your interest in contributing to the intSpLoiT Framework!  
Your efforts help us build a stronger, more versatile, and more powerful tool for the cybersecurity community.

💡 Interested in developing the framework core? See [CORE_DEVELOPERS.md](./CORE_DEVELOPERS.md)

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Getting Started](#getting-started)  
3. [Module Development Guidelines](#module-development-guidelines)  
4. [Code Style](#code-style)  
5. [Testing Your Module](#testing-your-module)  
6. [Submitting a Pull Request](#submitting-a-pull-request)  
7. [Support and Communication](#support-and-communication)

---

## Project Overview

intSpLoiT is a modular penetration testing and exploitation framework designed for efficiency and extensibility.  
Our goal is to provide a powerful set of modules including exploits, auxiliary tools, post-exploitation scripts, and OSINT capabilities.

---

## Getting Started

### Environment Setup

1. Fork the repository on GitHub.  
2. Clone your fork locally:

    ```bash
    git clone https://github.com/<your-username>/intframework.git
    cd intframework
    ```

3. Install Python 3.12 or above and required dependencies.

4. Optionally, create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

5. Familiarize yourself with the framework by running basic commands.

---

## Module Development Guidelines

### Structure and Location

Modules are organized by type inside the `modules/` directory:

- `exploits/`  
- `auxiliary/`  
- `post/`  
- `osint/`  

Create your module in the appropriate subfolder with a descriptive filename.

### Defining `option_schema`

Each module must define an `option_schema` dictionary to specify user-configurable options, e.g.:

    ```python
    option_schema = {
        "target": {
            "description": "Target IP address",
            "required": True,
        },
        "port": {
            "description": "Target port",
            "required": False,
            "default": 80
        }
    }
    ```

### Main Execution

- Implement the module logic within a `run()` function or equivalent.
- Use framework utilities like `inttable` or session managers when necessary.

### Documentation

- Add clear docstrings at the top of the module explaining its purpose and usage.
- Provide example usage in comments if possible.

---

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) guidelines for Python code.
- Use meaningful variable and function names.
- Include comments where the logic might be complex or non-obvious.

---

## Testing Your Module

- Test your module locally by running it within the framework shell or console.
- Handle exceptions gracefully and provide meaningful error messages.
- Ensure your module does not crash the framework.

---

## Submitting a Pull Request

1. Push your changes to a branch on your fork.

2. Open a Pull Request (PR) against the `main` branch of the main repository.

3. Provide a clear description of your changes and the module functionality.

4. Link any related issues if applicable.

5. Be responsive to code review feedback and make requested changes promptly.

---

## Support and Communication

If you have questions or need help:

- Open an issue on GitHub.  
- Join our Telegram/Discord channels: **(add your links here)**  
- Email the core development team at: **(add email)**

---

Thank you for helping make intSpLoiT stronger!

---

**intSpLoiT Core Development Team**