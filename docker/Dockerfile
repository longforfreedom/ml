FROM ubuntu:17.10
MAINTAINER migle <longforfreedom@gmail.com>

#更改成国内源
COPY ubuntu/sources.list /etc/apt/sources.list
RUN apt-get update

##中文显示
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales
RUN sed -i -e 's/# zh_CN.UTF-8 UTF-8/zh_CN.UTF-8 UTF-8/' /etc/locale.gen
RUN dpkg-reconfigure --frontend=noninteractive locales
ENV LANG zh_CN.UTF-8  
ENV LANGUAGE zh_CN:zh  
ENV LC_ALL zh_CN.UTF-8 

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


RUN apt-get install -y python3 python3-pip

#jupyter
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir jupyter      -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com    #使用国内镜像


#机器学习库
RUN pip3 install --no-cache-dir numpy       -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com    #使用国内镜像
RUN pip3 install --no-cache-dir pandas      -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com    #使用国内镜像
RUN pip3 install --no-cache-dir scipy       -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com    #使用国内镜像
RUN pip3 install --no-cache-dir matplotlib  -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com    #使用国内镜像
RUN pip3 install --no-cache-dir pillow  -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com    #使用国内镜像
RUN pip3 install --no-cache-dir -U scikit-learn -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com    #使用国内镜像
 
##for pytorch 
RUN pip3 install http://download.pytorch.org/whl/cpu/torch-0.3.0.post4-cp36-cp36m-linux_x86_64.whl 
RUN pip3 install torchvision  -i http://mirrors.aliyun.com/pypi/simple/  --trusted-host mirrors.aliyun.com


## for NLP
#RUN pip3 install nltk    -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
#RUN pip3 install jieba    -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
#RUN pip3 install gensim    -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

#clean
RUN apt-get -y autoremove
RUN apt-get -y clean

## port 8888 for jupyter
EXPOSE 8888
#
## 添加一个 notebook profile.否则启动时会报『OSError: [Errno 99] Address not available』
##RUN mkdir -p -m 700 /root/.jupyter/ && \
##    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py  
#给jupyter设置密码，如果有必要
#RUN  echo '{"NotebookApp": {"password": "sha1:1cff0f4d5c07:87a359e63f67a6e8b50497931fabe84135ad0672"}}' >> /root/.jupyter/jupyter_notebook_config.json
##启动jupyter notebook

VOLUME /workspace
WORKDIR /workspace


#--NotebookApp.token=''
CMD ["jupyter", "notebook","--no-browser", "--allow-root", "--ip=0.0.0.0", "--NotebookApp.token="]

#docker run  -p 8888:8888 -v /mnt/hgfs/E/workspace/ml:/workspace  -ti upyml /bin/bash
#docker run -it -p 8888:8888 -v ~/workspace/ml:/workspace upyml /bin/bash
#jupyter  notebook --no-browser --allow-root --NotebookApp.token=
#docker run -it -p 8888:8888 -v ~/workspace/ml:/workspace -d upyml

# open browser
#open http://$(docker-machine ip default):8888