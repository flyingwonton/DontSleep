# DontSleep

A basic python script to move your mouse and keep your PC awake ~~or keep appearing available~~ when you're away. 

## How to run

1. Clone the repository with: `git clone https://github.com/flyingwonton/DontSleep.git`

2. Install the requirements with: `pip install -r requirements.txt`

3. Run dontsleep.py specifying the  [arguments](#Arguments) below

### Arguments
Dontsleep takes only two positional arguments, both in minutes: 
1. **duration** (mandatory): how long the mouse should be moved
2. **delay** (optional): the minutes after which the mouse should be start moving

### Examples

Run Dontsleep and move the cursor for **5** minutes:

`python dontsleep.py 5`

Run Dontsleep and start moving in **2** minutes the cursor for **5** minutes:

`python dontsleep.py 5 2`
