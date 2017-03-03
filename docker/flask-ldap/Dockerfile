FROM ubuntu:14.04

# Install Packages
RUN apt-get update && \
    apt-get install -y curl python-dev python-pip libldap2-dev libsasl2-dev libssl-dev ldap-utils && \
    apt-get -y clean

# Install app dependencies
RUN pip install Flask Flask-SimpleLDAP python-ldap

# Bundle app source
COPY app.py /src/app.py

EXPOSE 5000
CMD ["python", "/src/app.py"]
