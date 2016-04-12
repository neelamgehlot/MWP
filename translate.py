#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
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

"""Simple command-line example for Translate.

Command-line application that translates some text.
"""
from __future__ import print_function

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

from googleapiclient.discovery import build

file = open("hindi.txt","wb")



def main():

    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build('translate', 'v2',
              developerKey='AIzaSyCOdKYjMPJBiAU3t2OJavzLbU5jYryz4x4')



    all_sentences = []
    with open("q_self_made.txt") as f:
        all_sentences = f.readlines()

    for each_senetence in all_sentences:
        dict = service.translations().list(source='en',target='hi',q=each_senetence).execute()

        file.write(dict['translations'][0]['translatedText'].encode('UTF-8')+'\n')
        print(dict['translations'][0]['translatedText'].encode('UTF-8')+'\n')
    file.close()




if __name__ == '__main__':
    main()