# Project description
一些工具函数

# Overview
- emails: 发送邮件


# Requirements
- python3.8

# Installation
pip install dx-tools

# Use
1. 发送邮件 
```python
from dx_tools.emails import Email

params = {
    "from_addr": "发件人",
    "to_addr_in": ["收件人1", "收件人2"],
    "password": "发件人授权码",
}

# 默认的smtp服务器使用的是163
email = Email(**params)
email.send_email(subject="new edition", content="alter")

```