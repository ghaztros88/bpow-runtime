# -*- coding: utf-8 -*-
"""Copy of Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/ghaztros88/6d960560eaa93495e1e57212a360d9f2/copy-of-untitled.ipynb
"""

!wget https://github.com/BananoCoin/boompow/releases/download/v3.0.1/bpow-client-v301.zip

!unzip -q "bpow-client-v301.zip"

!pip3 install --user -r requirements.txt

!sudo apt install ocl-icd-libopencl

!nohup ./bin/linux/nano-work-server --gpu 0:0 -l 127.0.0.1:7000 &

!python3 bpow_client.py --payout ban_35pearsw5kdbsaipnw9scjgep5956f9j7df681tr5i54aya1atfth5jacwqd --work any