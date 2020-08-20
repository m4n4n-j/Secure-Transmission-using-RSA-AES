## Introduction
Data is increasingly central to our personal lives, economic prosperity, and security. That data must be kept secure. We rely on encryption to keep cybercriminals away from our data. In this project, we understand and apply RSA and AES algorithms to mimic secure transmisson of data using a python program.


## Instructions:

1. Clone the repository. 

2. Install Pycryptodome package for python using:

	`pip install pycryptodome`

3. Change the input.mp4 file present in the Input folder, to your desired file mp4 and rename it as input.mp4.

    (For the demo, we have kept a song file in the Input folder)

4. Open the terminal and input the following command.
	
    `python3 secure.py`

5. You will find the decrypted output file in the Output folder. 


## Understanding the solution in detail:

 - The example currently showcases audio transmission (Although this method can work for text, audio and video files).
 - the program first converts the audio into hexadecimal format.
 - Then the program will set up dencryption and will use the RSA algorithm to interchange private AES key for further communication.
 - Once, the AES key gets delivered, secure communication can take place. Now the hexadecimal encrypted file gets transferred from one end to another.
 - Decryption and reconversion of the file then takes place at the other end.
 - Now, the audio message is ready to be heard on the other side.

## Read [Report.pdf](./Report.pdf) To know about the project. 
