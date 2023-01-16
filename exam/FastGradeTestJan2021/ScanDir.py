# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 18:23:45 2017
Written an tested under WinPython-64bit-3.4.4.6 with PyQt5

@author: Nicholas LeBow


Consistency checking utility for student answer files. Prints output to console. Edit __main__ call below if
file output, absolute paths, etc. are required.
"""

from PyQt5.QtWidgets import QFileDialog, QApplication
import os
import sys
import re

def scan(root, verbose=True, ext='.py', show_full_paths=False):
	"""
	Scans files in immediate subfolders of the selected root folder and returns a list of folders where
	inconsistencies were detected.
	
	The given folder is assumed to contain one subfolder for each student, with all student files contained in that
	folder, and no further subfolders. Student files are expected to have names of the form:
		q<X>_<Mat.Nr>_<Student Surname>.<date>.py
	or:
		q<X>_<Mat.Nr>_<Student surname>.py
	where <X> is a 1- or 2-digit number and <date> is of the form YYMMDD-HHMMSS.

	The student folders are scanned and a list of folders containing inconsistant filenames is generated and returned.
	A folder is considered inconsistent if it contains files with names of the forms above where the values of
	<Mat.Nr.> and <Student surname> are not identical for all files in the folder.
	
	Args:
		root (string): Root folder to scan.
		verbose (bool): True - print to stdout. False - No printing, just return list of folders.
		ext (string): File extension to scan
		show_full_paths (bool): True - Return absolute path strings. False - Return only folder names.
	
	Returns:
		Sorted list of strings of the form <folder>: <detected value>, <expected_value>
			where <folder> is the folder name or full folder path, and <detected value> and <expected value> are the
			name or student number strings found to be inconsistent. This list may contain multiple entries for a single
			folder, for example if the folder contains two different name inconsistencies, or both a name and student
			number inconsistency.
	"""
	if not root:
		if verbose: print("Error: No starting directory specified")
		sys.exit()
	regex = re.compile('^[qQ]\d{1,2}_\d{8}_[A-Za-z0-9]+(\.\d{6}-\d{6})?\.py')  # Used to filter student files to load. Starts with 'q', followed by a 1- or 2-digit number, 8-digit student id, name and optional 6-6-digit timestamp
	inconsistent_folders = set()
	upper_q_folders = set()
	if verbose: print("### Starting scan ###")
	for root, dirs, files in os.walk(root):
		for folder in dirs:
			if show_full_paths:
				disp_folder = os.path.join(root, folder)
			else:
				disp_folder = folder
			if verbose: print('Scanning folder "' + disp_folder + '" ...')
			mat_nr = None
			name = None
			for student_path, student_dirs, student_files in os.walk(os.path.join(root, folder)):
				for file in [x for x in student_files if regex.search(x)]:
					if regex.search(file) and file.endswith(ext):
						sections = file.split("_")
						current_mat_nr = sections[1]
						current_name = sections[2].split(".")[0]
						if mat_nr is None:
							mat_nr = current_mat_nr
						else:
							if current_mat_nr != mat_nr:
								if verbose: print("  - Inconsistent student numbers: %s, %s" % (current_mat_nr, mat_nr))
								inconsistent_folders.add(str("%s: %s, %s" % (disp_folder, current_mat_nr, mat_nr)))
						if name is None:
							name = current_name
						else:
							if current_name != name:
								if verbose: print("  - Inconsistent names: %s, %s" % (current_name, name))
								inconsistent_folders.add(str("%s: %s, %s" % (disp_folder, current_name, name)))
						if file[0] == 'Q':
							if verbose: print("  - File name starts with Q: %s" % (name))
							upper_q_folders.add(str("%s: %s" % (disp_folder, name)))
	if verbose:
		print("### Scan complete ###\n")
		if inconsistent_folders:
			print("Inconsistent folders:")
			for i in inconsistent_folders: print(i)
		else:
			print("No inconsistencies found")
		if upper_q_folders:
			print("\nFolders with files that start with q instead of Q:")
			for i in upper_q_folders: print(i)
		else:
			print("No files found that start with Q instead of q")
	return inconsistent_folders


if __name__ == '__main__':
	app = QApplication(sys.argv)
	root_folder = QFileDialog.getExistingDirectory(QFileDialog(), "Select folder to scan", os.path.realpath(__file__))
	scan(root_folder)
