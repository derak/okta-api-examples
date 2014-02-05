#!/usr/bin/python
#
# Copyright 2014 Derak Berreyesa.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Example of interacting with the Okta API using Python
#
# Add your token and your companies Okta url


import urllib2
import json
import pprint

token = 'WHATEVER_YOUR_TOKEN_IS'
limit = '10'
base_url = 'https://your_company.okta.com/api/v1/'

url = base_url + '/users?limit=' + limit

headers = {'Authorization' : 'SSWS ' + token,
          'Accept' : 'application/json',
          'Content-Type' : 'application/json' }

req = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(req)
the_page = response.read()

json_obj = json.loads(the_page)

#print json.dumps(json_obj)

print json.dumps(json_obj, sort_keys=True, indent=2, separators=(',', ': '))
#print the_page


for json_row in json_obj:
	#print json.dumps(json_row["profile"], sort_keys=True, indent=4, separators=(',', ': '))
	firstName = json_row["profile"]["firstName"]
	lastName = json_row["profile"]["lastName"]
	login = json_row["profile"]["login"]
	fullName = firstName + " " + lastName
	print "full Name: " + fullName
	print "login: " + login
	print " "
