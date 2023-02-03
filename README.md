# Adbro

Marketplace Integrator

## Prerequisites

- Python3 (>= v3.6 is recommended)
  Follow this tutorial : [Installing Python3](http://docs.python-guide.org/en/latest/starting/installation/#python-3-installation-guides) or [Setup Python3 on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04#step-2-%E2%80%94-setting-up-a-virtual-environment)
- PostgreSQL (>= v9.3 is recommended)
  Useful links: [PostgreSQL Guide: Install](http://postgresguide.com/setup/install.html), [DigitalOceanL Install Postgress on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)
- Install virtual environtment ubuntu
  Useful links: [How To Install Python 3 and Set Up a Programming Environment on an Ubuntu 16.04 Server](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-16-04-server)
- Editor using PyCharm
  Download: [Download PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac)
- Redis
  Useful links: [How To Install and Configure Redis on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04)
- Redis GUI using RDM (Redis Desktop Manager)
  Download: [Download RDM](https://redisdesktop.com/)
- Docker
  Download: [How To Install Docker](https://www.docker.com/products/docker-desktop)
  
These are 2 ways to run the program:
1. Pyhton virtual environment
2. Docker

## Python virtual environment
### Installing & Running
After prerequisites has been setup. You have to make the program run.

#### By using python virtual
- Install `python` ( >= v3.6 is recommended), `pip`, `virtualenv`
- Clone project
- Create `virtualenv` to `.venv` directory by using `virtualenv .venv`
- Activate python virtualenv with this command `source .venv/bin/activate`
- Create `.env` file by rename or copy `env.dists` to `.env`
- Make sure all variables value in your `.env` is yours
- Install dependency library for this project with run this command `pip3 install -r requirements.txt`

#### By using docker
- open your docker desktop
- open a new terminal and run this command to run the project `docker-compose up`
- run this command `docker exec -it adbro_1 bash`

## Migrate Database and Import Initial Data

Running all this script below in sequence inside your virtualenv or inside your docker container.

- `python manage.py migrate`
