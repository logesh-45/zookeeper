# zookeeper
mkdir zookeeper \n
cd zookeeper
docker-compose up -d zk1 zk2 zk3 zoonavigator
docker-compose up -d zk1 zk2 zk3 zoonavigator
docker logs zk1
docker logs zk2
docker logs zk3
docker-compose down -d zk1
cd zookeeper
cd OneDrive/Desktop/zookeeper/
docker-compose up -d zk1 zk2 zk3 zoonavigator
docker logs zk3
docker exec -it zk3 bash
docker exec -it zk1 bash
docker logs zk2
docker exec -it zk1 bash
docker logs zk1
docker logs zk2
docker exec -it zk1 bash
ping zk1
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' zk1
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' zk3
pip install kazoo
docker exec -it kazoo bash
docker-compose down -d zk1 zk2 zk3 zoonavigator
docker stop zk1
docker stop zk2
docker logs zk3
docker stop zk3
docker-compose up -d zk1 zk2 zk3 kazoo zoonavigator
mkdir kazoo-client
cd kazoo-client
docker stop zk3
docker stop zk2
docker stop zk1
docker logs kazoo
docker logs kazoo
docker start kazoo
docker logs kazoo
docker logs kazooclear
docker exec -it kazoo bash
docker exec -it zk2 bash
docker exec -it zk1 bash
docker exec -it zk3 bash
