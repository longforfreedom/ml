FROM alpine
MAINTAINER migle <longforfreedom@gmail.com>
RUN echo "https://mirrors.aliyun.com/alpine/v3.7/main/" >> /etc/apk/repositories
RUN echo "https://mirrors.aliyun.com/alpine/v3.7/community/" >> /etc/apk/repositories

#ENV JAVA_HOME /usr/java/default
RUN apk add --no-cache bash  gcc gfortran  build-base 
RUN apk add --no-cache python3 openssl-dev python3-dev

RUN pip3 install numpy -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com    #使用国内镜像
#pip install numpy 
#pip install scipy
#scipy pandas matplotlib
#RUN  rm -rf /var/cache/apk/* 
#RUN  rm -rf ~/.cache/ 



##py3-pillow 
#WORKDIR /opt

#download from spark website
#aliyun镜像在dockerhub上构建下载失败
#RUN wget https://mirrors.aliyun.com/apache/spark/spark-1.6.3/spark-1.6.3-bin-hadoop2.6.tgz
#RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-1.6.3-bin-hadoop2.6.tgz

#upload local spark
#COPY ./spark-1.6.3-bin-hadoop2.6.tgz /opt

#RUN tar xfvz /opt/spark-1.6.3-bin-hadoop2.6.tgz
#RUN rm -r /opt/spark-1.6.3-bin-hadoop2.6.tgz

# Set home
#ENV SPARK_HOME=/opt/spark-1.6.3-bin-hadoop2.6

#set spark/bin
#ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

# Ports
#EXPOSE 6066 7077 8080 8081


