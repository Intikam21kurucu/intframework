<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Bugs and Troubleshooting Guide</h1>
    <p>If <code>intconsole</code> does not work when executed, follow these steps:</p>
    <ol>
        <li>Navigate to the <code>intframework</code> directory:</li>
        <pre>
export INTFRAMEWORK_PATH="WRITE PATH HERE"
source ~/.bashrc
python intconsole
        </pre>
        <li>If it still does not work, use this alternative command:</li>
        <pre>
cd $INTFRAMEWORK_PATH
python3 intconsoleV4.py
        </pre>
    </ol>
    <p>Keep in mind that it is not strictly necessary for <code>intconsole</code> to run directly. The above commands should work as alternatives.</p>
    <h2>Fixing Module Errors</h2>
    <p>If you encounter a <code>ModuleNotFoundError</code>, resolve it by installing the missing module using:</p>
    <pre>
pip3 install "module_name"
    </pre>
    <p>This will resolve most of the issues related to missing modules.</p>
</body>
</html>