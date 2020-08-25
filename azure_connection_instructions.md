# Azure Remote Connection Instructions

1. Open MobaXTerm and enter a new SSH connection and enter the IP you received in the host, and `puser` as the username.
2. When asked to, enter `Hatam-ds-2020` as the password.
3. Fire the command `conda activate psagot-2020-ml`.
4. Fire the command `jupyter notebook --no-browser --port=8889` and copy the token that is auto-generated:

    ![image](https://user-images.githubusercontent.com/38311688/91127525-18535080-e6af-11ea-9210-47526f779e0c.png)

5. Open a new tab in MobaXTerm by clicking on the `+` icon in the upper tab area:

    ![image](https://user-images.githubusercontent.com/38311688/91127585-3d47c380-e6af-11ea-8c06-da982be9beec.png)
    
6. In the new tab fire the command `ssh -N -f -L localhost:8888:localhost:8889 username@your_remote_host_name` where `username` is `puser` and `your_remote_host_name` is the IP you received.
7. When asked to, enter `Hatam-ds-2020` as the password.
8. Open your browser in the local computer and go to `localhost:8888`.
9. In that window when prompted to enter the token, enter the token you copied before.
