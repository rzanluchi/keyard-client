# Keyard Client#

Is a client connector for the [keyard project](https://github.com/rzanluchi/keyard)

# Example #

There is a example app for you to check. 
```
gunicorn example.server:app -b 0.0.0.0:8000
gunicorn example.client2:app -b 0.0.0.0:8002
gunicorn example.client:app -b 0.0.0.0:8001

curl 0.0.0.0:8001/client1
```
