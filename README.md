## Cloudy Wordy

### Overview

This is an application for storing the 100 most used
words found at a url.

### Goals
This app will accumulate the frequency of words over time. When 
a given url is processed, a running total is kept reflecting
all the times that word has been counted in previous url requests.

### Storage of keys
For business reasons, the words are stored in a mysql database in an encrypted format.
We use asymmetrical encryption since this provides much better security, requiring a public and private key.

The keys have been generated using the [python rsa library](https://pypi.python.org/pypi/rsa). 

    pub, priv = rsa.newkeys(1024)
    
    with open('../keys/pub.pem', 'w') as f:
        f.write(pub.save_pkcs1())
        
    with open('../keys/priv.pem', 'w') as f:
        f.write(pub.save_pkcs1())
        
https://pypi.python.org/pypi/rsa'
Usually, asymmetrical encryption involves the use of a public and private key. The word or message is encrypted using the public key and sent another location where the message is decrypted
with the private key.

In the case of this application, the keys would be stored separately and imported into the environment at runtime. 

### Running locally

In order to make this work locally, you need to install [gae_installer](https://github.com/peterhudec/gae_installer).

- Create a virtual environment

`virtualenv env && . env/bin/activate`
    
- Install with php

`pip install gae_installer`

    
Once installed, run the following

`. ~/.virtualenvs/octopus/bin/dev_appserver --skip_sdk_update_check=yes .`


