# Overview
This folder contains the DSM File Processing Azure Functions.  The functions are responsible for processing incoming zip files into extracted files, the extracted files are then processed using logic defined by DSM scientists and the results are then stored in SQL Databases.

It's important to note that there is a workspace file in the folder.  It should be used to open VS Code as it will produce a better overall development and debugging experience.

# How to Use the Folder
Open the azure-functions.code-workspace file with VS Code.  VS Code does a nice job of building virtual python environments (if needed - .venv folder), as well as optimizing each function app for VS Code (.vscode folder)

# How to debug
The function apps were created using the latest templates within VS Code.  The Workspace approach makes it easy then to debug a single function.  Previously, once had to launch the debugger for all functions and that was a bit anoying.

Don't attempt to debug unless you've opened the workspace.

# Things to be aware of
Each function app contains it's own set of .venv, .vscode, requirements.txt, and local.settings.json.  This makes it easier to debug each of them seperately.