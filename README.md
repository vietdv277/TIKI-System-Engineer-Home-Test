# TIKI System Engineer Home Test

Home test for System Engineer position at TIKI

## Question 01

Build script to install base servers for production environment, use any automation tools suits you (ansible, saltstack, terraform, ...). The solution should setup following components, make any changes as you see fit, so we can assess your consideration for production-grade system.

- Sysadmin engineer accounts, hostname (dns), cli commands that you use often.
- Install docker daemon, specify logging driver + storage driver of your choice.
- Server should be prepared/tuned for high network traffic workload.

## [Answer for question 01](/question-01/README.md)

## Question 02

Write/dockerize and deploy a simple web application that echo back client ip and all request headers in json format. The application should listen on port TCP/80 and has a proper logging for later audit, debug purposes.

## [Answer for question 02](/question-02/README.md)

## Question 03

Describe your idea to monitor the response time of a web application. Draw a model that is scalable and responsive to the most traffic you have ever deployed.

When you receive an alert that a service is down or slow, what would you do to check that service and resolve the issue. Describe your steps to resolve and prevent the problem (you can describe a real situation which you have encountered).

## [Answer for question 03](/question-03/README.md)

## Question 04

Your dream team has 3 or 4 members. What would you do if you had destroyed a service by accident?
How about if it was your colleague that done it?

## [Answer for question 04](/question-04/README.md)
