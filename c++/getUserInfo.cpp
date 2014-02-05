/*
 * Example of interacting with the Okta API using C++ 
 *
 * Add your token and your companies okta url
 *
 * On Mac, compile with: gcc -lcurl -o get getUserInfo.cpp
 *
 * Author: Derak Berreyesa
 */

#include <stdio.h>
#include <curl/curl.h>

int main(void)
{
  CURL *curl;
  CURLcode res;
 
  curl = curl_easy_init();
  if(curl) {

    struct curl_slist *headers = NULL;

    headers = curl_slist_append(headers, "Authorization: SSWS WHATEVER_YOUR_TOKEN_IS");
    headers = curl_slist_append(headers, "Accept: application/json");
    headers = curl_slist_append(headers, "Content-Type: application/json");
    
    curl_easy_setopt(curl, CURLOPT_URL, "https://your_company.okta.com/api/v1/users?limit=2");
    //curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L); //if you want verbose mode
 
    /* do request with our own custom Accept: */ 
    res = curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    res = curl_easy_perform(curl);

    /* Check for errors */ 
    if(res != CURLE_OK)
      fprintf(stderr, "curl_easy_perform() failed: %s\n",
              curl_easy_strerror(res));
 
    /* always cleanup */ 
    curl_easy_cleanup(curl);
 
    /* free the custom headers */ 
    curl_slist_free_all(headers);

    printf("\n");
  }

  return 0;
}
