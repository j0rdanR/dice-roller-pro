> Please read this document before attempting to run the program. You may encounter issues which are resolved below.

<br>

# Dice Roller Pro - Code explaination

11 Computer Science: Task 8 - Jordan Rodrigues



<br>

## Running the program

There are two ways to run the program:
1. Using the precompiled executable for your operating system
2. By running the source code in a Python interpreter

It is recommended that you run the executable, as it is simple and requires no setup.




<br>

#### Using the executables:

While viewing the repository on GitHub, locate the 'Releases' section on the right side and click on the latest release. Then download the binaries for your specific machine (or them all).

Running it on Mac, you will have to make the file executable with the terminal:

     >  chmod 755 macos
     >  ./macos

     ...

On Windows, you should be able to double click on the file to run it.

<br>

Here is the info regarding the machines I compiled these on:
| Operating System | Compiled on |
| ------------- | ----------- |
| macOS         | macOS-12.3.1-x86_64-i386-64bit |
| Windows       | Windows-10-100.22000-SP0 |

<br>

#### Running using a Command Line: {#run-with-cmdline}

Check your Python install on Linux/macOS using a terminal:

     >  python3 --version
     >  Python 3.10.5

<br>

On Windows, using Command Prompt:

     >  py -3 --version
     >  Python 3.10.5


<br>

Then to run the program, use the command:

     >  python3 main.py
    
        ============================================================
                        |    DICE ROLLER PRO!    |                 
        ============================================================

        Enter a roll ('h' for help, 'x' to exit): █

> Make sure you are in the directory containing the `main.py` file, or you can provide an absolute reference to it instead.



<br>

#### Running using a Python editor (not recommended):

> WARNING: Some Python code editors, such as ‘Mu Editor’ do not work well when importing modules. It is recommended that you use the executables or another method.

1. Import the project files into the workspace of your editor
2. Run the code
    1. With the integrated terminal: use the same command in the [Running using a Command Line](#run-with-cmdline) step
    2. Or press the 'Run program' button, and the code should execute.