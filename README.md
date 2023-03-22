Hadoop Cluster using Docker Compose
This project sets up a Hadoop cluster using Docker Compose, making it easy to deploy and manage a multi-node Hadoop environment for development and testing purposes. The cluster consists of one NameNode and one or more DataNodes.

Prerequisites
Docker: Ensure Docker is installed on your system. You can download it from Docker's official website.
Docker Compose: Make sure you have Docker Compose installed. If not, follow the official installation guide.
Getting Started
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/hadoop-docker-compose.git
cd hadoop-docker-compose
Edit the docker-compose.yml file to adjust the number of DataNodes or customize the configuration according to your requirements.

Start the Hadoop cluster using Docker Compose:

Copy code
docker-compose up -d
Check the status of your Hadoop cluster:

Copy code
docker-compose ps
Access the Hadoop web interfaces:

NameNode: http://localhost:9870
DataNode(s): http://localhost:9864 (for the first DataNode, change the port for additional DataNodes accordingly)
Running Hadoop Commands
To interact with Hadoop using the command-line interface, you can use the hadoop command inside the NameNode container:

bash
Copy code
docker exec -it namenode hadoop fs -<command>
For example, to list the contents of the Hadoop filesystem root directory:

bash
Copy code
docker exec -it namenode hadoop fs -ls /
Stopping the Cluster
To stop the Hadoop cluster and remove the containers, run:

Copy code
docker-compose down
Troubleshooting
If you encounter any issues or errors, you can check the logs for each container:

Copy code
docker-compose logs namenode
docker-compose logs datanode
Replace namenode or datanode with the appropriate service name if you have customized the docker-compose.yml file.

Notes
This Hadoop cluster setup is designed for development and testing purposes only. It is not recommended for use in production environments.
Data stored in the Hadoop cluster will be lost when the Docker containers are removed. To persist data across container restarts, consider using Docker volumes or bind mounts.
Contributing
Please feel free to contribute to this project by submitting issues or pull requests.
