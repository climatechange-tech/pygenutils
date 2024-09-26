#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**Note**

This program is an application of the main module 'audio_and_video',
and it relies on the method 'cut_media_files'.
YOU MAY REDISTRIBUTE this program along any other directory,
but keep in mind that the module is designed to work with absolute paths.
"""

#-----------------------#
# Import custom modules #
#-----------------------#

from pyutils.audio_and_video.audio_and_video_manipulation import cut_media_files

#-------------------#
# Define parameters #
#-------------------#

# Input media #
#-------------#

# List #
media_file_list = []

# External file containing file names #
# media_name_containing_file = "media_name_containing_file.txt"

# Output media #
#--------------#

# Merged media file #
output_file_list = []
# output_file_list = None

# Starting and ending times #
start_time_list = ["start", "00:01:28", "00:02:28.345"]
end_time_list = ["00:05:21", "end", "00:07:56.851"]

# Zero-padding and bit rate factor #
"""The factor is multiplied by 32, so that the bit rate is in range [32, 320] kBps"""
ZERO_PADDING = 1
quality = 1

#------------#
# Operations #
#------------#

cut_media_files(media_file_list,
                start_time_list,
                end_time_list,
                output_file_list=output_file_list,
                ZERO_PADDING=ZERO_PADDING,
                quality=quality)

# cut_media_files(media_name_containing_file,
#                 start_time_list,
#                 end_time_list,
#                 output_file_list=output_file_list,
#                 ZERO_PADDING=ZERO_PADDING,
#                 quality=quality)