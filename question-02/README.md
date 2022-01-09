## Python Flask Web App

This is a simple web application that echo back client ip and all request headers in json format.

### Build docker image

```sh
docker build -t python-flask:0.1 .
```

### Run and test image on local machine

```sh
docker run -d -p 80:80 python-flask:0.1

```

```sh
# curl http://localhost | json_pp

{
   "Accept" : "*/*",
   "Host" : "localhost",
   "User-Agent" : "curl/7.68.0",
   "client_ip" : "172.17.0.1"
}

```
