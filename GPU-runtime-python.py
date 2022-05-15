!wget https://github.com/BananoCoin/boompow/releases/download/v3.0.1/bpow-client-v301.zip

!unzip -q "bpow-client-v301.zip"

!pip3 install --user -r requirements.txt

!sudo apt install ocl-icd-libopencl

!nohup ./bin/linux/nano-work-server --gpu 0:0 -l 127.0.0.1:7000 &

!python3 bpow_client.py --payout ban_35pearsw5kdbsaipnw9scjgep5956f9j7df681tr5i54aya1atfth5jacwqd --work any
