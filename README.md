# RSA-Asymetric-Encription
 RSA Private & Public Key Encryption in Python

## use correct version of Python when creating VENV
<pre>python3 -m venv venv </pre>

## activate on Unix or MacOS
<pre> source venv/bin/activate </pre>

## activate on Windows (cmd.exe)
<pre>venv\Scripts\activate.bat </pre>

## activate on Windows (PowerShell)
<pre>venv\Scripts\Activate.ps1 </pre>

## Activated environment will appear
<pre>(venv) D:\Flask-Simple-app> </pre>

 ## Install RSA library
 <pre> pip install -r requirements.txt </pre>


 ## Run Example 
 <pre>
 python rsa_example.py
 </pre>

## Why Asymetric encription ?
>Increased data security is the primary benefit of asymmetric cryptography. It is the most secure encryption process because users are never required to reveal or share their private keys, thus decreasing the chances of a cybercriminal discovering a user's private key during transmission.


 ## Scenario for asymetric encription.
    Here 2 parties will be involved, the sender and receiver. There can be mutiple senders in real scenario, who would like to share the information with reciever. Inorder to make sure the data is safe and is been sent and received by the valid parties, the asymetric encription is used  to achieve the same.

 ### Following are the steps followed to achive the same
 - Receiver will generate a public and private key as the initial step.

 - Public key will be public for all users who would like to send message to reciver.

 - Private key will be private for the person who will receive the message and this key will not be shared to any users.

 - If Sender want to send an encripted the message to receiver, then using public key the message is encripted.
 
 - The reciever decript the recived message from sender  using private key which reciever has.
