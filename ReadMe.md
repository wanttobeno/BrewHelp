

##### homebrew网页搜索

https://formulae.brew.sh/

##### Homebrew app real link extract


不安装brew，提取app的真实下载地址。


```
下载go
brew_find('go')

下载go1.16版本
brew_find('go@1.6')
```


```
请输入想要解析（如：mtr）：go
正在处理 go
go_1.17.8_arm64_monterey.tar.gz  https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:6537caf925f0a3ec1875c55b88a4184d58fc604f6979397b22e4b2a257175af1?se=2022-03-10T05%3A50%3A00Z&sig=Tg3ABisTtzK5MAqzOx97aRP8WToHollzMocl%2BJJUKvY%3D&sp=r&spr=https&sr=b&sv=2019-12-12
go_1.17.8_arm64_big_sur.tar.gz  https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:fdc0d8e3047cc35f601e1b8c8381bd50594711db9b90e81f01430b864a8ef579?se=2022-03-10T05%3A50%3A00Z&sig=Pvdi%2FyTCOt%2FgPRfIvlEBJtjpestdjiMVqpOgPu36UUY%3D&sp=r&spr=https&sr=b&sv=2019-12-12
go_1.17.8_monterey.tar.gz  https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:8e95cccc916d40254e2a56449fac8f4a5e36d86d63b619793ff1f372bae387a1?se=2022-03-10T05%3A50%3A00Z&sig=DRTQU94zawmxCzt8DtmDszxchPxp6VVl%2Bplo2vLY9Ko%3D&sp=r&spr=https&sr=b&sv=2019-12-12
go_1.17.8_big_sur.tar.gz  https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:62e6d0bdf5effc5b98f5de7004f7c70e4f27f120f334302622829f37f65676e8?se=2022-03-10T05%3A50%3A00Z&sig=ZIgXxVzizEc3bmz%2B109AJ68q32ZCdkjajc7yfwnCCas%3D&sp=r&spr=https&sr=b&sv=2019-12-12
go_1.17.8_catalina.tar.gz  https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:7d769c4b648931964a38850fa2774d40d2832ebecfeba97c35645f430ba80ab4?se=2022-03-10T05%3A50%3A00Z&sig=dk4nPaztN9N4sE1qZiwm3civvEG6DNb6SoyJFBZGKOc%3D&sp=r&spr=https&sr=b&sv=2019-12-12
go_1.17.8_x86_64_linux.tar.gz  https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:2c529a79f41ffc505361700c502661d9b6e0e11050d86f5dc6ff488ce854f4ac?se=2022-03-10T05%3A50%3A00Z&sig=5A%2BxdQFutKBtXjrFSWtQdUotJvDerveKdFi6MuCW880%3D&sp=r&spr=https&sr=b&sv=2019-12-12
历史版本大全 go@1.16 go@1.15 go@1.14 go@1.13
```



##### Homebrew

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```