                                                                                Fantasy Manhwa Collection Web Application

Overview Develop a cloud-deployed platform showcasing an assortment of fantasy manhwa titles, complete with genres and summaries. This application leverages AWS for robust hosting and infrastructure management, ensuring scalability, security, and the ability to handle traffic surges.

Key Features

Manhwa Catalog: Lists top fantasy manhwa titles with corresponding genres and descriptions, sourced from a sample JSON file.

Cloud Infrastructure: Utilizes an AWS EC2 instance for hosting, with an RDS database and S3 for asset storage.

Scalability: Equipped with auto-scaling capabilities to manage increased traffic by monitoring CPU usage.

Security: Implements HTTPS via AWS Certificate Manager, with configured firewall rules to secure port access.



                                                                                            Project Structure

app.py: Python Flask backend serving the web application.

manhwa.json: Sample data file containing manhwa titles, genres, and descriptions.

index1.html: Main HTML template for the front-end display of the manhwa collection.

static/: Directory housing static assets such as CSS files.



                                                                                       Cloud Deployment Components

Hosting: Deployed on an AWS EC2 instance running Flask.

Storage: Utilizes an S3 bucket for storing images and other static assets.

Database: Manages manhwa data using AWS RDS.

Auto-Scaling: Configured to scale EC2 instances based on CPU utilization metrics.

Security: Ensures secure connections with HTTPS, managed by AWS Certificate Manager, and employs security group rules to restrict port access to HTTP (80) and HTTPS (443).



                                                                                           Deployment Steps

EC2 Instance: Set up an EC2 instance on AWS.

S3 Bucket: Configure an S3 bucket for image storage.

RDS Setup: Establish an RDS instance for managing the manhwa database.

Auto-Scaling Configuration: Set up auto-scaling rules for EC2 based on CPU usage.

Flask App Deployment: Deploy the Python Flask app on the EC2 instance.

Enable HTTPS: Secure the application using AWS Certificate Manager to enable HTTPS.
