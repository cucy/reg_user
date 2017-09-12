# 注册账号流程
## 1.注册
/accounts/register/
	对应模板 registration_form.html

## 2. 发送激活账号邮箱
```
`REGISTRATION_EMAIL_HTML` 设置为False使用`activation_email.txt`为邮箱模板发送,

设置为True时使用`activation_email.html`为模板发送,默认是`True`通过邮箱模板发送邮件到客户邮箱中.
```
## 3. 发送邮箱完成后回显页面
/accounts/register/complete/
	对应模板 registration_complete.html

## 4. 收件箱点击激活链接
`/accounts/activate/8e26961fba516fdf7e0b5178ee43051d9e88efa5/`

## 5. 账号激活通过提醒
/accounts/activate/complete/
	对应模板 activation_complete.html

## 6. 重发激活邮箱
/accounts/activate/resend/
	对应模板 resend_activation_form.html
## 7. 重发邮件激活成功提示页面
resend_activation_complete.html

# 改密码
## 1.页面
/accounts/password/change/
## 2.成功提示页面
/accounts/password/change/done/

# 重置密码
## 1.重置密码页面
/accounts/password/reset/
    对应模板 password_reset_form.html
{# This is used by django.contrib.auth #}
## 2.邮件模板
password_reset_email.html
## 3.发送邮箱成功确认页面
/accounts/password/reset/done/
	对应模板 password_reset_done.html

## 4.点击邮箱中的连接确认修改密码
/accounts/password/reset/confirm/NA/set-password/
	对应模板 password_reset_confirm.html

## 5.重置密码成功提示页面
/accounts/password/reset/complete/
	对应模板 password_reset_complete.html
