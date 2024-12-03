# OpenWrt Package Build Action

`.github`目录下有一些可配置文件：

- `artifact-patterns.list`: 构建成功后，需要上传的文件列表
- `packages-to-build.list`: 想要构建的软件包列表
- `feeds.conf.default.in`: feeds配置文件, 会替换sdk的`feeds.conf.default`, 简单起见,
  且不失兼容性地, 选择各个feeds对应OpenWrt版本的最新分支

  需要注意, 如果该文件中存在自建feeds, 需要保证这些feeds存在目标分支, 例如`openwrt-23.05`

编辑`build.yaml`新增设备

## TODO

- [ ] 通过diffconf跳过tmate menuconfig