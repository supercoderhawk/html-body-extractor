# 网页正文抽取
论文《基于行块分布函数的通用网页正文抽取》的Python实现。

## 安装
```bash
pip install body-extractor-py3
```

## 使用方法
```python
from body_extractor import BodyExtractor
import requests

url = 'http://md.tech-ex.com/ired/2016/47848.html'
res = request.get(url)
extractor = BodyExtractor(res.content)
print(extractor.content)

```