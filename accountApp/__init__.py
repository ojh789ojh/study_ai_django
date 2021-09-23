"""python manage.py startapp accountApp
test"""
# python manage.py makemigrations       //생성
# python manage.py migrate              //반영
# pip install django-bootstrap4
# python manage.py createsuperuser
# python manage.py startapp profileapp
# pip install pillow
# python manage.py startapp articleapp
# ssh -i gis_test_1.pem ubuntu@3.16.67.10

# docker
# sudo apt-get update
# sudo apt-get install \
#     apt-transport-https \
#     ca-certificates \
#     curl \
#     gnupg \
#     lsb-release
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
#  echo \
#   "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
#   $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# sudo apt-get update
#  sudo apt-get install docker-ce docker-ce-cli containerd.io
#  sudo docker run hello-world

# sudo docker swarm init
# docker swarm join --token SWMTKN-1-0fcod1wk0sf9lxvh91cawit96pkq9xk3trxqftv3h5xm5lyr24-cck1k2vzrkknu8z0r0u8lgd10 172.31.0.146:2377