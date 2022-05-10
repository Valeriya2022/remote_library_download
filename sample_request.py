# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2 import service_account

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "still-gravity-346208-3d3a7396cf01.json"

    # Get credentials and create an API client
    flow = service_account.Credentials.from_service_account_file(
        client_secrets_file, scopes=scopes)
    # credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=flow)

    request = youtube.search().list(
        part="snippet",
        maxResults=3,
        q="пол"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()