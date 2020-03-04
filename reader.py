#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:26:28 2019
@author: askaydevs (sk_singh18@outlook.com)
"""
import argparse

import PyPDF2
import os
from os.path import join
import docx2txt
import pickle

def get_data(file):
    """
    Function to extract text from a file.
    Currently supports text, pdf, doc and, docx formats.
    :param file: name of the file must be placed in data folder in the same
                 directory as this script.
    :type str: string

    :return text, title: returns text contained in the file and title of the
                         file.
    :type str, str: String
    """
    path = 'data/'
    # Function for getting text from a PDF file
    def pdf_extract(file, dir_path=path):
        """
        A function to extract text from pdf files.
        """
        text = ""
        title = ""
        with open(join(dir_path, file), 'rb') as f:
            if pdf.isEncrypted:
                return " PDF is encrypted, decrypt and try again."
            else:
                pdf = PyPDF2.PdfFileReader(f)
                for _ in range(0, pdf.getNumPages()):
                    page = pdf.getPage(_)
                    text += page.extractText()
                title += str(pdf.getDocumentInfo().title)

        return text.strip(), title

    # Function for getting text from a text file
    def txt_extract(file, dir_path=path):
    """
    A function to extract text from text files.

    """
        title = ''.join(list(file)[:-4])

        text = ""
        with open(dir_path+file) as inp:
            for line in inp:
                text += line

        return text.strip(), title

    def doc_x_extract(file, dir_path=path):
    """
    A function to extract text from docx and docx files.
    """
        title = file[:-5]
        if file.endswith('doc'):
            title = file[:-4]
            file = title + '.docx'

        text = docx2txt.process(dir_path+file)
        return text.strip(), title

    if file:
        filename = file
        if filename.endswith('.pdf'):
            content, title = pdf_extract(filename)
        elif filename.endswith('.txt'):
            content, title = txt_extract(filename)
        elif filename.endswith('.docx'):
            content, title = doc_x_extract(filename)
        elif filename.endswith('doc'):
            content, title = doc_x_extract(filename)

    return content, title

'''
description = "Takes filename as an input and returns text in it."
parser = argparse.ArgumentParser(description = description)
parser.add_argument('--filename', '-f', help="Name of the file")
args = parser.parse_args()
if args.filename:
    filename = args.filename
    if filename.endswith('.pdf'):
        content, title = pdf_extract(filename)
    elif filename.endswith('.txt'):
        content, title = txt_extract(filename)
    elif filename.endswith('.docx'):
        content, title = doc_x_extract(filename)
    elif filename.endswith('doc'):
        content, title = doc_x_extract(filename)
'''
