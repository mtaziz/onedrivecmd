#!/usr/bin/env python
#coding:utf-8
# Author:  Beining --<i@cnbeining.com>
# Purpose: Static varibles for onedrivecmd
# Created: 09/24/2016


global VER, redirect_uri, client_secret, client_id, api_base_url, scopes, discovery_uri, auth_server_url, auth_token_url

VER = 'OnedriveCMD V0.0.3'


# If you are not sure whether this is safe,
# you can register your own APP and use your own URL.
# Don't just change it: you will have error.
redirect_uri = 'https://onedrive.live.com/about/business/'


## Normal 
client_secret_normal = 'RQdGA24FctsiBGuP8v3juea'
client_id_normal ='aeba6391-92fd-437d-a9d9-33a258b96c4e'
api_base_url='https://api.onedrive.com/v1.0/'
scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

## Business
discovery_uri = 'https://api.office.com/discovery/'
auth_server_url='https://login.microsoftonline.com/common/oauth2/authorize',
auth_token_url='https://login.microsoftonline.com/common/oauth2/token'

# If you are working with Office 365 you may want to create your own app
# and change the following:
# You can still use https://od.cnbeining.com as redirect URL.
client_id_business = 'cdf60547-0b22-4541-9315-f58169fe11b1'
client_secret_business = 'WkOhYmgFZYYDdNe6HwMBzYtK7DS5i78yruNBlJ7vEpA='

if __name__=='__main__':
    pass
