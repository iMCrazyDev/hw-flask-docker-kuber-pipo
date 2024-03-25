# hw-flask-docker-kuber-pipo

## Выполнил Андрян Арсен БПИ201
Сервер на Фласке, Докер, Кубер, Постгря  
2 эндпоинта, можно поюзать, если сервер Пети еще жив  
http://141.105.64.134:32074/get возвращает количество  
http://141.105.64.134:32074/update?action=add или delete  
одно добавляет к числу 1, другое вычитает все. все хранится в таблице постгри  
1.
```Bash
docker-compose build
```  
2.
```Bash
docker image tag heavymetal-back:latest imcrazy/heavymetal4:latest
```
залил всю эту тему в ```imcrazy/heavymetal4```  \
3. на хостинге с кубером поднял бд, аплаим бд
```Bash
microk8s kubectl apply -f db-deployment.yaml
microk8s kubectl apply -f db-service.yaml
```
4. Поднимаем и даем доступ
```Bash
microk8s kubectl create deployment arsen-back --image=imcrazy/heavymetal4:latest
microk8s kubectl expose deployment/arsen-back --type=NodePort --port=5227 --name=back-service --target-port=5228
```
