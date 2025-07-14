FROM ubuntu:20.04
RUN apt update && apt install -y vim wget curl
WORKDIR /home/surkov
RUN touch hello.sh && echo "echo 'Hello from container'" > hello.sh

#CMD ["bash", "hello.sh"]
COPY script.sh script.sh
ENTRYPOINT ["bash", "script.sh"]
# Задание 10 - https://lab.karpov.courses/learning/102/module/1276/lesson/12127/35058/194271/
CMD ["World"]
