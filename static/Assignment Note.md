- pip 安装指定 Python 版本的 package

  ```sh
  python3.8 -m pip install <package_name>
  ```

- pip 安装指定源下 package

  ```sh
  pip install <package_name> -i <source_url>
  ```

- 修改 pip 镜像源

  Method 1:

  ```sh
  # terminal 打开或创建 pip 配置文件 for Mac OS
  ~/.pip/pip.conf
  ~/Library/Application Support/pip/pip.conf
  ```

  ```sh
  [global]
  timeout = 120
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple
  trusted-host = pypi.tuna.tsinghua.edu.cn
  
  [search]
  index = https://pypi.tuna.tsinghua.edu.cn/simple
  ```

  pip 官方源

  ```sh
  index = https://pypi.org/simple
  ```

  Method 2:

  ```sh
  pip config set global.index-url
  ```

  

