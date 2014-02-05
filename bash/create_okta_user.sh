#!/bin/bash
#
# Creates an Okta user with basic information.
#
# Usage: create_okta_user.sh email firstname lastname password
#
# Token is read in by file, but could be hard-coded.
# Add your companies Okta url. 
#
# Author: Derak Berreyesa
#################################################################


token=$( cat token.txt )

email=$1
firstname=$2
lastname=$3
password=$4

echo $firstname
echo $lastname
echo $email
echo $password

curl -v -H "Authorization: SSWS $token" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-X POST "https://your_company.okta.com/api/v1/users?activate=true" \
-d \
"{ \
  \"profile\": { \
     \"firstName\": \"$firstname\", \
     \"lastName\": \"$lastname\", \
     \"email\": \"$email\", \
     \"login\": \"$email\", \
     \"mobilePhone\": \"\" \
  }, \
  \"credentials\": { \
     \"password\" : { \"value\": \"$password\" } \
  } \
}"

