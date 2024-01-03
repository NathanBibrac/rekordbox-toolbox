from lxml import etree
import xml.etree.ElementTree as ET
import pandas as pd
import os
import argparse
from colorama import Fore, Back, Style
import shutil
from datetime import datetime
import re

def ts_str():
    return datetime.now().strftime("%Y%m%d_%H%M%S")
def ts_log():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_args(): 
    parser = argparse.ArgumentParser(description='Create Rekordbox Playlist tree structure in a target directory')
    parser.add_argument('xml_source', metavar='xml_source', type=str, help='source rekordbox xml file')
    parser.add_argument('target', metavar='target', type=str, help='target directory')
    parser.add_argument('mode', metavar='mode', type=str, help='excel or exec. excel will create an excel file with the playlist structure. exec will create the playlist structure in the target directory')
    args = parser.parse_args()
    return args


def replace_hex_codes(string):
    pattern = r'%([0-9a-fA-F]{2})'  # Regular expression pattern to match hexadecimal codes after '%'
    result = re.sub(pattern, lambda match: chr(int(match.group(1), 16)), string)
    return result

def init_output_dir(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def parse_xml(xml):
    tree = etree.parse(xml)
    root = tree.getroot()
    return root

def get_playlist_list(root):
    playlist_list_xml = root.findall(".//NODE[@Type='1']")
    return(playlist_list_xml)

def build_path(playlist,target_dir="D:\\Music\\rekordbox"):
    parent_list = []
    parent = playlist.getparent()
    temp_parent_Name = parent.attrib["Name"]
    while parent.attrib["Name"] != "ROOT":
        temp_parent_Name = parent.attrib["Name"]
        parent_list.append(temp_parent_Name)
        parent = parent.getparent()
    parent_list.append(target_dir)
    parent_list.reverse()
    parent_list.append(playlist.attrib["Name"])
    path = "\\".join(parent_list)
    return path

def get_track_list(playlist):
    track_list = []
    for track in playlist.findall(".//TRACK"):
        track_list.append(track.attrib['Key'])
    return track_list


def map_track__to_playlist(playlist_list = playlist_list_xml, target_dir="D:\\Music\\rekordbox"):
    full_playlist_list = []
    playlist_dict = {}
    for elt in playlist_list:
        playlist_dict = {}
        playlist_dict["Name"] = elt.attrib["Name"]
        playlist_dict["Path"] = build_path(elt,target_dir)
        playlist_dict["Track_List"] = get_track_list(elt)
        full_playlist_list.append(playlist_dict)

    full_track_list = []
    track_dict = {}
    for elt in full_playlist_list:
        for track in elt["Track_List"]:
            track_dict = {}
            track_dict["Playlist"] = elt["Name"]
            track_dict["Path"] = elt["Path"]
            track_dict["TrackID"] = track
            full_track_list.append(track_dict)

    df_tracks_in_playlists = pd.DataFrame(full_track_list)

    return df_tracks_in_playlists


def get_tracks(xml_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    tracks = root.xpath("//COLLECTION/TRACK")
    all_tracks=[]
    for track in tracks:
        base_path = track.attrib['Location'][len('file://localhost/'):]
        if "D:/Music" in base_path:
            all_tracks.append({'TrackID': track.attrib['TrackID'], 'Name': track.attrib['Name'], 'Location': base_path.replace("/","\\")})
    df_tracks = pd.DataFrame(all_tracks)
    df_tracks['Location'] = df_tracks['Location'].apply(replace_hex_codes)
    return df_tracks

def merge_tracks_and_playlists(tracks, playlists,mode="excel"):
    df_tracks_in_playlists = pd.merge(tracks, playlists, on='TrackID', how='inner')
    df_tracks_in_playlists["Target_Path"] = df_tracks_in_playlists["Path"] +"\\" + df_tracks_in_playlists["Location"].str.split("\\").str[-1]
    if mode == "excel":
        init_output_dir()
        filename= f"playlist_structure_{ts_str()}.xlsx"
        filedir = os.path.join("output",filename)
        df_tracks_in_playlists.to_excel(filedir)
        print(f"{ts_log()}: Playlist structure saved in {filedir}")
    return df_tracks_in_playlists

def create_structure(target_path_column):
    for row in target_path_column.iterrows():
        if not os.path.exists(os.path.dirname(target_path_column)):
            os.makedirs(os.path.rootname(row["Target_Path"]))
            print(f'Path: {os.path.dirname(row["Target_Path"])} created')

def copie_tracks(merged_df,mode = "test"):
    for index, row in merged_df.iterrows():
        if index == 0 or row["Name"] != merged_df.iloc[index-1]["Name"]:
            print("\n"+"_"*50+"\n")
            print(f"Track {row['Name']} is being copied: \n")
        if os.path.exists(row["Target_Path"]):
            print(f'Track {row["Name"]} already exists in {row["Target_Path"]}')
        else:
                if mode == "test" or mode == "excel":
                    print(f'{ts_log()}: Copied from '+Fore.RED+f'{row["Location"]}'+Style.RESET_ALL +'\nTo '+Fore.RED+f'{row["Target_Path"]}'+Style.RESET_ALL)
                else:
                    shutil.copy(row["Location"], row["Target_Path"])


def main():

    XML, target_dir, mode = None, None, None

    args = get_args()
    #XML = args.xml_source
    #Si pas de XML en argument, on demande à l'utilisateur de le renseigner
    while XML is None:
        if args.xml_source == None:
            args.xml_source = input("Please enter the path to the rekordbox xml file: ")
        elif not os.path.exists(args.xml_source):
            args.xml_source = input("File does not exist. Please enter the path to the rekordbox xml file: ")
        elif not args.xml_source.endswith(".xml"):
            args.xml_source = input("File is not an xml file. Please enter the path to the rekordbox xml file: ")
        else:
            XML = args.xml_source

    #target_dir = args.target  
    #Si pas de target, on demande une target à l'utilisateur
    while target_dir is None:
        if args.target == None:
            args.target = input("Please enter the target directory: ")
        elif not os.path.exists(args.target):
            args.target = input("Target does not exist. Please enter the target directory: ")
        elif not os.path.isdir(args.target):
            args.target = input("Target is not a directory. Please enter the target directory: ")
        else:
            target_dir = args.target

    #mode = args.mode
    if args.mode == None or args.mode not in ["excel","exec"]:
        print(f'{ts_log()}: Mode defaulted to excel. To create the playlist structure, please use the argument "exec"')
    else:
        mode = args.mode

    
    root = parse_xml(XML)                                                                         #Parse XML
    playlist_list_xml = get_playlist_list(root)                                                   #Get playlist list
    result_playlist_df = map_track__to_playlist(playlist_list_xml,target_dir)                     #Map tracks to playlists
    track_df = get_tracks(XML)                                                                    #Get tracks
    merged_df = merge_tracks_and_playlists(track_df,result_playlist_df).drop_duplicates()         #Merge tracks and playlists
    copie_tracks(merged_df,mode)                                                                  #Copy tracks
