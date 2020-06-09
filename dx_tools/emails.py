# -*- coding: UTF-8 -*-
"""
@Summary : 发送邮件
@Author  : Rey
@Time    : 2020-06-08 14:45
@Log     :
           author datetime(DESC) summary
           Rey  2020-06-08 14:45  first edition
"""

from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr
import logging
import smtplib


class Email(object):

    def __init__(self, to_addr_in: list, from_addr: str, password: str,
                 server: str = 'smtp.163.com',
                 port: int = 465):
        """

        :param to_addr_in: 接收邮件地址 格式: "邮箱1,邮箱2"
        :param from_addr: 发送者邮箱地址
        :param password: 发送者smtp授权码
        :param server: SMTP服务器地址 默认是163
        :param port: SMTP端口 默认是465
        """
        self.to_addr_in = to_addr_in
        self.from_addr = from_addr
        self.password = password
        self.server = server
        self.port = port

    @classmethod
    def _format_addr(cls, s: str):
        """
        中文处理
        :param s: 待处理字符串
        :return:
        """
        name, addr = parseaddr(s)
        return formataddr((Header(name, "utf-8").encode(), addr))

    def send_email(self, content: str, subject: str, reporter: str = "BugReporter") -> bool:
        """
        发送邮件
        :param content: 邮件内容
        :param subject: 邮件主题
        :param reporter: 发件人别名
        :return: 成功True, 失败False
        """
        # smtp服务器信息
        smtp_server = self.server
        smtp_port = self.port  # 994

        # 接收方地址
        from_addr = self.from_addr
        password = self.password
        to_addr = ",".join(self.to_addr_in)

        # 邮件信息
        subject = subject
        msg = MIMEText(_text=content, _subtype="plain", _charset="utf-8")
        msg["From"] = self._format_addr(f'{reporter}<{from_addr}>')
        msg["To"] = to_addr
        msg["Subject"] = Header(subject)

        server = smtplib.SMTP_SSL(host=smtp_server)
        try:
            server.set_debuglevel(1)
            server.connect(host=smtp_server, port=smtp_port)
            server.login(user=from_addr, password=password)
            server.sendmail(from_addr=from_addr, to_addrs=self.to_addr_in, msg=msg.as_string())
        except Exception as e:
            logging.error(str(e), exc_info=True)
            return False
        finally:
            server.quit()
        return True
