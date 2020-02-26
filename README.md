## How to use this repo to create a map function container

1. Save [gen_container.py](https://raw.githubusercontent.com/columbustech/mapfn-test/master/gen_container.sh) to local disk. 
2. Install docker
3. Execute gen_container.py with correct arguments. An example execution:
```
python gen_container.py -f process.py -r requirements.txt -n mapfn-foo -u columbus -p REGISTRY_PASSWD
```
By default, the repository path is registry.columbustech.io/columbustech/CONTAINER_NAME, but this can be changed with
the b flag.
4. Give the image url to the sm-mapper app on Columbus. Eg: registry.columbustech.io/columbustech/mapfn-foo:latest in
the above example.
