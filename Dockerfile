FROM alpine
MAINTAINER migle <longforfreedom@gmail.com>
RUN echo "https://mirrors.aliyun.com/alpine/v3.7/main/" > /etc/apk/repositories
RUN echo "https://mirrors.aliyun.com/alpine/v3.7/community/" >> /etc/apk/repositories

#ENV JAVA_HOME /usr/java/default
RUN apk add --no-cache bash  gcc gfortran  build-base 
RUN apk add --no-cache python3 openssl-dev python3-dev
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir numpy       -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com    #使用国内镜像
RUN pip3 install --no-cache-dir pandas      -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com    #使用国内镜像
RUN pip3 install --no-cache-dir jupyter     -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com    #使用国内镜像
## for pillow scipy and matplotlib
RUN apk add --no-cache freetype-dev openblas-dev py3-pillow
RUN pip3 install --no-cache-dir scipy       -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com    #使用国内镜像
RUN pip3 install --no-cache-dir matplotlib  -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com    #使用国内镜像
 
#for pytorch 
RUN pip3 install http://download.pytorch.org/whl/cpu/torch-0.3.0.post4-cp36-cp36m-linux_x86_64.whl 
RUN pip3 install torchvision

RUN  rm -rf /var/cache/apk/* 
RUN  rm -rf ~/.cache/ 

 
#WORKDIR /opt

# Set home
#ENV SPARK_HOME=/opt/spark-1.6.3-bin-hadoop2.6

#set spark/bin
#ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

# Ports
EXPOSE 8888

# 添加一个 notebook profile.否则启动时会报『OSError: [Errno 99] Address not available』
RUN mkdir -p -m 700 /root/.jupyter/ && \
    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py
#启动jupyter notebook
CMD ["jupyter", "notebook", "--no-browser", "--allow-root","--pylab=%matplotlib"]



# run Jupyter Notebook container 
#docker run  -p 8888:8888 -v $(pwd):/code  -d smizy/scikit-learn

# open browser
#open http://$(docker-machine ip default):8888



