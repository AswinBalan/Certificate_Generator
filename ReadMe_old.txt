# Certificate_Generator
Steps to run this Project: Pull this project into a location in your Computer

# Method 1

step 1: Install Python 3.x 64 bit in Windows

step 2: Install virtualenv module using "pip install virtualenv"

step 3: Create a virutal environment by running "virtualenv {env_name}" on to preferred location

step 4: run "{env_name}\Scripts\activate to activate the virtual environment 

step 5: Go to the root directory of the project

step 6: run - "pip install -r requirements.txt" to install the required packages

step 7: run "python App.py"

# Method 2
Run as Desktop Application (Skip steps after step 1)

step 2: Change directory to the root of the Project and run - "pip install -r requirements.txt" to install the required packages

step 3: The executable file(.exe) of the project is present in Certificate_Generator/dist/App.exe - Double click to run this project
or Create a Desktop Shortcut and run as a Desktop Application

# Method 3
Run .exe using cmd (Skip steps after step 6)

step 7: Go to "cd dist" in cmd

step 8: Type "App" or "App.exe" and hit enter

# GUI Guide:

In First Option choose the (.csv) file containing certificate details.

In Second Option choose the Certificate-template(.pdf) file.

In the successive Entries, fill the starting x and y co-ordinates of the fields as space seperated values.

Then click Generate certificates to generate the Certificates for all the Participants.
