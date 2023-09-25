# togglebank-e13n-runner-public
Experiment events for the togglebank demoapp 

This script is for populating data in launchdarkly for the togglebank demo.

Run the script, and follow the prompts. The number_of_trades metric and customerGroup attribute still need some fixing.

Pre-requisites: Python - install python if you haven't, you'll probably need to install some packages too. 'pip install missingpackage' should work, will add more details here later or just ping me if you have trouble. Experiment created Have your server side sdk key handy

Steps to do this:

Create the experiment in LD, in your environment
Your first iteration should look similar to this this, but with Getting STarted variation instead of Trade Now:
<img width="1096" alt="image" src="https://github.com/launchchris/togglebank-e13n-runner-public/assets/81649468/f0240c95-53b0-4bae-bd88-2661cd3c18f5">

Run the python script
At the pause, stop the current running of the iteration. Set the value to be served to be Learn Now.
Edit the Experiment - Change the variation served to 50% Learn Now, and 50% Trade Now
Save the Changes
Start Running the experiment again to begin a new iteration
