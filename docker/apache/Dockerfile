FROM ubuntu
ENV LANG en_US.utf8
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y && apt-get autoremove -y && apt-get autoclean -y
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils vim curl apache2 apache2-utils
RUN apt-get -y install python3 libapache2-mod-wsgi-py3
RUN ln /usr/bin/python3 /usr/bin/python
RUN apt-get -y install python3-pip
RUN apt-get -y install libpq-dev python-dev
# RUN ln /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip

RUN pip install django==3.2.6 psycopg2==2.9.1

COPY docker/apache/apache2.conf /etc/apache2/apache2.conf

COPY docker/apache/my-vhosts.conf /etc/apache2/sites-enabled/000-default.conf
COPY . /var/www/html/osg-support
EXPOSE 8000
CMD ["apache2ctl", "-D", "FOREGROUND"]
# FROM httpd:2.4
# # COPY ./my-httpd.conf /usr/local/apache2/conf/httpd.conf
# COPY docker/apache/my-vhosts.conf /usr/local/apache2/conf/extra/httpd-vhosts.conf
# COPY . /usr/local/apache2/htdocs/osg-support
