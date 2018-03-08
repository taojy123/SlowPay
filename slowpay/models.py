# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Cashier(models.Model):

    name = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    # [alipay_wap]
    alipay_pid = models.CharField(max_length=255, blank=True, help_text=u'合作者身份（PID），对应商户申请的支付宝的partnerId')
    alipay_account = models.CharField(max_length=255, blank=True, help_text=u'支付宝企业账户（邮箱）')
    alipay_security_key = models.CharField(max_length=255, blank=True, help_text=u'安全校验码（Key）')
    alipay_mer_wap_private_key = models.CharField(max_length=255, blank=True, help_text=u'商户 RSA 私钥（非 PKCS8 编码）')
    alipay_wap_public_key = models.CharField(max_length=255, blank=True, help_text=u'商户支付宝公钥')
    alipay_version = models.CharField(max_length=255, blank=True, help_text=u'支付宝版本， 1:支付宝1.0接口， mapi ；2:支付宝2.0 接口 openapi')
    alipay_app_id = models.CharField(max_length=255, blank=True, help_text=u'APPID ，在参数 alipay_version 为 2.0 时，需要传入此参数')

    # [alipay_pc_direct]
    # alipay_pid
    # alipay_account
    # alipay_security_key
    alipay_private_key = models.CharField(max_length=255, blank=True, help_text=u'商户 RSA 私钥（非 PKCS8 编码）')
    alipay_public_key = models.CharField(max_length=255, blank=True, help_text=u'支付宝公钥')

    # [wx_pub]
    wx_pub_app_id = models.CharField(max_length=255, blank=True, help_text=u'微信公众号AppID（应用 ID）,获取地址：微信公众平台 => 开发 => 基本配置')
    wx_pub_mch_id = models.CharField(max_length=255, blank=True, help_text=u'微信支付商户ID.微信公众号支付申请完成之后，在微信商户平台的通知邮件中获取，请确保邮件上的 AppID 与微信公众平台上的 AppID 一致。')
    wx_pub_key = models.CharField(max_length=255, blank=True, help_text=u'商户支付API 密钥，用于报文签名及验签。微信商户平台 => API 安全 => 设置密钥，将设置的 32 位密钥填入此处')
    wx_pub_app_secret = models.CharField(max_length=255, blank=True, help_text=u'应用密钥，用于获取openid。获取地址：微信公众平台 => 开发 => 基本配置')
    wx_pub_operator_id = models.CharField(max_length=255, blank=True, help_text=u'由商户添加的退款操作员ID，用于退款、退款查询。获取地址：微信商户平台 => 员工账号 => 新增员工账号，将员工的登录账号填入此处')
    wx_pub_client_cert = models.CharField(max_length=255, blank=True, help_text=u'微信客户端证书(pem格式,不包含秘钥)，用于退款、退款查询。微信商户平台 => API 安全 => API 证书 =>下载证书')
    wx_pub_client_key = models.CharField(max_length=255, blank=True, help_text=u'微信客户端证书秘钥(pem格式)，用于退款、退款查询。微信商户平台 => API 安全 => API 证书 =>下载证书')

    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(default=timezone.now)
