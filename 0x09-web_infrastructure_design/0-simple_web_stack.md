# Simple Web Stack

## Description
This is a basic web infrastructure that enables access to a website via www.foobar.com, but lacks firewalls or SSL certificates for network protection. The server's CPU, RAM, and SSD are shared among all components, such as the database and application server.

## Specifics about the infrastructure
In this infrastructure,
+ a server refers to computer hardware or software that provides services to other computers, known as clients.
+ The domain name provides a human-friendly alias for an IP address and is mapped in the Domain Name System (DNS).
+ The DNS record used for www.foobar.com is an A record, which stores a hostname and its corresponding IPv4 address.
+ The web server accepts HTTP requests and returns the requested resource or error message.
+ The application server installs, operates, and hosts applications and services for end-users, IT services, and organizations, facilitating the delivery of high-end consumer or business applications.
+ The database maintains organized information that can easily be accessed, managed, and updated.
+ Communication between the server and client occurs through the internet network using the TCP/IP protocol suite.

## issues of the infrastructure
There are several Single Points of Failure (SPOF) in this infrastructure, such as: 
+ the entire site going down if the MySQL database server fails.
+ Maintenance checks require putting down a component or turning off the server, causing website downtime.
+ Scaling this infrastructure is challenging because all components are on a single server, causing resource depletion and slowdowns with increased traffic.
