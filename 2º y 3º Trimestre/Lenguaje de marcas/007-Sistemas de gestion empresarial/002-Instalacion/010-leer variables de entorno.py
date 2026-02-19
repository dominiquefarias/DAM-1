# En el shell (terminal):
# echo 'export NOMBRE="Dominique"' >> ~/.bashrc
# source ~/.bashrc

import os

print(os.environ.get("NOMBRE"))